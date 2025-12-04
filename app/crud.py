from sqlalchemy.orm import Session
from . import models, schemas

def get_documents(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of all documents from the database.
    """
    return db.query(models.Document).offset(skip).limit(limit).all()

def create_document(db: Session, doc: schemas.DocumentCreate):
    """
    Create a new document record in the database.
    """
    db_document = models.Document(
        filename=doc.filename,
        original_filename=doc.original_filename,
        status=doc.status
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
