import sqlite3
import os

# Initialize the database and create necessary tables
def initialize_database():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    # Create table for passwords
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Create table for metadata (e.g., salt, master password hash)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)

    # Check if the salt exists; if not, generate and store it
    cursor.execute("SELECT value FROM metadata WHERE key='salt'")
    if cursor.fetchone() is None:
        salt = os.urandom(16)  # Generate 16-byte salt
        cursor.execute("INSERT INTO metadata (key, value) VALUES (?, ?)", ("salt", salt.hex()))
        print("Salt generated and stored in the database.")

    conn.commit()
    conn.close()

# Retrieve the salt from the database
def get_salt():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM metadata WHERE key='salt'")
    result = cursor.fetchone()
    conn.close()
    if result:
        return bytes.fromhex(result[0])
    else:
        raise ValueError("Salt not found in the database.")

# Store the master password hash
def store_master_password_hash(password_hash):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO metadata (key, value) VALUES (?, ?)", ("master_password_hash", password_hash))
    conn.commit()
    conn.close()

# Retrieve the master password hash
def get_master_password_hash():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM metadata WHERE key='master_password_hash'")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Add a password entry
def add_password(service, username, password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO passwords (service, username, password)
        VALUES (?, ?, ?)
    """, (service, username, password))
    conn.commit()
    conn.close()

# Retrieve a password entry by service
def get_password(service):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT username, password FROM passwords WHERE service=?
    """, (service,))
    result = cursor.fetchone()
    conn.close()
    return result

# Delete a password entry by service
def delete_password(service):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM passwords WHERE service=?
    """, (service,))
    conn.commit()
    conn.close()

# Fetch all stored passwords
def get_passwords():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT service, username, password FROM passwords")
    results = cursor.fetchall()
    conn.close()
    return results
