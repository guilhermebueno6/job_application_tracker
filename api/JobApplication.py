import sqlite3
import datetime

class JobApplication:

    con = sqlite3.connect("main_app_db.db", check_same_thread=False)
    cur = con.cursor()

    def __init__(self):
        self.company = None
        self.title = None
        self.description = None
        self.skills = None
        self.link = None
        self.stage = 0
        self.date_applied = datetime.date.today()
        
    
    def saveApplication(self):
        print({self.link}, {self.company}, {self.title}, {self.description}, {self.skills}, {self.stage}, {self.date_applied})
        self.cur.execute(
            "INSERT INTO job_application VALUES (?, ?, ?, ?, ?, ?, ?)", 
            (self.link, self.company, self.title, self.description, self.skills, self.stage, self.date_applied)
        )
        self.con.commit()
        return
    
    def getMyJobApplications(self):
        self.cur.execute("SELECT * FROM job_application")
        res = self.cur.fetchall()
        print(res)

        return res
    