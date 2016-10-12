# -*- coding: utf-8 -*-
'''
class plotfit v0.1

## SAtraceView ver0.1

__USAGE__
ipython (プロットするのでjupyter consoleの方がいい)起動
%load SAtraceView

__INTRODUCTION__
プロットする

__ACTION__
# クラスの外側

* モジュールをインポート
* パラメータをロード(param=...)
* 使用するファイルの指定(file = ...)
* データフレームをロード(df=...)

# クラス Plotfit


__UPDATE0.1__
First commit

__TODO__
None

'''


# __MATH MODULES__________________________
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import doctest
from tqdm import tqdm
# __USER MODULES__________________________
import read_table as rt
import simplejson

with open('parameter.json', 'r') as f:
    param = simplejson.load(f)
file = param['out_csv'] + 'P20160111_20160210.csv'
# file = param['view_out'] + 'average_SN.csv'
print('\nLoading DataFrame takes a few minutes...\n')
df = rt.fitfile(file)
print(df)
print('\n...Loading END\n')


class Plotfit(object):
    '''
    fittingされて出てきたCSVの解析、可視化
    集計方法はcountからのパーセンテージ

    # pd.DataFrameの区切り方
    x=Plotfit(df)
    x.____で使う。
    引数dfはpd.Dataframe.ixクラスを使用して、以下のように区切る

    ```
    * df=df.ix[:,:]  # dataframe全体
    * df=df.ix[pd.Timestamp('20160101'):pd.Timestamp('20160811'),:]
    > dataframeのインデックス2016年1月1日から2016年8月11日まで。
    * df=df.ix[:,['a':'c']]
    > dataframeのカラムaからcまで
    * df=df.ix[pd.Timestamp('20160101'):,['a':'c']]
    > dataframeのインデックスが2016年1月1日以降、カラムaからcまで
    ```

    __TEST__

    >>>x=Plotfit(df)

    >>>x.count()

    >>>x.plot_count()

    >>>x.plot_prop()

    >>>dft=df.ix[:,[1]]

    >>>x=Plotfit(dft)

    >>>x.plot_time();plt.show()

    '''

    def __init__(self, df):
        self.df = df

    def plot_time(self):
        '''SNの時間変化をプロット'''
        return self.df.plot()

    def count(self):
        '''値のあるところをカウント '''
        return self.df.count()

    def plot_count(self):
        '''カウントしたやつを棒グラフ化 '''
        title = '%s ~ %s' % (self.df.index[0], self.df.index[-1])
        return self.count().plot.bar(title=title, rot=30)

    def prop(self):
        '''値の出ているところの比率。母数は測定回数'''
        return self.df.count() / len(self.df)

    def plot_prop(self):
        '''比率を棒グラフ化 '''
        title = '%s ~ %s' % (self.df.index[0], self.df.index[-1])
        return self.prop().plot.bar(title=title, rot=30)


# if __name__ == '__main__':
#     doctest.testmod()
