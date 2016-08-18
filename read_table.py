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




def onefile(fullpath):
	'''1ファイルの読み込み'''
	# fullpath='20160101_081243.txt'
	df=pd.read_table(fullpath,names=['Min','Ave','Max'],sep='\s+',header=0,skipfooter=1,usecols=[1,2,3],engine='python')
	df['Frequency']=np.linspace(freq_start,freq_stop,len(df))   #frequency column added
	df['Datetime']=datetime.strptime(fullpath[-19:-4],'%Y%m%d_%H%M%S')
	return df






def manyfile(start,stop):
	'''複数ファイルの読み込み
	'''
	import glob as g
	allfiles=g.glob(path+'*.txt')[start:stop]
	pieces=[]
	for file in allfiles:
		pieces.append(onefile(file))
		data=pd.concat(pieces,ignore_index=True)
	return data


# print(onefile(path+'20160101_081243.txt'))
print(manyfile(None,10))
