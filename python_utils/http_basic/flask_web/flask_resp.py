# coding:utf-8

from flask import Flask
from flask import Response
import json


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def api_hello():
    data = {'name': 'xy', 'greet': "hello"}
    js_str = json.dumps(data)

    resp = Response(js_str, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://xy.com'

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    pass
