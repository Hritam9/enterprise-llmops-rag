from pathlib import Path
import sqlite3

DB_PATH = Path("data/chat_history.db")

DB_PATH.parent.mkdir(parents=True, exist_ok=True)


class Database:

    @staticmethod
    def connect():

        conn = sqlite3.connect(DB_PATH)

        conn.row_factory = sqlite3.Row

        return conn


def initialize():

    conn = Database.connect()

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS conversations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id TEXT,

            question TEXT,

            answer TEXT,

            confidence REAL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)

    conn.commit()

    conn.close()
