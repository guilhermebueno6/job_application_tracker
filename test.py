import sqlite3

con = sqlite3.connect("main_app_db.db", check_same_thread=False)
cur = con.cursor()
cur.execute("SELECT * FROM job_application")
data = []
res = cur.fetchall()
print(res)

