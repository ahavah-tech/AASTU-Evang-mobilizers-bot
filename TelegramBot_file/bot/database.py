import sqlite3
from datetime import datetime
from .config import DATABASE

def db():
    return sqlite3.connect(DATABASE)

def init_db():
    conn = db()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        username TEXT,
        message TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_chat(uid, username, text):
    conn = db()
    c = conn.cursor()
    c.execute(
        "INSERT INTO chat_history (user_id, username, message, timestamp) VALUES (?,?,?,?)",
        (uid, username, text, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()
