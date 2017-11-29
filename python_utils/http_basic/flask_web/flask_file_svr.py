# coding:utf-8

from flask import Flask
from flask import Response


app = Flask(__name__)


@app.route('/audio/pcm_mp3/')
def stream_mp3():
    def generate():
        path = 'F:/826.mp3'
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)

    return Response(generate(), mimetype="audio/mpeg3")


if __name__ == '__main__':
    # so the other machine can visit the website by ip
    app.run(host='0.0.0.0')
    pass
