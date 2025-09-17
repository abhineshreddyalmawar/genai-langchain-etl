from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv()
url = os.getenv("DATABASE_URL")
print("DATABASE_URL:", url)

eng = create_engine(url, future=True)
with eng.connect() as c:
    db, port = c.execute(text("select current_database(), inet_server_port()")).fetchone()
    print("USING -> DB:", db, " PORT:", port)

    tables = c.execute(text("""
        select table_schema, table_name
        from information_schema.tables
        where table_schema='public'
        order by table_name
    """)).fetchall()
    print("PUBLIC TABLES:", tables)

    if any(t[1] == "sales" for t in tables):
        rows = c.execute(text("select * from public.sales limit 5")).fetchall()
        print("\nSAMPLE ROWS FROM sales:")
        for r in rows:
            print(dict(r._mapping))
