from flask import Flask,session, render_template, request, redirect
from flask_pymongo import PyMongo
from datetime import date, datetime

app = Flask(__name__)
app.secret_key = 'super secret key'

app.config["MONGO_URI"] = "mongodb+srv://abdullah201:saveyourgrades@abdullah1065.hhjja0s.mongodb.net/uSavior"
db = PyMongo(app).db

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

#---------------------------------------------Student---------------------------------------------------------
@app.route("/student_login", methods = ['POST', 'GET'])
def student_login():
    if request.method == 'GET': 
        if 'email' in session.keys(): return redirect('/student_dashboard')
        return render_template('student_login.html', **locals())
    elif request.method == 'POST':
        recieved = request.form
        found = db.student.find_one({'email':recieved['email'],'password':recieved['password']})
        if found is None: return redirect('/student_login') 
        session['email'] = recieved['email']
        return redirect('/student_dashboard')

        

@app.route("/student_registration", methods = ['POST', 'GET'])
def student_registration():
    message = None
    if request.method == 'GET': 
        if 'email' in session.keys(): return redirect('/student_dashboard')
        return render_template('student_registration.html', **locals())
    elif request.method == 'POST':
        recieved = request.form
        found = db.student.find_one({'email':recieved['email']})
        if found is not None: return redirect('/student_registration')
        elif recieved ['password'] != recieved ['password_repeat']: return redirect('/student_registration')
        db.student.insert_one(dict(recieved))
        return redirect('/student_login')      
    

@app.route("/student_dashboard")
def student_dashboard():
    if 'email' not in session.keys(): return redirect('/student_login')
    data, today = db.student.find_one({'email':session['email']}), date.today()
    print()
    date_of_birth = datetime.strptime(data['birthday'], "%Y-%m-%d").date()
    age = today.year - date_of_birth.year
    if today.month < date_of_birth.month or (today.month == date_of_birth.month and today.day < date_of_birth.day): age -= 1
    return render_template('student_dashboard.html', **locals())

@app.route("/student_edit_profile")
def student_edit_profile():
    if 'email' not in session.keys(): return redirect('/student_login')
    data = db.student.find_one({'email':session['email']})
    return render_template('student_editProfile.html', **locals())

@app.route("/student_my_courses")
def student_my_courses():
    if 'email' not in session.keys(): return redirect('/student_login')
    return render_template('student_myCourses.html', **locals())

@app.route("/student_View_AllCourses")
def student_View_AllCourses():
    if 'email' not in session.keys(): return redirect('/student_login')
    return render_template('student_ViewAllCourses.html', **locals())

@app.route("/specific_course_details")
def student_specific_course_details():
    if 'email' not in session.keys(): return redirect('/student_login')
    return render_template('specific_course_details.html')

@app.route("/student_View_Cart")
def student_View_Cart():
    if 'email' not in session.keys(): return redirect('/student_login')
    return render_template('student_ViewCart.html', **locals())

@app.route("/play_video")
def student_play_video():
    if 'email' not in session.keys(): return redirect('/student_login')
    return render_template('play_video.html', **locals())

@app.route("/video_list")
def student_video_list():
    if 'email' not in session.keys(): return redirect('/student_login')
    return render_template('video_list.html', **locals())

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

@app.route("/admin")
def admin_dashboard():
    return render_template('admin_dashboard.html')

#---------------------------------------------Others---------------------------------------------------------

@app.route("/forgotten_password")
def forgotten_password():
    return render_template('forgotten_password.html')

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

@app.route("/showError")
def showError():
    return render_template('showError.html', **locals())

@app.route("/logout")
def logout():
    if 'email' in session.keys():
        session.pop('email')
    return redirect('/home')


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)
