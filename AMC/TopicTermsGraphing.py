#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '4/3/2015-003'
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
import networkx as nx
import matplotlib.pyplot as plt
# %matplotlib inline
from numpy import ndarray


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
    # print(topic_list)


    # topic_array = loadtxt(twords_file, dtype='S', delimiter='\t', skiprows=1).transpose()
    # print(topic_array)
    # topic_list = topic_array.tolist()
    # print(type(topic_list[0][0]), topic_list[0][0])

    twords_file.close()
    return topic_list


def graph_terms_to_topics(tword_list):
    # create a new graph and size it
    G = nx.Graph()
    plt.figure(figsize=(10, 10))

    # generate the edges
    num_topics = tword_list.shape[0]
    for i in range(0, num_topics):
        topicLabel = "topic " + str(i)
        for term in tword_list[i]:
            G.add_edge(topicLabel, term)

    pos = nx.spring_layout(G)  # positions for all nodes

    # we'll plot topic labels and terms labels separately to have different colours
    g = G.subgraph([topic for topic, _ in pos.items() if "topic " in topic])
    nx.draw_networkx_labels(g, pos, font_color='r')
    g = G.subgraph([term for term, _ in pos.items() if "topic " not in term])
    nx.draw_networkx_labels(g, pos)

    # plot edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.1)

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    twords_filename = r'E:\mine\javaworkspace\AMC_master\Data\Output\AMC\100Reviews\DomainModels\foramc\t100w10.twords'
    twords_filename = r'E:\mine\javaworkspace\AMC_master\Data\pre_output\Output0\AMC\100Reviews\DomainModels\CellPhone\CellPhone.twords'
tword_list = get_topic_list(twords_filename)
graph_terms_to_topics(tword_list)
