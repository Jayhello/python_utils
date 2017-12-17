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


def str_split():
    s = 'python_worker_name&topSid_111_appid_111&topSid_222_appid_222'
    print s[0:s.find('&')]
    print s.split('&')
    print s.split('&')[1:]


def remove_sub_str():
    src = 'channel_1'
    sub_s = 'chan'
    print src[src.find(sub_s):]
    print src.find(sub_s)
    print src.replace(sub_s, '')


def str_format_once():
    query = """insert into {tb_name} (create_time, appid) VALUES (%s,%s)"""
    tb_name = 'tb_audio_rec_ret_2017_11'
    # query % tb_name  error
    print query.format(tb_name=tb_name)
    # insert into tb_audio_rec_ret_2017_11 (create_time, appid) VALUES (%s,%s)


def str_replace():
    import time
    s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print s
    # 2017-11-09 17:26:34
    print s[0:7].replace('-', '_')
    # 2017_11


def char_2int_2char():
    print ord('a')
    # 97
    print chr(97)
    # a

if __name__ == '__main__':
    char_2int_2char()
    # str_replace()
    # str_format_once()
    # remove_sub_str()
    # str_split()
    # str_format()
    # print generator_random_str()
    # print generator_random_str(3, 'abc123')
    # s = '123'
    # if s.find("12") == -1:
    #     print 'no no '

    b = 0
    b = None
    # if b is not zero not None(like -1, 1) it will print
    if b:
        print '%s not zero' % b

    # url = 'bear fish.com'
    # if url.endswith('.com'):
    #     url = url[:-4]
    #     print url

    url = 'www.myzaker.com/article/58daf1b69490cbe53400001b/'
    # if 'aa' in url:
    #     print '1'
    # elif 'comp' in url:
    #     print '2'
    # else:
    #     print '3'
    # print url.find('myzaker')
    # print url.find('www.myzaker')
    # print url.find('http')

    # print s[1:]
    # print s[:]
    # print s[:2]
    pass
