from flask import Flask,session, render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://abdullah201:saveyourgrades@abdullah1065.hhjja0s.mongodb.net/uSavior"
db = PyMongo(app).db

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

#---------------------------------------------Student---------------------------------------------------------
@app.route("/student_login")
def student_login():
    return render_template('student_login.html')

@app.route("/student_registration")
def student_registration():
    return render_template('student_registration.html')

@app.route("/student_dashboard")
def student_dashboard():
    #db.student.insert_one({'abdullah':2})
    return render_template('student_dashboard.html')

@app.route("/student_edit_profile")
def student_edit_profile():
    return render_template('student_editProfile.html')

@app.route("/student_my_courses")
def student_my_courses():
    return render_template('student_myCourses.html')

@app.route("/student_View_AllCourses")
def student_View_AllCourses():
    return render_template('student_ViewAllCourses.html')

@app.route("/student_View_Cart")
def student_View_Cart():
    return render_template('student_ViewCart.html')
#---------------------------------------------Instructor---------------------------------------------------------
@app.route("/instructor_login")
def instructor_login():
    return render_template('instructor_login.html')

@app.route("/instructor_registration")
def instructor_registration():
    return render_template('instructor_registration.html')

@app.route("/instructor_dashboard")
def instructor_dashboard():
    return render_template('instructor_dashboard.html')

@app.route("/instructor_edit_profile")
def instructor_edit_profile():
    return render_template('instructor_editProfile.html')

@app.route("/instructor_my_courses")
def instructor_my_courses():
    return render_template('instructor_myCourses.html')

@app.route("/instructor_view_AllCourses")
def instructor_view_AllCourses():
    return render_template('instructor_ViewAllCourses.html')


#---------------------------------------------Admin---------------------------------------------------------

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template('admin_dashboard.html')

#---------------------------------------------Others---------------------------------------------------------

@app.route("/forgotten_password")
def forgotten_password():
    return render_template('forgotten_password.html')

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
