from flask import Flask, render_template, request
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
    print(link)
    return link