from kazoo.client import KazooClient
import time

import logging
logging.basicConfig()

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# Ensure a path, create if necessary
zk.ensure_path("/test/failure_detection")

# Create a node with data
zk.create("/test/failure_detection/worker",
          value=b"a test value", ephemeral=True)

while True:
    print "I am alive!"
    time.sleep(3)

zk.stop()
