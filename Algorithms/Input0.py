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
sys.path.append(os.path.join(CWD, '..'))
from Oth.Utility.TimeStump import time_block

import random

random.seed(1)

N1 = 50
N2 = 50
MAXRANGE = 10000
input1 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N1)])
input1 = str(N1) + '\n' + input1
input2 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N2)])
input2 = str(N2) + '\n' + input2
input3 = input1 + '\n' + input2 + '\n'
# print input3
sys.stdin = io.StringIO(unicode(input3))
# sys.stdin = io.StringIO('''4,6
sys.stdin = io.StringIO(u'''4,6
8 9 6 5
9,7
8,5
8,4
9,3
7,3
7,2
''')

with time_block('running time: '):
    import re, sys, os

    a = []
    while True:
        try:
            ai = sys.stdin.readline().strip()
            if not ai:
                break
            a.append([int(i) for i in re.split('\s|,', ai)])
        except:
            break
    print(a)
