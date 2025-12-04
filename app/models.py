import enum
from sqlalchemy import Column, Integer, String, DateTime, func, Enum
from .database import Base

class DocumentStatus(str, enum.Enum):
    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    
    # The name of the file stored on the server's disk
    filename = Column(String, unique=True, index=True, nullable=False)
    
    # The original name of the file uploaded by the user
    original_filename = Column(String, nullable=False)
    
    status = Column(Enum(DocumentStatus), nullable=False, default=DocumentStatus.UPLOADED)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Document(id={self.id}, name='{self.original_filename}', status='{self.status}')>"
