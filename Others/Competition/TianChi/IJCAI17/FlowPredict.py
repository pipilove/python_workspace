#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '商家人流量预测'
__author__ = 'pipi'
__mtime__ = '2/23/17'
__email__ = 'pipijob@126.com'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓    ┏┓
            ┏━┛┻━━━━┛┻━┓
            ┃     ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃     ┻    ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━┓┓┏━━┳┓┏━┛
                ┃┫┫  ┃┫┫
                ┗┻┛  ┗┻┛
"""
import pandas as pd
import os, sys, pickle
import numpy as np
import matplotlib.pylab as plt

CWD = os.path.split(os.path.realpath(__file__))[0]
print(CWD)
sys.path.append(os.path.join(CWD, '../../../..'))
from Oth.Utility.TimeStump import time_block

datadir = r'~/files/DATASETS/tianchi/ijcai17/dataset/'
shop_info_filename = os.path.join(datadir, r'shop_info.csv')
user_pay_filename = os.path.join(datadir, r'user_pay2.csv')


def readData():
    user_pay_df = pd.read_csv(user_pay_filename, header=None, parse_dates=[2], names=['uid', 'sid', 'time'])
    # user_pay_df['time'] = user_pay_df['time'].dt.date.astype('M8[D]')
    user_pay_df['time'] = user_pay_df['time'].dt.normalize()
    # print(user_pay_df.head())
    # print(user_pay_df.dtypes)
    pickle.dump(user_pay_df, open('./user_pay_df.pkl', 'wb'))
    return user_pay_df


def showData(user_pay_df):
    print(user_pay_df.head())
    print('#shop: {}'.format(len(user_pay_df['sid'].unique())))
    print('#date: {}'.format(len(user_pay_df['time'].unique())))
    print('#user: {}'.format(len(user_pay_df['uid'].unique())))
    # print('mean of each shop:\n{}'.format(np.mean(user_pay_df.groupby(by=['sid']).count())))


def test_stationarity(timeseries):
    '''
    测试时间序列的稳定性
    '''
    from statsmodels.tsa.stattools import adfuller
    from multiprocessing import Process

    # Determing rolling statistics
    # rolmean = pd.rolling_mean(timeseries, window=12)
    # rolstd = pd.rolling_std(timeseries, window=12)
    rolmean = timeseries.rolling(window=30).mean()
    expwighted_avg = timeseries.ewm(halflife=15).mean()
    # shiftmean = timeseries.shift()
    rolstd = timeseries.rolling(window=30).std()

    def draw():
        # Plot rolling statistics:
        plt.plot(timeseries, color='blue', label='Original')
        plt.plot(rolmean, color='red', label='Rolling Mean')
        plt.plot(expwighted_avg, color='green', label='Expwighted Avg')
        # plt.plot(shiftmean, color='orange', label='Shift Mean')
        plt.plot(rolstd, color='black', label='Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show()

    p = Process(target=draw)
    p.start()

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)
    p.join()


def decompose(ts, freq):
    '''
    时间序列季节分解：trend + seasonal + residual
    '''
    from statsmodels.tsa.seasonal import seasonal_decompose

    decomposition = seasonal_decompose(ts, freq=freq)

    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    plt.subplot(411)
    plt.plot(ts, label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal, label='Seasonality')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residuals')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

    return trend, seasonal, residual


def draw_parameter(ts):
    '''
    时间序列预测。ts是经过消除趋势和季节性之后的时序。
    p-部分自相关函数图第一次截断上层置信区间的滞后值。
    q- 自相关函数图第一次截断上层置信区间的滞后值。
    '''
    from statsmodels.tsa.stattools import acf, pacf
    lag_acf = acf(ts, nlags=20)
    lag_pacf = pacf(ts, nlags=20, method='ols')

    # Plot ACF
    plt.subplot(121)
    plt.plot(lag_acf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96 / np.sqrt(len(ts)), linestyle='--', color='gray')
    plt.axhline(y=1.96 / np.sqrt(len(ts)), linestyle='--', color='gray')
    plt.title('Autocorrelation Function')

    # Plot PACF
    plt.subplot(122)
    plt.plot(lag_pacf)
    plt.axhline(y=0, linestyle='--', color='gray')
    plt.axhline(y=-1.96 / np.sqrt(len(ts)), linestyle='--', color='gray')
    plt.axhline(y=1.96 / np.sqrt(len(ts)), linestyle='--', color='gray')
    plt.title('Partial Autocorrelation Function')
    plt.tight_layout()

    plt.show()


def draw_models(ts, p=1, d=1, q=1):
    '''
    建立三种模型进行对比，融合模型更好，所以就只采用融合模型的结果
    '''
    from statsmodels.tsa.arima_model import ARIMA

    ts = ts.astype(float)
    ts_diff = (ts - ts.shift()).dropna()
    # print(ts.head())
    # print(ts_diff.head())

    # AR Model
    model = ARIMA(ts, order=(p, d, 0))  # order = (p,d,q), 其中就是计算了一阶差分了
    results_AR = model.fit(disp=-1)

    # MA Model
    model = ARIMA(ts, order=(0, d, q))
    results_MA = model.fit(disp=-1)

    # Combined Model
    model = ARIMA(ts, order=(p, d, q))
    results_ARIMA = model.fit(disp=-1)

    def draw():
        plt.subplot(311)
        plt.plot(ts_diff)
        plt.plot(results_AR.fittedvalues, color='red')
        plt.title('RSS: %.4f' % sum((results_AR.fittedvalues - ts_diff) ** 2))

        plt.subplot(312)
        plt.plot(ts_diff)
        plt.plot(results_MA.fittedvalues, color='red')
        plt.title('RSS: %.4f' % sum((results_MA.fittedvalues - ts_diff) ** 2))

        plt.subplot(313)
        plt.plot(ts_diff)
        plt.plot(results_ARIMA.fittedvalues, color='red')
        plt.title('RSS: %.4f' % sum((results_ARIMA.fittedvalues - ts_diff) ** 2))
        plt.show()

    draw()


def predict(ts, forecast_days, p=1, d=1, q=1):
    '''
    :param forecast_days: 最后时间值之后forecast_days天的预测值
    '''
    from statsmodels.tsa.arima_model import ARIMA

    ts = ts.astype(float)

    # Combined Model
    model = ARIMA(ts, order=(p, d, q))
    results_ARIMA = model.fit(disp=-1)

    # taking these values back to the original scale
    predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
    # print(predictions_ARIMA_diff.head())
    # print(predictions_ARIMA_diff.tail())

    predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
    # print(predictions_ARIMA_diff_cumsum.head())
    predictions_ARIMA = pd.Series(ts.ix[0], index=ts.index)
    predictions_ARIMA = predictions_ARIMA.add(predictions_ARIMA_diff_cumsum, fill_value=0)
    print('head个预测值：\n{}'.format(predictions_ARIMA.head()))

    def compare_result(ts, predictions_ARIMA):
        plt.plot(ts)
        plt.plot(predictions_ARIMA)
        plt.title('RMSE: %.4f' % np.sqrt(sum((predictions_ARIMA - ts) ** 2) / len(ts)))
        plt.show()

    # compare_result(ts, predictions_ARIMA)

    forecast_values = results_ARIMA.forecast(forecast_days)[0]
    print('预测的未来{}天的值：\n{}'.format(forecast_days, forecast_values))


# user_pay_df = readData()
user_pay_df = pickle.load(open('./user_pay_df.pkl', 'rb'))
showData(user_pay_df)
shop_ids = user_pay_df['sid'].unique()
# print(shop_ids)
s_group = user_pay_df.groupby(by=['sid', 'time']).count()
s_group.columns = ['#user']

# print(s_group)

for i, sid in enumerate(shop_ids):
    print('*' * 18, ' ' + str(i) + ' ', '*' * 18)
    ts = s_group.ix[sid]['#user']  # df => series
    print('head个实际值：\n{}'.format(ts.head()))
    # print(ts.tail())
    # print(ts.index)

    # rolling mean
    # ts -= ts.rolling(window=30).mean()
    # ts.dropna(inplace=True)

    # 指数移动平均ewn
    # ts -= ts.ewm(halflife=15).mean()

    # differencing
    # ts -= ts.shift()
    # ts.dropna(inplace=True)

    # test_stationarity(ts)

    # decompose
    # _, __, ts_decompose = decompose(ts, freq=30)
    # ts_decompose.dropna(inplace=True)
    # test_stationarity(ts_decompose)

    # draw_parameter(ts)
    # draw_models(ts)
    predict(ts, 14)
    break
