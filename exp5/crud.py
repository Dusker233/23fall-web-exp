# execute `python3 -m doctest -v test.txt` to run the test suite
from sql_conn import DataBase

db = DataBase('./course.db')


def retrieve(index):
    """ retrieve the course from the database
    when index = 0 means to retrieve all
    other means to retrieve the day of the week corresponding to index
    """

    if index == 0:
        desp, results = db.selectAll('courses')
    else:
        desp, results = db.Query2('courses', ['week'], [index])
    assert desp, results
    print(desp)
    for course in results:
        print(course)
    return len(results)

def create():
    """ create a new course and insert it into the database
    """

    data = dict(
        id = 10,
        week = 6,
        name = 'pysqlite',
        duration = '8-8 周',
        section = '7-8',
        classroom = '知行南楼 408',
        teacher = '<NAME>'
    )
    db.Insert('courses', data)
    _, results = db.Query2('courses', ['id'], [10])
    print(results)

def update():
    """ update the data in the database
    the type of the ID field is list, which contains the list of id fields
    rest of the data fields will be updated
    """
    _, results = db.Query2('courses', ['id'], [10])
    print(results)
    data = dict(
        ID = ['id'],
        id = 10,
        week = 7,
        section = '9-10'
    )
    db.Update('courses', data)
    _, results = db.Query2('courses', ['id'], [10])
    print(results)

def delete():
    """ delete the data in the database
    """
    _, results = db.Query2('courses', ['id'], [10])
    print(results)
    db.DeleteById('courses', 'id', 10)
    # when id more than 1, use list as parameter
    # db.DeleteById('courses', ['id'], [10])
    _, results = db.Query2('courses', ['id'], [10])
    print(results)
