from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000

    # Use absolute container paths so they match docker-compose mounts.
    # - catalog images are mounted to /app/catalog_images
    # - storage (faiss index + meta) is mounted to /app/backend/app/storage
    CATALOG_DIR: str = "/app/catalog_images"
    STORAGE_DIR: str = "/app/backend/app/storage"

    TOP_K: int = 8


settings = Settings()
