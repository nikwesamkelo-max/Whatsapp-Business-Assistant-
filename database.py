import sqlite3

DB_NAME = "whatsapp.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        bot_response TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_message(user_message: str, bot_response: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO messages (user_message, bot_response)
        VALUES (?, ?)
    """, (user_message, bot_response))

    conn.commit()
    conn.close()


def get_all_messages():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")
    rows = cursor.fetchall()

    conn.close()
    return rows
