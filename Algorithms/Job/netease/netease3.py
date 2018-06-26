#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
蜡烛排列时间限制：C/C++ 1秒，其他语言 2秒
空间限制：C/C++ 65536K，其他语言 131072K
题目描述
注意：本题只允许使用C/C++，Java或Python进行解答，其他编程语言提交均视作无效处理。
小Q有N根长短不一的蜡烛。他希望这些蜡烛中挑选出M根，然后把这些蜡烛从低到高排列成一行。假设排列成一行后，所有相邻的蜡烛间的高度差为T1-T0，T2-T1,…TM-1-TM-2，其中Ti为第i根蜡烛的高度。假设这些高度差中的最小值为K，即K=min{T1-T0，T2-T1,…TM-1-TM-2}。
排列后蜡烛的美感取决于K的大小，小Q认为K越大蜡烛排列得越有层次感，所以他想知道，在已知N根蜡烛的长度以及给定M的情况下，K的最大值是多少。
输入描述:
每个输入数据包含多个测试点。每个测试点后有一个空行。 第一行为测试点的个数T(T<=10)。 每个测试点包含包含1行，其中前两个数为N（1 < N <= 100000），M(1 < M <= N)，然后是N个整数Ri（0 <= i < N，0 < Ri <= 1000000），分别表示N根蜡烛的长度。
输出描述:
对于每个测试点，输出一行，包含一个整数，代表K的最大值是多少。示例1
输入

2
3 2 10 2 3
5 3 1 3 4 7 11
输出

8
4
'''
import sys, io

sys.stdin = io.StringIO(u'''2
3 2 10 2 3
5 3 1 3 4 7 11
''')

import sys

its = int(sys.stdin.readline().strip())
for _ in range(its):
    ai = sys.stdin.readline().strip()
    a = [int(i) for i in ai.split()]
    n = a[0]
    m = a[1]
    hs = a[2:]
    hs.sort()
    hss = [i - j for i, j in zip(hs[1:], hs[0:-1])]
    print(hss)
    print(n, m, hs)
