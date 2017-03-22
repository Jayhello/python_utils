# _*_ coding:utf-8 _*_

import os
import multiprocessing


def get_process_id():
    print os.getpid()
    print multiprocessing.current_process().pid
    print multiprocessing.current_process().name


if __name__ == '__main__':
    get_process_id()
