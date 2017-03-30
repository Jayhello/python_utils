# _*_ coding:utf-8 _*_
"""
This file is about some basic operator of socket
"""


import socket


def get_ip():
    """
    local host ip not 127.0.0.1
    socket.gethostbyname(socket.gethostname()) will return 127.0.0.1
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    # s.getsockname() -> ip:port
    print s.getsockname()[0]
    s.close()


if __name__ == '__main__':
    get_ip()
