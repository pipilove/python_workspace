#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '回归模型预测优惠券使用概率'
__author__ = 'pipi'
__mtime__ = '10/30/16'
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
import pwd
from sklearn import linear_model, preprocessing, svm
import numpy as np
import os
import pandas as pd

if pwd.getpwuid(os.geteuid()).pw_name == 'piting':
    DIR = '/media/items/pipi/datasets/tianchi/ccf_data_revised'
    # mkdir -p /media/items/pipi/datasets/tianchi/ccf_data_revised/
    # scp -r ~/files/DATASETS/tianchi/ccf_data_revised/* piting@192.168.0.172:/media/items/pipi/datasets/tianchi/ccf_data_revised/
elif pwd.getpwuid(os.geteuid()).pw_name == 'pipi':
    DIR = '/home/pipi/files/DATASETS/tianchi/ccf_data_revised'
else:
    print("please set like wd.getpwuid(os.geteuid()).pw_name == 'pipi'")
    exit()
trains = ['data_test.txt', 'data_test1.txt', 'data_test2.txt', 'data_test3.txt', 'data_test4.txt',
          'data_train_tichu.txt']
tests = ['data_test2.txt', 'data_test6.txt']

data_scale_flag = 0  # 使用scaled的数据
data_rescale_flag = 0  # 对数据重新scaling
reg_flag = 0  # 使用regression，否则classification
reg_id = 2  # 回归模型编号
cla_id = 0  # 分类模型编号
train_file = trains[5]  # 用于训练的特征
test_file = tests[1]  # 用于预测的特征

train_file1 = 'data_train_scaled.txt'
test_file1 = 'data_test_scaled.txt'
result_file0 = 'ccf_offline_stage1_test_revised.csv'
result_file = 'submission.csv'


def preprocess():
    if data_scale_flag:
        # items scaler
        if not os.path.exists(os.path.join(DIR, train_file1)) or not os.path.exists(
                os.path.join(DIR, test_file1)) or data_rescale_flag:
            xy = np.loadtxt(os.path.join(DIR, train_file), delimiter=',', dtype=float)
            x, y = xy[:, 0:-1], xy[:, -1]
            scaler = preprocessing.StandardScaler().fit(x)
            xy = np.hstack([scaler.transform(x), y.reshape(-1, 1)])
            np.savetxt(os.path.join(DIR, train_file1), xy, fmt='%.7f')

            x_test = np.loadtxt(os.path.join(DIR, test_file), delimiter=',', dtype=float)
            x_test = scaler.transform(x_test)
            np.savetxt(os.path.join(DIR, test_file1), x_test, fmt='%.7f')
        else:
            print('items loading...')
            xy = np.loadtxt(os.path.join(DIR, train_file1), dtype=float)
            x_test = np.loadtxt(os.path.join(DIR, test_file1), dtype=float)
    else:
        print('items loading...')
        xy = np.loadtxt(os.path.join(DIR, train_file), delimiter=',', dtype=float)
        x_test = np.loadtxt(os.path.join(DIR, test_file), delimiter=',', dtype=float)

    return xy[:, 0:-1], xy[:, -1], x_test


def reg_estimators():
    '''
    List of the different estimators.
    '''
    estimators = [
        # regression models
        # ('Lasso', linear_model.Lasso(alpha=0.1), True),
        ('Ridge', linear_model.Ridge(alpha=0.1), True),
        # ('Hinge', linear_model.Hinge(), True),
        # ('ElasticNet', linear_model.ElasticNet(alpha=0.1), True),
        # ('LassoLars', linear_model.LassoLars(alpha=0.1), True),
        # ('OrthogonalMatchingPursuit', linear_model.OrthogonalMatchingPursuit(), True),
        ('OrthogonalMatchingPursuitCV', linear_model.OrthogonalMatchingPursuitCV(), True),
        ('BayesianRidge', linear_model.BayesianRidge(), True),
        ('PassiveAggressiveRegressor', linear_model.PassiveAggressiveRegressor(), True),
        # ('RANSACRegressor', linear_model.RANSACRegressor(), True),
        # ('TheilSenRegressor', linear_model.TheilSenRegressor(), True),
        # ('HuberRegressor', linear_model.HuberRegressor(), True),
    ]
    return estimators


