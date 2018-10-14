# coding: utf-8

from SimpleXMLRPCServer import SimpleXMLRPCServer


def is_even(n):
    return n % 2


def test_server_1():
    port = 8888
    rpc_server = SimpleXMLRPCServer(("localhost", port))
    print 'now listening in %s' % port

    rpc_server.register_function(is_even, "is_even")
    rpc_server.serve_forever()


if __name__ == '__main__':

    # -----test rpc server 1-----
    if 1:
        test_server_1()
    # ----- end -----

    pass
