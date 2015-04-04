from scipy import spatial
from numpy import loadtxt
from numpy import random
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


if __name__ == '__main__':
    generate_random_mat()
