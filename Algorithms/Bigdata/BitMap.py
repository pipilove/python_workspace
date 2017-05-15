#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'BitMap算法。不一定最优'
__author__ = 'pipi'
__mtime__ = '3/16/17'
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
# import os, sys
#
# CWD = os.path.split(os.path.realpath(__file__))[0]
# sys.path.append(os.path.join(CWD, '../..'))
# from Oth.Utility.TimeStump import time_block

import array


def power2n(x):
    '''
    求比x大(或相等)且是2的n次方的数
    '''
    if x > 0 and (x & x - 1) == 0:  # x正好是2的n次方的数
        return x
    for i in (1, 2, 4, 8, 16, 32):  # 支持到64位int型，加上64则可以支持到128等等
        x |= x >> i
    # print(x + 1)
    return x + 1


class BitMap():
    def __init__(self, num_int=None, max_num=None, bit_num=32, shift=0):
        '''
        :param num_int: 数组大小
        :param max_num: 输入数据中最大的数
        :param shift: 如果数组中有<0的数，则所有数都要减去最小的那个负数
        '''
        if bit_num == 32:  # 位数组是32位的整数数组
            k = 5
            bit_type = 'I'  # unsigned int
        elif bit_num == 8:  # 位数组是8位的字符数组
            k = 3
            bit_type = 'B'  # unsigned char
        else:
            print('bit num?')
            exit()

        self.K = k
        self.BIT_TYPE = bit_type  # 默认32位unsighed int存储位。

        self.BIT_NUM = 1 << self.K
        self.shift = shift

        if num_int:  # 指定了数组大小就直接开num_int大的数组
            self.a = array.array(self.BIT_TYPE, [0] * num_int)
        elif max_num:  # 没有指定了数组大小，但是指定了最大的数，求出num_int
            num_int = power2n(max_num) >> self.K
            num_int = num_int if num_int > 0 else 1  # 至少应该有一个数组
            # with time_block():
            self.a = array.array(self.BIT_TYPE, [0] * num_int)  # todo 太慢了！
        else:  # 数组大小和最大数都没有指定，就默认数据都是1个int型
            self.a = array.array(self.BIT_TYPE, [0])
            # else:  # 数组大小和最大数都没有指定，就默认数据都是int型，最大为2^32
            #     self.a = array.array(self.BIT_TYPE, [0] * ((2 ** 32) >> self.K))

    def fit(self, x):
        '''
        将数据读入bitmap中存储
        '''
        MIN_NUM = min(x)
        if MIN_NUM < 0:
            self.shift = -MIN_NUM  # 如果数组中有<0的数，则所有数都要减去最小的那个负数
            x = [i + self.shift for i in x]
        else:
            self.shift = 0
        MAX_NUM = max(x)

        num_int = power2n(MAX_NUM) >> self.K
        num_int = num_int if num_int > 0 else 1  # 至少应该有一个数组
        # print(num_int)
        self.a = array.array(self.BIT_TYPE, [0] * num_int)
        for xi in x:
            self.set(xi)

    def set(self, xi, value=1):
        '''
        设置数xi在数组a中对应元素对应的位为1
        '''
        array_ix = xi >> self.K  # 数组的元素位置(从0开始)
        bit_ix = xi & ((1 << self.K) - 1)  # 数组元素中的bit位置(从0开始)，取模
        if value == 1:
            self.a[array_ix] |= 1 << bit_ix  # 对应的第bit_ix位置的2**bit_ix置1
        else:
            self.a[array_ix] &= ~((1 << bit_ix))  # 对应的第bit_ix位置的2**bit_ix置0

    def show_array(self):
        for ai in self.a:
            print('{:032b}'.format(ai))  # bin(ai)

    def search(self, xi):
        '''
        bitmap查找
        '''
        if self.shift != 0:
            xi += self.shift

        array_ix = xi >> self.K
        bit_ix = xi & ((1 << self.K) - 1)
        if (self.a[array_ix] & (1 << bit_ix)):
            flag = True
        else:
            flag = False
        return flag

    def sort(self):
        '''
        bitmap排序
        '''
        sorted_x = []
        for array_ix, ai in enumerate(self.a):
            for bit_ix in range(self.BIT_NUM):
                # 首先得到该第j位的掩码（0x01＜＜j），将内存区中的,位和此掩码作与操作。最后判断掩码是否和处理后的结果相同
                if (ai & (1 << bit_ix)) == (1 << bit_ix):
                    sorted_x.append(self.BIT_NUM * array_ix + bit_ix)
        # print(sorted_x)
        if self.shift != 0:
            sorted_x = [i - self.shift for i in sorted_x]
        return sorted_x

    def cnt(self):
        '''
        计数，看bit array中有多少个数。
        '''
        return sum([self.bit_cnt(i) for i in self.a])

    def bit_cnt(self, n):
        '''
        求某个整数的二进制表示中1的个数。平行算法。
        '''
        n = (n & 0x55555555) + (n >> 1 & 0x55555555)
        n = (n & 0x33333333) + (n >> 2 & 0x33333333)
        n = (n & 0x0f0f0f0f) + (n >> 4 & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + (n >> 8 & 0x00ff00ff)
        n = (n & 0x0000ffff) + (n >> 16 & 0x0000ffff)
        return n


def test():
    import os, sys

    CWD = os.path.split(os.path.realpath(__file__))[0]
    sys.path.append(os.path.join(CWD, '../..'))
    from Oth.Utility.TimeStump import time_block

    with time_block('time'):
        bm = BitMap()
        bm.fit([-3, -44, 7, 2, 5, 3, 32])
        bm.show_array()
        print(bm.search(7))
        print(bm.search(6))
        print(bm.sort())

# test()
