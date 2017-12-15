# this is the main file that runs da biz.
# The entrypoint, the runner.  banana

from flask import Flask,render_template, redirect, url_for
from flask import request
from datetime import datetime

from db_manager import find_daily_tutors, save_tutor_data, create_db  #save_student_data, create_db

app = Flask(__name__)

@app.route('/')#route to home page
def index():
    # tutors = find_daily_tutors()#gets the array of dictionaries that have the data
    return render_template('Main Display.html') #, tutors=tutors)#displays the data on the html page

@app.route('/student_sign_in', methods=["post"])
#the main page has a form that posts to here
#student login info SN,SID = name
def student_information():
    StudentName = request.form['studentName']#gets from html form/name
    StarID = request.form['starId']#gets html form/ name
    dateTime = datetime.now()   #get the time NOW!
    # save_student_data(StudentName, StarID, datetime)

    return redirect(url_for('index'))

@app.route('/login')
def login():
    return  render_template('login.html')

@app.route('/admin_menu')
def admin():
    return render_template('admin_menu.html')

@app.route('/Add_tutor', methods=["get", "post"])
def add_tutor():
    if request.method == "GET":
        return render_template('Add a tutor.html')
    else:
        name = request.form['name']
        course = request.form['course_info']
        m_time = request.form['m_time']
        t_time = request.form['t_time']
        w_time = request.form['w_time']
        tr_time = request.form['tr_time']
        f_time = request.form['f_time']

        save_tutor_data(name, course, m_time,t_time,w_time,tr_time,f_time)
        return render_template("Confirmation page.html")
# @app.route('')

# TTTTToDao:  add all the admin pages and routes, don't do actual login


if __name__ == '__main__':
    # create_db()# function creates DB when program starts
    app.run(debug=True) #kind of like the web server



# TOOODOOO:
# clock api  https://dev.fitbit.com/reference/device-api/clock/#variable-clock-