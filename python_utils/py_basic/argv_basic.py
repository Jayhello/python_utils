# _*_ coding:utf-8 _*_

import sys
import logging


def parse_js():
    kv = {}
    for line in sys.stdin:
        print line

    if len(sys.argv) > 4:
        try:
            print sys.argv[1]
            id = int(sys.argv[1])
            sid = int(sys.argv[2])
            pre = int(sys.argv[3])
        except ValueError, e:
            logging.error("Can't convert id or sid to int")
        sys.exit()
    else:
        msg = sys.argv[4]
        for arg in sys.argv[5:]:
            msg += " "
            msg += arg
        kv["id"] = id
        kv["alarm"] = 1
        kv["msg"] = msg.replace("'", "")

if __name__ == '__main__':
    # config script para
    print sys.argv
    # ['E:/git_code/python_utils/py_basic/argv_basic.py', '1', '2', '3']
    print len(sys.argv)
    # 4
    # parse_js()
