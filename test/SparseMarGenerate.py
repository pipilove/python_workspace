#!/usr/bin/env python
# coding=gbk
"""
__title__ = 'how to generate sparse mat'
__author__ = 'pi'
__mtime__ = '2014.12.16'
"""
from math import floor
import random
import numpy


a = [floor(random.random() * 1.05) for i in range(100)]
aa = numpy.array(a).reshape((10, -1))
print(aa)
