# coding:utf-8

from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"


@app.route('/idx')
def index_js():
    d = {"k": "hello world"}
    return jsonify(d)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    pass
