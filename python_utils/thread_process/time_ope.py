# _*_ coding:utf-8 _*_

"""get the seconds since epoch from the time + date output"""

import time


if __name__ == '__main__':

    time_stamp = int(time.time())
    s = '123'
    print time_stamp
    print "%s_%s.pcm" % (s, time_stamp)
    s += str(time_stamp)
    print s

    print time.ctime(time_stamp)

    print time.strftime("%Y-%m-%d %H:%M:%S")
    pass
