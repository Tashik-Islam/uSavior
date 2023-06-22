from flask import Flask,session, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://abdullah201:saveyourgrades@abdullah1065.hhjja0s.mongodb.net/uSavior"
db = PyMongo(app).db

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/student_dashboard")
def student_dashboard():
    db.student.insert_one({'abdullah':2})
    return render_template('student_dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)