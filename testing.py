from data.db import get_connection

conn = get_connection()
print(
    conn.execute(
        "SELECT COUNT(*) FROM simulation_data"
    ).fetchone()[0]
)