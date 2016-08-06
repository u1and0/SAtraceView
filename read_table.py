import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import matplotlib.dates as pltd
import sys
from datetime import datetime, timedelta
import time



sys.path.append('../../gnuplot/SAtraceGraph/main')  #importできるディレクトリ追加
import directoryParam as di
path=di.in1()



# __1ファイルの読み込み__________________________
file=path+'20160101_081243.txt'
po201601=pd.read_table(file,names=['min','ave','max'],sep='\s+',header=0,skipfooter=1,usecols=[0,1,2],engine='python')



# __10ファイルの読み込み__________________________
import glob as g
allfiles=g.glob('*.txt')
pieces=[]
freq_start=di.freq_start()
freq_stop=di.freq_stop()
for file in allfiles[:10]:
	frame=pd.read_table(path+file,names=['Min','Ave','Max'],sep='\s+',header=0,skipfooter=1,usecols=[1,2,3],engine='python')   #1ファイルの読み込み
	frame['Freqency']=np.arange(freq_start,freq_stop)
	frame['Datetime']=datetime.strptime(file[:-4,'%Y%m%d_%H%M%S'])
	pirces.append(frame)
	data=pd.concat(pieces,ignore_index=True)
# print(data)