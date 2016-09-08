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

param=param.param()

## __DATA__________________________
df=rt.dataframe(path=param['in'],regex='201602*')   #regexが空のときはdataglob()によって入力が施される

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
	if plot_element<=12:   #データ12こ(1時間分)までなら凡例表示
		plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', borderaxespad=0,fontsize='small',ncol=3)
		plt.subplots_adjust(bottom=0.25)
	plt.show()





def timepower(df,columns):
	'''時間軸で特定周波数観察'''
	df.T.plot(y=columns)
	plt_setting(len(columns))

'''timepower() TEST
columns=[22,23,25.1,25]
timepower(df,columns)
'''




def oneplot(df,columns):
	'''
	dfのcolumnsの数だけプロット
	plt.show()だと消すの大変だからplt.savefigにしようかな。
	引数:
		df:データフレーム
		columns:行の名前(タイムスタンプ形式)
	'''
	print('\n[グラフ化したデータ一覧]\n',columns)
	oneframe=pd.DataFrame([stats.scoreatpercentile(df[col],100/4) for i in frequency],index=frequency,columns=['NoiseFloor'])	#NoiseFloor is 1/4 median.
	df.plot(y=col,grid=True,ylim=param['ylim'])
	oneframe['NoiseFloor'].plot(color='k')
	plt_setting(len(df.columns))
'''
oneplot() TEST
columns=[pd.Timestamp('2016-02-25 12:00:02'),pd.Timestamp('2016-02-25 12:45:02')]
for col in columns:
	oneplot(df,columns)
oneplot(df,pd.Timestamp('2016-02-25 12:00:02'),pd.Timestamp('2016-02-25 12:45:02'))
'''


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
	plt_setting(len(df.columns))

'''allplot() TEST
allplot(df)
'''

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
