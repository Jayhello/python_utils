# coding:utf-8

import socket
import BaseHTTPServer
import time


HOST = "127.0.0.1"
PORT = 8888

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello!</h1>""".replace(b"\n", b"\r\n")


RESPONSE = 'a' * (1024 * 1)


def test_simple():
    server_sock = socket.socket()
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen(0)
    print "Listening on %s:%s..." % (HOST, PORT)

    while 1:
        client_sock, client_addr = server_sock.accept()
        print "New connection from %s:%s." % (client_addr)
        # client_sock.sendall(RESPONSE)
        time.sleep(12)

        data = client_sock.recv(1024)
        print "recv :%s" % data

        n = client_sock.send(RESPONSE)
        print "just send %s bytes" % n


if __name__ == '__main__':
    test_simple()
    pass
