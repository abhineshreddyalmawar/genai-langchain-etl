# scripts/peek_db.py
import argparse
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--table", default="sales", help="table to preview")
    args = parser.parse_args()

    load_dotenv()
    url = os.getenv("DATABASE_URL")
    if not url:
        raise SystemExit("DATABASE_URL not set. Check your .env")

    eng = create_engine(url, future=True)
    with eng.connect() as c:
        db, port = c.execute(text("select current_database(), inet_server_port()")).fetchone()
        print(f"USING -> DB: {db}  PORT: {port}")

        tables = c.execute(text("""
            select table_schema, table_name
            from information_schema.tables
            where table_schema='public'
            order by table_name
        """)).fetchall()
        print("PUBLIC TABLES:", tables or "None")

        # preview rows if table exists
        if any(t[1] == args.table for t in tables):
            rows = c.execute(text(f"select * from public.{args.table} limit 5")).fetchall()
            print(f"\nSAMPLE ROWS FROM {args.table}:")
            for r in rows:
                print(dict(r._mapping))
        else:
            print(f"\nTable '{args.table}' not found in public schema.")

if __name__ == "__main__":
    main()
