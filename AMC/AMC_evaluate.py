#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '3/10/2015-010'
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
from genericpath import exists
from os import listdir
from os.path import join
from Tools.Scripts.ftpmirror import makedir
from math import log
from numpy import array, matrix, zeros, dot, savetxt, ndarray, loadtxt
import numpy


def get_word_id(vocab_filename):
    '''
    获取每个domain中word_id的对应词典
    :param domain_filename:
    :return:
    '''
    domain_word_id_file = open(vocab_filename)
    word_id_dict = dict()
    for line in domain_word_id_file:
        word_id_dict[line.strip().split(':')[1]] = int(line.strip().split(':')[0])
    return word_id_dict


def write_word_occur_mat(AMC_TEST_INPUT_DIT, WORD_COOCCUR_DIR):
    '''
    从测试集中找出word共现矩阵并存档
    :param AMC_TEST_INPUT_DIT:
    :return:
    '''
    domain_filenames = listdir(AMC_TEST_INPUT_DIT)
    # print(domain_filenames)
    domain_filedirs = [join(AMC_TEST_INPUT_DIT, domain_filename) for domain_filename in domain_filenames]

    for domain_filedir, domain_filename in zip(domain_filedirs, domain_filenames):
        word_id = get_word_id(join(domain_filedir, domain_filename) + '.vocab')
        word_num = len(word_id)
        # print('word_num : ', word_num)  #first doc 103

        # 获取每个domain中doc_word的对应矩阵
        # print(join(domain_filedir, domain_filename + '.docs'))
        domain_file = open(join(domain_filedir, domain_filename + '.docs'))
        doc_num = len(domain_file.readlines())
        domain_file.seek(0)
        doc_word_mat = zeros([doc_num, word_num], dtype='i')  # int32
        for doc_id, line in enumerate(domain_file):
            # print(doc_id, domain_filenames[doc_id], line.strip().split(' '))
            for word in line.strip().split(' '):
                doc_word_mat[doc_id][int(word)] = 1
                # doc_word_mat[doc_id][int(word)] += 1
                # print(doc_id, int(word), doc_word_mat[doc_id][int(word)])
        domain_file.close()
        # print(doc_word_mat)

        # 将doc_word矩阵存入文件
        if not exists('./doc_word_mat'):
            makedir('./doc_word_mat')
        doc_word_mat_file = open('./doc_word_mat/' + domain_filename + '_doc_word_mat_file.txt', 'wb')
        savetxt(doc_word_mat_file, doc_word_mat, fmt='%d')
        doc_word_mat_file.close()

        # 计算两个词之间的共现并写入文件
        word_cooccur = dot(doc_word_mat.transpose(), doc_word_mat)
        if not exists('./word_cooccur'):
            makedir('./word_cooccur')
        word_cooccur_file = open(WORD_COOCCUR_DIR + domain_filename + '_word_cooccur_file.txt', 'wb')
        savetxt(word_cooccur_file, word_cooccur, fmt='%d')
        word_cooccur_file.close()


def load_word_occur_mat(word_cooccur_filename):
    '''
    将文件中的word_word共现矩阵读入word_cooccurs矩阵中
    :param AMC_TEST_INPUT_DIT:
    :return:
    '''
    word_cooccur_file = open(word_cooccur_filename, 'rb')
    word_cooccur = loadtxt(word_cooccur_file, dtype='i')
    word_cooccur_file.close()
    # print(word_cooccur)
    return word_cooccur


