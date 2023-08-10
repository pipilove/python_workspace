#!/usr/bin/env python
# coding=gbk
"""
__title__ = '带参数和不带参数的timeStump for py3'
__author__ = 'pi'
__mtime__ = '2014.12.12'
"""
from contextlib import contextmanager
import datetime
import time


def time_process(func):
    '''
    program process time. 处理时间而非自然时间
    :return:
    '''

    def wrapped_func(*nkw, **kwargs):
        start_time = time.process_time()
        r = func(*nkw, **kwargs)  # 没有返回值就不用记录r
        print('{}.{} : {}'.format(func.__module__, func.__name__, time.process_time() - start_time))
        return r

    return wrapped_func


def time_nature(func):
    '''
    function nature process time. 自然时间(会被很多其他因素影响，如计算机的负载)
    :return:
    '''

    def wrapped_func(*nkw, **kwargs):
        start_time = time.perf_counter()
        r = func(*nkw, **kwargs)
        print('{}.{} : {}'.format(func.__module__, func.__name__, time.perf_counter() - start_time))
        return r

    return wrapped_func


@contextmanager
def time_block(label='counting'):
    '''
    program block nature process time. 针对代码块的.
    usage:
    with time_block('counting'):
        statement block
    :return:
    '''
    start_time = time.perf_counter()
    try:
        yield
    finally:
        print('{} : {}'.format(label, time.perf_counter() - start_time))


def time_stump(func):
    """
    time stump decorator of func 不带参数的时间戳函数
    :param func:
    :return:
    """

    def wrappedFunc(*nkw):
        print(("start_time %s" % datetime.datetime.now()))  # Accurate to microseconds
        result = func(*nkw)
        print(("end_time %s" % datetime.datetime.now()))
        return result

    return wrappedFunc


def total_time(func):
    """
    total running time of func
    :param func:
    :return:
    """

    def wrappedFunc(*nkw):
        start_time = datetime.datetime.now()  # Accurate to microseconds
        result = func(*nkw)
        end_time = datetime.datetime.now()
        print('{}.{} : {}'.format(func.__module__, func.__name__, (end_time - start_time).total_seconds()))
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
            print(("start_time %s" % time.ctime()))
            result = func(*nkw)
            print(("end_time %s" % time.ctime()))
            return result

        return wrappedFunc

    return getFunc

# # # example

# import sys, os
#
# CWD = os.path.split(os.path.realpath(__file__))[0]
# sys.path.append(os.path.join(CWD, '../..'))
# from Oth.Utility.TimeStump import time_process
#
# @time_process
# def do_sth(*nkw):
#     print("%s" % nkw)
