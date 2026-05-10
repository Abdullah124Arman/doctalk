
---
title: DocTalk
emoji: 📄
colorFrom: purple
colorTo: blue
sdk: streamlit
sdk_version: 1.57.0
app_file: app.py
pinned: false
---
# 📄 DocTalk — Universal AI Document Intelligence Platform

> Chat with any document using RAG (Retrieval-Augmented Generation)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![LLaMA](https://img.shields.io/badge/LLaMA-3.3--70b-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector--DB-orange)

## 🌐 Live Demo
👉 👉 [DocTalk on Hugging Face](https://huggingface.co/spaces/abdarman124/doctalk)

## 🚀 What is DocTalk?
DocTalk is a RAG-based document intelligence platform where users can upload any PDF and have a context-aware conversation with it. The system retrieves exact relevant sections and uses LLaMA 3 to generate grounded, cited answers.

## ✨ Features
- 📁 **Multi-PDF Support** — Upload multiple PDFs simultaneously
- 🔍 **Semantic Search** — FAISS vector database for intelligent retrieval
- 🤖 **LLaMA 3 Powered** — Meta's LLaMA 3.3-70b via Groq API
- 📌 **Source Citations** — See exactly which part of document answered your question
- 📝 **One-Click Summary** — Instant document summary in bullet points
- 💬 **Chat History** — Full conversation memory within session

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Database | FAISS |
| LLM | LLaMA 3.3-70b via Groq API |
| Document Parsing | PyPDF2 |

## ⚙️ How It Works
1. User uploads PDF(s)
2. Text extracted and split into chunks
3. Chunks converted to embeddings using sentence-transformers
4. Embeddings stored in FAISS vector database
5. User asks a question
6. Semantically similar chunks retrieved from FAISS
7. LLaMA 3 generates answer based strictly on retrieved chunks
8. Source citations shown for transparency

## 🏃 Run Locally
```bash
git clone https://github.com/Abdullah124Arman/doctalk.git
cd doctalk
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Add your GROQ_API_KEY to .env file
streamlit run app.py
```

## 👨‍💻 Author
**Abdullah Arman** — B.Tech CSE, Parul University
- GitHub: [@Abdullah124Arman](https://github.com/Abdullah124Arman)
- LinkedIn: [Abdullah Arman](https://linkedin.com/in/abdullah-arman-755a123b3/)