from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
tasklist = []

@app.route("/")
def home():
    return render_template("index.html",task = tasklist)

@app.route("/addtask",methods = ["POST"])
def addtask():
    if request.method == "POST":
        task = request.form["task"]
        tasklist.append(task)
        print(tasklist)
    
    return render_template("index.html",task = tasklist)

@app.route("/clear",methods = ["POST"])
def clear():
    if request.method == "POST":
        tasklist.pop()
    return render_template("index.html",task = tasklist)

@app.route("/clearall",methods = ["POST"])
def clearall():
    if request.method == "POST":
        tasklist.clear()
        print(tasklist)
    return render_template("index.html",task = tasklist)
