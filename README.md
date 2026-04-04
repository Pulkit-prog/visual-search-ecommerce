AI Visual Search Engine for E-Commerce
A visual search engine for e-commerce that allows users to search for products using images. Users can upload an image, and the system returns visually similar products from the catalog using advanced machine learning techniques.

Tech Stack
Backend: FastAPI
Frontend: Streamlit
Feature Extraction: ResNet50 (via PyTorch)
Similarity Search: FAISS
Containerization: Docker
Working Pipeline
Image Upload: User uploads a query image
Feature Extraction: ResNet50 extracts visual features from the image
Similarity Search: FAISS performs vector similarity search against the product catalog
Results: Returns the most similar products with similarity scores
Setup Instructions
Option 1: Run with Docker (Recommended)
# Build and run all services
docker-compose up --build
Access the application:

Backend API: http://localhost:8000/docs
Frontend: http://localhost:8501
Option 2: Run Locally
Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Frontend
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py
Project Structure and Development Phases
This project structure reflects a systematic development approach:

Phase 1-2: Planning - Project setup, requirements analysis, and architecture design
Phase 3: Dataset Preparation - scripts/download_sample_catalog.py for preparing product catalog data
Phase 4: Feature Extraction & Indexing - backend/app/services/embedder.py and indexer.py for building FAISS index
Phase 5: Backend API - backend/app/main.py, schemas.py, and API endpoints in FastAPI
Phase 6: Frontend - frontend/streamlit_app.py for user interface
Phase 7: Integration - Connecting frontend to backend, testing end-to-end flow
Phase 8: Dockerization - Dockerfiles and docker-compose.yml for containerization
Notes
Dataset images are not included in the repository (ignored via .gitignore)
FAISS index files are generated at runtime and also ignored
Use the provided scripts to download sample catalog data for testing
How to use
Open Streamlit UI
Click Rebuild Index (first time)
Upload an image
Click Search
Non-Docker Run (Optional)
Backend
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
Frontend
cd frontend
python -m venv .venv
pip install -r requirements.txt
streamlit run streamlit_app.py
Notes
No paid APIs used
Runs fully on CPU
Works with your own product images
