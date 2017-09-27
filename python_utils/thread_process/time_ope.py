# _*_ coding:utf-8 _*_

"""get the seconds since epoch from the time + date output"""

import time


if __name__ == '__main__':

    time_stamp = int(time.time())
    print time_stamp

    print time.ctime(time_stamp)

    print time.strftime("%Y-%m-%d %H:%M:%S")
    pass
