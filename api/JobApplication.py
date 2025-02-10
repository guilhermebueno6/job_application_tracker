import sqlite3
import datetime
import markdown

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
        self.cur.execute(
            "INSERT INTO job_application (link, company, title, description, skills, stage, date_applied) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (self.link, self.company, self.title, self.description, self.skills, self.stage, self.date_applied)
        )
        self.con.commit()
        return
    
    def getMyJobApplications(self):
        self.cur.execute("SELECT * FROM job_application")
        data = []
        res = self.cur.fetchall()
        i=0

        for row in res:
            data.append(list(row))
            full_text = markdown.markdown(row[4])
            
            preview_text = full_text[:150]

            data[i][4] = full_text
            data[i].append(preview_text)
            i += 1

        return data
    