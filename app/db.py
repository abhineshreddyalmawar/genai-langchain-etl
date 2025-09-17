from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from app.config import DATABASE_URL

_engine: Engine | None = None

def get_engine() -> Engine:
    global _engine
    if _engine is None:
        _engine = create_engine(DATABASE_URL, future=True)
    return _engine

def execute(sql: str):
    eng = get_engine()
    with eng.connect() as conn:
        return conn.execute(text(sql))
