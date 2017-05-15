#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '排序算法'
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


def insertion_sort(x):
    '''
    插入排序。O(n^2)，稳定。
    '''
    for j in range(1, len(x)):
        i = j - 1
        key = x[j]
        while x[i] > key and i >= 0:  # 升序
            # while x[line] < key and line >= 0:  # 降序
            x[i + 1] = x[i]  # 插入排序可以使用折半插入，因为0:j-1是有序的
            i -= 1
        x[i + 1] = key
    print(x)




def quick_sort(x):
    '''
    快排。O(nlgn)，稳定+不稳定。
    '''
    import random

    def stable_partition0(x, low, high):  # 包含[low, high]
        '''
        稳定快排未完成
        '''
        pivot = x[high]
        i = low
        for j in range(low, high):  # [low, high-1] # 类似冒泡操作
            if x[j] <= pivot:
                while x[i] <= x[j] and i < j:#可能不是快排了，可能O(n^2)了
                    i += 1
                if i < j:
                    x[i], x[j] = x[j], x[i]
                i += 1
        x[high], x[i] = x[i], pivot
        return i

    def partition(x, low, high):  # 包含[low, high]
        # random partition
        # pivot_ix = random.choice(range(low, high + 1))
        # x[pivot_ix], x[high] = x[high], x[pivot_ix]
        # 三数取中partition
        # pivot_ixs = [random.choice(range(low, high + 1))]

        pivot = x[high]
        i = low
        for j in range(low, high):  # [low, high-1] # 类似冒泡操作
            if x[j] <= pivot:
                x[i], x[j] = x[j], x[i]
                i += 1
        x[high], x[i] = x[i], pivot
        return i

    def qsort(x, i, j):
        if i < j:
            pivot_ix = partition(x, i, j)
            qsort(x, i, pivot_ix - 1)
            qsort(x, pivot_ix + 1, j)

    qsort(x, 0, len(x) - 1)
    print(x)


if __name__ == '__main__':
    xs = [[5, 2, 4, 6, 1, 3], [], [1, 2, 3, -2, -3, 1.0], [2, 2, 2, 2, 2], [3, 2, 2, 2, 3, 4],
          [2, 2, 2.0, 2, 2.0, 2, 2.0, 2.0, 2.0, 2]]
    for x in xs:
        # print('x:{}\n排序后：'.format(x), end='')
        # insertion_sort(x)
        # bubble_sort(x)
        quick_sort(x)
