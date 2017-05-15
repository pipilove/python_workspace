#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '两数组找相同的元素'
'两数组找相同的元素-array
今日头条2017实习生招聘418在线笔试编程
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
给两个整数(int)数组，输出相同的元素。
输入
给定两个整型数组[a1, a2, ...., am]，[b1, b2, ..., bn]
输入格式如下，第一行给定第一个数组的大小m，接下来的m行为其数组元素a1 -- am，每行一个元素；第m+1行为第二个数组的大小n，接下来的n行为其数组元素b1 -- bn，也是每行一个元素。示例如下：
m
a1
a2
…
am
n
b1
b2
…
bn
​
输出
两个数组中相同的元素，以空格分隔在一行中显示，显示顺序为其在第二个数组中出现的顺序。

样例输入
5
11
15
9
12
3
4
11
3
9
7

样例输出
11 3 9
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

random.seed(1)

N1 = 500000
N2 = 5000000
MAXRANGE = 10000000
input1 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N1)])
input1 = str(N1) + '\n' + input1
input2 = '\n'.join([str(random.randint(1, MAXRANGE)) for _ in range(N2)])
input2 = str(N2) + '\n' + input2
input = input1 + '\n' + input2 + '\n'
# print input3
sys.stdin = io.StringIO(unicode(input))

with time_block('time:'):
    import sys, os

    with time_block('a'):
        an = int(raw_input())
        a = set([sys.stdin.readline().strip() for _ in range(an)])

    bn = int(raw_input())
    with time_block('b'):
        b = [raw_input() for _ in range(bn)]
        c = [i for i in b if i in a]
        print ' '.join(c)
