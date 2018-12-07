import struct
import socket
import math


def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]


def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))


def str_ip2_int(s_ip='192.168.1.100'):
    lst = [int(item) for item in s_ip.split('.')]
    print lst
    # [192, 168, 1, 100]

    int_ip = lst[3] | lst[2] << 8 | lst[1] << 16 | lst[0] << 24
    return int_ip   # 3232235876


def str_ip2_int_v2(s_ip='192.168.1.100'):
    lst = [int(item) for item in s_ip.split('.')]
    lst = map(int, s_ip.split('.'))
    print lst
    # [192, 168, 1, 100]

    int_ip = lst[3] + lst[2] * pow(2, 8) + lst[1] * pow(2, 16) + lst[0] * pow(2, 24)
    return int_ip   # 3232235876


def int_ip2str(int_ip=3232235876):
    lst = []
    for i in xrange(4):
        shift_n = 8 * i
        lst.insert(0, str((int_ip >> shift_n) & 0xff))

    return ".".join(lst)


if __name__ == '__main__':
    str_ip = '192.168.1.100'
    int_ip = ip2int(str_ip)
    print "%s -> int is: %s" % (str_ip, int_ip)
    # 192.168.1.100 -> int is: 3232235876

    str_ip = int2ip(int_ip)
    print "%s -> str is: %s" % (int_ip, str_ip)
    # 3232235876 -> str is: 192.168.1.100

    print str_ip2_int_v2()

    print int_ip2str(int_ip)

