#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import sys, io
#
# # sys.stdin = io.StringIO('''4,6
# sys.stdin = io.StringIO(u'''2
# 3
# 1 10 100
# 4
# 1 2 3 4
# ''')

import sys

cnts = int(sys.stdin.readline().strip())
for _ in range(cnts):
    sys.stdin.readline().strip()
    ai = sys.stdin.readline().strip()
    a = [int(i) for i in ai.split()]
    s_1 = [(i & 1) == 1 for i in a]
    s_4 = [(i % 4) == 0 for i in a]
    if sum(s_4) >= sum(s_1):
        print('YES')
    else:
        print('NO')
