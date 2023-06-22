from flask import Flask,session, render_template, request, redirect

app = Flask(__name__)


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/student_dashboard")
def student_dashboard():
    return render_template('student_dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)