import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.finance as fin
from matplotlib.dates import date2num
import tushare as ts
import datetime



def date_to_num(dates):
    num_time = []
    for date in dates:
        date_time = datetime.datetime.strptime(date,'%Y-%m-%d')
        num_date = date2num(date_time)
        num_time.append(num_date)
    return num_time


# 将日期作为索引，并修改收盘价为股票名
hs300 = ts.get_k_data('hs300', start='2012-01-01', end='2012-12-31')

# 将时间转化成画K线图函数需要的格式
hs300['time'] = date_to_num(hs300.loc[:,'date'])


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
arr = hs300[['time', 'open', 'close', 'high', 'low']].values
fin.candlestick_ochl(ax, arr, colorup='red', colordown='green')
plt.grid()
plt.show()
