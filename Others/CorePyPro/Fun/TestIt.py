#!/usr/bin/env python
# coding=gbk
"""
__title__ = '11.6 Testing Functions (testit.py)testit()用其参数地调用了一个给定的函数，
成功的话，返回一个和那函数返回值打包的True的返回值，或者False 和失败的原因'
__author__ = 'pi'
__mtime__ = '2014.12.10'
"""


def testIt(func, *nkw, **kw):
    try:
        retVal = (True, func(*nkw, **kw))
    except Exception as diag:
        retVal = (False, diag)  # str(diag))
    return retVal


def test():
    funcs = (int, int, float)
    args = (1234, 12.34, '1234', '12.34')

    for func in funcs:
        for arg in args:
            retVal = testIt(func, arg)
            if retVal[0]:
                print("%s(%s) = " % (func.__name__, repr(arg)), retVal[1])
            else:
                print("%s(%s) = FAILED!!!" % (func.__name__, repr(arg)), retVal[1])


if __name__ == '__main__':
    test()
