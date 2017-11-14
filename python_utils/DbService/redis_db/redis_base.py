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
        # self._rds_pool = redis.ConnectionPool(host=self._ip, port=self._port, socket_timeout=3)
        self._rds_pool = redis.ConnectionPool(host=self._ip, port=self._port, db=2,
                                              socket_timeout=3)

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
            print sub.unsubscribe(*sub_lst)

            print sub.subscribe(*sub_lst)
            sub.subscribe('abc')

            for item in sub.listen():
                print item
                print type(item['data'])
                if 'chan' in item['channel']:
                    print item['channel'], item['channel'][item['channel'].find('chan'):]
                if item['channel'] == 'channel_1' and item['type'] == 'subscribe':
                    print sub.unsubscribe(item['channel'])

        except redis.ConnectionError as e:
            pass

    def test_set(self):
        # rds = redis.Redis(connection_pool=self._rds_pool)
        rds = redis.Redis(host=self._ip, port=self._port)
        try:
            print rds.sadd('set_2', 123)
            # if success return 1
            rv_set = set([123, 456])
            print rds.srem('set_1', *rv_set)
            # if success return 1
            # s_member = rds.smembers('set_1')
            s_member = rds.smembers('set_2')
            print s_member
            # set(['123'])
            print type(s_member)
            # <type 'set'>

        except Exception as e:
            # if redis server goes down, then 'Error 10061 connecting to 127.0.0.1:6379'
            print e

    def test_publish(self):
        """
        注意的是，无论redis上面那个db订阅了频道，都会收到 publish消息
        """
        rds = redis.Redis(connection_pool=self._rds_pool)
        channel = 'test_channel'
        for i in xrange(1, 5):
            print rds.publish(channel, str(i))

    def del_keys(self):
        rds = redis.Redis(connection_pool=self._rds_pool)
        keys = ['set_1', 'set_2']
        keys = [123]
        # 下面的 keys前记得加上 *
        # 返回实际删除的个数(例如上面的keys中 set_2不存在，只是删除了set_1, 故而返回结果 1)
        print rds.delete(*keys)

    def del_hset_keys(self):
        rds = redis.Redis(connection_pool=self._rds_pool)
        keys = ['id_1', 'id_3', 'id_2']
        print rds.hdel('hset_1', *keys)

    def get_all_key(self):
        rds = redis.Redis(connection_pool=self._rds_pool)
        s = set(rds.keys('set_python_worker*'))
        print s
        s_sub = {'set_python_worker_1', 'set_python_worker_asdasdasd'}
        print s - s_sub

    def test_select_db(self):
        # db = 2
        # can't select db by the below
        # rds = redis.Redis(connection_pool=self._rds_pool, db=db)

        # choose db in connection_pool directly
        rds = redis.Redis(connection_pool=self._rds_pool)
        print rds.sadd('set_2', 123)

    def test_pop(self):
        rds = redis.Redis(connection_pool=self._rds_pool)
        QUE_NEW_AUDIO_STREAM = "que_new_audio_stream"

        try:
            print rds.rpop(QUE_NEW_AUDIO_STREAM)
        except Exception as e:
            print e

    def test_pipeline(self):
        rds = redis.Redis(connection_pool=self._rds_pool)
        pipe = rds.pipeline()
        pipe.set('foo', 'bar')
        pipe.get('bing')
        pipe.delete('foo')
        print pipe.execute()[0]
        # print ret
        # [True, None, 1]


if __name__ == '__main__':
    rs = RdsServer()
    # rs.test_pop()
    rs.test_pipeline()
    # rs.test_sub_lst()
    # rs.test_select_db()
    # rs.test_set()
    # rs.del_keys()
    # rs.get_all_key()
    # rs.del_hset_keys()
    # rs.test_publish()
    pass
