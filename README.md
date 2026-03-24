# 🔬 ResearchMate AI

AI-powered research assistant that allows users to upload research papers (PDF) and ask questions using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload research papers (PDF)
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered question answering
- ⚡ Fast retrieval using FAISS
- 🧠 Context-based answers from documents

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **AI/NLP:** LangChain  
- **Embeddings:** HuggingFace (sentence-transformers)  
- **Vector DB:** FAISS  
- **Frontend:** HTML, CSS  

---

## 🧠 How It Works

1. Upload a PDF file  
2. Text is extracted and split into chunks  
3. Chunks are converted into embeddings  
4. Stored in FAISS vector database  
5. User asks a question  
6. Relevant chunks are retrieved  
7. AI generates an answer based on context  

---

## ▶️ Run Locally

```bash
git clone https://github.com/bejjenkisrinithya-dot/researchmate-ai.git
cd researchmate-ai
pip install -r requirements.txt
python app.py
