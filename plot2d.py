'''
データ選択してグラフ化するするモジュール

やっていること

1. パラメータを読み込む
    `param.param()`
2. データフレームを作成する
    `df=rt.glob_dataframe(rt.dataglob())`
3. df.plotでプロットする
    `df.plot(grid=True,ylim=(-120,0),legend=False)`
4. プロットの設定をする
5. プロットを別ウィンドウで表示
    `plot.show()`
'''


# __MATH MODULES__________________________
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# __USER MODULES__________________________
import read_table as rt
import param

param = param.param()
path = param['in']
freq_start = param['freq_start']
freq_stop = param['freq_stop']
freq_num = param['number_of_rows']
freq_index = np.linspace(freq_start, freq_stop, freq_num)   # 周波数範囲


# __DATA__________________________
df = rt.dataframe(path, regex='20160201_00')  # regexが空のときはdataglob()によって入力が施される


def plt_setting(plot_element):
    '''
    引数:
            plot_element:プロットする要素数(value)
            グラフ中に入りそうなら凡例表示
            そうでないなら表示しない
    '''
    # __PLOT SETTING__________________________
    plt.xlabel(param['xlabel'])
    plt.ylabel(param['ylabel'])
    plt.grid(True)
    if plot_element <= 12:  # データ12こ(1時間分)までなら凡例表示
        plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center',
                   borderaxespad=0, fontsize='small', ncol=3)
        plt.subplots_adjust(bottom=0.25)
    plt.show()


def timepower(df, columns):
    '''時間軸で特定周波数観察'''
    df.T.plot(y=columns)
    plt_setting(len(columns))

'''timepower() TEST
columns = [22, 23, 25.1, 25]
timepower(df, columns)
'''


def oneplot(df, col):
    '''
    dfのcolの数だけプロット
    plt.show()だと消すの大変だからplt.savefigにしようかな。
    引数:
            df:データフレーム
            col:行の名前(タイムスタンプ形式)
    '''
    print('\n[グラフ化したデータ一覧]\n', col)
    # NoiseFloor is 1/4 median.
    oneframe = pd.DataFrame([stats.scoreatpercentile(df[col], 100 / 4)
                             for i in freq_index], index=freq_index, columns=['NoiseFloor'])
    df.plot(y=col, grid=True, ylim=param['ylim'])
    oneframe['NoiseFloor'].plot(color='k')
    plt_setting(len(df.columns))
'''
oneplot() TEST
# read_table.spectrum()のSNmodeがココから触れないからグラフ表示されるけどSN表示
'''
df = rt.dataframe(path, regex='20160225_')  # regexが空のときはdataglob()によって入力が施される
columns = [pd.Timestamp('2016-02-25 12:00:02'), pd.Timestamp('2016-02-25 12:45:02')]
for col in columns:
    oneplot(df, col)
oneplot(df, pd.Timestamp('2016-02-25 12:00:02'), pd.Timestamp('2016-02-25 12:45:02'))


def allplot(df):
    '''
    時間ごとに横軸index, 縦軸valuesでプロット
    データフレームのプロットを重ねて表示
    引数:
            df:データフレーム
    '''
    print('\n[グラフ化したデータ一覧]\n', df.columns)
    # ____________________________
    df.plot(grid=True, ylim=param['ylim'], legend=False)
    plt_setting(len(df.columns))

'''allplot() TEST
# read_table.spectrum()のSNmodeがココから触れないからグラフ表示されるけどSN表示
allplot(df)
'''
