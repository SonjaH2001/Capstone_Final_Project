def find_daily_tutors():
    daily_tutors = [{
        "name": "mason",
        "courses": "ITEC 1050, 1100, 1234",
        "availability": "2 - 6"
    },
        {
            "name": "bhjghj",
            "courses": "ITEC 1050, 1100, 1234",
            "availability": "2 - 6"
        },
        {
            "name": "werwer",
            "courses": "ITEC 1050, 1100, 1234",
            "availability": "2 - 6"
        }, ]
    return daily_tutors

#replace with a database quesry
#ned to build these tables for the search
#function to set up database, call that when progrm starts up
#if name = main, the entrypoint check cookie

def save_student_data(name, star, timestamp):
    print(name, star, timestamp)
    print("saving to the database...success")
    #TODO: do this
    #datetime.now is an object, when stored in a database need to parse
    #in the sqlite.3 connect google python sqlite datetime
    # (connection string   filepath,detect_types = sqlite3.parse_decltypes)
