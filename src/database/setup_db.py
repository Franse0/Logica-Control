"""
Database setup script - creates tables from schema.sql
"""

import sqlite3
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()


def setup_database():
    """Create database and tables from schema"""
    # Get database path from env or use default
    db_path = os.getenv("DATABASE_PATH", "data/gimnasio.db")

    # Create data directory if it doesn't exist
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    # Read schema
    schema_file = Path(__file__).parent / "schema.sql"
    with open(schema_file, 'r', encoding='utf-8') as f:
        schema = f.read()

    # Create database and execute schema
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

    print(f"✅ Database created at: {db_path}")
    print("✅ Tables created successfully")


if __name__ == "__main__":
    setup_database()
