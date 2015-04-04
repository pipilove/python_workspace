#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'LML_CH'
__mtime__ = '2015/3/24'
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
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicapp.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()

def main():
    from music.models import Item1
    f = open('data/item_infor.tsv')
    start_time = datetime.datetime.now()
    from_line = 224816
    for line_id, line in enumerate(f):
        if line_id >= from_line:
            if line_id % 10000 == 0:
                print line_id
                print(datetime.datetime.now() - start_time)
            item_id, item_name, art_name = line.split('\t')
            Item1.objects.create(item_id=item_id, item_name=item_name,art_name=art_name)
    f.close()

    # from music.models import Hotmusic,Item1
    # f = open('data/top_n_items.tsv')
    # for line in f.readlines():
    #     idss = line.split()
    #     ids = [int(id) for id in idss]
    #     for id in ids:
    #         item_id = id
    #         item = Item1.objects.get(item_id = id)
    #         item_name = item.item_name
    #         art_name = item.art_name
    #         Hotmusic.objects.create(item_id=item_id, item_name=item_name,art_name=art_name)
    # f.close()


if __name__ == "__main__":
    main()
    print('Done!')

