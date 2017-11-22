# this is the main file that runs da biz.
# The entrypoint, the runner.  banana

from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')#route to home page
def index():
    return render_template('fun_time.html')


if __name__ == '__main__':
    # DB_orm.DB_setup()
    # DB_manager.create_db()
    app.run(debug=True) #kind of like the web server