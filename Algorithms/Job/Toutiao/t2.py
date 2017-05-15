#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'DAU 统计'
'DAU 统计
今日头条2017实习生招聘418在线笔试编程
时间限制：C/C++语言 2000MS；其他语言 4000MS
内存限制：C/C++语言 32768KB；其他语言 557056KB
题目描述：
日活跃用户数 (DAU) 是衡量一个产品表现的重要指标。
需要编写程序，根据给定的某一天的 n 条访问记录，对当天的用户总数 m 进行统计。
每个用户可能访问多次。
为了方便，我们用数字 (uid) 唯一标识每个用户。
输入
每一行包含一个 uid，遇到 0 时认为输入结束。
输入共包含 n+1 行，可认为是无序的。
输出
一个数字：去重后 uid 的数量 m。

样例输入
12933
111111
59220
69433
59220
111111
0
样例输出
4

Hint
数据范围
0 < uid < 2^63
对于 30% 的数据，0 < n < 100,000, 0 < m < 100,000
对于 100% 的数据，0 < n < 1,000,000, 0 < m < 800,000
'
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

import random

random.seed(0)

N1 = 100
MAXRANGE = 800000
input1 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N1)])
input1 = input1 + '\n' + '0'
# print input1
sys.stdin = io.StringIO(unicode(input1))
sys.stdin = io.StringIO(u'''12933
111111
59220
69433
59220
111111
0
''')

with time_block('time:'):
    a = set()
    ai = sys.stdin.readline().strip()
    while ai != '0':
        a.add(ai)
        ai = sys.stdin.readline().strip()
    print len(a)
