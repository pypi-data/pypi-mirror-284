from datetime import datetime
from enum import Enum
from typing import Union, Any, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class ExportTaskStatus(str, Enum):
    INIT = "INIT"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class MediaType(Enum):
    OBJECT = "object"
    IMAGE = "image"
    VIDEO = "video_frame"


class MetadataType(Enum):
    ISSUE = "Issue"
    ANNOTATION = "Annotation"
    ENRICHMENT = "Enrichment"
    USER_TAG = "User Tag"


class MediaExportInfo(BaseModel):
    id: UUID
    type: MediaType
    name: str
    path: str
    cluster_id: UUID
    file_size: str
    height: int
    width: int
    url: str
    properties: Union[dict[str, Any], None]


class MetadataExportInfo(BaseModel):
    id: UUID
    type: MetadataType
    media_id: UUID
    properties: Union[dict[str, Any], None]


class GeneralExportInfo(BaseModel):
    dataset: str
    description: str
    url: str = ""
    contributor: str
    export_task_id: UUID
    export_created: datetime
    dataset_created: datetime
    exported_by: str
    total_media_items: int
    total_metadata_items: int


class ExportInfo(BaseModel):
    info: GeneralExportInfo
    media: list[MediaExportInfo] = Field(default_factory=list)
    metadata: list[MetadataExportInfo] = Field(default_factory=list)

    @property
    def export_name_suffix(self):
        return self.info.export_created

    @property
    def export_name(self):
        return f'vl_export_{self.export_name_suffix}'


class ExportTask(BaseModel):
    id: UUID
    dataset_id: UUID
    created_at: datetime
    download_uri: Optional[str]
    progress: float
    status: ExportTaskStatus
