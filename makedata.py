# __グラフ系__________________________ 
import matplotlib.dates as pltd
import matplotlib.pyplot as plt
# __数値演算系__________________________
import numpy as np
from random import random
import scipy.stats as stats
# __時間系__________________________
from datetime import datetime, timedelta
import time
# __システム系__________________________
import sys
import os


def soubakan(low, high, mu, si, length=1):
	'''
	正規分布に従う乱数の入ったリストを返す
	low, high: 正規分布の最小値、最大値
	mu, si: 正規分布の中央値、標準偏差
	length: いくつの要素のリストを返すか
	'''
	return stats.truncnorm.rvs((low-mu)/si, (high-mu)/si,loc=mu, scale=si,size=length)


def string_maker():
	string='# <This is DUMMY DATA made by %s>\n'% os.path.basename(__file__)   #このファイル名を書き込む
	for i in iter(soubakan(low=0, high=100, mu=50, si=0.5, length=1000)):
		string+=i
	string+='\n# <eof>'
	return string


start_dt=datetime(2016,2,25,0,0,23)
stop_dt=datetime(2016,2,25,0,55,23)
step_dt=timedelta(minutes=5)
for filename in pltd.drange(start_dt,stop_dt,step_dt):
	filename='./DATA/'+pltd.num2date(filename).strftime('%Y%m%d_%H%M%S')+'.txt'
	with open(filename,mode='w') as f:
		f.write(string_maker())
