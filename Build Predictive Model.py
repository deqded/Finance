import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import  MinMaxScaler
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from tensorflow.keras.callbacks import EarlyStopping
from pandas.tseries.offsets import CustomBusinessMonthBegin

df = pd.read_csv('sp500_Adj close values.csv')

df.set_index('Date', inplace=True)

ticker = input('> What is the ticker for the company'
               ' whose adjusted close value you want to predict for? \n>').upper()

df = df.loc[:,[f'{ticker}']]
#
#
# df = df[::28]
#
# print(df)


#----- build custom calendar -----
month_index =df.index.to_period('M')
min_day_in_month_index = pd.to_datetime(df.set_index(month_index, append=True).reset_index(level=0).groupby(level=0)['Open'].min())
custom_month_starts = CustomBusinessMonthBegin(calendar = min_day_in_month_index)
#----- convert daily data to monthly data -----
ohlc_dict = {'Open':'first','High':'max','Low':'min','Close': 'last','Volume': 'sum','Adj Close': 'last'}
mthly_ohlcva = df.resample(custom_month_starts, how=ohlc_dict)

print(mthly_ohlcva)