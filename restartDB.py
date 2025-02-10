import sqlite3
import os

DB_PATH = "main_app_db.db"

if os.path.exists(DB_PATH):
    try:
        os.remove(DB_PATH)
        print(f"Database '{DB_PATH}' has been successfully deleted.")
    except Exception as e:
        print(f"Error deleting database: {e}")
else:
    print(f"Database '{DB_PATH}' does not exist.")
print("Creating local database...")
con = sqlite3.connect("main_app_db.db")
print("Database created")
cur = con.cursor()
print("Creating table to store job applications...")
cur.execute("CREATE TABLE job_application (id INTEGER PRIMARY KEY AUTOINCREMENT, link TEXT, company TEXT, title TEXT, description TEXT, skills TEXT, stage TEXT, date_applied TEXT)")
print("Table created")