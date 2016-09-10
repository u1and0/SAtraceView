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

csv_fullpath=param['view_out']+'average_SN.csv'
df=aggregate_csv(csv_fullpath,csvlist)   #columnごとに集計を行う(max,meanなど)



freq_index=np.linspace(freq_start,freq_stop,freq_num)
def df_marker(series, freq):
	return pd.Series(np.where(series.index==freq,series.ix[freq],np.nan), index= freq_index, name=param['country'][freq])



# def df_marker(series, freq_list):
# 	'''
# dfにtrue_or_false(TrueとFalseの入ったデータフレーム)を追加していく
# 引数:
# 	df:一列のdf(pd.DataFrame形式)
# 戻り値:
# 	df_marker:freq_listの周波数だけに値の入ったdf
# 		columnsはfreq_list
# 		indexは引数のdfと同じ
# 	'''
# 	df_mark=pd.DataFrame([i for i in range(freq_num)],columns=['Temp'])
# 	df_mark.index=freq_index
# 	for freq in freq_list:   # freq_listの周波数だけ抜き出したdfを作製
# 		true_or_false=pd.Series(np.where(series.index==22,se.ix[22,0],np.nan),index=freq_index,name='22')
# 		# ([True if i==freq else False for i in freq_index],index=freq_index)   # freq_lsitにある周波数はTrue,それ以外はFalse
# 		label=param['country'][freq]
# 		df_mark[label]=pd.DataFrame(df[true_or_false],columns=[label])
# 	del df_mark['Temp']
# 	return df_mark
# # marks=pd.DataFrame(df_mark, index=np.linspace(freq_start,freq_stop,freq_num), columns=[i+'kHz' for i in freq_list])
# # df_mark=pd.DataFrame(df,index=freq_list)   #freq_listのindexだけ抜き出し

title='%s_%s'%(csvlist[0][0],csvlist[0][1])

fig, ax1=plt.subplots()
ax1.plot(df.index, df[title], 'k-')

df_mark=df_marker(df[title], freq_list[0])
ax1.plot(df_mark.index, df_mark, linestyle='',marker='D',markeredgewidth=1,fillstyle='none')

# for dic in df_mark.columns:
# 	ax1.plot(df_mark.index, df_mark[dic],linestyle='',marker='rD',markeredgewidth=1,fillstyle='none')
plt.show()
# plt.savefig(param['view_out']+'SNmax%s.png'%title,size=(5.12,2.56))
# plt.close()
