# 🛍️ AI Visual Search Engine for E-Commerce

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![FAISS](https://img.shields.io/badge/Search-FAISS-orange)
![Status](https://img.shields.io/badge/Status-Phase%206%20Completed-success)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 📌 Overview

An AI-powered visual search system that allows users to search for products using images instead of text.  
The system extracts deep visual features and retrieves similar products from a catalog using efficient similarity search techniques.

---

## 🧰 Tech Stack

- 🔧 **Backend:** FastAPI  
- 🎨 **Frontend:** Streamlit  
- 🧠 **Feature Extraction:** ResNet50 (PyTorch)  
- 🔍 **Similarity Search:** FAISS  
- 📦 **Containerization:** Docker *(Planned)*  

---

## ⚙️ Working Pipeline

User Image Upload  
↓  
Streamlit Frontend  
↓  
FastAPI Backend  
↓  
ResNet50 (Feature Extraction)  
↓  
FAISS (Similarity Search)  
↓  
Top Similar Products Displayed  

---

## 📊 Project Progress (As per Timeline)

### ✅ Phase 1 – Requirement Analysis
- Identified limitations of text-based product search  
- Defined objectives and system scope  

### ✅ Phase 2 – System Design
- Designed architecture (FastAPI + FAISS + ResNet50 + Streamlit)  
- Planned data flow and modular structure  

### ✅ Phase 3 – Dataset Preparation
- Prepared and structured product image dataset  
- Implemented scripts for dataset handling  

### ✅ Phase 4 – Feature Extraction & Indexing
- Used ResNet50 for feature extraction  
- Generated image embeddings  
- Built FAISS index for efficient similarity search  

### ✅ Phase 5 – Backend API
- Developed FastAPI backend  
- Created endpoints for image upload and search  
- Integrated embedding + FAISS pipeline  

### ✅ Phase 6 – Frontend Development
- Built Streamlit-based user interface  
- Implemented image upload functionality  
- Displayed similar product results  
- Connected frontend with backend APIs  

---

## 📁 Project Structure

    visual-search-ecommerce/
    │
    ├── backend/              # FastAPI backend and ML pipeline
    ├── frontend/             # Streamlit UI
    ├── scripts/              # Dataset preparation scripts
    ├── docker-compose.yml    # (Planned for deployment)
    ├── README.md
    └── .gitignore

---

## 🚀 Upcoming Work

- Integration testing and performance optimization  
- Dockerization and deployment  
- Final documentation and evaluation  

---

## ▶️ How to Run

### 🔹 Backend

    cd backend
    pip install -r requirements.txt
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

👉 API Docs: http://localhost:8000/docs  

---

### 🔹 Frontend

    cd frontend
    pip install -r requirements.txt
    streamlit run streamlit_app.py

👉 Streamlit UI: http://localhost:8501  

---

## 📝 Notes

- Dataset images are not included in the repository (ignored via .gitignore)  
- FAISS index files are generated dynamically  
- Runs fully on CPU (no GPU required)  



## ⭐ Key Highlights

- 🔎 Image-based product search (no text needed)  
- 🧠 Deep learning + vector similarity search  
- ⚡ Fast and scalable architecture  
- 🛒 Real-world e-commerce use case  

## Major project for IBM

