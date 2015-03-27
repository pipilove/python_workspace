#!/usr/bin/env python
# coding=utf-8
"""
__title__ = 'topic model - LDA - AP dataset'
__author__ = 'pi'
__mtime__ = '12/24/2014-024'
# code is far away from bugs with the god animal protecting
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
from collections import defaultdict
from os import path
from gensim import corpora, models
import matplotlib.pyplot as plt
import numpy as np
from scipy import spatial


def build_model(dat, vocab, num_topics=100, alpha=None):
    """
    loading data & training lda model
    """
    if not path.exists(dat) or not path.exists(vocab):
        print('Error: Expected data to be present at ./datasets/ap/')
    # Corpus is just the preloaded list of words
    # dat:term_num term_id:term_freq ... for each line
    # vocab:term for each line(line no is term_id implicit)
    corpus = corpora.BleiCorpus(dat, vocab)  # class 'gensim.corpora.bleicorpus.BleiCorpus
    # #doc_line=2246 #vocab=10473
    # print(corpus.id2word)   #{0: 'i', 1: 'new', 2: 'percent'...} same as vocab:word_id:word
    model = models.LdaModel(corpus, num_topics=num_topics, alpha=alpha, id2word=corpus.id2word)
    # corpus_list = [c for c in corpus]
    # print 'len(corpus_list[0]) = ', len(corpus_list[0]), '\n', corpus_list[0] #<=>ap.dat line 1
    return corpus, model


def get_all_topics_list(model, corpus):
    """
    model训练出来的所有topics
    """
    # list of(doci_topic_id, topic_probability) 2-tuples <=> [(topicid, topicvalue)]
    topics = [model[c] for c in corpus]
    # print(len(topics))  #2246 = #doc_line
    # The returned num_topics <= self.num_topics subset of all topics is arbitrary
    # for topic in model.show_topics(num_topics=-1, num_words= 3, formatted=False):
    # print topic
    # print
    return topics


def lookup_doci_topic(topics, doc_id=0):
    """
    lookup doci对应的topic_id及topic_str
    """
    doc_topics = topics[doc_id]  # topic_id-topic_weight tuple list for doc_line i
    doci_topic_ids = [topic[0] for topic in topics[doc_id]]
    # doci所有topic_id对应的str, a part of model.show_topics()
    doci_topic_strs = [model.show_topic(topicid=t, topn=3) for t in doci_topic_ids]
    # print 'topics[%d]:\n' % doc_id, doc_topics, '\n'
    print(('doc_%d_topic_ids : ' % doc_id, doci_topic_ids))
    # print('doc_%d_topic_str : ' % doc_id)
    # for doci_topic_str in doci_topic_strs: print(doci_topic_str)
    # print


def draw_topicnum_docnum_hist(all_topics):
    """
    draw Nr of all_topics(x) - Nr of documents(y) histogram
    """
    # # 这里只实现1个topics的情况
    # all_topics = all_topics[0]
    # topicno_docnum = defaultdict(int)
    # for doc_id in list(range(len(all_topics))):
    # topicno_docnum[len(all_topics[doc_id])] += 1
    # # print(topicno_docnum)
    # topicno = list(topicno_docnum.keys())
    # docnum = list(topicno_docnum.values())
    # # plt.subplot(211)
    # plt.hist([topicno], list(range(100)), weights=[docnum])
    # plt.title('i write')
    # plt.xlabel('Nr of all_topics')
    # plt.ylabel('Nr of documents')
    # plt.subplot(212)

    flat_topicno = [[len(doci_t) for doci_t in topics] for topics in all_topics]  # doci_t doci对应topic数目
    max_topicno = max([max(f) for f in flat_topicno])  # topicno(x)轴最大值
    # print('max_topicno : ', max_topicno)
    plt.hist(flat_topicno, list(range(max_topicno)))

    """
    对应位置输出相关信息
    """
    plt.title('topicnum_docnum_hist')
    plt.xlabel('Nr of topics')
    plt.ylabel('Nr of documents')
    pos = [(3, 210, 'alpha=default'), (6, 220, 'alpha=1.e-8'), (11, 145, 'alpha=auto'), (52, 115, 'alpha=1.0')]
    for i in list(range(0, len(all_topics))):
        plt.text(pos[i][0], pos[i][1], pos[i][2])

    plt.savefig('./LDA/topicnum_docnum_hist.png')  # 先save再show不然是空白
    plt.show()


def topics2doc_topic_mat(topics, num_topics=100):
    """
    store all these topic counts in NumPy arrays
    """
    doc_topic_mat = np.zeros((len(topics), num_topics))
    for doc_id, doc_topic in enumerate(topics):
        for topic_id, topic_weight in doc_topic:
            doc_topic_mat[doc_id, topic_id] = topic_weight
    # print(doc_topic_mat[0])
    return doc_topic_mat


def compute_pairwise_dist(doc_topic_mat):
    """
    compute all pairwise distances from sparse doc_topic_mat
    """
    # pairwise_dist = numpy.zeros((len(topics), len(topics)))
    # for i, doc_i_vec in enumerate(doc_topic_mat):
    # for j in list(range(i + 1, len(topics))):
    # doc_delta = doc_i_vec - doc_topic_mat[j]
    # pairwise_dist[i][j] = scipy.linalg.norm(doc_delta)
    # pairwise_dist[j][i] = pairwise_dist[i][j]
    # print 'pairwise_dist: \n', pairwise_dist[:5][:5], '\n'
    pairwise_dist = spatial.distance.pdist(doc_topic_mat)  # ndarray : condensed distance matrix
    pairwise_dist = spatial.distance.squareform(pairwise_dist)
    # print 'pairwise_dist: \n', pairwise_dist[:5][:5]
    """
    set the diagonal elements of the distance matrix to a high value
    """
    largest_dist = round(pairwise_dist.max()) + 1
    # largest_dist = pairwise_dist.max() + 1
    for i in list(range(len(topics))):pairwise_dist[i][i] = largest_dist
    # print 'pairwise_dist: \n', pairwise_dist[:5][:5], '\n'
    return pairwise_dist


def look_up_closest(doc_id, pairwise_dist, topn):
    """
    look up the closest docs for doc_id
    """
    return pairwise_dist[doc_id].argsort()[:topn]
    # return pairwise_dist[doc_id].argmin()


"""
find doc_1 closest docs
"""
num_loops = 1
for it in list(range(0, num_loops)):
    dat='./datasets/ap/ap.dat'
    vocab='./datasets/ap/vocab.txt'
    num_topics = 100

    """
    测试alpha为不同值时topicnum_docnum的图形变化
    """
    all_topics = []
    all_alphas = [None, 1.e-8, 'auto', 1.0]
    for alpha in all_alphas[:1]:
        corpus, model = build_model(dat, vocab, num_topics=num_topics,alpha=alpha)
        all_topics.append(get_all_topics_list(model, corpus))
    draw_topicnum_docnum_hist(all_topics)

    topics = all_topics[0]

    # i don't know it means
    # for ti in list(range(1)):
    # words = model.show_topic(topicid=ti, topn=64)  # topic ti 对应的词
    # tf = sum(f for f, w in words)  # 前topn个词的词频和
    # print('\n'.join('{}:{}'.format(w, int(1000. * f / tf)) for f, w in words))

    doc_topic_mat = topics2doc_topic_mat(topics, num_topics)
    pairwise_dist = compute_pairwise_dist(doc_topic_mat)

    doc_id = 1
    lookup_doci_topic(topics, doc_id)
    closest_doc_ids = look_up_closest(doc_id, pairwise_dist, topn=10)
    print(('closest_doc_ids : ', closest_doc_ids, '\n'))
    # for closest_doc_id in closest_doc_ids:
    # lookup_doci_topic(closest_doc_id)
