# _*_ coding:utf-8 _*_

"""
This file is about basic operator of redis
"""
import redis


def demo1():
    ip = '183.36.123.188'
    ip = 'localhost'
    p = 6712
    p = 6379

    r = redis.StrictRedis(host=ip, port=p, db=4)
    # r.set('name', '必死')
    # print r.get('name')
    lst = r.keys(pattern='*')
    val = r.mget(lst)

    for i, item in enumerate(lst):
        lst[i] += '1'

    d = {'a':1, 'b':7, 'foo':'bar'}
    # r.mset(zip(lst, val))
    r.mset(d)

if __name__ == '__main__':
    demo1()
    pass
