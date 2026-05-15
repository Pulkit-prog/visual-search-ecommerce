from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io

from app.services.embedder import get_embedding
from app.services.indexer import search_index, rebuild_index

app = FastAPI(title="Visual Search API")

# ------------------------------------------------
# Correct catalog path inside Docker container
# ------------------------------------------------
CATALOG_DIR = "/app/backend/catalog_images"

# Serve catalog images
app.mount("/images", StaticFiles(directory=CATALOG_DIR), name="images")


@app.get("/")
def root():
    return {"message": "Visual Search API Running"}


# ------------------------------------------------
# Rebuild FAISS index
# ------------------------------------------------
@app.post("/index/rebuild")
def rebuild_catalog_index():
    try:
        rebuild_index()
        return {"status": "index rebuilt"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------------------------------------
# Search similar images
# ------------------------------------------------
# System will try to search for similar images

@app.post("/search")
async def search_image(file: UploadFile = File(...)):

    try:
        contents = await file.read()

        image = Image.open(io.BytesIO(contents)).convert("RGB")

        embedding = get_embedding(image)

        results = search_index(embedding)

        return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))