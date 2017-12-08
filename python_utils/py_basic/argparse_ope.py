# _*_ coding:utf-8 _*_

"""
this file is demo about basic args parse usage
"""

import argparse


def args_num_sum():
    parser = argparse.ArgumentParser(description="process some integers")

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for accumulator')

    parser.add_argument('--sum', dest='accumulate', action='store_const',
                         const=sum, default=max, help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)


if __name__ == '__main__':
    args_num_sum()
    pass
