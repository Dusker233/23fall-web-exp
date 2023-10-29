from flask import Flask, render_template, request
from sql_conn import DataBase


app = Flask(__name__)
db = DataBase("./course.db")
desp = ['周', '课程名', '周次', '节次', '教室', '教师']
days = [(0, '全周'), (1, '周一'), (2, '周二'), (3, '周三'), (4, '周四'), (5, '周五'), (6, '周六'), (7, '周日')]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('courses.html', days=days)
    day = int(request.form.get('day'))
    if day == 0:
        _, results = db.selectAll('courses')
    else:
        _, results = db.Query2('courses', ['week'], [day])
    assert _
    data = [desp]
    for result in results:
        result = list(result)
        result[1] = (list(days[result[1]])[1])[1]
        result.pop(0)
        data.append(result)
    return render_template('courses.html', days=days, data=data)


if __name__ == '__main__':
    app.run(debug=True)