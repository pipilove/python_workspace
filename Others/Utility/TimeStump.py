#!/usr/bin/env python
# coding=gbk
"""
__title__ = '带参数和不带参数的timeStump'
__author__ = 'pi'
__mtime__ = '2014.12.12'
"""
from contextlib import contextmanager
import datetime
from time import ctime

try:  # py3
    from time import perf_counter
    from time import process_time
except:  # py2
    from time import clock as perf_counter
    from time import clock as process_time


def time_process(func):
    '''
    program process time
    :return:
    '''

    def wrapped_func(*nkw, **kwargs):
        start_time = process_time()
        r = func(*nkw, **kwargs)  # 没有返回值就不用记录r
        print('{}.{} : {}'.format(func.__module__, func.__name__, process_time() - start_time))
        return r

    return wrapped_func


def time_nature(func):
    '''
    function nature process time
    :return:
    '''

    def wrapped_func(*nkw, **kwargs):
        start_time = perf_counter()
        r = func(*nkw, **kwargs)
        print('{}.{} : {}'.format(func.__module__, func.__name__, process_time() - start_time))
        return r

    return wrapped_func


@contextmanager
def time_block(label='counting'):
    '''
    program block nature process time
    usage:
    with time_block('counting'):
        statement block
    :return:
    '''
    start_time = perf_counter()
    try:
        yield
    finally:
        print('{} : {}'.format(label, perf_counter() - start_time))


def time_stump(func):
    """
    time stump decorator of func 不带参数的时间戳函数
    :param func:
    :return:
    """

    def wrappedFunc(*nkw):
        print(("start_time %s" % datetime.datetime.now()))  # ctime())  #Accurate to microseconds
        result = func(*nkw)
        print(("end_time %s" % datetime.datetime.now()))  # ctime())
        return result

    return wrappedFunc


def total_time(func):
    """
    total running time of func
    :param func:
    :return:
    """

    def wrappedFunc(*nkw):
        start_time = datetime.datetime.now()
        # print(("start_time %s" % start_time ))  # ctime())  #Accurate to microseconds
        result = func(*nkw)
        end_time = datetime.datetime.now()
        # print(("end_time %s" % end_time ))  # ctime())
        print('{}.{} : {}'.format(func.__module__, func.__name__, end_time - start_time))
        return result

    return wrappedFunc


def timeStumpFunc_args(deco_args):
    """
    time stump decorator of func 不带参数的时间戳函数
    :param deco_args:
    :return:
    """
    print("time_stump for function %s" % deco_args)

    def getFunc(func):
        def wrappedFunc(*nkw):
            print(("start_time %s" % ctime()))
            result = func(*nkw)
            print(("end_time %s" % ctime()))
            return result

        return wrappedFunc

    return getFunc


# example
@time_process
# @timeStumpFunc_args('do_sth')
def do_sth(*nkw):
    print("%s" % nkw)


# import sys, os, io
#
# CWD = os.path.split(os.path.realpath(__file__))[0]
# sys.path.append(os.path.join(CWD, '../..'))
# from Oth.Utility.TimeStump import time_block
