from pydantic import BaseModel
from datetime import datetime
from .models import DocumentStatus

class DocumentBase(BaseModel):
    original_filename: str

class DocumentCreate(DocumentBase):
    filename: str
    status: DocumentStatus = DocumentStatus.UPLOADED

class Document(DocumentBase):
    id: int
    filename: str
    status: DocumentStatus
    created_at: datetime

    class Config:
        orm_mode = True
