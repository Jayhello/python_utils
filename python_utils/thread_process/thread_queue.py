# _*_ coding:utf-8 _*_
"""

"""
import Queue
import threading
import logging
import random
import time
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(threadName)s %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')
lst_que = Queue.Queue()


def produce_item():
    return threading.currentThread().name, random.randint(0, 10)
    pass


def producer(num):
    for i in xrange(num):
        item = produce_item()
        lst_que.put(item)
        logging.info('produce item : ' + str(item))
        time.sleep(0.5)


def consume():
    while True:
        try:
            # non-block if lst_queue is empty then, it will raise Empty error
            item = lst_que.get(False)
            if item:
                logging.debug('consume item: ' + str(item))
            time.sleep(0.5)
        except Queue.Empty, e:
            # if lst_que is empty then do the following code snippet
            logging.warn('queue empty ' + str(e) + 'now sleep 1 S')
            time.sleep(1)


def create_mul_thread(thread_num, prefix_name, target_name):
    """
    A template of creating and starting n thread, do the same task.
    :param thread_num:  the num of thread
    :param prefix_name:
    :param target_name:
    :return:
    """
    for i in xrange(thread_num):
        t_name = prefix_name + str(i)
        produce_num = random.randint(10, 100)
        if prefix_name == 'consume--':
            t = threading.Thread(name=t_name, target=target_name)
        else:
            t = threading.Thread(name=t_name, target=target_name, args=(produce_num, ))
        t.start()


def create_mul_thread_producer(num):
    for i in xrange(num):
        t_name = 'producer--' + str(i)
        produce_num = random.randint(10, 100)
        t = threading.Thread(name=t_name, target=producer, args=(produce_num, ))
        t.start()


def test_consume_produce_queue():
    produce_num, consume_num = 2, 3
    # create 2 producer thread
    create_mul_thread(produce_num, 'producer--', producer)
    # create 3 consumer thread
    create_mul_thread(consume_num, 'consume--', consume)
    pass

if __name__ == '__main__':
    test_consume_produce_queue()
    pass
