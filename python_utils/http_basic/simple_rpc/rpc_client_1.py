# coding:utf-8

import xmlrpclib


def test_client_1():
    host = "http://localhost:8888/"
    proxy = xmlrpclib.ServerProxy(host)
    print "using proxy %s" % proxy

    print "3 is even %s" % str(proxy.is_even(3))
    print "100 is even %s" % str(proxy.is_even(100))


if __name__ == '__main__':

    # ----- test simple rpv client -----
    if 1:
        test_client_1()
    # ----- end -----

    pass
