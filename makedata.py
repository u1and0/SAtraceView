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

def gaussian(num,a=1,mu=500,sigma=50,shift=0):
	'''
	x:リスト
	xに対してガウシアンexp()に従う値のリストを返す
	x=np.arange(-5.,5.,0.001)
	a=1   #最大値
	mu=500   #中央値
	sigma=50   #分散
	shift=0   #yの持ち上げ
	x=np.arange(1001)
	'''
	x=np.arange(num)
	y=a*np.exp(-(x-mu)**2/2/sigma**2)+shift
	return y


def dummy_data(row):
	df=pd.DataFrame()
	alllist=['lista' ,'listb' ,'listc']
	for listname in alllist:
		df[listname]=pd.Series(gaussian(row,mu=row*rand(),sigma=row/10*rand(),shift=rand()))   #randomパラメータガウシアンをデータフレームに入れる
	return df
	# print(df)
	# df.plot(y=alllist);plt.show()



start_dt=datetime(2016,2,25,0,0,23)
stop_dt=datetime(2016,2,25,0,15,23)
step_dt=timedelta(minutes=5)
for filename in pltd.drange(start_dt,stop_dt,step_dt):
	filename='./DATA/'+pltd.num2date(filename).strftime('%Y%m%d_%H%M%S')+'.txt'
	df=dummy_data(1001)
	print(df)
	df.to_csv(path_or_buf=filename,sep=',',index_label=False,header=False)   #rowもcolumnもラベルいらない
	# with open(filename,mode='w') as f:
	# 	f.write(randn(1000,3).tostring)
