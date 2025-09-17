# GenAI LangChain ETL (Postgres + Groq)

🚀 End-to-end ETL pipeline powered by **LangChain**, **PostgreSQL**, and **Groq LLMs**, demonstrating **natural language to SQL (NL→SQL)** for analytics.  
This project highlights **Data Engineering + GenAI integration**, making it portfolio-ready for Data Engineer roles.

---

## 📖 Overview
This project demonstrates how to:
- Ingest raw CSV data into a **Postgres** database  
- Run ETL transformations using Python + SQLAlchemy  
- Ask **natural language questions** → get **SQL queries** generated → see live results  
- Use **LangChain** with **Groq’s LLMs** for query generation  
- Showcase **end-to-end ETL + analytics workflows**  

---

## ⚙️ Tech Stack
- **Python**: Pandas, SQLAlchemy, dotenv  
- **PostgreSQL**: local DB (via pgAdmin or Docker)  
- **LangChain**: orchestration for NL→SQL  
- **Groq LLMs**: `llama-3.1-8b-instant`  
- **ETL Scripts**: ingestion, DB check, and query execution  

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/abhineshreddyalmawar/genai-langchain-etl.git
cd genai-langchain-etl
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` → `.env` and update:
```env
GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=postgresql+psycopg2://postgres:your_password@127.0.0.1:5432/genai
```

### 5. Run Postgres (via Docker or local install)
```bash
docker-compose up -d
```

---

## 📊 Usage

### 1. Ingest CSV into Postgres
```bash
python -m scripts.ingest_csv --csv data/sample_sales.csv --table sales
```

### 2. Check DB tables
```bash
python -m scripts.check_db
```

### 3. Ask NL→SQL query
```bash
python -m app.nl2sql_query --question "average order value by customer_city"
```

✅ Example generated SQL:
```sql
SELECT customer_city, AVG(revenue) AS avg_order_value
FROM sales
GROUP BY customer_city;
```

✅ Example result:

| customer_city | avg_order_value |
|---------------|-----------------|
| New York      | 144.49          |
| Chicago       | 45.00           |
| Miami         | 198.00          |
| San Francisco | 240.00          |

---

## 📂 Project Structure
```
app/          # Core app (DB connection, NL→SQL logic)
scripts/      # ETL scripts (ingest_csv, check_db, etc.)
data/         # Sample CSVs
docs/         # Screenshots / DB outputs
README.md     # Project overview
requirements.txt
docker-compose.yml
```

---

## 🖼️ Screenshots

### CSV ingestion
![CSV Ingestion](docs/csv_ingestion.png)

### Database check
![DB Tables](docs/check_db.png)

### NL→SQL query output
![Query Result](docs/query_result.png)

*(Screenshots are stored inside `docs/` folder — add your own screenshots here for better recruiter visibility.)*

---

## 🧑‍💻 Author
**Abhinesh Reddy Almawar**  
🎯 Targeting **Data Engineer roles with GenAI extension** (U.S. OPT → H-1B sponsorship)  

---
