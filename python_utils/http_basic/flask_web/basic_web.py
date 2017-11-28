# _*_coding:utf-8 _*_

from flask import Flask
from flask import abort
from flask import redirect
from flask import request
from flask import Response


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>from win10 slow machine</hi>'


@app.route('/user/<name>')
def say_hello(name):
    return '<h1>hello, %s</h1>' % name


@app.route('/paras/')
def multi_paras():
    ret_str = ''
    for para in request.args:
        print para, request.args[para]
        ret_str += para

    return '<h1>multi_paras, %s</h1>' % ret_str


@app.route('/audio/pcm_mp3/<file_key>')
def stream_mp3(file_key):
    def generate():
        path = 'F:/10191.wav'
        path = 'F:/826.mp3'
        # path = '10191.wav'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg3")


if __name__ == '__main__':
    # app.run(debug=True)
    # so the other machine can visit the website by ip
    app.run(host='0.0.0.0')

    pass
