import sqlite3

DB_NAME = "plague.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():

    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS simulation_data (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        day INTEGER,

        state TEXT,

        healthy INTEGER,

        infected INTEGER,

        dead INTEGER,

        gdp REAL,

        support REAL

    )
    """)

    conn.commit()

    conn.close()

def clear_db():

    conn = get_connection()

    conn.execute(
        "DELETE FROM simulation_data"
    )

    conn.commit()

    conn.close()