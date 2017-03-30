# _*_ coding:utf-8 _*_

import os
import multiprocessing


def get_process_id():
    print os.getpid()
    # 8844
    print multiprocessing.current_process().pid
    # 8844
    print multiprocessing.current_process().name
    # MainProcess


if __name__ == '__main__':
    get_process_id()
