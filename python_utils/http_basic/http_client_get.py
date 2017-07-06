# _*_ coding:utf-8 _*_

"""
This file a sample demo to do http stress test
"""
import requests
import time
from multiprocessing.dummy import Pool as ThreadPool


def get_ret_from_http(url):
    """cited from https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
    """
    ret = requests.get(url)
    print ret.content
    # eg. result: {"error":false,"resultMap":{"check_ret":1},"success":true}


def multi_process_stress_test():
    """
    start up 4 process to issue 1000 http requests to server
    and test consume time
    :return:
    """
    start = time.time()
    url = """http://127.0.0.1:9325/shortvideo/checkBlack?url=http%3A%2F%2Fzbasecapture.bs2.yy.com%2F42269159_1499248536403_3.jpg&serial=abc123"""
    lst_url = [url] * 1000
    pool = ThreadPool(5)
    ret = pool.map(get_ret_from_http, lst_url)
    pool.close()
    pool.join()
    print 'time consume %s' % (time.time() - start)

if __name__ == '__main__':
    # get_ret_from_http()
    multi_process_stress_test()
    pass
