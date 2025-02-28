from api.Scraper import Scraper
from flask import Flask, render_template, request, redirect, url_for
from api.JobApplication import JobApplication
import os
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add-application')
def addApplication():
    return render_template("add-application.html")

@app.route('/add-new-application', methods=['POST'])
def addNewApplication():
    link = request.form['link']
    scraper = Scraper()
    scraper.archiveJob(link)
    return render_template("add-application.html")

@app.route('/track-applications')
def trackApplications():
    jobApplications = JobApplication()
    data = jobApplications.getMyJobApplications()
    return render_template("track-applications.html", data=data)

@app.route("/update-status/<int:job_id>", methods=['POST'])
def update_status(job_id):
    new_status = request.form.get("status")

    conn = sqlite3.connect("main_app_db.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE job_application SET stage = ? WHERE id = ?", (new_status, job_id))
    conn.commit()
    conn.close()

    return redirect(url_for("trackApplications"))
@app.route("/delete/<int:job_id>")
def delete_application(job_id):
    conn = sqlite3.connect("main_app_db.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM job_application WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()

    return redirect(url_for("trackApplications"))

if __name__ == "__main__":
    app.run(host="jobapplication.local", port=80, debug=True)