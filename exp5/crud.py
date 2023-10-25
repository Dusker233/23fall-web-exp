from sql_conn import DataBase

db = DataBase('./course.db')


def retrieve(index):
    """ retrieve the course from the database
    when index = 0 means to retrieve all
    other means to retrieve the day of the week corresponding to index
    """

    if index == 0:
        desp, result = db.Query('select * from courses')
    else:
        desp, result = db.Query("select * from courses where week = '%s'" % index)
    assert len(desp) != 0
    assert result != None
    print(desp)
    for course in result:
        print(course)
    return len(result)

def create():
    pass

def update():
    pass

def delete():
    pass