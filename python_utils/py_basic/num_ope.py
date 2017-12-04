# _*_coding:utf-8 _*_
"""
float decimal points
https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
"""


def round_float():
    f = 3.1415
    print round(f, 2)
    # 3.14

    a = 13.95
    print a
    # 13.95

    print "%.2f" % a
    # 13.95

    print "%.2f" % 13.9499999
    # 13.95

    a = 13.949999999999999
    print format(a, '.2f')
    # 13.95

if __name__ == '__main__':
    round_float()
    pass
