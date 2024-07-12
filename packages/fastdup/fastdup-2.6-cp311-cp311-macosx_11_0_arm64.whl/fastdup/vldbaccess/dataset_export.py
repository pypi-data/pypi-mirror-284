import asyncio
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

import sqlalchemy as sa

from fastdup.vl.common import logging_helpers
from fastdup.vl.common.settings import Settings
from fastdup.vl.utils import formatting
from fastdup.vl.utils.useful_decorators import timed
from fastdup.vldbaccess import sql_template_utils
from fastdup.vldbaccess.cluster_model import ClusterType
from fastdup.vldbaccess.connection_manager import get_async_session, get_async_engine, get_engine_dialect
from fastdup.vldbaccess.models.dataset import Dataset
from fastdup.vldbaccess.models.exploration_context import ExplorationContext
from fastdup.vldbaccess.models.export_info import ExportInfo, GeneralExportInfo, MediaExportInfo, MetadataExportInfo, \
    MediaType, MetadataType, ExportTask, ExportTaskStatus
from fastdup.vldbaccess.sql_template_utils import QueryModule
from fastdup.vldbaccess.user import User


SOURCE_DISPLAY_NAME = {
    "VL": "Visual Layer",
    "USER": "User",
}


def concat_uuids(u1: UUID, u2: UUID) -> UUID:
    return UUID(((u1.int + u2.int) % (2 ** 128)).to_bytes(16, "big").hex())


async def _stream_query_results(query, ctx):
    if get_engine_dialect() == "postgresql":
        async with (get_async_engine()).connect() as conn:
            async_result = await conn.stream(sa.text(query), ctx)
            async for row in async_result.mappings():
                yield row
    else:
        async with get_async_session() as session:
            for row in (await session.execute(sa.text(query), ctx)).mappings().all():
                yield row
                await asyncio.sleep(0)


@timed
async def _export_info_images(
    ctx: dict
) -> dict[UUID, MediaExportInfo]:
    media: dict[UUID, MediaExportInfo] = {}
    query = sql_template_utils.render(QueryModule.EXPLORATION, "export/export_medias.jinja2", **ctx)
    with logging_helpers.log_sql_query_time(__name__, "export_medias", query, ctx, ):
        async for row in _stream_query_results(query, ctx):
            cluster_type = ClusterType[row["cluster_type"]]
            metadata = row["metadata"] or {}
            video = metadata.get("video")
            frame_timestamp = metadata.get("frame_timestamp")
            if cluster_type is ClusterType.OBJECTS:
                media_type = MediaType.OBJECT
                properties = {
                    "bbox": row["bounding_box"],  # labels metadata is being added when iterating over labels
                    "image_id": row["image_id"]
                }
            elif video:
                media_type = MediaType.VIDEO
                properties = {
                    "video_name": video,
                    "frame_timestamp": frame_timestamp
                }
            else:
                media_type = MediaType.IMAGE
                properties = {}
            media[row["media_id"]] = MediaExportInfo(
                id=row["media_id"],
                type=media_type,
                name=row["image_original_uri"].split("/")[-1],
                path=row["image_original_uri"],
                cluster_id=row["cluster_id"],
                file_size=formatting.sizeof_fmt(row["image_file_size"]),
                height=row["image_height"],
                width=row["image_width"],
                url=row["image_uri"],
                properties=properties
            )
        return media


@timed
async def _export_info_labels(
    ctx: dict,
    entity_type: ClusterType,
) -> dict[UUID, MetadataExportInfo]:
    query_name = f"export/export_labels_{entity_type.value.lower()}.jinja2"

    metadata: dict[UUID, MetadataExportInfo] = {}
    query = sql_template_utils.render(QueryModule.EXPLORATION, query_name, **ctx)
    with logging_helpers.log_sql_query_time(__name__, query_name, query, ctx, ):
        async for row in _stream_query_results(query, ctx):
            metadata[row["label_id"]] = MetadataExportInfo(
                id=row["label_id"],
                type=MetadataType.ENRICHMENT if row["source"] == "VL" else MetadataType.ANNOTATION,
                media_id=row["media_id"],
                properties={
                    "name": f'{row["label_type"].lower()}_label',
                    "category_name": row["category_id"],
                    "value": row["category_display_name"],
                    # "source": SOURCE_DISPLAY_NAME.get(row["source"], row["source"])
                }
            )
    return metadata


@timed
async def _export_info_issues(
        ctx: dict
) -> dict[UUID, MetadataExportInfo]:
    query = sql_template_utils.render(QueryModule.EXPLORATION, "export/export_issues.jinja2", **ctx)
    metadata: dict[UUID, MetadataExportInfo] = {}
    async for row in _stream_query_results(query, ctx):
        if row["issue_type_name"] != "normal":
            metadata[row["issue_id"]] = MetadataExportInfo(
                id=row["issue_id"],
                type=MetadataType.ISSUE,
                media_id=row["media_id"],
                properties={
                    "issue_type": row["issue_type_name"],
                    "issues_description": row["issues_description"],
                    "confidence": row["issue_confidence"],
                }
            )
    return metadata


