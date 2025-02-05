from api.Scraper import Scraper
from flask import Flask, render_template, request
from api.JobApplication import JobApplication

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
    print(link)
    return render_template("add-application.html")

@app.route('/track-applications')
def trackApplications():
    jobApplications = JobApplication()
    data = jobApplications.getMyJobApplications()
    return render_template("track-applications.html", data=data)