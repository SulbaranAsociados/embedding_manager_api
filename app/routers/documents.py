import shutil
from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import os

from .. import crud, models, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
    responses={404: {"description": "Not found"}},
)

# Define a directory to store uploaded files
UPLOAD_DIRECTORY = "uploads"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@router.get("/", response_model=List[schemas.Document])
def read_documents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all documents.
    """
    documents = crud.get_documents(db, skip=skip, limit=limit)
    return documents

@router.post("/upload/", response_model=schemas.Document)
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Upload a document file.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file name provided.")

    # Create a safe filename and define the path
    # Note: In a real-world scenario, generate a unique ID for the filename
    # to prevent overwrites and handle file name collisions.
    original_filename = file.filename
    safe_filename = f"{original_filename}" # simplified for now
    file_path = os.path.join(UPLOAD_DIRECTORY, safe_filename)

    # Save the file
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    # Create the database entry
    document_create = schemas.DocumentCreate(
        filename=safe_filename,
        original_filename=original_filename
    )
    db_document = crud.create_document(db, doc=document_create)
    
    return db_document