@timed
async def _export_info_tags(
        ctx: dict
) -> dict[UUID, MetadataExportInfo]:
    query = sql_template_utils.render(QueryModule.EXPLORATION, "export/export_tags.jinja2", **ctx)
    metadata: dict[UUID, MetadataExportInfo] = {}
    async for row in _stream_query_results(query, ctx):
        media_tag_id = concat_uuids(row["media_id"], row["tag_id"])  # TODO: add an id to media_to_tags table
        metadata[media_tag_id] = MetadataExportInfo(
            id=media_tag_id,
            type=MetadataType.USER_TAG,
            media_id=row["media_id"],
            properties={
                "tag_name": row["tag_name"],
                "assigned_date": row["media_to_tags_created_at"],
            }
        )
    return metadata


@timed(context_keys=["context.dataset_id"])
async def generate_export_info(
    context: ExplorationContext,
    cluster_ids: Optional[list[UUID]] = None,
    media_ids: Optional[list[UUID]] = None
):
    ctx = context.dict() | {"cluster_ids": cluster_ids, "media_ids": media_ids}
    (export_info_images, export_info_labels_images, export_info_labels_objects,
     export_info_issues, export_info_tags) = (
        await asyncio.gather(
            _export_info_images(ctx),
            _export_info_labels(ctx, ClusterType.IMAGES),
            _export_info_labels(ctx, ClusterType.OBJECTS),
            _export_info_issues(ctx),
            _export_info_tags(ctx)
        )
    )

    return (
        export_info_images, export_info_labels_images, export_info_labels_objects, export_info_issues,
        export_info_tags
    )


def _build_export_info(
        export_task_id: UUID,
        user: User,
        dataset: Dataset,
        export_info_images: dict[UUID, MediaExportInfo],
        export_info_labels_images: dict[UUID, MetadataExportInfo],
        export_info_labels_objects: dict[UUID, MetadataExportInfo],
        export_info_issues: dict[UUID, MetadataExportInfo],
        export_info_tags: dict[UUID, MetadataExportInfo],
) -> ExportInfo:
    for label_info in export_info_labels_objects.values():
        export_info_images[label_info.media_id].properties.update(
            {"category_name": label_info.properties["value"]}
        )
    metadata = export_info_labels_images | export_info_labels_objects | export_info_issues | export_info_tags
    export_info = ExportInfo(
        info=GeneralExportInfo(
            dataset=dataset.display_name,
            description=f"Exported from {dataset.display_name} at Visual Layer",
            url="",
            contributor="Visual Layer",
            export_created=datetime.now(),
            dataset_created=dataset.created_at,
            exported_by=str(user.name or user.email or user.user_identity or user.user_id or ''),
            total_media_items=len(export_info_images),
            total_metadata_items=len(metadata),
            export_task_id=export_task_id,
        ),
        media=list(export_info_images.values()),
        metadata=list(metadata.values()),
    )

    return export_info


async def build_export_info(
    export_task_id: UUID,
    context: ExplorationContext,
    cluster_ids: Optional[list[UUID]] = None,
    media_ids: Optional[list[UUID]] = None,

) -> ExportInfo:
    if media_ids:
        assert context.threshold is not None
    (
        export_info_images, export_info_labels_images, export_info_labels_objects, export_info_issues, export_info_tags
     ) = await generate_export_info(
        context, cluster_ids, media_ids
    )
    export_info = _build_export_info(
        export_task_id, context.user, context.dataset, export_info_images, export_info_labels_images,
        export_info_labels_objects, export_info_issues, export_info_tags)
    return export_info


async def check_for_concurrent_export_task(
        user_id: UUID,
        max_concurrent_tasks=Settings.MAX_NUM_OF_CONCURENT_EXPORT_TASKS
) -> bool:
    if max_concurrent_tasks:
        async with get_async_session() as session:
            res = (await session.execute(
                sa.text("""
                SELECT 1 FROM export_task 
                WHERE user_id = :user_id AND status NOT IN ('COMPLETED', 'FAILED') and created_at > :duration_window
                """), {"user_id": user_id, "duration_window": datetime.now() - timedelta(days=1)},
            )).all()
        return res and (len(res) >= max_concurrent_tasks)
    else:
        return False


async def create_export_task_in_db(dataset_id: UUID, user_id: UUID) -> UUID:
    async with get_async_session(autocommit=True) as session:
        export_task_id = (await session.execute(
            sa.text("""
            INSERT INTO export_task(dataset_id, user_id) VALUES(:dataset_id, :user_id)
            RETURNING id
            """),
            {"dataset_id": dataset_id, "user_id": user_id},
        )).scalar()
    return export_task_id


async def update_export_task_in_db(
        export_task_id: UUID, export_task_status: ExportTaskStatus, progress, download_uri: Optional[str] = None):
    async with get_async_session(autocommit=True) as session:
        await session.execute(sa.text("""
            UPDATE export_task 
            SET status = :export_task_status, progress = :progress, download_uri = :download_uri  
            WHERE id = :export_task_id
        """), {
            "export_task_id": export_task_id,
            "export_task_status": export_task_status,
            "progress": progress,
            "download_uri": download_uri
        })


async def get_export_task_status(
        export_task_id: UUID, user_id: UUID) -> ExportTask:
    async with get_async_session(autocommit=True) as session:
        res = (await session.execute(sa.text("""
            SELECT * FROM export_task WHERE id = :export_task_id AND user_id = :user_id
        """), {
            "export_task_id": export_task_id,
            "user_id": user_id
        })).mappings().one_or_none()
    if res:
        return ExportTask(**res)
