#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '判断字符串是否由数字组成（int或者float）'
__author__ = '皮'
__mtime__ = '11/19/2015-019'
__email__ = 'pipisorry@126.com'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
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
import re


def IsFloatStr(s):
    '''
    浮点数判断
    '''
    try:
        float(s)
        # s.isdigit()  # 这个是错的，不能判断
        # 正则表达式实现
        # return True if re.match(r'[-+]?\d+?\.?\d*$', s) else False
        return True
    except:
        return False


def IsIntStr(s):
    '''
    整数判断
    '''
    try:
        int(s)
        # s.isdigit()#这个是错的，不能判断
        # return True if re.match(r'[-+]?\d+$', s) else False
        return True
    except:
        return False


for s in ['123', '-123', '+123', '-12.3', '-1.2.3', '123hello']:
    print('s is a num str' if IsFloatStr(s) else 's is not a num str')
    # print('s is a num str' if IsIntStr(s) else 's is not a num str')
