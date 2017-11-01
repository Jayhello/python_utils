# _*_ coding:utf-8 _*_

from kazoo.client import KazooClient
import time
import uuid

import logging
logging.basicConfig()

my_id = uuid.uuid4()


def work():
    print "{} is working! ".format(str(my_id))


zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

lock = zk.Lock("/lockpath", str(my_id))

print "I am {}".format(str(my_id))

while True:
    with lock:
        work()
    time.sleep(3)

zk.stop()

if __name__ == '__main__':

    pass
