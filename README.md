# GenAI LangChain ETL (Postgres + Groq)

This repo demonstrates using **LangChain + Groq LLMs** to translate **natural language questions → SQL** over a Postgres database.

---

## 🚀 Features
- Ingest CSV into Postgres (`scripts/ingest_csv.py`)
- Query DB in natural language via LangChain + Groq (`app/nl2sql_query.py`)
- REST API with FastAPI (`/ask?question=...`)

---

## 🛠 Setup
```bash
git clone https://github.com/<your-username>/genai-langchain-etl.git
cd genai-langchain-etl
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
