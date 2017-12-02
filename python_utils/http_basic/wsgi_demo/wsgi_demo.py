# coding:utf-8

"""
C:\Users\DW>curl -i -X POST 127.0.0.1:8080
HTTP/1.0 200 OK
Date: Fri, 01 Dec 2017 12:06:27 GMT
Server: WSGIServer/0.1 Python/2.7.12
Content-Type: text/html
Content-Length: 257

<html>   <head> <title>Hello User!</title> </head>
    <body>
.......
    </body>
    </html>
"""

from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello my friend!".encode("utf-8")]


form = """<html>   <head> <title>Hello User!</title> </head>
    <body>
        <form method="post">
            <label>Hello</label>
            <input type="text" name="name">
            <input type="submit" value="Go">
        </form>
    </body>
    </html>
    """


def app_post(environ, start_response):
    html = form
    start_response('200 OK', [('Content-Type', 'text/html')])
    print environ
    if environ['REQUEST_METHOD'] == 'POST':
        return [html]

    elif environ['REQUEST_METHOD'] == 'GET':
        return ["get request".encode("utf-8")]

if __name__ == '__main__':
    # server = make_server('localhost', 8080, application)
    server = make_server('localhost', 8080, app_post)
    server.serve_forever()
    pass
