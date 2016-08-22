import read_table as rt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



## __パラメータ読み込み__________________________
import param
param=param.param()

path=param['in']
freq_start=param['freq_start']
freq_stop=param['freq_stop']
num=1001

## __Make DataFrame__________________________
frequency=pd.Series(np.linspace(freq_start,freq_stop,num))   #横軸はSeriesで定義
df=rt.glob_dataframe(rt.dataglob('20160225_12*'))
df.index=frequency   #インデックス(横軸)を振りなおす

## __PLOT1__________________________
'''時間ごとに横軸index, 縦軸valuesでプロット'''
df.plot()
plt.show()   #それぞれ別のウィンドウで開く
