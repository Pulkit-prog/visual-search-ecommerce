import os
import faiss
import numpy as np
from PIL import Image

from app.services.embedder import get_embedding

CATALOG_DIR = "/app/backend/catalog_images"

index = None
image_paths = []


def rebuild_index():

    global index
    global image_paths

    embeddings = []
    image_paths = []

    for file in os.listdir(CATALOG_DIR):

        if file.lower().endswith((".jpg", ".jpeg", ".png")):

            path = os.path.join(CATALOG_DIR, file)

            try:
                image = Image.open(path).convert("RGB")

                emb = get_embedding(image)

                embeddings.append(emb)

                image_paths.append(file)

            except Exception:
                continue

    if len(embeddings) == 0:
        raise Exception("No images found in catalog_images")

    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(embeddings)


def search_index(query_embedding, k=8):

    global index

    if index is None:
        raise Exception("Index not built. Run rebuild_index first.")

    query = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query, k)

    results = []

    for i, idx in enumerate(indices[0]):

        if idx < len(image_paths):

            results.append({
                "image": image_paths[idx],
                "score": float(1 / (1 + distances[0][i]))
            })

    return results