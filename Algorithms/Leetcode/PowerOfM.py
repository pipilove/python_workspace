#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '判断一个数是否是M的幂数'
__author__ = 'pipi'
__mtime__ = '4/21/17'
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


def isPowerOfM(num, m, func=1):
    '''
    判断一个数是否是M的幂数的通用方法
    '''
    if func == 1:
        # 不停除M法 O(n)?
        if (num > 1):
            while (num % m == 0):
                num /= m
        return num == 1

    elif func == 2:
        # 对数换底法 O(1)
        from math import log10
        if num <= 0:
            return False
        r = log10(num) / log10(m)  # log(m, 10)精度还是会出错，num超出2**32也会出错！
        return not bool(r - int(r))

    elif func == 3:
        # m^k次方一定能被最大的M^maxk (<2^32)整除
        from math import log, pow
        maxPowerOfM = int(pow(m, (int)(log(0x7fffffff) / log(m))))
        # print maxPowerOfM
        return maxPowerOfM % num == 0 if num > 0 else False

    else:
        pass


def isPowerOfTwo(num):
    """
    :type num: int
    :rtype: bool
    """
    return num > 0 and (num & num - 1) == 0


def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    return num > 0 and (num & num - 1) == 0 and (num & 0x5555555555555555) != 0

    # return num > 0 and (num & num - 1) == 0 and (num & 0x5555555555555555) == num

    # return num > 0 and (num & num - 1) == 0 and (num - 1) % 3 == 0


def isPowerOfTree(num):
    """
    :type num: int
    :rtype: bool
    """
    # max_power_of3 = 3 ** 19
    return isPowerOfM(num, 3, func=3)


def test():
    import sys, os, io

    CWD = os.path.split(os.path.realpath(__file__))[0]
    sys.path.append(os.path.join(CWD, '../..'))
    from Oth.Utility.TimeStump import time_block

    import random

    random.seed(1)

    N1 = 50000
    MAXRANGE = 19
    input1 = '\n'.join([str(3 ** random.randint(1, MAXRANGE)) for _ in range(N1)])
    # input1 = '\n'.join([str(4 ** random.randint(1, MAXRANGE)) for _ in range(N1)])
    # input2 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N1)])
    input4 = '\n'.join(['-2147483648', '-2', '0', '243'])
    # input3 = input1 + '\n' + input2 + '\n' + input4
    input3 = input1 + '\n' + input4
    # print input3
    sys.stdin = io.StringIO(unicode(input3))

    with time_block('running time: '):
        while True:
            try:
                x = int(sys.stdin.readline().strip())
            except:
                break
            # r= solute.isPowerOfTwo(x)
            # r= solute.isPowerOfFour(x)
            r = isPowerOfTree(x)
            rm = isPowerOfM(x, 3)
            if r != rm:
                print x
                print r
                print rm

# test()
