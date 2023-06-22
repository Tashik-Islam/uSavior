from flask import Flask,session, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://abdullah201:saveyourgrades@abdullah1065.hhjja0s.mongodb.net/uSavior"
db = PyMongo(app).db

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/student_login")
def student_login():
    return render_template('student_login.html')

@app.route("/student_registration")
def student_registration():
    return render_template('student_registration.html')

@app.route("/instructor_login")
def instructor_login():
    return render_template('instructor_login.html')

@app.route("/instructor_registration")
def instructor_registration():
    return render_template('instructor_registration.html')

@app.route("/forgotten_password")
def forgotten_password():
    return render_template('forgotten_password.html')

@app.route("/student_dashboard")
def student_dashboard():
    #db.student.insert_one({'abdullah':2})
    return render_template('student_dashboard.html')

@app.route("/instructor_dashboard")
def instructor_dashboard():
    return render_template('instructor_dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)