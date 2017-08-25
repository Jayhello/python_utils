# _*_coding: utf-8 _*_
"""
test for global variable
note that in multiprocess, every process has it's own
global variable, so if the function fun2 is in subprocess
it will still be 0
"""
g_dst_dir = ''

g_val = 0


def fun2():
    print g_val


def fun1():
    global g_val
    g_val = 3
    fun2()


if __name__ == '__main__':
    fun1()
    pass
