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
path=param['in']

def aggregate(path):
	'''
	dfを周波数ごとに集計
	DataSource上のtxtデータから読む場合
	引数:
		path:Data Source
	'''
	li=['201511','201512']+[str(x) for x in range(201601,201609)]
	sub=pd.DataFrame([],columns=['Temp'])

	for i in li:
		df=rt.dataframe(path,i)
		sub[i]=df.T.max()

	del sub['Temp']
	return sub

'''TEST aggregate()
df=aggregate(path)
'''

def subplot(df):
	df.plot(subplots=True,layout=(3,3),figsize=(6,6),sharex=False)
# plt.savefig(param['out']+'SAtraceViewResult/sub.png')

# subplot(df);plt.show()



def aggregate_csv(csv_fullpath,*list_of_taple):
	'''
	dfを周波数ごとに集計
	データフレームに取り出しやすいcsvデータから読み込む場合
	引数:
		path:Data Source
	'''
	sub=pd.DataFrame([],columns=['Temp'])

	df=rt.fitfile(csv_fullpath)
	for std,end in csvlist:
		sub[std+'_'+end]=df.loc[std:end].max()

	del sub['Temp']
	return sub



## __MAIN__________________________
csvlist=[
	('20151111','20151210'),
	('20151211','20160110'),
	('20160111','20160210'),
	('20160211','20160310'),
	('20160311','20160410'),
	('20160411','20160510'),
	('20160511','20160610'),
	('20160611','20160710'),
	('20160711','20160810'),
	]

country_keys=list(param['country'].keys())   #注目周波数
freq_list=sorted([i[:4] for i in country_keys])   #注目周波数をタイトルに使えるようにkHz抜いた

csv_fullpath=param['view_out']+'average_SN.csv'
df=aggregate_csv(csv_fullpath,csvlist)   #columnごとに集計を行う(max,meanなど)
df_mark=pd.DataFrame(df,index=freq_list)   #freq_listのindexだけ抜き出し
for title in df.columns:
	plt.plot(df[title])
	plt.plot(df_mark[title],linestyle='',marker='D',markeredgewidth=1,fillstyle='none')
	plt.savefig(param['view_out']+'SNmax%s.png'%title)
	plt.close()
