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
file=path+'20160101_081243.txt'
po201601=pd.read_table(file,names=['Min','Ave','Max'],sep='\s+',header=0,skipfooter=1,usecols=[0,1,2],engine='python')
po201601['Frequency']=[i for i in np.linspace(freq_start,freq_stop,len(po201601))]   #frequency column added

print(po201601)






# __10ファイルの読み込み__________________________
import glob as g
allfiles=g.glob('*.txt')
pieces=[]
for file in allfiles[:10]:
	frame=pd.read_table(path+file,names=['Min','Ave','Max'],sep='\s+',header=0,skipfooter=1,usecols=[1,2,3],engine='python')   #1ファイルの読み込み
	frame['Frequency']=np.arange(freq_start,freq_stop)
	frame['Datetime']=datetime.strptime(file[:-4,'%Y%m%d_%H%M%S'])
	pirces.append(frame)
	data=pd.concat(pieces,ignore_index=True)
# print(data)