#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '冒泡排序+简单选择排序。O(n^2)，稳定'
__author__ = 'pipi'
__mtime__ = '4/14/17'
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
from random import randint


def bubble_sort0(lst):
    '''
    原始冒泡排序
    '''
    length = len(lst)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            # 比较相邻两个元素大小，并根据需要进行交换
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort1(x):
    '''
    改进：添加swap
    '''
    for i in range(len(x), 0, -1):
        swap = False
        for j in range(i - 1):
            if x[j] > x[j + 1]:  # 升序
                # if x[j] < x[j + 1]:  # 降序
                x[j], x[j + 1] = x[j + 1], x[j]
                swap = True
        if not swap:  # 本次排序没有交换，后面数据已有序，则结束
            break
    print(x)


def bubble_sort2(x):
    '''
    改进：记录上次交换的最后位置L，L后面的都是有序的（后面部分有序），因为没有发生交换。可知这个改进的特殊情况就是添加swap变量判断是不是整个都有序。
    '''
    i = len(x) - 1  # 需要进行比较的j的最大索引
    while (i > 0):
        last_swap = 0
        for j in range(0, i):
            if x[j] > x[j + 1]:  # 升序
                # if x[j] < x[j + 1]:  # 降序
                x[j], x[j + 1] = x[j + 1], x[j]
                last_swap = j
        i = last_swap


def bubble_sort(x):
    '''
    改进：简单选择排序。每次选择子数组（长度为i，从最大到0）中最大的数放在子数组最后。
    '''
    for i in range(len(x), 1, -1):
        max = i - 1  # 当前需要比较的子数组中最大的数的下标
        for j in range(0, i):
            if x[max] < x[j]:
                max = j
        x[j], x[max] = x[max], x[j]
        # for line in range(0, length):
        #     min = line;
        #     for j in range(line+1, length):
        #         #比较相邻两个元素大小，并根据需要进行交换
        #         if lst[min] > lst[j]:
        #             min = j
        #     lst[line], lst[min] = lst[min], lst[line]


lst = [randint(1, 100) for i in range(20)]
# lst = [23, 15, 14, 25, 28, 30]
print('Before sort:\n{} {}'.format(len(lst), lst))
bubble_sort(lst)
print('After sort:\n{} {}'.format(len(lst), lst))
