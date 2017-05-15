#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
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

N1 = 5
N2 = 50
MAXRANGE = 100
input1 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N1)])
input1 = str(N1) + '\n' + input1
input2 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N2)])
input2 = str(N2) + '\n' + input2
input3 = input1 + '\n' + input2 + '\n'
# print input3
# sys.stdin = io.StringIO(unicode(input3))
# sys.stdin = io.StringIO('''4,6
# sys.stdin = io.StringIO(u'''1000 1000000''')
# sys.stdin = io.StringIO(u'''4 1''')
# sys.stdin = io.StringIO(u'''4 4''')
# sys.stdin = io.StringIO(u'''4 5''')
# sys.stdin = io.StringIO(u'''4 6''')
# sys.stdin = io.StringIO(u'''4 7''')
# sys.stdin = io.StringIO(u'''4 8''')
# sys.stdin = io.StringIO(u'''4 9''')
# sys.stdin = io.StringIO(u'''4 10''')
# sys.stdin = io.StringIO(u'''4 11''')
# sys.stdin = io.StringIO(u'''4 12''')
# sys.stdin = io.StringIO(u'''4 13''')
# sys.stdin = io.StringIO(u'''4 14''')
# sys.stdin = io.StringIO(u'''4 15''')
sys.stdin = io.StringIO(u'''4 16''')

# with time_block('running time: '):
import re, sys, os

a = sys.stdin.readline().strip().split()
n = int(a[0])
m = int(a[1])
# print(n)
# print(m)

if m < n:
    print '1' + str(m)
else:
    m -= n
    k = 1
    while m > k * (2 * n - k - 1):
        k += 1
    k -= 1
    # print 'k', k
    s = m - k * (2 * n - k - 1)

    # print 's', s

    if k % 2 == 0:
        # st = [2, n]
        # st = [2 + k // 2, n - k // 2]
        x, y = 2 + k // 2, n - k // 2
        # print x, y
        if s <= n - k - 1:
            x += s - 1
        else:
            # print 'n - k - 1', n - k - 1
            y = y - (s - (n - k - 1))
            x = x + (n - k - 1) - 1
            # x = x + (s - (n - k - 1) + 1)
            # print 'x, y', x, y
    else:
        # st = [n - 1, 1]
        # st = [(n - 1) - k // 2, 1 + k // 2]
        x, y = (n - 1) - k // 2, 1 + k // 2
        if s <= n - k - 1:
            x -= s - 1
        else:
            # print 'x, y', x, y
            y = y + (s - ((n - k - 1)))
            x = x - ((n - k - 1) - 1)
            # print 'x, y', x, y
            # x = x - (s - (n - k - 1) + 1)
    print x,y
