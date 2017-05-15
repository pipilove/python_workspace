#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pipi'
__mtime__ = '11/2/16'
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
import os

import pandas as pd

DIR = '/home/pipi/files/DATASETS/tianchi/ccf_data_revised'
train_file = 'data_train_tichu.txt'


def dataProcess():
    df = pd.read_csv(os.path.join(DIR, train_file), header=None, sep=',')
    df.loc[df[len(df.columns) - 1] > 0.5, len(df.columns) - 1] = 1
    df.loc[df[len(df.columns) - 1] <= 0.5, len(df.columns) - 1] = 0
    df.to_csv(os.path.join(DIR, 'data_train_tichu_01.txt'), header=False, index=False, float_format='%.7f')


if __name__ == '__main__':
    dataProcess()
