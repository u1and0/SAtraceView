## __MATH MODULES__________________________ 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


## __USER MODULES__________________________
import read_table as rt
import param


## __READ PARAMETER__________________________
param=param.param()

path=param['in']
freq_start=param['freq_start']
freq_stop=param['freq_stop']
num=1001

## __Make DataFrame__________________________
frequency=pd.Series(np.linspace(freq_start,freq_stop,num))   #横軸はSeriesで定義
df=rt.glob_dataframe(rt.dataglob())
df.index=frequency   #インデックス(横軸)を振りなおす

##__PLOT SETTING__________________________
# def plot_setting():
# 	## __LEGEND SETTING__________________________
# 	# plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', borderaxespad=0,fontsize='small',ncol=3)
# 	# plt.subplots_adjust(bottom=0.25)
# 	## __LABEL SETTING__________________________ 
# 	plt.xlabel(param['xlabel'])
# 	plt.ylabel(param['ylabel'])
# 	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)





def plot_time_val(df):
	'''
	開発中
	時間軸で特定周波数観察
	'''
	trace=df.T
	print(trace)
	trace.plot(trace[22.000])
	plt.show()


print('\n[グラフ化したデータ一覧]\n',df.columns)
##__時間ごとに横軸index, 縦軸valuesでプロット__________________________
df.plot(grid=True,ylim=(-120,0),legend=False)
# __PLOT SETTING__________________________
plt.xlabel(param['xlabel'])
plt.ylabel(param['ylabel'])
if len(df.columns)<=12:   #データ12こ(1時間分)までなら凡例表示
	plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', borderaxespad=0,fontsize='small',ncol=3)
	plt.subplots_adjust(bottom=0.25)
plt.show()
