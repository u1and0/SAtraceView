import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
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
	allfiles=glob.glob(path+'*.txt')[start:stop]
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
	df=pd.read_table(fullpath,names=[columns_name],sep='\s+',header=0,skipfooter=1,usecols=[use['Ave']],engine='python')
	# df['Frequency']=np.linspace(freq_start,freq_stop,len(df))
	return df




## __MAIN__________________________

# file='20160818_145913.txt'
allfiles=glob.glob(path+'*.txt')[:10]
num=len(spectrum(allfiles[1]))
df=pd.DataFrame(np.linspace(freq_start,freq_stop,num),columns=['Frequency'])
print(df)
for file in allfiles:
	filebasename=file[-19:-4]
	df[pd.to_datetime(filebasename,format='%Y%m%d_%H%M%S')]=spectrum(file)
	df.plot(x='Frequency',y=pd.Timestamp(pd.to_datetime(filebasename,format='%Y%m%d_%H%M%S')))
print(df)
plt.show()   #それぞれ別のウィンドウで開く
