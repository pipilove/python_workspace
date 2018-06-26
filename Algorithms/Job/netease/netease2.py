#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
[编程|100分] 字符迷阵时间限制：C/C++ 1秒，其他语言 2秒
空间限制：C/C++ 65536K，其他语言 131072K
题目描述
注意：本题只允许使用C/C++，Java或Python进行解答，其他编程语言提交均视作无效处理。
字符迷阵是一种经典的智力游戏。玩家需要在给定的矩形的字符迷阵中寻找特定的单词。在这题的规则中，单词是如下规定的：1. 在字符迷阵中选取一个字符作为单词的开头；2. 选取右方、下方、或右下45度方向作为单词的延伸方向；3. 以开头的字符，以选定的延伸方向，把连续得到的若干字符拼接在一起，则称为一个单词。

以图1为例，如果要在其中寻找单词"WORD"，则绿色框所标示的都是合法的方案，而红色框所标示的都是不合法的方案。现在的问题是，给出一个字符迷阵，及一个要寻找的单词，问能在字符迷阵中找到多少个该单词的合法方案。注意合法方案是可以重叠的，如图1所示的字符迷阵，其中单词"WORD"的合法方案有4种。






输入描述:
输入的第一行为一个正整数T，表示测试数据组数。 接下来有T组数据。每组数据的第一行包括两个整数m和n，表示字符迷阵的行数和列数。接下来有m行，每一行为一个长度为n的字符串，按顺序表示每一行之中的字符。再接下来还有一行包括一个字符串，表示要寻找的单词。  数据范围： 对于所有数据，都满足1<=T<=9，且输入的所有位于字符迷阵和单词中的字符都为大写字母。要寻找的单词最短为2个字符，最长为9个字符。字符迷阵和行列数，最小为1，最多为99。 对于其中50%的数据文件，字符迷阵的行列数更限制为最多为20。
输出描述:
对于每一组数据，输出一行，包含一个整数，为在给定的字符迷阵中找到给定的单词的合法方案数。示例1
输入

3
10 10
AAAAAADROW
WORDBBBBBB
OCCCWCCCCC
RFFFFOFFFF
DHHHHHRHHH
ZWZVVVVDID
ZOZVXXDKIR
ZRZVXRXKIO
ZDZVOXXKIW
ZZZWXXXKIK
WORD
3 3
AAA
AAA
AAA
AA
5 8
WORDSWOR
ORDSWORD
RDSWORDS
DSWORDSW
SWORDSWO
SWORD
输出

4
16
5
'''
import sys, io

sys.stdin = io.StringIO(u'''3
10 10
AAWAAAWROW
WORDBBBBBB
OCCCWCCCCC
RFFFFOFFFF
DHHHHHRHHH
ZWZVVVVDID
ZOZVXXDKIR
ZRZVXRXKIO
ZDZVOXXKIW
ZZZWXXXKIK
WORD
3 3
AAA
AAA
AAA
AA
5 8
WORDSWOR
ORDSWORD
RDSWORDS
DSWORDSW
SWORDSWO
SWORD
''')
# 4
# 16
# 5

import re, sys


def count0(s, query):
    cnt = 0
    id = s.find(query)
    while 1:
        if id == -1:
            return cnt
        else:
            cnt += 1
            s = s[id + 1:]
            id = s.find(query)
    # a = [i.start() for i in re.finditer(query, s)]
    # return len(a)


its = int(sys.stdin.readline().strip())
for _ in range(its):
    a = []
    row, col = sys.stdin.readline().strip().split()
    row, col = int(row), int(col)
    for _ in range(row):
        a.append(sys.stdin.readline().strip())
    at = [''.join([i[k] for i in a]) for k in range(col)]
    query = sys.stdin.readline().strip()
    # cnt = sum([r.count(query) for r in a])

    cnt = sum([count0(r, query) for r in a])
    # print(cnt)
    cnt += sum([count0(r, query) for r in at])
    # print(cnt)

    q_len = len(query)
    for rid, r in enumerate(a[:-q_len + 1]):
        ids = [i.start() for i in re.finditer(query[0], r[:-q_len + 1])]
        for id in ids:
            cnt_add = 1
            for i, q in enumerate(query[1:]):
                if q != a[rid + i + 1][id + i + 1]:
                    cnt_add = 0
                    break
            cnt += cnt_add
    print(cnt)
    # exit()
