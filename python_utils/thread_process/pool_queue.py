# _*_ coding:utf-8 _*_
"""
This file light weight thread pool queue
Mainly cited from
`http://stackoverflow.com/questions/3033952/python-thread-pool-similar-to-the-multiprocessing-pool`
"""
import threading
import logging
from time import sleep
from random import randint
from Queue import Queue

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(threadName)s %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')


class Worker(threading.Thread):
    def __init__(self, task):
        super(Worker, self).__init__()
        self.task = task
        self.daemon = True  # if don't set that, then the thread won't stop automatically
        self.start()

    def run(self):
        while True:
            logging.debug('waiting for queue')
            func, args, kargs = self.task.get()
            try:
                logging.debug('now I am going to do task')
                func(*args, **kargs)
            except Exception, e:
                logging.warn(e)
            finally:
                self.task.task_done()


class ThreadPool:
    def __init__(self, num_thread):
        self.tasks = Queue(num_thread)
        for w in xrange(num_thread):
            Worker(self.tasks)

    def add_task(self, func, *args, **kwargs):
        self.tasks.put((func, args, kwargs))
        pass

    def wait_completion(self):
        """
        the corresponding consume thread should be a daemon thread,
        so it can exit automatically
        :return:
        """
        self.tasks.join()
        pass


def handler(sec):
    logging.debug('now I will sleep %s S', sec)
    sleep(sec)


def test():
    lst_sleep_sec = [randint(5, 20) for i in xrange(20)]
    pool = ThreadPool(5)
    for sec in lst_sleep_sec:
        pool.add_task(handler, sec)

    pool.wait_completion()
    pass

if __name__ == '__main__':
    test()
    pass
