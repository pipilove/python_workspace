#!/usr/bin/env python
# coding=utf-8
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '12/24/2014-024'
# code is far away from bugs with the god animal protecting
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ━      ┃
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
from gensim import corpora

"""
Corpora and Vector Spaces
通过documents抽取一个词袋（bag-of-words)，将文档的token映射为id
"""
documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

"""
#对英文文本预处理的一种方法：去停用词，tokenize，stemming，过滤低频词
#use StemmedCountVectorizer to get stemmed without stop words corpus
Vectorizer = StemmedCountVectorizer
# Vectorizer = CountVectorizer
vectorizer = Vectorizer(decode_error='ignore', stop_words='english',min_df=1, max_df=0.9)
vectorizer.fit_transform(documents)
texts = vectorizer.get_feature_names()
# print(texts)
"""

# remove common words and tokenize
stop_list = 'for a of the and to in'.split()
# texts = [doc_line.lower().split() for doc_line in documents]
texts = [[word for word in doc.lower().split() if word not in stop_list] for doc in documents]
print((texts, '\n'))

# remove words that appear only once in all docs
all_words = sum(texts, [])
token_once = [word for word in set(all_words) if all_words.count(word) == 1]
texts = [[word for word in text if word not in token_once] for text in texts]
print((texts, '\n'))

dict = corpora.Dictionary(texts)  # 自建词典
# print dict, dict.token2id
# 通过dict将用字符串表示的文档转换为用id表示的文档向量
corpus = [dict.doc2bow(text) for text in texts]
print(corpus)
