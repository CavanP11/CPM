import sqlite3

def initialize_database():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_password(service, username, password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO passwords (service, username, password)
        VALUES (?, ?, ?)
    """, (service, username, password))
    conn.commit()
    conn.close()

def get_password(service):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT username, password FROM passwords WHERE service=?
    """, (service,))
    result = cursor.fetchone()
    conn.close()
    return result

def delete_password(service):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM passwords WHERE service=?
    """, (service,))
    conn.commit()
    conn.close()
