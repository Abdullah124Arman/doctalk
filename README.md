---
title: DocTalk
emoji: 📄
colorFrom: blue
colorTo: purple
sdk: streamlit
app_file: app.py
pinned: false
---
# 📄 DocTalk — Universal AI Document Intelligence Platform

> Chat with any document using RAG (Retrieval-Augmented Generation)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![LLM](https://img.shields.io/badge/LLM-Gemini_1.5_Flash-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector--DB-orange)

## 🌐 Live Demo
👉 👉 [DocTalk on Hugging Face](https://huggingface.co/spaces/abdarman124/doctalk)

## 🚀 What is DocTalk?
DocTalk is a RAG-based document intelligence platform where users can upload any PDF and have a context-aware conversation with it. The system retrieves exact relevant sections and uses Gemini 1.5 Flash to generate grounded, cited answers.

## ✨ Features
- 📁 **Multi-PDF Support** — Upload multiple PDFs simultaneously
- 🔍 **Semantic Search** — FAISS vector database for intelligent retrieval
- 🤖 **Gemini Powered** — Google's Gemini 1.5 Flash via Generative AI API
- 📌 **Source Citations** — See exactly which part of document answered your question
- 📝 **One-Click Summary** — Instant document summary in bullet points

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Database | FAISS |
| LLM | Gemini 1.5 Flash via Google API |
| Document Parsing | PyPDF2 |

## ⚙️ How It Works
1. User uploads PDF(s)
2. Text extracted and split into chunks
3. Chunks converted to embeddings using sentence-transformers
4. Embeddings stored in FAISS vector database
5. User asks a question
6. Semantically similar chunks retrieved from FAISS
7. Gemini generates answer based strictly on retrieved chunks
8. Source citations shown for transparency

## 🏃 Run Locally
```bash
git clone https://github.com/Abdullah124Arman/doctalk.git
cd doctalk
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 👨‍💻 Author
**Abdullah Arman** — B.Tech CSE, Parul University
- GitHub: [@Abdullah124Arman](https://github.com/Abdullah124Arman)
- LinkedIn: [Abdullah Arman](https://linkedin.com/in/abdullah-arman-755a123b3/)