#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '模拟吃药'
__author__ = 'pipi'
__mtime__ = '9/26/17'
__email__ = 'pipijob@126.com'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓    ┏┓
            ┏━┛┻━━━━┛┻━┓
            ┃     ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃     ┻    ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━┓┓┏━━┳┓┏━┛
                ┃┫┫  ┃┫┫
                ┗┻┛  ┗┻┛
"""
import random

pills = [[1, j] for j in range(1, 101)]
for i in range(200):
    p = random.choice(pills)
    if p[0] == 1:
        p[0] = 0.5
    else:
        pills.remove(p)
    print('DAY {}: Pill #{}'.format(i, p[1]))
