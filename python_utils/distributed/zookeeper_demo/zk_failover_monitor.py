from kazoo.client import KazooClient

import time

import logging
logging.basicConfig()

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# Determine if a node exists
while True:
    if zk.exists("/test/failure_detection/worker"):
        print "the worker is alive!"
    else:
        print "the worker is dead!"
        break
    time.sleep(3)

zk.stop()
