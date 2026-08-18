import sys
import streamlit_authenticator as stauth
import sqlite3
from services.auth_db import init_db, get_all_users
import getpass

def add():
    name = input("Enter name: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    email = input("Enter email: ")
    role = input("Enter role (admin/user): ")

    # Hashing
    hasher = stauth.Hasher([password])
    password_hash = hasher.generate()[0]
    conn = sqlite3.connect("auth.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (name, username, password_hashed, email, role) VALUES (?, ?, ?, ?, ?)
        ''', (name, username, password_hash, email, role))
        conn.commit()
        print(f"User created: {username, email}")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
    finally:    
        conn.close()

    



def list_users():
    users = get_all_users()
    for user in users:
        print(f"Name: {user['name']}, Username: {user['username']}, Email: {user['email']}, Role: {user['role']}")

def remove():
    username = sys.argv[2] if len(sys.argv) > 2 else input("Enter username to remove: ")
    conn = sqlite3.connect("auth.db")
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM users WHERE username = ?
    ''', (username,))
    conn.commit()
    conn.close()
    print(f"User removed: {username}")



if __name__ == "__main__":
    init_db()
    if len(sys.argv) < 2:
        print("Usage: python manage_users.py [add|list|remove]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add":
        add()
    elif command == "list":
        list_users()
    elif command == "remove":
        remove()
    else:
        print(f"Unknown command {sys.argv[1]}. Use 'add', 'list', or 'remove'.")


