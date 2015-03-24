#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '3/20/2015-020'
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
import datetime

from scipy import spatial
from numpy import argsort, array, zeros, savetxt, loadtxt
from numpy.ma import dot
from RecSys.MusicRec.Data_preprocess import get_convert_no_small_dataset_max_item_id, convert_no_small_filename

from RecSys.MusicRec.Models import User, Item


def get_info_class_list(filename):
    '''
    将用户和歌曲信息读入相应的class中，所有class存在users_list、items_list中
    :param filename:
    :return:
    '''
    file = open(filename, encoding='utf-8')
    users_list = list()
    items_list = list()
    user_ids = list()
    item_ids = list()

    start_time = datetime.datetime.now()
    for line_id, line in enumerate(file):
        if line_id % 100000 == 0:
            print('******** %d ********' % line_id)
            print(datetime.datetime.now() - start_time)
        user_id, timestamp, art_id, art_name, item_id, item_name = array(line.strip().split('\t'))
        if item_id not in item_ids:
            item_ids.append(item_id)
            item_class = Item(item_id=item_id, item_name=item_name, art_id=art_id)
            items_list.append(item_class)
        if user_id not in user_ids:
            user_ids.append(user_id)
            user_class = User(user_id=user_id)
            user_class.add_item(item_class, timestamp, preference=1)
            users_list.append(user_class)
        else:
            users_list[user_ids.index(user_id)].add_item(item_class, timestamp, preference=1)  # 已存在就不会添加
    file.close()
    # print(users_list, len(users_list), items_list, len(items_list))
    return users_list, items_list


def write_info_class_list(users_list, items_list, users_output_filename, items_output_filename):
    '''
    将user和item的class list写入文件
    :param users_list:
    :param items_list:
    :param users_output_filename:
    :param items_output_filename:
    :return:
    '''
    users_output_file = open(users_output_filename, 'w')
    for user_class in users_list:
        users_output_file.write("%s %s" % (user_class.user_id))
    users_output_file.close()


def get_user_item_mat0(users_list, items_list):
    '''
    构建user_item_mat
    :param users_list:
    :param items_list:
    :return:
    '''
    start_time = datetime.datetime.now()
    user_item_mat = zeros([len(users_list), len(items_list)])  # print(user_item_mat.shape)

    for user_class in users_list:
        for item_id in user_class.items_dict.keys():
            user_item_mat[user_class.user_id, item_id] = user_class.items_dict[item_id][1]  # 时间相关调整到后期再考虑

    print(datetime.datetime.now() - start_time)
    return user_item_mat


def get_raw_user_item_mat(max_user_id, max_item_id, input_filename):
    '''
    构建初始user_item_mat
    :param input_filename:
    :return:
    '''
    print("starting get raw_user_item_mat ... ")
    start_time = datetime.datetime.now()
    raw_user_item_mat = zeros([max_user_id + 1, max_item_id + 1])  # print(user_item_mat.shape)

    input_file = open(input_filename)
    for line in input_file:
        user_id, timestamp, art_id, art_name, item_id, item_name = array(line.strip().split('\t'))
        raw_user_item_mat[int(user_id)][int(item_id)] += 1
    input_file.close()
    print("raw_user_item_mat gotten ,lasting time:", datetime.datetime.now() - start_time)
    return raw_user_item_mat


def get_user_item_mat(raw_user_item_mat_filename):
    '''
    从初始user_item_mat构建user_item_mat
    :param raw_user_item_mat:
    :return:
    '''
    pass


def cal_similar(user_item_mat, new_user_flag=False):
    '''
    计算相关度
    :return:
    '''
    # 构建item_item相似度矩阵
    item_item_mat = spatial.distance.squareform(spatial.distance.pdist(user_item_mat.transpose(), metric='cosin'))

    # 构建user_user相似度矩阵
    if new_user_flag:
        user_user_mat = None  # 之后加入新用户重新计算
    else:
        user_user_mat = spatial.distance.squareform(spatial.distance.pdist(user_item_mat, metric='cosin'))

    return item_item_mat, user_user_mat


def recommend_one(user_item_mat):
    '''
    对某个用户推荐歌曲
    :param user_item_mat:
    :return:
    '''


def recommend_all(user_item_mat):
    item_item_mat, user_user_mat = cal_similar(user_item_mat)


def recommend_new(user_class, user_item_mat):
    '''
    对用户user_class推荐item
    :param item_item_mat:
    :param user_user_mat:
    :return:
'''
    user_item_vec = zeros([1, len(user_item_mat[0])])
    for item_id in user_class.items_dict.keys():
        user_item_vec[item_id] = 1
    user_item_mat[len(user_item_mat)] = user_item_vec
    users_similar = array([dot(user_item_vec, old_user_item_vec) for old_user_item_vec in user_item_mat])
    sorted_users_similar_indexs = argsort(-users_similar)
    print(sorted_users_similar_indexs)
    for sorted_users_similar_index in sorted_users_similar_indexs:
        old_user_item_vector = user_item_mat[sorted_users_similar_index]
        rec_item_list = not user_item_vec and old_user_item_vector
        print(rec_item_list)

    item_item_mat = cal_similar(user_item_mat, new_user_flag=True)


if __name__ == '__main__':
    train_filename = r'E:\machine_learning\datasets\lastfm-dataset-1K\train_data.tsv'
    user_item_mat_filename = r'E:\machine_learning\datasets\lastfm-dataset-1K\user_item_mat.npy'
    raw_user_item_mat_filename = r'E:\machine_learning\datasets\lastfm-dataset-1K\raw_user_item_mat.npy'

    max_item_id = get_convert_no_small_dataset_max_item_id(convert_no_small_filename)
    raw_user_item_mat = get_raw_user_item_mat(max_user_id=1000, max_item_id=max_item_id, input_filename=train_filename)
    savetxt(raw_user_item_mat_filename, raw_user_item_mat, fmt="%d")

