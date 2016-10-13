# -*- coding: utf-8 -*-
'''
## SAtraceView ver1.0

__USAGE__

# ipythonを起動

コマンドラインで`ipython`と打つ
> プロットするので`jupyter console`や`jupyter notebook`の方がいい



# モジュールのインポート

最初のセルに`%load SAtraceView`と打ち込む
データのロードが完了すると
ロードしたデータフレームが表示される


# データの代入

`x=Plotfit(df)`


## 解説

* データはソース内で指定したcsvから読み込まれ`df`というオブジェクトに格納されている。
* `x`などといったオブジェクトにクラスPlotfit(* データフレーム型の引数)を代入する。


# データの選択方法

```
dft=df.ix['20160211':'20160310',[0,4]]  # 選択したものをdftに代入する
x=Plotfit(dft)
```

* 2016年2月11日から2016年3月10日までの行
* 0番目、4番目の列
* 0,4...といった列番号ではなく、列名('xxxkHz')を指定しても良い。
> クォーテーションでくくること
* xというオブジェクトに`dft`を使用したクラスを代入する


__INTRODUCTION__

プロットする


__ACTION__

# クラスの外側

* モジュールをインポート
* パラメータをロード(param=...)
* 使用するファイルの指定(file = ...)
* データフレームをロード(df=...)

# クラス Plotfit

self.df : 引数にしたデータフレーム
self.title : データフレームの日時の最初と最後


__UPDATE1.0__

* count_agg追加
* README追加


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
# __USER MODULES__________________________
import read_table as rt
import simplejson

with open('parameter.json', 'r') as f:
    param = simplejson.load(f)
# file = param['out_csv'] + 'P20160111_20160210.csv'  # テスト用
file = param['out_csv'] + 'SNallfit_allseason.csv'
print('''
Loading DataFrame takes a few minutes...
Please wait.
''')
df = rt.fitfile(file)
print(df)
print('\n...Loading END\n')

print('''
# データの代入

`x=Plotfit(df)`


# データの選択方法

```
dft=df.ix['20160211':'20160310',[0,4]]
x=Plotfit(dft)
```

* 以下を選択したものをdftに代入する
    * 2016年2月11日から2016年3月10日までの行
    * 0番目、4番目の列
    * 0,4...といった列番号ではなく、列名('xxxkHz')を指定しても良い。
    > クォーテーションでくくること


# 集計とプロット

```
x=Plotfit(df)
x.df  # ロードしたデータフレームの表示
x.plot_time()  # SN時間変化
x.plot_count()  # 日でグループ化してカウント
x.plot_count_agg()  # 日でグループ化してカウント
                    # x.count_agg().plot.bar()同義
x.plot_count_agg('month')  # 月でグループ化してカウント
```
詳細は`Plotfit??`で表示されます。




''')

class Plotfit(object):
    '''
    fittingされて出てきたCSVの解析、可視化
    集計方法はcountからのパーセンテージ


    # 集計とプロット

    ```
    x=Plotfit(df)
    x.df  # ロードしたデータフレームの表示
    x.plot_time()  # SN時間変化
    x.plot_count()  # 日でグループ化してカウント
    x.plot_count_agg()  # 日でグループ化してカウント
                        # x.count_agg().plot.bar()同義
    x.plot_count_agg('month')  # 月でグループ化してカウント
    ```
    詳細は`Plotfit??`で表示されます。


    __TEST__

    >>>x=Plotfit(df)  # データのインスタンス化

    >>>x.df  # ロードしたデータフレーム

    >>>x.plot_time()  # SN時間変化

    >>>x.count()  # 日でグループ化

    >>>x.plot_count()  # 日でグループ化したものをプロット

    >>>x.plot_prop()

    >>>x.plot_count_agg()  # 日で

    >>>x.plot_count_agg('month')  # 月でグループ化してカウント

    >>>dft=df.ix[:,[1]]  # データの選択

    >>>x=Plotfit(dft)  # 選択されたデータをインスタンス化

    '''

    def __init__(self, df):
        '''Plotfitの引数をインスタンス化'''
        self.df = df
        self.title = '%s~%s'% (df.index[0].date(),df.index[-1].date())

    def plot_time(self):
        '''SNの時間変化をプロット'''
        return self.df.plot()

    def count(self):
        '''値のあるところをカウント'''
        return self.df.count()

    def plot_count(self):
        '''カウントしたやつを棒グラフ化'''
        title = '%s ~ %s' % (self.df.index[0], self.df.index[-1])
        return self.count().plot.bar(title=title, rot=30)

    def prop(self):
        '''値の出ているところの比率。母数は測定回数'''
        return self.df.count() / len(self.df)

    def plot_prop(self):  # Plotfit(df).prop.plot.bar()とほぼ同義
        '''比率を棒グラフ化'''
        return self.prop().plot.bar(title=self.title, rot=30)

    def count_agg(self, func='date'):
        '''
        funcに使用する関数でグループ分け
        # 使用できるもの一覧

        * date : 日付
        * week : 週
        * month : 月
        * hour : 時間
        * minute : 分
        * second : 秒

        '''
        groupfunc = 'lambda x: x.%s' % func
        return self.df.groupby(eval(groupfunc)).count()

    def plot_count_agg(self, func='date'):
        '''count_agg().plot.bar(x.title, rot=30)と同義'''
        return self.count_agg(func).plot.bar(title=self.title, rot=30)