def cla_estimators():
    estimators = [
        # classification model
        ('LogisticRegression', linear_model.LogisticRegression(), True),
        ('SVC', svm.SVC(probability=True), True),
    ]
    return estimators


def rocAucScorer(*args):
    '''
    自定义ROC-AUC评价指标rocAucScorer(clf, x_test, y_true)
    :param y_true: y_test真值
    :param x_test: x测试集
    '''
    from sklearn import metrics
    # y值比对函数
    fun = lambda yt, ys: metrics.roc_auc_score([1.0 if _ > 0.0 else 0.0 for _ in yt],
                                               np.select([ys < 0.0, ys > 1.0, True],
                                                         [0.0, 1.0, ys]))
    return metrics.make_scorer(fun, greater_is_better=True)(*args)


def plotRUC(yt, ys, color='darkorange', title=None):
    '''
    绘制ROC-AUC曲线
    :param yt: y真值
    :param ys: y预测值
    '''
    from sklearn import metrics
    from matplotlib import pyplot as plt
    f_pos, t_pos, thresh = metrics.roc_curve(yt, ys)
    auc_area = metrics.auc(f_pos, t_pos)

    plt.plot(f_pos, t_pos, color=color, lw=2, label='AUC = %.2f' % auc_area)

    plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
    plt.legend(loc='lower right')
    plt.title('ROC-AUC curve for %s' % title)
    plt.ylabel('True Pos Rate')
    plt.xlabel('False Pos Rate')
    plt.show()


def regEstimate(x, y, x_test):
    from sklearn.model_selection import cross_val_score, train_test_split
    from sklearn import metrics

    def predict():
        df = pd.read_csv(os.path.join(DIR, result_file0), sep=',', header=None)[[0, 2, 5]]
        # print(df[0:2])
        # print(len(df))

        if reg_flag:
            name, clf, _ = reg_estimators()[reg_id]
            print('items trainning...')
            clf.fit(x, y)
            print('items trainning end...')
            print(name, '\n', clf.coef_)
            y_score = clf.predict(x_test)
        else:
            name, clf, _ = cla_estimators()[cla_id]
            print('items trainning...')
            clf.fit(x, y)
            print('items trainning end...')
            y_score = clf.predict_proba(x_test)[:, clf.classes_.tolist().index(1)]

        df[6] = np.select([y_score < 0.0, y_score > 1.0, True], [0.0, 1.0, y_score])
        print(df[0:2], len(df))

        df.to_csv(os.path.join(DIR, result_file), float_format='%.3f', index=False, header=False)

    predict()

    def cross_validate():
        for name, clf, flag in reg_estimators():
            mean_score = cross_val_score(clf, x, y, cv=10, scoring=rocAucScorer).mean()
            print(mean_score)

    # cross_validate()

    def holdoutTest():
        from itertools import cycle
        from matplotlib import pyplot as plt
        colors = cycle(['aqua', 'darkorange', 'cornflowerblue', 'r', 'answers', 'g'])
        for name, clf, flag in reg_estimators():
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)
            clf.fit(x_train, y_train)
            print(name, '\n', clf.coef_)

            y_score = clf.predict(x_test)
            y_score = np.select([y_score < 0.0, y_score > 1.0, True], [0.0, 1.0, y_score])
            y_true = [1.0 if _ > 0.0 else 0.0 for _ in y_test]

            # scores = metrics.roc_auc_score(y_true=y_true, y_score=y_score)
            # print(scores)

            f_pos, t_pos, thresh = metrics.roc_curve(y_true, y_score)
            auc_area = metrics.auc(f_pos, t_pos)

            plt.plot(f_pos, t_pos, color=colors.__next__(), lw=1, label='{} AUC = {:.2f}'.format(name, auc_area))

        plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
        plt.legend(loc='lower right')
        plt.title('ROC-AUC curve for regressions')
        plt.ylabel('True Pos Rate')
        plt.xlabel('False Pos Rate')
        plt.show()

    # holdoutTest()

    pass


def t():
    x, y, x_test = preprocess()
    # x, y = x[:10], y[:10]
    # print(x, y)
    regEstimate(x, y, x_test)


if __name__ == '__main__':
    t()
