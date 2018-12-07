# coding:utf-8

import httplib, urllib
import json
import sys
import binascii
import base64
import time

S2S_COOKIE = ""
SERVICE_ID = 155442216984

# test for server
S2S_NAME = "xy_test_s2s_usage"
S2S_KEY = "6427d483e41014088b3dc1866ea37034b8e642ffd5ffba87ad0d30620d03a0441df6d1db8403b074"

# test for client
# S2S_NAME = "xy_test_s2s_usage_client"
# S2S_KEY = "6427d483e41014088b3dc1866ea37034d9ed3a63a7ff752c01d56be7c6b4fe49e4a6896657759e121f734bc75e8ab1a30cb2e0de51526ceb"

headers = {"Content-type": "application/json;charset=UTF-8"}


def s2s_auth():
    http_auth = httplib.HTTPConnection("meta.yy.com", 8080, timeout=30)
    auth_data = {"s2sname": S2S_NAME, "s2skey": S2S_KEY}
    auth_params = json.dumps(auth_data)
    http_auth.request("POST", "/auth", auth_params, headers)

    auth_rsp = http_auth.getresponse()
    auth_rsp_data = auth_rsp.read()
    print "auth result: ", auth_rsp.status, auth_rsp.reason, auth_rsp_data
    # auth result: 200 OK {"s2scookie":"E80300..............."}

    auth_rsp_decoded = json.loads(auth_rsp_data)
    print "auth_rsp_decoded: %s" % auth_rsp_decoded
    # auth_rsp_decoded: {u's2scookie': u'E8030000110078795F......"}

    global S2S_COOKIE
    if auth_rsp.status == 200:
        S2S_COOKIE = auth_rsp_decoded['s2scookie']

    http_auth.close()

    return auth_rsp.status


def create_meta():
    global S2S_COOKIE
    global SERVICE_ID

    dt = "test"
    dt = base64.b16encode(dt)
    meta = {"s2sname": S2S_NAME, "s2scookie": S2S_COOKIE, "groupId": 63, "type": 4, "data": dt}
    create_params = json.dumps(meta)

    http_client = httplib.HTTPConnection("meta.yy.com", 8080, timeout=30)
    http_client.request("POST", "/createMeta", create_params, headers)
    create_rsp = http_client.getresponse()
    create_rsp_data = create_rsp.read()
    print "createMeta result:", create_rsp.status, create_rsp.reason, create_rsp_data
    # createMeta result: 200 OK {"s2scookie":"E80300001100.....","serverId":141794623583}

    decoded = json.loads(create_rsp_data)
    if create_rsp.status == 200:
        SERVICE_ID = decoded['serverId']
        S2S_COOKIE = decoded['s2scookie']

    http_client.close()
    return create_rsp.status


def update_meta(data):
    global S2S_COOKIE
    global SERVICE_ID

    new_dt = base64.b16encode(data)
    modify_meta = {"s2scookie": S2S_COOKIE, "data": new_dt, "serverId": SERVICE_ID}
    update_params = json.dumps(modify_meta)

    http_client = httplib.HTTPConnection("meta.yy.com", 8080, timeout=30)
    http_client.request("POST", "/updateMeta", update_params, headers)
    update_rsp = http_client.getresponse()
    update_rsp_data = update_rsp.read()
    print "updateMeta result:", update_rsp.status, update_rsp.reason, update_rsp_data

    decoded = json.loads(update_rsp_data)
    if update_rsp.status == 200:
        S2S_COOKIE = decoded['s2scookie']
    http_client.close()
    return update_rsp.status


def remove_meta():
    global S2S_COOKIE
    global SERVICE_ID
    del_meta = {"s2scookie": S2S_COOKIE, "serverId": SERVICE_ID}
    del_params = json.dumps(del_meta)

    http_client = httplib.HTTPConnection("meta.yy.com", 8080, timeout=30)
    http_client.request("POST", "/removeMeta", del_params, headers)
    del_rsp = http_client.getresponse()

    print "removeMeta result:", del_rsp.status, del_rsp.reason, del_rsp.read()
    http_client.close()


def print_meta(metas):
    for meta in metas:
        meta_data = meta['data']
        data = binascii.unhexlify(meta_data)
        print 'serverId = %d, name = %s, groupId =%d, type = %d, timeStamp = %d, data = %s, status =%d\r' \
              % (meta["serverId"], meta['name'], meta["groupId"], meta["type"], meta["timestamp"], data, meta["status"])


def snap_shot():
    global S2S_COOKIE
    snap_data = {"s2scookie": S2S_COOKIE, "conditions": [{'name': "xy_test_s2s_usage", 'groupId': 63}]}
    params = json.dumps(snap_data)
    http_client = httplib.HTTPConnection("meta.yy.com", 8080, timeout=30)
    http_client.request("POST", "/snapShot", params, headers)

    snap_rsp = http_client.getresponse()
    print "snapShot result:", snap_rsp.status, snap_rsp.reason
    snap_rsp_data = snap_rsp.read()
    decoded = json.loads(snap_rsp_data)
    print "snap_shot, decoded: " % decoded

    metas = decoded['metas']
    print_meta(metas)
    # serverId = 1...3, name = xy_test_s2s_usage, groupId =63, type = 4, timeStamp = 6...3, data = test, status =0
    # serverId = 1...5, name = xy_test_s2s_usage, groupId =63, type = 4, timeStamp = 6...9, data = new_xy, status =0

    if snap_rsp.status == 200:
        S2S_COOKIE = decoded['s2scookie']

    return snap_rsp.status


if __name__ == '__main__':
    s2s_auth()

    remove_meta()

    # create_meta()

    # update_meta("new_xy")

    # snap_shot()

    pass
