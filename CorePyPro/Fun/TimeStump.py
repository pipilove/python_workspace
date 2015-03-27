#!/usr/bin/env python
# coding=gbk
"""
__title__ = '带参数和不带参数的timeStump'
__author__ = 'pi'
__mtime__ = '2014.12.12'
"""
from time import ctime
import datetime


def timeStump(func):
    """
    time stump decorator of func 不带参数的时间戳函数
    :param func:
    :return:
    """

    def wrappedFunc(*nkw):
        print(("start_time %s" % datetime.datetime.now() ))  # ctime())  #Accurate to microseconds
        func(*nkw)
        print(("end_time %s" % datetime.datetime.now() ))  # ctime())

    return wrappedFunc


def totalTime(func):
    """
    total running time of func
    :param func:
    :return:
    """

    def wrappedFunc(*nkw):
        print(("start_time %s" % datetime.datetime.now() ))  # ctime())  #Accurate to microseconds
        func(*nkw)
        print(("end_time %s" % datetime.datetime.now() ))  # ctime())

    return wrappedFunc


def timeStumpFunc_args(deco_args):
    """
    time stump decorator of func 不带参数的时间戳函数
    :param deco_args:
    :return:
    """
    print("timeStump for function %s" % deco_args)

    def getFunc(func):
        def wrappedFunc(*nkw):
            print(("start_time %s" % ctime()))
            func(*nkw)
            print(("end_time %s" % ctime()))

        return wrappedFunc

    return getFunc


"""
example
"""
@timeStump
# @timeStumpFunc_args('do_sth')
def do_sth(*nkw):
    print("%s" % nkw)

