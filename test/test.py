import heapq
from itertools import tee
import numpy
from numpy.ma import argsort, sort, count
from scipy import spatial
from numpy import loadtxt, array, arange, piecewise, random
from scipy.spatial.distance import pdist


def desktop2_read():
    file = open(r'C:\Users\pi\Desktop\2.txt', encoding='utf-8')
    d = loadtxt(file, dtype=bytes)
    print(d)


def diff_dist():
    user_item_mat = random.randint(1, 10, (2, 3))
    print(user_item_mat)
    x = spatial.distance.squareform(pdist(user_item_mat, 'minkowski'))
    print(x)


def generate_random_mat():
    user_item_mat = random.randint(1, 10, (5, 4))
    print(user_item_mat)


def test():
    x = arange(10)
    x = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    piecewise(x, [x < 2, x > 6], [7 - x, x, 2 * x])


import networkx as nx  # 导入networkx包
import matplotlib.pyplot as plt  # 导入绘图包matplotlib（需要安装，方法见第一篇笔记）

if __name__ == '__main__':
    # generate_random_mat()
    sub_items = {1,2}
    list2 = [2,3]
    if sub_items.intersection(set(list2)):
        print('idjf')