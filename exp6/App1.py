from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show1', methods=['GET', 'POST'])
def show1():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form.get('num') == "":
        return render_template('show1.html')    
    num = int(request.form.get('num'))
    data = []
    for i in range(1, num + 1):
        times = []
        for j in range(1, i + 1):
            times.append("%d*%d=%d" % (i, j, i * j))
        data.append(times)
    return render_template('show1.html', data=data)


@app.route('/show2', methods=['GET', 'POST'])
def show2():
    if request.method == 'GET':
        return render_template('show2.html')
    if request.form.get('num') == "":
        return render_template('show2.html')
    num = int(request.form.get('num'))
    data = []
    for i in range(1, num + 1):
        times = []
        for j in range(1, i + 1):
            times.append("%d*%d=%d" % (i, j, i * j))
        data.append(times)
    return render_template('show2.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)