#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '2/16/2015-016'
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
from os import listdir, mkdir, makedirs
import os
from os.path import join, exists


def domain_preprocess(domaFileName, STORE_DOMA_DIR_NAME):
    domaFilePre = domaFileName.split('\\')[-1].split('.')[0]
    domaDir = join(STORE_DOMA_DIR_NAME,domaFilePre)  # 每个domain存在一个目录下，每个domain包含docs, vocab
    # print(domaDir)
    if (not exists(domaDir)):
        # mkdir(domaDir)
        makedirs(domaDir)
    domaFile = open(domaFileName, encoding='utf-8', newline='\r\n', errors='ignore')

    # 建立字典id-word映射
    words = []
    for doc_line in domaFile:
        words += doc_line.strip().split(',')
    # print(len(words))
    vocab = list(set(words))
    vocab.remove('')
    # print(vocab)
    vocabFileName = join(domaDir, str(domaFilePre) + '.vocab')
    vocabFile = open(vocabFileName, 'w', encoding='utf-8')
    for vid, v in enumerate(vocab):
        # vocabFile.write(str(vid) + ':' + v + os.linesep)
        vocabFile.write(str(vid) + ':' + v + '\n')
    vocabFile.close()

    # 重新建立docs，用id表示word
    docFileName = join(domaDir, str(domaFilePre) + '.docs')
    # print(docFileName)
    docFile = open(docFileName, 'w', encoding='utf-8')

    # domaFile.close()
    # domaFile = open(domaFileName, encoding='utf-8', newline='\r\n', errors='ignore')
    domaFile.seek(0)
    for doc_line in domaFile:
        words_line = doc_line.strip().split(',')
        while '' in words_line:
            words_line.remove('')
        # print(words_line)
        wordIds = [vocab.index(word) for word in words_line]
        # print(wordIds)
        for wordId in wordIds:
            docFile.write(str(wordId) + " ")
        docFile.write('\n')
        # docFile.writelines(str(wordIds).replace(',', ' ').replace('[', '').replace(']', '') + '\n')

    domaFile.close()
    docFile.close()


def amc_preprocess(DIR, STORE_DOMA_DIR_NAME):
    domaFileNames = listdir(DIR)
    domaFileNames = [join(DIR, domaFileName) for domaFileName in domaFileNames]
    # print(domaFileNames)
    for domaFileName in domaFileNames:
        domain_preprocess(domaFileName, STORE_DOMA_DIR_NAME)


def docs_coopration(DOMA_DIR, TEST_DOMA_DIR):
    allDocFileNames = listdir(DOMA_DIR)
    domainNames = set([docFileName.split('_')[0] for docFileName in allDocFileNames])
    if (not exists(TEST_DOMA_DIR)):
        makedirs(TEST_DOMA_DIR)

    # print(docFileNames)
    for domainName in domainNames:
        domainFileName = join(TEST_DOMA_DIR, domainName + '.csv')
        # print(domainFileName)
        domainFile = open(domainFileName, 'w', encoding='utf-8', errors='ignore')
        # docFileNames = [join(DOMA_DIR, docFileName) for docFileName in allDocFileNames if domainName in docFileName]
        docFileNames = [join(DOMA_DIR, docFileName) for docFileName in allDocFileNames if
                        docFileName.__contains__(domainName)]
        # print(docFileNames)

        for docFileName in docFileNames:
            # print(docFileName)
            docFile = open(docFileName, encoding='utf-8', newline='\r\n')
            lines = ''
            for line in docFile:
                lines += line.strip() + ','
            lines = lines.strip(",")
            # print(lines)
            domainFile.writelines(lines + '\n')


if __name__ == '__main__':
    # docs_coopration(DOMA_DIR='E:\DESKTOP\数据from张晨\\testData', TEST_DOMA_DIR='E:\DESKTOP\数据from张晨\\testDomains')
    print("test docs coopration complete!!!\n\n")

    # amc_preprocess(TAG_DIR='E:\DESKTOP\数据from张晨\domians',
    # STORE_DOMA_DIR_NAME='E:\mine\javaworkspace\AMC_master\Data\Input\\15000Domains\\15000Domains')
    print("15000Domains preprocess complete!!!\n\n")

    # amc_preprocess(TAG_DIR='E:\DESKTOP\数据from张晨\\testDomains',
    #                STORE_DOMA_DIR_NAME='E:\mine\javaworkspace\AMC_master\Data\Input\\1600tests\\1600tests')
    print("1600tests preprocess complete!!!\n\n")

    amc_preprocess(DIR=r'E:\mine\javaworkspace\AMC_master\Data\Input\nokia_data_明兰', STORE_DOMA_DIR_NAME=r'E:\mine\javaworkspace\AMC_master\Data\Input\nokia_data_明兰\foramc')
    print("nokia data preprocess complete!!!\n\n")

