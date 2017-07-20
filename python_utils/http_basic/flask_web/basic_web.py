# _*_coding:utf-8 _*_

from flask import Flask
from flask import abort
from flask import redirect


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>from win10 slow machine</hi>'


@app.route('/user/<name>')
def say_hello(name):
    return '<h1>hello, %s</h1>' % name


if __name__ == '__main__':
    # app.run(debug=True)
    # so the other machine can visit the website by ip
    app.run(host='0.0.0.0')

    pass
