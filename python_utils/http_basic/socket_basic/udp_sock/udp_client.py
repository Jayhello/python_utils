# coding: utf-8

import socket

"""
Test for upd max end size.
"""


def udp_client():
    host, port = "localhost", 8888

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = 'a' * 1024 * 65
    msg = 'a' * 65507

    sent = sock.sendto(msg, (host, port))
    # sent = sock.sendto(msg, (host, port))

    data, server_add = sock.recvfrom(1024 * 64)
    print 'rcv from %s: %s' % (server_add, len(data))


if __name__ == '__main__':
    udp_client()
    pass


