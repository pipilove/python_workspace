#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '3/5/2015-005'
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


def twords_process(input_filename, output_filename):
    '''
    对齐格式化输出到new文件中
    :param input_file_name:
    :param output_file_name:
    :return:
    '''
    twordFile = open(input_filename)
    new_twordFile = open(output_filename, 'w')
    for line in twordFile:
        for word in line.strip().split('\t'):
            # new_twordFile.write("%-15s" % word)
            new_twordFile.write(word.ljust(15))
        new_twordFile.write('\n')
    twordFile.close()
    new_twordFile.close()


def sorted_topic_word_dist(input_filename, output_filename):
    '''
    将每个主题下的词分布降序排序，存入output_filename
    :param input_filename:
    :param output_filename:
    :return:
    '''
    word_dist_file = open(input_filename)
    sorted_word_dist_file = open(output_filename, 'w')
    for line in word_dist_file:
        word_dist_list = line.strip().split()
        word_dist_list = sorted([float(word_dist) for word_dist in word_dist_list], reverse=True)
        word_dist_list = [str(f) for f in word_dist_list]
        # print(word_dist_list)
        word_dist_str = ' '.join(word_dist_list) + '\n'
        # print(word_dist_str)
        sorted_word_dist_file.write(word_dist_str)
    word_dist_file.close()
    sorted_word_dist_file.close()


if __name__ == '__main__':
    input_filename = r'E:\mine\javaworkspace\AMC_master\Data\Output\AMC\100Reviews\DomainModels\foramc\foramc.twords'
    output_filename = r'E:\mine\javaworkspace\AMC_master\Data\Output\AMC\100Reviews\DomainModels\foramc\foramc_1.twords'
    # twords_process(input_filename, output_filename)

    twdist_filename = r'E:\mine\javaworkspace\AMC_master\Data\Output\AMC\100Reviews\DomainModels\foramc\foramc.twdist'
    sorted_twdist_filename = r'E:\mine\javaworkspace\AMC_master\Data\Output\AMC\100Reviews\DomainModels\foramc\foramc.sortedtwdist'
    # sorted_topic_word_dist(twdist_filename, sorted_twdist_filename)
