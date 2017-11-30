# coding:utf-8

"""
cited from http://blog.luisrei.com/articles/flaskrest.html
test different http request head Content-Type
"""

from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/message', methods=['POST'])
def api_msg():
    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "Json Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        print len(request.data)
        with open('./file.name', 'wb') as f:
            f.write(request.data)

        return "binary file written"

    elif request.headers['Content-Type'] == 'multipart/form-data':
        print "111"
        print request.args
    else:
        return "415 unsupported media type"


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
    pass
