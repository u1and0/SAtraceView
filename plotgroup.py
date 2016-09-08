## __MATH MODULES__________________________ 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

## __USER MODULES__________________________
import read_table as rt
import param
param=param.param()

def aggregate(path):
	'''dfを周波数ごとに集計
	引数:
		path:Data Source
		functuion:How to aggregete'''
	li=['201511','201512']+[str(x) for x in range(201601,201608)]
	sub=pd.DataFrame([],columns=['Temp'])

	for i in li:
		df=rt.dataframe(path,i)
		sub[i]=df.T.max()

	del sub['Temp']
	return sub


path=param['in']
df=aggregate(path)
df.plot(subplots=True,layout=(3,3),figsize=(6,6),sharex=False)
plt.show()
# plt.savefig(param['out']+'SAtraceViewResult/sub.png')
