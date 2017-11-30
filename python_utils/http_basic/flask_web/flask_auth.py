# coding:utf-8
"""
cited https://github.com/miguelgrinberg/Flask-HTTPAuth
"""

from flask import Flask
from flask import request
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {"xy1": "11111", "xy2": "22222"}


@auth.get_password
def get_pw(user_name):
    if user_name in users:
        return users.get(user_name)

    return None


@app.route('/')
@auth.login_required
def index():
    print request.authorization
    return "hello, %s" % auth.username()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    pass
