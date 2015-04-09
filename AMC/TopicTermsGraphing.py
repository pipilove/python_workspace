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
import linecache
from os import makedirs
from os.path import exists, dirname

import networkx as nx
import matplotlib.pyplot as plt
from numpy import ndarray, zeros, argsort


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


    # topic_array = loadtxt(twords_filename, dtype='S', delimiter='\t', skiprows=1).transpose()
    # print(topic_array)
    # topic_list = topic_array.tolist()
    # print(type(topic_list[0][0]), topic_list[0][0])

    twords_file.close()
    return topic_list


def get_most_overlap_topics(tword_list):
    '''
    从tword_list中找到word覆盖最多的一些topic
    :param tword_list:
    :return:
    '''
    topic_num = len(tword_list)
    # print(set(tword_list[0]), set(tword_list[10]))
    overlap_topics_cnt = zeros([topic_num, topic_num])
    for topic_id in range(topic_num):
        for topic_id_j in range(topic_id + 1, topic_num):
            # print((set(tword_list[topic_id]).intersection(set(tword_list[topic_id_j]))))
            overlap_topics_cnt[topic_id, topic_id_j] = len(
                set(tword_list[topic_id]).intersection(set(tword_list[topic_id_j])))
            overlap_topics_cnt[topic_id_j, topic_id] = len(
                set(tword_list[topic_id]).intersection(set(tword_list[topic_id_j])))
            # print(topic_id, topic_id_j, overlap_topics_cnt[topic_id, topic_id_j])
    top_overlap = overlap_topics_cnt.argmax(axis=1)
    top_overlap_cnt = [overlap_topics_cnt[line_id, i] for line_id, i in enumerate(top_overlap)]
    print([str(i) + ':' + str(j) for i, j in zip(top_overlap, top_overlap_cnt)])
    print(argsort(-overlap_topics_cnt[0]))
    return top_overlap


def graph_terms_to_topics(tword_list, topic_ids=None, savefig_filename=None, show_flag=True):
    # create a new graph and size it
    G = nx.Graph()
    plt.figure(figsize=(10, 10))

    # generate the edges
    if topic_ids is None:
        topic_ids = range(0, tword_list.shape[0])
    for i in topic_ids:
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
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=1.0, width=0.2, edge_color='g')

    plt.axis('off')
    if savefig_filename is not None:
        if not exists(dirname(savefig_filename)):
            makedirs(dirname(savefig_filename))
        plt.savefig(savefig_filename, dpi=1000, fmt='png')
    if show_flag:
        plt.show()


def get_must_links(must_links_filename):
    '''
    从文件中读取must_links对，
    :param must_links_filename:
    :return:
    '''
    lines = linecache.getlines(must_links_filename)
    must_links_list = list()
    for line in lines:
        must_links_list.append(line.strip().split())
    # print(must_links_list)
    return must_links_list


def graph_must_links(must_links_list):
    '''

    :param must_links_list:
    :return:
    '''
    # create a new graph and size it
    G = nx.Graph()
    plt.figure(figsize=(15, 10))

    # generate the edges
    for must1, must2 in must_links_list:
        G.add_edge(must1, must2)

    # Compute the clustering coefficient for nodes
    # print(nx.clustering(G, nodes='phone'))

    pos = nx.spring_layout(G)  # positions for all nodes

    # we'll plot topic labels and terms labels separately to have different colours
    nx.draw_networkx_labels(G, pos)  # , font_color='r')

    # plot edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), alpha=0.4, edge_color='r')  # alpha:The node transparency

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    # twords_filename = r'E:\mine\java_workspace\AMC_master\Data\Output\AMC\100Reviews\DomainModels\foramc\t100w10.twords'
    twords_filename = r'E:\mine\java_workspace\AMC_master\Data\pre_output\Output0\AMC\100Reviews\DomainModels\CellPhone\CellPhone.twords'
    tword_list = get_topic_list(twords_filename)

    savefig_filename = './graph_terms_to_topics_png/graph_terms_to_topics0,1,4,9,10,14'
    graph_terms_to_topics(tword_list, topic_ids=[0, 1, 4, 9, 10, 14], savefig_filename=savefig_filename)

    top_overlap = get_most_overlap_topics(tword_list)
    must_links_list = zip(range(len(top_overlap)), top_overlap)

    # must_links_filename = r'E:\mine\java_workspace\AMC_master\Data\Output\AMC\100Reviews\DomainModels\foramc\foramc.knowl_mustlinks'
    must_links_filename = r'E:\mine\java_workspace\AMC_master\Data\pre_output\Output0\AMC\100Reviews\DomainModels\CellPhone\CellPhone.knowl_mustlinks'
    # must_links_list = get_must_links(must_links_filename)
    graph_must_links(must_links_list)