def get_topic_list(twords_filename):
    '''
    将tword.txt文件的内容读入topic_list列表中
    :param twords_filename:
    :return:
    '''
    twords_file = open(twords_filename, 'r', encoding='utf-8')

    word_num = len(twords_file.readlines()) - 1
    twords_file.seek(0)
    topic_num = twords_file.readline().count('Topic')  # twords_file已经向下移动了一行！

    topic_list = ndarray([topic_num, word_num], dtype=object)
    for word_id, line in enumerate(twords_file):
        for topic_id, word in enumerate(line.strip().split()):
            topic_list[topic_id][word_id] = word
    print(topic_list)


    # topic_array = loadtxt(twords_file, dtype='S', delimiter='\t', skiprows=1).transpose()
    # print(topic_array)
    # topic_list = topic_array.tolist()
    # print(type(topic_list[0][0]), topic_list[0][0])

    twords_file.close()
    return topic_list


def transform_topic_list(topic_list, vocab_filename):
    '''
    将topic_list中的topic_word转换成topic_wordid存入topic_wid_list
    :param topic_list:
    :param vocab_filename:
    :return:
    '''
    word_id_dict = get_word_id(vocab_filename)
    topic_wid_list = [[word_id_dict[word] for word in topic] for topic in topic_list]
    # print(topic_wid_list)
    return topic_wid_list


def cal_domain_topic_coherence(twords_filename, vocab_filename, word_cooccur_filename):
    '''
    计算某个domain的topic coherence
    :param twords_filename:
    :return:
    '''
    word_cooccurs = load_word_occur_mat(word_cooccur_filename)

    topic_list = get_topic_list(twords_filename)
    topic_wid_list = transform_topic_list(topic_list, vocab_filename)
    # print(topic_wid_list)

    word_id_dict = get_word_id(vocab_filename)

    topic_coher = 0
    for topic in topic_wid_list:
        '''  计算某个topic下词之间的coherence  '''
        # topic_coher = 0
        word_num = len(topic)
        for i in range(1, word_num):
            for j in range(0, i):
                # print(list(word_id_dict.keys())[list(word_id_dict.values()).index(topic[i])], list(word_id_dict.keys())[list(word_id_dict.values()).index(topic[j])])
                if ( word_cooccurs[topic[j], topic[j]] ) < 0:
                    print(word_cooccur_filename)
                    print(topic[j], topic[j], word_cooccurs[topic[j], topic[j]])
                topic_coher += log((word_cooccurs[topic[i], topic[j]] + 1) / word_cooccurs[topic[j], topic[j]])
                # print(topic_coher)
    topic_num = len(topic_wid_list)
    topic_coher /= topic_num
    # print(topic_coher)
    return topic_coher


def cal_domains_topic_coherence(AMC_OUTPUT_DIR, WORD_COOCCUR_DIR):
    domain_names = listdir(AMC_OUTPUT_DIR)
    domain_filedirs = [join(AMC_OUTPUT_DIR, domain_name) for domain_name in domain_names]
    topic_coher = 0
    for domain_name, domain_filedir in zip(domain_names, domain_filedirs):
        twords_filename = join(domain_filedir, domain_name) + '.twords'
        vocab_filename = join(domain_filedir, domain_name) + '.vocab'
        word_cooccur_filename = WORD_COOCCUR_DIR + domain_name + '_word_cooccur_file.txt'
        topic_coher = cal_domain_topic_coherence(twords_filename, vocab_filename, word_cooccur_filename)
        print(topic_coher)
        # topic_coher += cal_domain_topic_coherence(twords_filename, vocab_filename, word_cooccur_filename)
        # print(topic_coher / len(domain_names))


if __name__ == '__main__':
    AMC_TEST_INPUT_DIT = r'E:\mine\javaworkspace\AMC_master\Data\Input\100Reviews\Electronics'
    WORD_COOCCUR_DIR = './word_cooccur/'
    # write_word_occur_mat(AMC_TEST_INPUT_DIT, WORD_COOCCUR_DIR)

    AMC_OUTPUT_DIR = r'E:\mine\javaworkspace\AMC_master\Data\pre_output\Output0\AMC\100Reviews\DomainModels'
    cal_domains_topic_coherence(AMC_OUTPUT_DIR, WORD_COOCCUR_DIR)
