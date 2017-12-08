# this is the main file that runs da biz.
# The entrypoint, the runner.  banana

from flask import Flask,render_template, redirect, url_for
from flask import request
from datetime import datetime

from db_manager import find_daily_tutors, save_student_data

app = Flask(__name__)

@app.route('/')#route to home page
def index():
    tutors = find_daily_tutors()#gets the array of dictionaries that have the data
    return render_template('Main Display.html', tutors=tutors)#displays the data on the html page

@app.route('/student_sign_in', methods=["post"])
def student_information():
    StudentName = request.form['studentName']
    StarID = request.form['starId']
    dateTime = datetime.now()   #get the time NOW!
    save_student_data(StudentName, StarID, datetime)

    return redirect(url_for('index'))



if __name__ == '__main__':
    # DB_orm.DB_setup()
    # DB_manager.create_db()
    app.run(debug=True) #kind of like the web server



# TOOODOOO:
# clock api  https://dev.fitbit.com/reference/device-api/clock/#variable-clock-