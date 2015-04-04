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
from os.path import join, exists


def domain_preprocess(DOMA_DIR_NAME, domaFileName):
    domaDir = join(DOMA_DIR_NAME,
                   domaFileName.split('\\')[-1].split('.')[0])  # 每个domain存在一个目录下，domain中每篇文档又存在各自目录下  # print(domaDir)
    if (not exists(domaDir)):
        # mkdir(domaDir)
        makedirs(domaDir)
    domaFile = open(domaFileName, encoding='utf-8', newline='\r\n', errors='ignore')
    for i, doc_line in enumerate(domaFile):
        docDir = join(domaDir, str(i))
        if (not exists(docDir)):
            makedirs(docDir)

        words = doc_line.strip().split(',')
        # print(words)

        # 建立字典id-word映射
        vocab = list(set(words))
        # print(vocab)
        vocabFileName = join(docDir, str(i) + '.vocab')
        vocabFile = open(vocabFileName, 'w', encoding='utf-8')
        for vid, v in enumerate(vocab):
            vocabFile.write(str(vid) + ':' + v + '\n')
        vocabFile.close()

        # 重新建立docs，用id表示word
        wordIds = [vocab.index(word) for word in words]
        # print(wordIds)
        docFileName = join(docDir, str(i) + '.docs')
        docFile = open(docFileName, 'w')
        docFile.writelines(str(wordIds).replace(',', ' ').replace('[', '').replace(']', ''))
        docFile.close()


def amc_preprocess(DIR, DOMA_DIR_NAME):
    domaFileNames = listdir(DIR)
    domaFileNames = [join(DIR, domaFileName) for domaFileName in domaFileNames]
    # print(domaFileNames)
    for domaFileName in domaFileNames:
        domain_preprocess(DOMA_DIR_NAME, domaFileName)


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
            docFile = open(docFileName, encoding='utf-8', newline='\r\n')
            lines = ''
            for line in docFile:
                lines += line.strip() + ','
            lines = lines.strip(",")
            # print(lines)
            domainFile.writelines(lines + '\n')


if __name__ == '__main__':
    docs_coopration(DOMA_DIR='E:\DESKTOP\数据from张晨\\testData', TEST_DOMA_DIR='E:\DESKTOP\数据from张晨\\testDomains')
    print("test docs coopration complete!!!\n\n")

    amc_preprocess(DIR='E:\DESKTOP\数据from张晨\domians',
                   DOMA_DIR_NAME='E:\mine\javaworkspace\AMC_master\Data\Input\\15000Domains')
    print("15000Domains preprocess complete!!!\n\n")

    amc_preprocess(DIR='E:\DESKTOP\数据from张晨\\testDomains',
                   DOMA_DIR_NAME='E:\mine\javaworkspace\AMC_master\Data\Input\\1600tests')
    print("1600tests preprocess complete!!!\n\n")
