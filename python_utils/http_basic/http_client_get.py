# _*_ coding:utf-8 _*_

"""
This file a sample demo to do http stress test
"""
import requests
import time
from multiprocessing.dummy import Pool as ThreadPool
import urllib


def get_ret_from_http(url):
    """cited from https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
    """
    ret = requests.get(url)
    print ret.content
    # eg. result: {"error":false,"resultMap":{"check_ret":1},"success":true}


def multi_process_stress_test():
    """
    start up 4 thread to issue 1000 http requests to server
    and test consume time
    :return:
    """
    start = time.time()
    url = """http://127.0.0.1:9325/shortvideo/checkBlack?url=http%3A%2F%2Fzbasecapture.bs2.yy.com%2F42269159_1499248536403_3.jpg&serial=abcdddddddd"""
    url1 = """http://127.0.0.1:9325/shortvideo/checkBlack?url=http%3A%2F%2Fgenie.bs2dl.yy.com%2Ff4955aa1ab1c479256e2a2c5cdec73a6&serial=abceeeeeeee"""
    lst_url = [url, url1]*50
    pool = ThreadPool(5)
    ret = pool.map(get_ret_from_http, lst_url)
    pool.close()
    pool.join()
    print 'time consume %s' % (time.time() - start)


def make_url():
    """
    generate url with parameter
    https://xy.com/index.php?url=http%3A//xy.xxx.com/22.jpg&SecretId=xy_123_move
    cited from https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python
    https://github.com/gruns/furl a good util for url operator
    :return:
    """
    para = {"SecretId": "xy_123_move", "url": "http://xy.xxx.com/22.jpg"}

    print urllib.urlencode(para)
    # url=http%3A%2F%2Fxy.xxx.com%2F22.jpg&SecretId=xy_123_move

    base_url = 'xy.com/index.php'

    return 'https://%s?%s' % (base_url, '&'.join('%s=%s' % (k, urllib.quote(str(v))) for k, v in para.iteritems()))


if __name__ == '__main__':
    # get_ret_from_http()
    # multi_process_stress_test()

    print make_url()
    # s = "abc"
    s = "abc"
    print urllib.quote(s)
    pass
