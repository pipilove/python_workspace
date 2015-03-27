#!/usr/bin/env python
# coding=gbk
"""
__title__ = '�������Ͳ���������timeStump'
__author__ = 'pi'
__mtime__ = '2014.12.12'
"""
from time import ctime
import datetime


def timeStump(func):
    """
    time stump decorator of func ����������ʱ�������
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
    time stump decorator of func ����������ʱ�������
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

