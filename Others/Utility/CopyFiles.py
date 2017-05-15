#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '$Package_name'
__author__ = '$USER'
__mtime__ = '$DATE'
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
from os import listdir, path
import subprocess

if __name__ == "__main__":
    INPUT_DIR = r'E:\Entertain\Videos'
    OUTPUT_DIR = r'C:\Users\pline\Desktop\out'
    all_output_dir_filenames = listdir(OUTPUT_DIR)
    all_output_dir_filenames.append('desktop.ini')

    for file_name in listdir(INPUT_DIR):
        if file_name not in all_output_dir_filenames:
            filename = path.join(INPUT_DIR, file_name)
            # print(filename)
            subprocess.Popen(["copy", filename, OUTPUT_DIR], shell=True)
