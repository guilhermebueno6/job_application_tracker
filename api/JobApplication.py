import sqlite3
import datetime

class JobApplication:

    con = sqlite3.connect("main_app_db.db")
    cur = con.cursor()

    def __init__(self):
        self.company = None
        self.title = None
        self.description = None
        self.skills = None
        self.link = None
        self.stage = 0
        self.date_applied = datetime.datetime.now("%Y-%m-%d")
        
    
    def saveApplication(self):
        self.cur.execute(f"INSERT INTO job_application VALUES ({self.link}, {self.company}, {self.title}, {self.description}, {self.skills}, {self.stage}, {self.date_applied})")
        self.con.commit()
        return
    