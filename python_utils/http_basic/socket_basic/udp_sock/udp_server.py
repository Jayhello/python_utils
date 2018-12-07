# coding: utf-8

import socket


def udp_server():
    host, port = "localhost", 8888

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.bind((host, port))

    rcv_size = 1024 * 65
    while True:
        data, address = sock.recvfrom(rcv_size)
        print "recv from %s: %s" % (address, len(data))

        if data:
            send_size = sock.sendto(data, address)
            print "sendto %s: %s" % (address, send_size)


if __name__ == '__main__':

    udp_server()

    pass