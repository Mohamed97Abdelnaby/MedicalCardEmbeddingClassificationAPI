<h1 align="center" style="color:#4CAF50;">🌟 Medical Cards Embedding Classification API 🌟</h1>

<p align="center">
    <img src="https://img.shields.io/badge/FastAPI-0.95.2-brightgreen" alt="FastAPI">
    <img src="https://img.shields.io/badge/License-MIT-blue" alt="MIT License">
</p>

---

## ✨ **Features**
- 🔍 **Find Similar Card**: Easily find the most similar medical card based on a given sample text using state-of-the-art embeddings.
- 📝 **Add New Card**: Seamlessly add new medical cards to your database with automatically generated embeddings.

---

## 🎨 **Project Structure**

```plaintext
app/
├── __init__.py                # Package initializer
├── main.py                    # 🚀 Entry point for the FastAPI application
├── models/                    # Contains the Pydantic models
│   ├── __init__.py            # Makes 'models' a package
│   └── card_models.py         # Defines Pydantic models (e.g., CardInput)
├── services/                  # Contains service functions for the application
│   ├── __init__.py            # Makes 'services' a package
│   ├── embedding_service.py   # Handles embedding generation and similarity computation
│   └── file_service.py        # Handles loading and saving of the CSV/Excel file
└── requirements.txt           # Lists project dependencies

```
---

<h1 align="center" style="color:#4CAF50;">🚀 Getting Started with Medical Cards Embedding Classification API</h1> <p align="center"> <img src="https://img.shields.io/badge/FastAPI-0.95.2-brightgreen" alt="FastAPI"> <img src="https://img.shields.io/badge/License-MIT-blue" alt="MIT License"> </p>

---

## 📦 **Step 1: Clone the Repository**

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/medical-cards-embedding-classification.git
cd medical-cards-embedding-classification
