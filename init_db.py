import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    address TEXT,
    email TEXT UNIQUE,
    phone TEXT
)
""")

conn.close()

print("Database created!")