# _*_ coding:utf-8 _*_

import string
import random


def str_format():
    s1 = """abc%sddd""" % 'asd'
    print s1
    url = """http://127.0.0.1:9325/shortvideo/checkBlack?url=%s&serial=%s""" % ('http%3A%2F%2Fzbasecapture.bs2.yy.com%2F42269159_1499248536403_3.jpg', '77777777')
    print url


def generator_random_str(size=6, str_source=string.digits + string.lowercase):
    """:return size num str(in 'A~z, 0-9')
    eg. size=6 return 'ad14df'
    [random.choice('abcde') for _ in range(3)] -> ['a', 'b', 'b']
    ''.join(['a', 'b', 'b']) -> 'abb'
    """
    return ''.join(random.choice(str_source) for _ in xrange(size))

if __name__ == '__main__':
    # str_format()
    print generator_random_str()
    print generator_random_str(3, 'abc123')
    # s = '123'
    # if s.find("12") == -1:
    #     print 'no no '

    # url = 'www.myzaker.com/article/58daf1b69490cbe53400001b/'
    # print url.find('myzaker')
    # print url.find('www.myzaker')
    # print url.find('http')

    # print s[1:]
    # print s[:]
    # print s[:2]
    pass
