# this is the main file that runs da biz.
# The entrypoint, the runner.  banana

from flask import Flask,render_template, request

from db_manager import find_daily_tutors

app = Flask(__name__)

@app.route('/')#route to home page
def index():
    tutors = find_daily_tutors()#gets the array of dictionaries that have the data
    return render_template('Main Display.html', tutors=tutors)#displays the data on the html page

@app.route('/student_id')
def student_sign_in(): #route to this page

    return render_template('student_id.html')

if __name__ == '__main__':
    # DB_orm.DB_setup()
    # DB_manager.create_db()
    app.run(debug=True) #kind of like the web server