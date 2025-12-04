from fastapi import FastAPI
from .database import engine
from . import models
from .routers import documents

# This line creates the database tables if they don't exist.
# For production apps, you would typically use a migration tool like Alembic.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Embedding Manager API",
    description="API to manage document uploads and embeddings for the ChatVilaSeca RAG system.",
    version="0.1.0",
)

# Include the routers
app.include_router(documents.router)


@app.get("/", tags=["Health Check"])
def read_root():
    """
    Root endpoint for health check.
    """
    return {"status": "ok", "message": "Welcome to the Embedding Manager API!"}
