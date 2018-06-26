#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, io

sys.stdin = io.StringIO(u'''9
1 2 3 3 5 3 4 2 2
3
1 4 1
2 6 5
3 9 3
''')

import sys, collections


def BinarySearch(a, target, flag):
    low = 0
    high = len(a) - 1
    if (not flag and a[-1] < target) or (flag and a[0] > target):
        return -1

    while low <= high:
        mid = (low + high) // 2
        midVal = a[mid]

        if midVal < target:
            low = mid + 1
        elif midVal > target:
            high = mid - 1
        else:
            return mid
    return mid


man_cnt = int(sys.stdin.readline().strip())

query_dict = collections.defaultdict(list)
prefers = sys.stdin.readline().strip().split()
for id, q in enumerate(prefers):
    query_dict[q].append(id + 1)
# print(query_dict)

query_cnt = int(sys.stdin.readline().strip())
for _ in range(query_cnt):
    q1, q2, q = sys.stdin.readline().strip().split()
    l1 = query_dict[q]
    ind_low = BinarySearch(l1, int(q1), 0)
    if ind_low == -1:
        print(0)
        continue
    ind_high = BinarySearch(l1, int(q2), 1)
    if ind_high == -1:
        print(0)
        continue
    # print('ind_low', ind_low)
    # print('ind_high', ind_high)
    print(ind_high - ind_low + 1)
    # print('*' * 8)
