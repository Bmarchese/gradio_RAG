# RAG-based Chatbot with File Processing, ChromaDB, and Gradio

## 📖 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents in various formats such as **PDF**, **Word (DOCX)**, **TXT**, and more. The contents of these documents are processed and stored as vector embeddings in **ChromaDB**, a vector database. Using these embeddings, the system enables efficient retrieval of relevant information to augment the generation of responses by a **chatbot interface**, built with **Gradio**.

## 🚀 Key Features

- ✅ Supports multiple document formats: PDF, DOCX, TXT, etc.
- ✅ Text extraction and preprocessing pipeline.
- ✅ Embedding generation using state-of-the-art models.
- ✅ Vector storage and retrieval with **ChromaDB**.
- ✅ Conversational chatbot interface powered by **Gradio**.
- ✅ Retrieval-Augmented Generation for more accurate, context-aware responses.

## 🛠️ Tech Stack

- **Python**
- **LangChain** or **LlamaIndex** (for RAG orchestration) — optional but recommended
- **ChromaDB** (Vector Database)
- **Sentence Transformers** / **OpenAI embeddings** (for vector representation)
- **Gradio** (for chatbot interface)
- **PyMuPDF**, **python-docx** (for document parsing)
