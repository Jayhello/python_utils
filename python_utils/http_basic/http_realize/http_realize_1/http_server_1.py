# coding: utf-8

import socket


RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello!</h1>""".replace(b"\n", b"\r\n")


def http_server_1():
    # host, port = "127.0.0.1", 8888
    host, port = "127.0.0.1", 0

    # By default, socket.socket creates TCP sockets.
    # with socket.socket() as server_sock:
    server_sock = socket.socket()
    # This tells the kernel to reuse sockets that are in `TIME_WAIT` state.
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # This tells the socket what address to bind to.
    server_sock.bind((host, port))

    server_sock.listen(0)

    # print "listening on %s:%s" % (host, port)
    print "listening on %s:%s" % (server_sock.getsockname())

    while True:
        client_sock, client_addr = server_sock.accept()
        print "new connection from %s: %s" % (client_addr, client_sock)
        data = client_sock.recv(1024)
        print "recv :%s" % data

        with client_sock:
            client_sock.sendall(RESPONSE)


if __name__ == '__main__':
    http_server_1()
    pass
