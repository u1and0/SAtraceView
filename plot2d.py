import read_table
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



## __パラメータ読み込み__________________________
import param
param=param.param()

path=param['in']
freq_start=param['freq_start']
freq_stop=param['freq_stop']


## __MAIN__________________________
df=glob_dataframe(dataglob())
df.plot(x=frequency,y=pd.Timestamp(pd.to_datetime(filebasename,format='%Y%m%d_%H%M%S')))
plt.show()   #それぞれ別のウィンドウで開く
