import sqlite3

DB_PATH = "auth.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password_hashed TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()


def get_all_users(*args):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name, username, password_hashed,email,role FROM users
    ''')
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

