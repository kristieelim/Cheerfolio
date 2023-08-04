# To be run only once in the beginning
import sqlite3

# Connect to the database (creates if doesn't exist)
conn = sqlite3.connect('cheerfolio.db')

# Create a cursor
db = conn.cursor()

# Create database tables
create_users_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL
);
'''

create_entries_table_query = '''
CREATE TABLE IF NOT EXISTS entries (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    entry TEXT NOT NULL,
    category TEXT DEFAULT "default" NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
'''

db.execute(create_users_table_query)
db.execute(create_entries_table_query)

# Commit changes and close connection
conn.commit()
conn.close()
