from fastapi import FastAPI, Query
from app.config import DATABASE_URL
from app.db import get_engine
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from sqlalchemy import text

app = FastAPI(title="genai-langchain-etl")

SYSTEM = ("You are a careful data analyst. Generate ONLY SQL for a {dialect} database. "
          "No DDL/DML. Use exact table/column names. Return raw SQL only.")
USER_TMPL = "Question: {question}\nSchema:\n{schema}\nReturn SQL only."

def build_chain(db: SQLDatabase):
    model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0)
    system = SYSTEM.format(dialect=db._engine.dialect.name)
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", USER_TMPL)])
    return (
        {"question": RunnablePassthrough(), "schema": lambda q: db.get_table_info()}
        | prompt | model | StrOutputParser()
    )

@app.get("/ask")
def ask(question: str = Query(..., description="Natural language question")):
    eng = get_engine()
    db = SQLDatabase.from_uri(DATABASE_URL)
    chain = build_chain(db)
    sql = chain.invoke(question).strip()
    if sql.startswith("```"):
        sql = sql.strip("`")
        if sql.lower().startswith("sql"):
            sql = sql[3:].strip()
    with eng.connect() as conn:
        result = conn.execute(text(sql))
        rows = [dict(r._mapping) for r in result.fetchall()]
        return {"sql": sql, "rows": rows}
