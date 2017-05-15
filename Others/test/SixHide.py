#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pika'
__mtime__ = '16-3-21'
__email__ = 'pipisorry@126.com'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import os
import sh
import uuid

DIR = r"/media/pika/softwares/New folder/New folder"
EX_FILENAME = r'/media/pika/softwares/New folder/exchange_names'
DIR2 = r"/media/pika/softwares/New folder/原创800"
EX_FILENAME2 = r'/media/pika/softwares/New folder/exchange_names2'
SATE_FILENAME = r'/media/pika/softwares/New folder/state'


def ChangeName(DIR, EX_FILENAME):
    filenames = [os.path.join(DIR, filename) for filename in os.listdir(DIR)]
    new_filenames = [os.path.join(DIR, str(uuid.uuid1())) for _ in range(len(filenames))]
    with open(EX_FILENAME, 'w') as write_file:
        for filename, new_filename in zip(filenames, new_filenames):
            write_file.write(new_filename + '\t' + filename + '\n')
            # print("{} => {}".format(filename, new_filename))
            sh.mv(filename, new_filename)


def ChangeBackName(EX_FILENAME):
    with open(EX_FILENAME) as file:
        all_filenames = [line.strip().split('\t') for line in file.readlines()]
        for [new_filename, filename] in all_filenames:
            # print("{} => {}".format(new_filename, filename))
            sh.mv(new_filename, filename)


with open(SATE_FILENAME, 'r') as file:
    try:
        state = int(file.readline().strip())  # 空则表示没改过
    except:
        state = 0
    # print(state)

    if not state:
        print("change names\n")
        ChangeName(DIR, EX_FILENAME)
        ChangeName(DIR2, EX_FILENAME2)
        print("change names finished\n")
        state = 1
    else:
        print("change back names\n")
        ChangeBackName(EX_FILENAME)
        ChangeBackName(EX_FILENAME2)
        print("change back names finished\n")
        state = 0
with open(SATE_FILENAME, 'w') as file:
    file.write(str(state))
