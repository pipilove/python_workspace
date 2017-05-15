#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '动态规划：编辑距离算法'
__author__ = 'pipi'
__mtime__ = '16-9-18'
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
import sys
import io


class arithmetic():
    def __init__(self):
        pass

    ''''' 【编辑距离算法】 【levenshtein distance】 【字符串相似度算法】 '''

    def levenshtein(self, first, second):
        if len(first) > len(second):
            first, second = second, first
        if len(first) == 0:
            return len(second)
        if len(second) == 0:
            return len(first)
        first_length = len(first) + 1
        second_length = len(second) + 1
        distance_matrix = [list(range(second_length)) for x in list(range(first_length))]
        # print distance_matrix
        for i in list(range(1, first_length)):
            for j in list(range(1, second_length)):
                deletion = distance_matrix[i - 1][j] + 1
                insertion = distance_matrix[i][j - 1] + 1
                substitution = distance_matrix[i - 1][j - 1]
                if first[i - 1] != second[j - 1]:
                    substitution += 1
                distance_matrix[i][j] = min(insertion, deletion, substitution)
        # print(distance_matrix)
        return distance_matrix[first_length - 1][second_length - 1]


if __name__ == "__main__":
    try:
        sys.stdin = io.StringIO("geek gesek")
        word1, word2 = input().split()
    except:
        sys.stdin = io.StringIO(u"geek gesek")
        word1, word2 = raw_input().split()
    arith = arithmetic()
    print(arith.levenshtein(word1, word2))
