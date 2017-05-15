#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '天池优惠券预测数据分析'
__author__ = 'pipi'
__mtime__ = '16-10-24'
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
import subprocess


def table():
    dir = '/home/pipi/files/DATASETS/tianchi/ccf_data_revised'
    # subprocess.run("cat ccf_offline_stage1_train.csv | cut -d ',' -f 2 | sort -un > /tmp/12.txt", shell=True, cwd=dir)
    # subprocess.run("cat ccf_online_stage1_train.csv | cut -d ',' -f 2 | sort -un > /tmp/22.txt", shell=True, cwd=dir)
    # subprocess.run("cat ccf_offline_stage1_test_revised.csv | cut -d ',' -f 2 | sort -un > /tmp/32.txt", shell=True,
    #                cwd=dir)

    with open('/tmp/12.txt') as f1, open('/tmp/22.txt') as f2, open('/tmp/32.txt') as f3:
        a = [l.strip() for l in f1.readlines()]
        b = [l.strip() for l in f2.readlines()]
        c = [l.strip() for l in f3.readlines()]
        print(a[-100:-1], '\n', b[0: 100], '\n', c[0:10])
        print(len(set(b).intersection(set(c))))


def t2():
    dir = '/home/pipi/files/DATASETS/tianchi/ccf_data_revised'
    filename = 'data_train_tichu_01.txt'
    # filename = 'submission.csv'

    subprocess.run("cat " + filename + " | cut -d ',' -f 9 | sort| uniq -c | (head && tail)",
                   shell=True, cwd=dir)
    subprocess.run("cat " + filename + " | wc -l", shell=True, cwd=dir)
    # subprocess.run("head " + filename, shell=True, cwd=dir)


if __name__ == '__main__':
    # table()
    t2()
