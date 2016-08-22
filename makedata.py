# __グラフ系__________________________ 
import matplotlib.dates as pltd
import matplotlib.pyplot as plt
# __数値演算系__________________________
import numpy as np
from numpy.random import *
import scipy.stats as stats
import pandas as pd
# __時間系__________________________
from datetime import datetime, timedelta
import time
# __システム系__________________________
import sys
import os

def gaussian_param(i):
	'''
	gaussianのパラメータ
	呼び出されるたびにランダムの値返す
	'''
	return {'mu':rand(),'sigma':50*rand(),'shift':i*rand(0)}


def gaussian(x,a=1,mu=500,sigma=50,shift=0):
	'''
	x:value
	xに対してガウシアンを返す
	x=np.arange(-5.,5.,0.001)
	a=1   #最大値
	mu=500   #中央値
	sigma=50   #分散
	shift=0   #yの持ち上げ
	'''
	return a*np.exp(-(x-mu)**2/2/sigma**2)+shift


# def dummy_data(row):
# 	df=pd.DataFrame()
# 	alllist=['lista' ,'listb' ,'listc']
# 	for listname in alllist:
# 		df[listname]=pd.Series(gaussian(row,mu=row*rand(),sigma=row/10*rand(),shift=rand()))   #randomパラメータガウシアンをデータフレームに入れる
# 	return df
	# print(df)
	# df.plot(y=alllist);plt.show()


def makefile(fullpath):
	'''ダミーデータ書き込む'''
	with open(fullpath,mode='w') as f:
		c='# <This is DUMMY DATA made by %s>\n'% os.path.basename(os.getcwd())
		for index in range(1001):
			# for index in range(3)
			c+=str(index).rjust(6)
			for val in range(3):
				# cval=gaussian(index,
				# 	mu=gaussian_param(val)['mu'],
				# 	sigma=gaussian_param(val)['sigma'],
				# 	shift=gaussian_param(val)['shift'])
				# cval_round=np.around(cval,29)
				# c+=str(cval_round).rjust(11)   #np.float64形式になっている。なぜだ
				c+=str(round(rand(),4)).rjust(11)
			c+='\n'
		c+='# <eof>\n'
		f.write(c)



start_dt=datetime(2016,2,25,0,0,23)
stop_dt=datetime(2016,2,25,23,59,23)
step_dt=timedelta(minutes=5)
for filename in pltd.drange(start_dt,stop_dt,step_dt):
	filename='../../../../Documents/SAtraceView/DATA/'+pltd.num2date(filename).strftime('%Y%m%d_%H%M%S')+'.txt'
	makefile(filename)
	# df=dummy_data(1001)
	# print(df)
	# df.to_csv(path_or_buf=filename,sep='\t',index_label=False,header=False)   #rowもcolumnもラベルいらない
	# with open(filename,mode='w') as f:
	# 	f.write(randn(1000,3).tostring)
