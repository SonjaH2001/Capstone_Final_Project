import sqlite3 as sql

# sqlite_file = 'itech_tutor_program_db.sqlite'
sqlite_file = 'itech_tutor_program_db.sqlite'

def find_daily_tutors():
    print("checking...")

    # get current day using datetime, blah blah List of strings with weekday number
    day = "tuesday"
    find_tutor_query = "SELECT name, courses, {day} FROM tutor WHERE {day} is NOT NULL ".format(day=day)
    conn_man = sql.connect(sqlite_file)
    cursor = conn_man.cursor()
    cursor.execute(find_tutor_query)
    rows = cursor.fetchall()
    daily_tutors = []
    for row in rows:
        tutor = {
            "name": row[0],
            "courses": row[1],
            "availability": row[2]
        }
        daily_tutors.append(tutor)
    # return daily_tutors

    # conn_man.commit()
    conn_man.close()
    print(rows)
    print(daily_tutors)
    return daily_tutors
#     daily_tutors = [{
#         "name": "Tech Tutor 1",
#         "courses": "ITEC 1050, 1100, 1234",
#         "availability": "2 - 6"
#     },
#         {
#             "name": "Tech Tutor 2",
#             "courses": "ITEC 2950, 1150, 1234",
#             "availability": "2 - 6"
#         },
#         {
#             "name": "Tech Tutor 3",
#             "courses": "ITEC 2950, 1150, 1234",
#             "availability": "10 - 12"
#         }, ]
#     return daily_tutors

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
        # save_student_data()

    # cursor.commit()
    conn_man.close()

def save_tutor_data(name, courses, monday, tuesday, wednesday, thursday, friday):
    print("adding a tutor...")
    #save information from the add-tutor page to the database

    add_query = "INSERT INTO tutor VALUES (NULL, ?, ?, ?, ?, ? ,?, ?)"
    conn_man = sql.connect(sqlite_file)
    cursor = conn_man.cursor()
    cursor.execute(add_query, (name, courses, monday, tuesday, wednesday,thursday,friday))

    conn_man.commit()
    conn_man.close()

# def save_student_data():
#     print("saving to the database...")
#     #TOoDO: do this
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