import sqlite3
import os
from passlib.hash import sha256_crypt

# Database path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "wellness.db")

# Ensure database folder exists
os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)

# Connect DB
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# Initialize schema
def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT,
        full_name TEXT,
        age INTEGER,
        gender TEXT,
        language TEXT
    )
    """)
    conn.commit()

init_db()

# Register user
def register_user(email, password, full_name, age, gender, language="English"):
    hashed = sha256_crypt.hash(password)
    try:
        cursor.execute("""
            INSERT INTO users (email, password, full_name, age, gender, language)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (email, hashed, full_name, age, gender, language))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # email already exists

# Login
def login_user(email, password):
    cursor.execute("SELECT id, password FROM users WHERE email=?", (email,))
    row = cursor.fetchone()
    if row and sha256_crypt.verify(password, row[1]):
        return row[0]  # return user_id
    return None

# Get profile
def get_user(user_id):
    cursor.execute("SELECT id, email, full_name, age, gender, language FROM users WHERE id=?", (user_id,))
    return cursor.fetchone()

# Update profile
def update_user(user_id, full_name, age, gender, language):
    cursor.execute("""
        UPDATE users
        SET full_name=?, age=?, gender=?, language=?
        WHERE id=?
    """, (full_name, age, gender, language, user_id))
    conn.commit()

# Change password
def change_password(user_id, new_password):
    hashed = sha256_crypt.hash(new_password)
    cursor.execute("UPDATE users SET password=? WHERE id=?", (hashed, user_id))
    conn.commit()
