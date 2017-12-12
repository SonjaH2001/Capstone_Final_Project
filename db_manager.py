import sqlite3 as sql

# sqlite_file = 'itech_tutor_program_db.sqlite'
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

# def create_db():  # call when start up the server
#     print("--->creating the database<---")  # for testing
#
#     conn_man = sql.connect(sqlite_file)  # not a great way to do this, needs framework
#     cursor = conn_man.cursor()
#     with open("schema.sql", "r") as schema:
#         create_table = schema.read()
#         cursor.executescript(create_table)
#         save_student_data()
#
#     # cursor.commit()
#     conn_man.close()


# def save_student_data():
#     print("saving to the database...")
#     #TODO: do this
#     student_list = []
#     student_list.append([1, "Seasonal Sensation", 4.30])
#     student_list.append([2, "Suger Hill Gang", 6.70])
#     student_list.append([3, "Chocolate Pinky Delights", 3.10])
#     student_list.append([4, "Chocolate Chip Peanust Butter Dream", 9.60])
#     for student in student_list:
#         add_student(student)
#
#     print("Cookie is added in the table")
#     #datetime.now is an object, when stored in a database need to parse
#     #in the sqlite.3 connect google python sqlite datetime
#     # (connection string   filepath,detect_types = sqlite3.parse_decltypes)
#
# def add_student(student):
#     print(student)

# example of search for day column
# >>> from datetime import datetime
# >>> d = datetime.now()
# >>> d.day
# 8
# >>> d.weekday
# <built-in method weekday of datetime.datetime object at 0x0000000002D7E2D0>
# >>> d.weekday()
# 4
# >>> if d.weekday() == 0:
# ...     col_day = "M"
# ...
# >>> "SELECT * FROM TUTORS WHERE ? does not eq null"