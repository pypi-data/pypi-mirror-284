import shutil
import io
from pathlib import Path
from typing import Optional, Iterator
from urllib.parse import urlparse, ParseResult

from fastdup.vl.common.settings import Settings
from fastdup.vl.common.logging_init import get_vl_logger

if Settings.IS_FASTDUP:
    session = None
    boto3 = None
else:
    import boto3
    import aioboto3
    from botocore.exceptions import ClientError
    from boto3_type_annotations.s3 import Client as S3Client
    session = boto3.session.Session(
        aws_access_key_id=Settings.AWS_ACCESS_KEY,
        aws_secret_access_key=Settings.AWS_SECRET_KEY,
        region_name='us-east-2'
    )
    async_session = aioboto3.session.Session(
        aws_access_key_id=Settings.AWS_ACCESS_KEY,
        aws_secret_access_key=Settings.AWS_SECRET_KEY,
        region_name='us-east-2'
    )
    s3: S3Client = session.client(
        's3',
    )


logger = get_vl_logger(__name__)
expiration = 60 * 60 * 24 * 30 * 12


def generate_presigned_url(bucket, path):
    _url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': path}, ExpiresIn=expiration)
    return _url


def stream_object(bucket, path):
    obj = s3.get_object(Bucket=bucket, Key=path)
    return obj['Body']


def upload_file(source_file_path: str, bucket: str, key: str):
    s3.upload_file(source_file_path, bucket, key)


async def upload_fileobj_async(file_obj, bucket: str, key: str, upload_copy=True):
    async with async_session.client("s3") as s3_client:
        await s3_client.upload_fileobj(file_obj, bucket, key)


def check_s3_objects(objs, bucket) -> bool:
    for obj in objs:
        if not check_s3_object(obj, bucket):
            return False
    return True


def check_s3_object(obj, bucket) -> bool:
    try:
        obj = obj.strip()
        s3.head_object(Bucket=bucket, Key=obj)
        return True
    except Exception as e:
        if e.response['Error']['Code'] == "404":
            logger.error(obj)
        else:
            logger.error(e)
        return False


def check_connectivity_to_bucket(bucket_path: str, assume_role: Optional[str] = None) -> bool:
    path = Path(bucket_path)
    bucket_name = path.parts[0]

    if assume_role:
        sts_client = boto3.client(
            "sts", aws_access_key_id=Settings.AWS_ACCESS_KEY, aws_secret_access_key=Settings.AWS_SECRET_KEY
        )
        try:
            response = sts_client.assume_role(RoleArn=assume_role, RoleSessionName="AssumeRoleDemoSession")
            temp_credentials = response["Credentials"]
        except ClientError as error:
            logger.error(f"Couldn't assume role {assume_role}: {error.response['Error']['Message']}")
            return False

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=temp_credentials["AccessKeyId"],
            aws_secret_access_key=temp_credentials["SecretAccessKey"],
            aws_session_token=temp_credentials["SessionToken"],
        )
        try:
            s3_client.head_bucket(Bucket=bucket_name)
            return True
        except ClientError as error:
            logger.error(f"Couldn't connect to bucket {bucket_name}: {error.response['Error']['Message']}")
            return False
    else:
        try:
            response = s3.get_bucket_acl(Bucket=bucket_name)
            grants = response["Grants"]
            public_access = any(
                (  # from lying chatgpt
                        grant["Grantee"]["Type"] == "Group"
                        and grant["Grantee"]["URI"] == "http://acs.amazonaws.com/groups/global/AllUsers"
                        and grant["Permission"] == "READ"
                )
                or
                (
                        grant["Grantee"]["Type"] == 'CanonicalUser'
                        and grant["Permission"] == 'FULL_CONTROL'
                )
                for grant in grants
            )
            return public_access
        except (s3.exceptions.NoSuchBucket, s3.exceptions.AccessDenied) as e:
            logger.warning(f"Cannot access Bucket %s, %s", bucket_name, repr(e))
            return False


def create_customized_session(aws_access_key=None, aws_secret_key=None, region=None):
    aws_access_key = aws_access_key or Settings.AWS_ACCESS_KEY
    aws_secret_key = aws_secret_key or Settings.AWS_SECRET_KEY
    sts_client = boto3.client(
        "sts",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
    )
    response = sts_client.get_session_token()
    session = boto3.Session(
        aws_access_key_id=response["Credentials"]["AccessKeyId"],
        aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
        aws_session_token=response["Credentials"]["SessionToken"],
        region_name=region,
    )
    return session


def parse_and_validate_s3_url(s3_url: str) -> tuple[bool, Optional[bool], Optional[str], Optional[str], Optional[str]]:
    """
    returns: tuple [is_valid, is_recoverable, bucket_name, path, message]
    """
    try:
        parse_result: ParseResult = urlparse(s3_url)
        if parse_result.scheme != 's3':
            return False, True, None, None, 'Missing expected S3 protocol'
        bucket_name = parse_result.netloc
        if not bucket_name:
            return False, True, None, None, 'Missing bucket name.'

        path = parse_result.path
        if path:
            path = path.strip('/')

        return True, None, bucket_name, path, None
    except Exception as e:
        logger.exception(e)
        return False, False, None, None, None


class S3FileInfo:
    def __init__(self, bucket_name: str, key: str, size: int):
        self.bucket_name = bucket_name
        self.key = key
        self.size = size


def s3_iterate_files(bucket_name: str, prefix: str) -> Iterator[S3FileInfo]:

    for page in s3.get_paginator('list_objects_v2').paginate(Bucket=bucket_name, Prefix=prefix):
        for content in page.get('Contents', ()):
            yield S3FileInfo(bucket_name, content['Key'], content['Size'])
