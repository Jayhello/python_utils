# coding:utf-8
import socket


def basic_block():
    s = socket.socket()
    s.connect(('www.baidu.com', 80))
    print("We are connected to %s:%d" % s.getpeername())
    # We are connected to 61.135.169.121:80


def basic_non_block():
    s = socket.socket()
    s.setblocking(0)

    try:
        s.connect(('http://vis-www.cs.umass.edu', 80))
    except socket.error as e:
        print(str(e))
        i = 0
        while True:
            try:
                print("We are connected to %s:%d" % s.getpeername())
                break
            except:
                print("Let's do some math while waiting: %d" % i)
                i += 1
    else:
        print("We are connected to %s:%d" % s.getpeername())


def basic_connect_rcv():
    """
    connect to server and receive msg from server
    :return:
    """
    s = socket.socket()
    # s.connect(('127.0.0.1', 8888))
    s.connect(('221.228.106.244', 8888))
    print("We are connected to %s:%d" % s.getpeername())
    # s_rcv = str(s.recv(1024 * 1024))
    # print 'recv, len: %s, %s' % (len(s_rcv), s_rcv)

    buf = 'a' * 1024 * 1024
    while 1:
        n = s.send(buf)
        print "now send %s" % n


if __name__ == '__main__':
    # basic_block()
    # basic_non_block()
    basic_connect_rcv()
    pass
