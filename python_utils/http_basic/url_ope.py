# _*_ coding:utf-8 _*_


import urllib
import requests


def url_quote():
    raw_url = 'http://bs2-audiorec.oss-cn-shanghai.aliyuncs.com/e98f81fb526061e92a26eda17955c219.pcm'
    url = urllib.quote(raw_url)
    print url
    # http%3A//bs2-audiorec.oss-cn-shanghai.aliyuncs.com/e98f81fb526061e92a26eda17955c219.pcm
    print urllib.unquote(url)
    # http://bs2-audiorec.oss-cn-shanghai.aliyuncs.com/e98f81fb526061e92a26eda17955c219.pcm
    print urllib.quote("河=&源")
    # %E6%B2%B3%E6%BA%90


def req_with_para():
    d_para = {"name": "xy", "age": 21}
    print requests.get('http://xy.com', params=d_para)

    # ordered name-value pairs
    d_sorted_para = [("age", 21), ("name", "xy")]
    print requests.get('http://xy.com', params=d_sorted_para)


def url_encode_v1():
    f = {'eventName': 'myEvent', 'eventDescription': '飞龙在天'}
    print urllib.urlencode(f)
    # eventName=myEvent&eventDescription=%E9%A3%9E%E9%BE%99%E5%9C%A8%E5%A4%A9


def url_encode_v2():
    d_para = {"name": "xy熊大", "age": 21}
    print '&'.join('%s=%s' % (k, v) for k, v in d_para.iteritems())
    # age=21&name=xy熊大
    print '&'.join('%s=%s' % (k, urllib.quote(str(v))) for k, v in d_para.iteritems())
    # age=21&name=xy%E7%86%8A%E5%A4%A7

    base_url = 'xy.com/'
    url = 'http://%s?%s' % (base_url, '&'.join('%s=%s' % (k, urllib.quote(str(v))) for k, v in d_para.iteritems()))
    print url
    # http://xy.com/?age=21&name=xy%E7%86%8A%E5%A4%A7

    print urllib.unquote(url)
    # http://xy.com/?age=21&name=xy熊大


def post_request_tw():
    d_para = {"mp4Url": "http://bilinaudiop.bs2dl.yy.com/odgu3face5561f374d188f8915ed27602173_54673772546203998_17794996?token=rgB8AFyARE0BAEV0MloAAAAA9S0yWgAAAAB7GjUrB0NPTlRFWFQJZQB7ImJ1Y2tldCI6ImJpbGluYXVkaW9wIiwiZmlsZW5hbWUiOiJvZGd1M2ZhY2U1NTYxZjM3NGQxODhmODkxNWVkMjc2MDIxNzNfNTQ2NzM3NzI1NDYyMDM5OThfMTc3OTQ5OTYifQRBVVRIAwQAAwAAAD0Fw82IteG44FVTltIdijGKcfhW",
              "secretKey": "XY-bl-audio-rec-text-ret",
              "serial": "17598411"}

    print urllib.urlencode(d_para)

    # rsp = requests.get('http://172.27.49.16:8887/bilin/audiorec/', params=d_para)
    rsp = requests.get('http://61.147.186.82:9997/bilin/audiorec/', params=d_para)
    print rsp.content

    s = "sign=052c177ab75dfd53ab6b1cdc25569ef1&text=%E9%83%BD%E6%95%8F%E6%B3%95%E8%BD%AE%E5%8A%9F%E7%BB%83%E4%B9%A0%E8%80%85%E8%B7%B3%E6%A5%BC%E5%89%B2%E8%85%95%E6%8A%95%E6%B2%B3%EF%BC%8C&ts=1513238084&code=0&serial=17598411"
    print urllib.unquote(s)

if __name__ == '__main__':
    post_request_tw()
    # url_quote()
    # url_encode_v1()
    # url_encode_v2()
    pass
