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
freq_start=param['freq_start']
freq_stop=param['freq_stop']
freq_num=param['number_of_rows']


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
	sub.index=np.linspace(freq_start,freq_stop,freq_num)
	return sub



## __MAIN__________________________
'''
matplotlib.pyplot.subplots()を使って、スペクトラムは黒線、注目周波数は色つきマーカーでplotする

csvlist: csvから抜き出す日付(始りの日、終わりの日)yyyymmdd形式
freq_list: 注目周波数、param.pyに記載
freq_index: 周波数
'''
csvlist=[
	('20151111','20151210'),
	# ('20151211','20160110'),
	# ('20160111','20160210'),
	# ('20160211','20160310'),
	# ('20160311','20160410'),
	# ('20160411','20160510'),
	# ('20160511','20160610'),
	# ('20160611','20160710'),
	# ('20160711','20160810'),
	]

country_keys=list(param['country'].keys())   #注目周波数
freq_list=sorted([i for i in country_keys])   #注目周波数をタイトルに使えるようにkHz抜いた

csv_fullpath=param['view_out']+'average_SN.csv'   # データソース
df=aggregate_csv(csv_fullpath,csvlist)   #columnごとに集計を行う(max,meanなど)

freq_index=np.linspace(freq_start,freq_stop,freq_num)   # 周波数範囲
title='%s_%s'%(csvlist[0][0],csvlist[0][1])

fig, ax1=plt.subplots()
ax1.plot(df.index, df[title], color='gray',linewidth=0.5)   # spectrum plot
for freq in freq_list:
	df_mark= pd.Series(np.where(df[title].index==freq,df[title].ix[freq],np.nan), index= freq_index, name=param['country'][freq])   # 特定の周波数だけ値、他はNaNを返すpd.Series
	ax1.plot(df_mark.index, df_mark, linestyle='',marker='D',markeredgewidth=1,fillstyle='none')   # 注目周波数plot as marker

plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', borderaxespad=0,fontsize='small',ncol=3)   # 別枠にラベルを書く
plt.subplots_adjust(bottom=0.25)
plt.show()
# plt.savefig(param['view_out']+'SNmax%s.png'%title,size=(5.12,2.56))
# plt.close()
