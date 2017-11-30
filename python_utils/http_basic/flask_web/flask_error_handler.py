# coding:utf-8


from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    msg = {'status': 404, 'message': 'Not Found: ' + request.url}

    resp = jsonify(msg)
    resp.status_code = 404

    return resp


@app.route('/users/<userid>', methods=['GET'])
def api_users(userid):
    users = {'1': 'xy1', '2': 'xy2', '3': 'xy3'}

    if userid in users:
        return jsonify({userid: users[userid]})
    else:
        return not_found()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

    pass
