#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'DAU 统计'
__author__ = 'pipi'
__mtime__ = '4/18/17'
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
from Algorithms.Bigdata.BitMap import BitMap

import random

random.seed(0)

N1 = 1
MAXRANGE = 800
input1 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N1)])
input1 = input1 + '\n' + '0'
# print input1
# sys.stdin = io.StringIO(unicode(input1))
sys.stdin = io.StringIO(u'''12933
111111
59220
69433
59220
111111
0
''')

with time_block('2.1:'):
    bm = BitMap(max_num=2 ** 32)  # 假设最大的数是2^32而不是2^64才能这样做，否则不行
    ai = int(sys.stdin.readline().strip())
    while ai:
        bm.set(ai)
        ai = int(sys.stdin.readline().strip())
    print(bm.cnt())
