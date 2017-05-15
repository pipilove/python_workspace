#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'catenate files into 1 file '
__author__ = 'pi'
__mtime__ = '1/4/2015-004'
# I love animals. They taste delicious.
"""
from Colors import REDL, DEFAULT, GREENL
import os

DIR = r'.\datasets\dataset-379-20news-18828_NENPP\train\sci.med'
filenames = os.listdir(DIR)
print(GREENL, '#files : ', len(filenames), DEFAULT)

cat_file_name = DIR + '.cat_file.txt'
print(REDL, cat_file_name, DEFAULT)
cat_file = open(cat_file_name, 'w')

for filename in filenames:
    filename = os.path.join(DIR, filename)
    # print(filename)
    file = open(filename, errors='ignore')  # ignore encoding errors
    for eachline in file:
        cat_file.writelines(eachline)
    cat_file.write('\n')
    file.close()

cat_file.close()
