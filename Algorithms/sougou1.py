#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
钝角三角形个数
'''
import sys, io

sys.stdin = io.StringIO(u'''4
0.00000000
56.00000000
179.00000000
180.00000000
''')

import sys

points = int(sys.stdin.readline().strip())
a0 = float(sys.stdin.readline().strip())
a = [float(sys.stdin.readline().strip()) - a0 for _ in range(points - 1)]
# a0 = a[0]
# a = [i - a0 for i in a]
a = [a0] + a
cnt0 = 0
for i in range(points):
    cnt = cnt2 = 0
    for p in a[i:]:
        if a[i] < p < a[i] + 180:
            cnt += 1
        if a[i] + 180 < p < a[i] + 360:
            cnt2 += 1
    cnt0 += cnt * (cnt - 1) / 2 + cnt2 * (cnt2 - 1) / 2
print(cnt0)
