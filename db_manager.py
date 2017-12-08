import sqlite3 as sql

sqlite_file = 'itech_tutor_program_db.sqlite'
def find_daily_tutors():
    daily_tutors = [{
        "name": "Tech Tutor 1",
        "courses": "ITEC 1050, 1100, 1234",
        "availability": "2 - 6"
    },
        {
            "name": "Tech Tutor 2",
            "courses": "ITEC 2950, 1150, 1234",
            "availability": "2 - 6"
        },
        {
            "name": "Tech Tutor 3",
            "courses": "ITEC 2950, 1150, 1234",
            "availability": "10 - 12"
        }, ]
    return daily_tutors

#replace with a database quesry
#ned to build these tables for the search
#function to set up database, call that when progrm starts up
#if name = main, the entrypoint check cookie


def create_db():  # call when start up the server
    print("--->creating the database<---")  # for testing

    conn_man = sql.connect(sqlite_file)  # not a great way to do this, needs framework
    cursor = conn_man.cursor()
    with open("schema.sql", "r") as schema:
        create_table = schema.read()
        cursor.executescript(create_table)

    # cursor.commit()
    conn_man.close()

def save_student_data(name, star, timestamp):
    print(name, star, timestamp)
    print("saving to the database...success")
    #TODO: do this
    #datetime.now is an object, when stored in a database need to parse
    #in the sqlite.3 connect google python sqlite datetime
    # (connection string   filepath,detect_types = sqlite3.parse_decltypes)
