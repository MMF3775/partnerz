# Task 1: Retrieval-Augmented Q&A Agent

This task implements a **Retrieval-Augmented Generation (RAG) agent** that can answer questions using the exported Intercom Help Center (`articles.json`).

---

## Project Overview
- **Data ingestion & indexing**: Parse the `articles.json`, chunk content, embed it using OpenAI embeddings, and store in a FAISS vector database.
- **Agent implementation**: Query the FAISS index, retrieve relevant context, and generate concise answers with an LLM.
- **Documentation & testing**: Includes setup instructions, usage guide, and automated tests.

---
This app make simple retriever rag and store it as faiss in database folder.

This app with help of codes in rag folder, load documents and make faiss file.

This can extend to various of file formats.

---

### To run this app 

1- Run docker
2- make venv, install requirements and run main.py