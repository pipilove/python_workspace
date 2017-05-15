#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '求某个整数的二进制表示中1的个数'
__author__ = 'pipi'
__mtime__ = '4/23/17'
__email__ = 'pipijob@126.com'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓    ┏┓
            ┏━┛┻━━━━┛┻━┓
            ┃     ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃     ┻    ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━┓┓┏━━┳┓┏━┛
                ┃┫┫  ┃┫┫
                ┗┻┛  ┗┻┛
"""


def bit_cnt0(n):
    '''
    计算整数x的二进制中bit位为1的个数
    '''
    # 最低位为1（类似2**k幂的判断）
    cnt = 0
    while n:
        cnt += 1
        n &= n - 1
    return cnt


def bit_cnt(n):
    '''
    平行算法：类似归并
    '''
    n = (n & 0x55555555) + (n >> 1 & 0x55555555)
    n = (n & 0x33333333) + (n >> 2 & 0x33333333)
    n = (n & 0x0f0f0f0f) + (n >> 4 & 0x0f0f0f0f)
    n = (n & 0x00ff00ff) + (n >> 8 & 0x00ff00ff)
    n = (n & 0x0000ffff) + (n >> 16 & 0x0000ffff)
    return n


def test():
    import sys, io
    sys.stdin = io.StringIO(unicode('3'))
    # sys.stdin = io.StringIO(unicode(str(2 ** 32 - 1)))

    x = int(sys.stdin.readline().strip())
    print bit_cnt0(x)
    print bit_cnt(x)

# test()
