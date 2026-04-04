# AI Visual Search Engine for E-Commerce

A visual search engine for e-commerce that allows users to search for products using images. Users can upload an image, and the system returns visually similar products from the catalog using advanced machine learning techniques.

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Feature Extraction**: ResNet50 (via PyTorch)
- **Similarity Search**: FAISS
- **Containerization**: Docker

## Working Pipeline

1. **Image Upload**: User uploads a query image
2. **Feature Extraction**: ResNet50 extracts visual features from the image
3. **Similarity Search**: FAISS performs vector similarity search against the product catalog
4. **Results**: Returns the most similar products with similarity scores

## Setup Instructions

### Option 1: Run with Docker (Recommended)

```bash
# Build and run all services
docker-compose up --build
```

Access the application:
- Backend API: http://localhost:8000/docs
- Frontend: http://localhost:8501

### Option 2: Run Locally

#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Project Structure and Development Phases

This project structure reflects a systematic development approach:

- **Phase 1-2: Planning** - Project setup, requirements analysis, and architecture design
- **Phase 3: Dataset Preparation** - `scripts/download_sample_catalog.py` for preparing product catalog data
- **Phase 4: Feature Extraction & Indexing** - `backend/app/services/embedder.py` and `indexer.py` for building FAISS index
- **Phase 5: Backend API** - `backend/app/main.py`, `schemas.py`, and API endpoints in FastAPI
- **Phase 6: Frontend** - `frontend/streamlit_app.py` for user interface
- **Phase 7: Integration** - Connecting frontend to backend, testing end-to-end flow
- **Phase 8: Dockerization** - `Dockerfile`s and `docker-compose.yml` for containerization

## Notes

- Dataset images are not included in the repository (ignored via .gitignore)
- FAISS index files are generated at runtime and also ignored
- Use the provided scripts to download sample catalog data for testing

## How to use

1. Open Streamlit UI
2. Click Rebuild Index (first time)
3. Upload an image
4. Click Search

## Non-Docker Run (Optional)

### Backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
python -m venv .venv
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Notes

- No paid APIs used
- Runs fully on CPU
- Works with your own product images
