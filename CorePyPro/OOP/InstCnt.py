#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '13.5 - 解构器、跟踪实例计数'
__author__ = 'pi'
__mtime__ = '12/26/2014-026'
# code is far away from bugs with the god animal protecting
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ━      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


class P(object):
    def __init__(self):
        print("parent's __init__ called")

    def __del__(self):
        print("parent's __del__ called")


class C(P):
    def __init__(self):
        print("child's __init__ called")

    def __del__(self):
        P.__del__(self)
        # print("child's __del__ called")


class InstCnt(object):
    """
    track #instance of class InstCnt
    """
    inst_count = 0

    def __init__(self):
        print("__init__ called")
        InstCnt.inst_count += 1

    def __del__(self):
        print("__del__ called")
        InstCnt.inst_count -= 1

    def get_inst_count(self):
        return InstCnt.inst_count


def test_InstCnt():
    """
    测试类的实例数目
    :return:
    """
    inst0 = InstCnt()
    inst1 = InstCnt()
    print(inst0.get_inst_count())
    del inst0
    print(inst1.get_inst_count())
    del inst1
    print()

    """
    测试调用了多少次解构器
    """
    inst0 = InstCnt()
    inst1 = inst0
    inst2 = inst1
    print(inst2.get_inst_count())
    del inst0
    del inst1
    print(inst2.get_inst_count())
    del inst2


def test_C():
    """
    测试调用了多少次解构器
    :return:
    """
    inst0 = C()
    inst1 = inst0
    inst2 = inst0
    del inst0
    del inst1
    del inst2


if __name__ == '__main__':
    test_InstCnt()
    # test_C()
