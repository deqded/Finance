from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
import pandas_datareader.data as web
from matplotlib import style
import datetime as dt
import matplotlib.pyplot as plt
import os
import pickle

def get_sp500_tickers():
    url = rq.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

    soup = BeautifulSoup(url.content, 'lxml')

    table = soup.find(id = "constituents")

    ticks = table.find_all(class_= 'external text')

    tickers = []
    count = 0
    for x in ticks:
        tickers.append(ticks[count].get_text())
        count+=1
    sc = 1
    for x in tickers:
        if x == 'reports':
            tickers.pop(sc)
            sc+=1
    with open('sp500tickers.pickle', 'wb') as f:
        pickle.dump(tickers, f)

    return tickers


def get_data():
    tickers = get_sp500_tickers()
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()
    os.chdir('C:\\Users\\khatt\\Desktop\\Coding\\Finance\\SP_500')
    count = 0
    while True:
        try:
            for x in tickers[count:]:
                if not os.path.exists(f'stock_dfs{x}.csv'):
                    df = web.DataReader(f"{x}", 'yahoo', start, end)
                    df.to_csv(f'{x}.csv')
                print(f"got {x} {count}")
                count += 1

        except Exception:
            count += 1
            failed = open('failed.csv', 'a')
            failed.write(f'{x}')
            failed.close()
            pass
        break
    return

def combine_data():
    tickers = get_sp500_tickers()
    del tickers[69]
    del tickers[80]
    maindataframe = pd.DataFrame()
    os.chdir('C:\\Users\\khatt\\Desktop\\Coding\\Finance\\SP_ 500')
    count = 0

    for x in tickers[count:]:
        df = pd.read_csv(f'{x}.csv')
        df.set_index('Date', inplace=True)
        df.rename(columns={'Adj Close': x}, inplace=True)
        df.drop(['Open'],1, inplace=True)
        df.drop(['High'],1, inplace=True)
        df.drop(['Low'],1, inplace=True)
        df.drop(['Close'],1, inplace=True)
        df.drop(['Volume'], 1, inplace=True)

        count +=1

        if maindataframe.empty:
            maindataframe = df
        else:
            maindataframe = maindataframe.join(df, how='outer')
        if count % 10 == 0:
            print(count)
        print(maindataframe.head())
        maindataframe.to_csv('sp500_Adjclose.csv')


combine_data()

