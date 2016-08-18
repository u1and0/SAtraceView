import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import sys
# import matplotlib.dates as pltd
# from datetime import datetime, timedelta
# import time


# __パラメータ読み込み__________________________
import param
param=param.param()

path=param['in']
freq_start=param['freq_start']
freq_stop=param['freq_stop']




def onefile(fullpath):
	'''
	Read single file
	Store dataframe
	'''
	# fullpath='20160101_081243.txt'
	df=pd.read_table(fullpath,names=['Min','Ave','Max'],sep='\s+',header=0,skipfooter=1,usecols=[1,2,3],engine='python')
	df['Frequency']=np.linspace(freq_start,freq_stop,len(df))   #frequency column added
	df['Datetime']=pd.to_datetime(fullpath[-19:-4],format='%Y%m%d_%H%M%S')
	return df






def manyfile(start,stop):
	'''
	Read multiple files
	Store dataframe
	'''
	import glob as g
	allfiles=g.glob(path+'*.txt')[start:stop]
	pieces=[]
	for file in allfiles:
		pieces.append(onefile(file))
		data=pd.concat(pieces,ignore_index=True)
	return data


# print(onefile(path+'20160101_081243.txt'))
# print(manyfile(None,10))

def spectrum(fullpath):
	'''
	Make dataframe as ploting spectrums.
	indexをnp.linspaceにできないかなぁ
	'''
	use={'Min':1,'Ave':2,'Max':3}
	columns_name=pd.to_datetime(fullpath[-19:-4],format='%Y%m%d_%H%M%S')
	# au=list(np.arange(1001))
	df=pd.read_table(fullpath,names=[columns_name],index_col=False,sep='\s+',header=0,skipfooter=1,usecols=[2],engine='python')
	# df['Frequency']=np.linspace(freq_start,freq_stop,len(df))
	return df

k=spectrum(path+'20160818_145913.txt')

# kk=pd.DataFrame(k,index='Frequency',columns=0)
print(k)
# print(spectrum(path+'20160818_145913.txt'))
# spectrum(path+'20160818_145913.txt').plot()
# plt.show()