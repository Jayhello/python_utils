# _*_ coding:utf-8 _*_

"""
This file is about basic operator of redis
"""
import redis


def demo1():
    ip = '183.36.123.180'
    ip2 = 'localhost'
    p = 36712
    p2 = 6379

    # r = redis.StrictRedis(host=ip, port=p, db=4)
    # r.set('name', 'bear fish')
    # print r.get('name')
    # lst = r.keys(pattern='*')
    # val = r.mget(lst)
    #
    # d = dict(zip(lst, val))

    r2 = redis.StrictRedis(host=ip2, port=p2, db=4)

    # r2.mset(d)
    lst = r2.keys(pattern='*')
    for item in lst[-100:]:
        print item

    # d = {'a':1, 'b':7, 'foo':'bar'}
    # r.mset(zip(lst, val))
    # r.mset(d)


class RdsServer(object):
    def __init__(self):
        self._ip = '127.0.0.1'
        self._port = 6379
        self._rds_pool = redis.ConnectionPool(host=self._ip, port=self._port, socket_timeout=3)

    def test_sub_lst(self):
        """
        更新master节点的time stamp值
        """
        # 使用下面这个pool中的redis，3S会超时
        # rds = redis.Redis(connection_pool=self._rds_pool)
        rds = redis.Redis(host=self._ip, port=self._port)
        try:
            sub = rds.pubsub()
            sub_lst = ['channel_1', 'channel_2']
            sub.subscribe(*sub_lst)
            sub.subscribe('abc')

            for item in sub.listen():
                print item
                print type(item['data'])
                if 'chan' in item['channel']:
                    print item['channel'], item['channel'][item['channel'].find('chan'):]
                if item['channel'] == 'channel_1' and item['type'] == 'subscribe':
                    sub.unsubscribe(item['channel'])

        except redis.ConnectionError as e:
            pass

if __name__ == '__main__':
    rs = RdsServer()
    rs.test_sub_lst()
    pass
