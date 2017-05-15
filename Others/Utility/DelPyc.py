#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '7/29/2015-029'
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
import fnmatch
from os import walk, path, remove
import sys

# 默认删除路径
DEFAULT_DEL_DIRS = ['CorePyPro', 'MachineLearning', 'PyQt', 'Recsys', 'TopicModel', 'Utility', 'Website', 'LanguageAnalysis']
# 默认删除文件后缀名
EXT = 'pyc'


def del_pyc(DEL_DIR, EXT):
    '''
    删除某个路径DEL_DIR下的所有.EXT文件
    '''
    if not path.exists(DEL_DIR):
        print('error: DEL_DIR not found!!!')
        exit()

    for filepath, _, filename_list in walk(DEL_DIR):
        for filename in filename_list:
            if fnmatch.fnmatch(filename, '*.' + EXT):  # unix shell风格匹配方式
                # if filename.endswith('.pyc'):
                print(filename)
                remove(path.join(filepath, filename))


if __name__ == '__main__':
    # console
    if len(sys.argv) >= 3:
        EXT = sys.argv[2]
        DEL_DIR = sys.argv[1]
    elif len(sys.argv) >= 2:
        DEL_DIR = sys.argv[1]
    else:
        DEL_DIR = [path.join(r'E:\mine\python_workspace', subdir) for subdir in DEFAULT_DEL_DIRS]

    print('DEL_DIR: ', DEL_DIR, '\ndelete file extension: ', EXT)
    print('deleted files:\n')

    if type(DEL_DIR) == list:
        for del_dir in DEL_DIR:
            del_pyc(del_dir, EXT)
    else:
        del_pyc(DEL_DIR, EXT)
