#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '未完成'
__author__ = 'pipi'
__mtime__ = '3/24/17'
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
import sys, os, io

CWD = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CWD, '../..'))
from Oth.Utility.TimeStump import time_block

import random

random.seed(1)

N1 = 50
N2 = 500
MAXRANGE = 100
input1 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N1)])
input1 = str(N1) + '\n' + input1
input2 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N2)])
input2 = str(N2) + '\n' + input2
input3 = input1 + '\n' + input2 + '\n'
# print input3
# sys.stdin = io.StringIO(unicode(input3))
# sys.stdin = io.StringIO('''4,6
'''N T
a1 b1 … aN bN
c11 d11 … c1N d1N
:
cT1 dT1 … cTN dTN
'''
sys.stdin = io.StringIO(u'''3 2
100 2 300 4 500 6
100 1 300 3 500 5
100 0 300 2 500 4
''')
sys.stdin = io.StringIO(u'''7 7
67713 33909 33836 41869 48202 -55981 25228 73097 -36409 68204 -18112 53282 -90146 27557
94032 -51410 84572 -19631 -96923 -17401 57340 93364 -2401 651 51373 -1461 -47225 53199
-23113 -49093 43632 -65826 32479 -51039 -76774 -17794 -67028 92308 93409 23587 -12614 -42196
96134 -78703 95445 67153 46853 99595 24723 -5170 28312 -11609 -23248 -32142 -10519 28123
-92881 -46756 15061 -44646 -50838 -80756 -43565 8998 90821 36119 11184 -80166 -97177 -66486
49294 78278 -58495 -2590 852 -28113 -85652 59762 36511 -92147 11573 89991 792 -19780
-66975 6920 76003 21403 8703 71236 -23879 -22392 -84066 70015 37068 46390 -2390 -31264
99874 27238 -45279 94110 23675 32134 -7035 -3878 -42939 -41090 488 53101 -3945 -78084
''')

with time_block('running time: '):
    import re, sys, os

    a = sys.stdin.readline().strip().split()
    n, t = int(a[0]), int(a[1])
    b = sys.stdin.readline().strip().split()
    b = [int(i) for i in b]
    robot = zip(b[0::2], b[1::2])
    # print robot

    check_list_all = []
    for i in range(t):
        a = sys.stdin.readline().strip().split()
        a = [int(i) for i in a]
        check_list_all.append(zip(a[0::2], a[1::2]))
    # print check_list_all

    all_l = 0
    for check_list in check_list_all:
        for check in check_list:
            l0 = 4 * (10 ** 5) + 1
            for r in robot:
                l = abs(check[0] - r[0]) + abs(check[1] - r[1])
                if l < l0:
                    l0 = l
                    # c0 = check_list
                    # r0 = r
            # robot -= r0
            all_l += l0
        robot = check_list
    print all_l
