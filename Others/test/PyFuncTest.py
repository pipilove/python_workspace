#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'python实例方法，类方法和静态方法区别及使用'
__author__ = '皮'
__mtime__ = '2/19/2016-019'
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
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import traceback


class T:
    def InstanceMethod(self):
        print("instance Method!")
        print(self)

    @classmethod
    def ClassMethod(cls):
        # def ClassMethod(self):#当然这样也不会出错
        print("class Method")
        print(cls)

    @staticmethod
    def StaticMethod():
        print("static METHOD")


t = T()

t.InstanceMethod()
t.ClassMethod()
t.StaticMethod()

T.ClassMethod()
T.StaticMethod()

T.InstanceMethod(t)

# 错误的情况
try:
    t.ClassMethod(T)
    T.InstanceMethod()
except:
    print(traceback.format_exc())
