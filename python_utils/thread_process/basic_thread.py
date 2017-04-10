# _*_ coding:utf-8 _*_
"""
This file is about basic operator about thread
"""

import threading
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(threadName)s %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')


def join_all_others_thread():
    """
    block the thread invoking this method
    :return:
    """
    logging.debug('now join all the other threads')
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()

    # the following msg will be print after all the other thread done
    logging.debug('join all the other threads success')
