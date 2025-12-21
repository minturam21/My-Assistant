import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "memory", "long_term.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            mem_key TEXT NOT NULL,
            mem_value TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def store_memory(category: str, key: str, value: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO memory (category, mem_key, mem_value, created_at) VALUES (?, ?, ?, ?)",
        (category, key, value, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()


def recall_memory(keyword: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT category, mem_key, mem_value, created_at FROM memory WHERE mem_key LIKE ?",
        (f"%{keyword}%",)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
