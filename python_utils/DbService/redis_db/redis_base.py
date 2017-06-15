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
    # r.set('name', '必死')
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

if __name__ == '__main__':
    demo1()
    pass
