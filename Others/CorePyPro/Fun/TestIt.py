#!/usr/bin/env python
# coding=gbk
"""
__title__ = '11.6 Testing Functions (testit.py)testit()��������ص�����һ�������ĺ�����
�ɹ��Ļ�������һ�����Ǻ�������ֵ�����True�ķ���ֵ������False ��ʧ�ܵ�ԭ��'
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
