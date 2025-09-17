import argparse
import pandas as pd
from sqlalchemy import text
from app.db import get_engine

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, help="Path to CSV file")
    parser.add_argument("--table", required=True, help="Target table name")
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    eng = get_engine()
    with eng.begin() as conn:
        df.to_sql(args.table, conn, if_exists="replace", index=False, schema="public")

        # Optional: create common derived columns for demo
        try:
            conn.execute(text(f"""
                ALTER TABLE {args.table}
                ADD COLUMN IF NOT EXISTS revenue NUMERIC;
            """))
            conn.execute(text(f"""
                UPDATE {args.table}
                SET revenue = quantity * unit_price
            """))
        except Exception:
            # SQLite fallback (no IF NOT EXISTS on alter add in older versions)
            pass
    print(f"Ingested {len(df)} rows into table '{args.table}'.")

if __name__ == "__main__":
    main()
