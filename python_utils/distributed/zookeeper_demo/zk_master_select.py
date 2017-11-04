from kazoo.client import KazooClient
import time
import uuid

import logging
logging.basicConfig()

my_id = uuid.uuid4()


def leader_func():
    print "I am the leader {}".format(str(my_id))
    while True:
        print "{} is working! ".format(str(my_id))
        time.sleep(3)

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

election = zk.Election("/electionpath")

# blocks until the election is won, then calls
# leader_func()
election.run(leader_func)

zk.stop()
