# coding:utf-8
from SocketServer import TCPServer, StreamRequestHandler

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello!</h1>""".replace(b"\n", b"\r\n")


class MyHandler1(StreamRequestHandler):
    """process tcp server, and send http response back"""
    def handle(self):
        addr = self.request.getpeername()
        print 'get connection from %s, %s ' % addr
        self.wfile.write(RESPONSE)


def test_handler1():
    # http server
    server = TCPServer(('', 8888), MyHandler1)
    server.serve_forever()


if __name__ == '__main__':
    test_handler1()
    pass
