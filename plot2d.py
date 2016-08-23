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




## __MATH MODULES__________________________ 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

## __USER MODULES__________________________
import read_table as rt
import param


## __READ PARAMETER__________________________
param=param.param()

path=param['in']
freq_start=param['freq_start']
freq_stop=param['freq_stop']
num=param['number_of_rows']
outpath=param['out']

## __DATA__________________________
fullpath=[None,'20160225_12*']   #fullpathが空のときはdataglob()によって入力が施される

## __Make DataFrame__________________________
frequency=pd.Series(np.linspace(freq_start,freq_stop,num))   #横軸はSeriesで定義
df=rt.glob_dataframe(rt.dataglob(fullpath[1]))   #データフレーム;テストのときはfullpath[1], リリースのときはfullpath[0]
df.index=frequency   #インデックス(横軸)を振りなおす




'''
開発中
def plot_time_val(df):
	時間軸で特定周波数観察
	trace=df.T
	print(trace)
	trace.plot(trace[22.000])
	plt.show()
'''


def plot_setting(df):
	# __PLOT SETTING__________________________
	plt.xlabel(param['xlabel'])
	plt.ylabel(param['ylabel'])
	if len(df.columns)<=12:   #データ12こ(1時間分)までなら凡例表示
		plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', borderaxespad=0,fontsize='small',ncol=3)
		plt.subplots_adjust(bottom=0.25)
	plt.show()

def oneplot(df,*columns):
	'''
	引数:
		df:データフレーム
		columns:行の名前(タイムスタンプ形式)
	'''
	print('\n[グラフ化したデータ一覧]\n',columns)
	for i in columns:
		plt.plot(df[i])
		plt.show()


def allplot(df):
	'''
	時間ごとに横軸index, 縦軸valuesでプロット
	データフレームのプロットを重ねて表示
	引数:
		df:データフレーム
	'''
	print('\n[グラフ化したデータ一覧]\n',df.columns)
	##____________________________
	df.plot(grid=True,ylim=param['ylim'],legend=False)
	plot_setting(df)

'''TEST
'''
oneplot(df,pd.Timestamp('2016-02-25 12:00:02'),pd.Timestamp('2016-02-25 12:45:02'))


'''
開発中
def heatmap_freq_time_val(df):
	ax=sns.heatmap(df.T)
	xlabels=[i if i in np.arange(22,26,0.5) else None for i in df.index]   #xラベル間引き22から26(0.5ずつ増加)以外はNoneにする
	timegroup=pd.date_range(df.columns[0],df.columns[-1],freq='H')   #df.columns1時間後とのイテレータ
	ylabels=[i if i in timegroup else None for i in df.columns]
	ax.set_xtickslabels(xlabels)
	ax.set_ytickslabels(ylabels)
	plt.ylabel(param['ylabel'])
	plt.show()
'''


# heatmap_freq_time_val(df)