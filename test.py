import sqlite3

con = sqlite3.connect("main_app_db.db")
cur = con.cursor()

res = cur.execute("SELECT * FROM job_application")
res.fetchall()