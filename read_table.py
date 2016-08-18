import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as pltd
import sys
from datetime import datetime, timedelta
import time


# __パラメータ読み込み__________________________
import param
param=param.param()
path=param['in']
freq_start=param['freq_start']
freq_stop=param['freq_stop']




# __1ファイルの読み込み__________________________
file='20160101_081243.txt'
series=pd.read_table(path+file,names=['Min','Ave','Max'],sep='\s+',header=0,skipfooter=1,usecols=[1,2,3],engine='python')
series['Frequency']=np.linspace(freq_start,freq_stop,len(series))   #frequency column added
series['Datetime']=datetime.strptime(file[:-4],'%Y%m%d_%H%M%S')

# print(series)






# __10ファイルの読み込み__________________________
import glob as g
allfiles=g.glob(path+'*.txt')[:10]
pieces=[]
print(allfiles)
for file in allfiles:
	df=pd.read_table(file,names=['Min','Ave','Max'],sep='\s+',header=0,skipfooter=1,usecols=[1,2,3],engine='python')
	df['Frequency']=np.linspace(freq_start,freq_stop,len(series))   #frequency column added
	df['Datetime']=datetime.strptime(file[-19:-4],'%Y%m%d_%H%M%S')
	pieces.append(df)
	data=pd.concat(pieces,ignore_index=True)
print(data)