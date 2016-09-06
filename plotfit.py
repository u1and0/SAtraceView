## __MATH MODULES__________________________ 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib
# font = {'family' : 'gothice'}
# matplotlib.rc('font', **font)
from scipy import stats
import seaborn as sns
# sns.set(font=['IPAPGothic'])

## __USER MODULES__________________________
import read_table as rt
import makedata
import param
param=param.param()

# df=makedata.make_dummy_dataframe()
# csv_files=['S2015_11',
# 	'S2015_11',
# 	'S2016_01',
# 	'S2016_02',
# 	'S2016_03',
# 	'S2016_04',
# 	'S2016_05',
# 	'S2016_06',
# 	'S2016_07',
# 	'S2016_08',
# 	# 'S2016_09',
# 	# 'S2016_10',
# 	# 'S2016_11',
# 	]
df=rt.fitfile_all(param['out']+'CSV/','S????_??.csv')

# std,end='20160111','20160210'
# df_loc=df.loc[std:end]   #std~endまでのインデックスを選択


def prop_plot(df_loc):
	print('読み込んだデータフレーム')
	print(df_loc)
	print('_'*20+'\n')


	print('全columnを集計')
	print(df_loc.count())   #全columnを集計
	print('_'*20+'\n')

	prop=df_loc.count()/len(df_loc)   #全dfに対して、いくつ値が入っているかの比率
	print('値が入っている比率')
	print(prop)
	print('_'*20+'\n')

	return prop.plot.bar(title='%s-%s'%(std,end),rot=30)

'''TEST prop_plot()
plt.show(prop_plot(df_loc))
'''






def prop_date(df_loc):
	key=lambda x:x.date
	df_cnt=df_loc.groupby(key).count()   #日ごとに集計
	print(df_cnt)
	print('_'*20+'\n')


	print(df_cnt.sum())   #周波数ごとに合計する
	print('_'*20+'\n')


	prop=df_cnt.sum()/len(df_loc)   #月ごとの比率はdf_locで割り算
	print(prop)
	print('_'*20+'\n')
	return prop

'''TEST
prop_date(df_loc)
'''



def plot_legend_setting(plot_element):
	'''データ12こ(1時間分)までなら凡例表示'''
	if plot_element<=12:
		plt.legend(bbox_to_anchor=(0.5, -0.3), loc='center', borderaxespad=0,fontsize='small',ncol=4)
		plt.subplots_adjust(bottom=0.25)







csvlist=[
('20151111','20151210'),
('20151211','20160110'),
('20160111','20160210'),
('20160211','20160310'),
('20160311','20160410'),
('20160411','20160510'),
('20160511','20160610'),
('20160611','20160710'),
('20160711','20160810')
]
propdf=pd.DataFrame([],columns=['temp'])
for std,end in csvlist:
	df_loc=df.loc[std:end]   #std~endまでのインデックスを選択
	propdf['%s/%s'%(std[:4],std[4:6])]=prop_date(df_loc)
del propdf['temp']
print(propdf)

month_ratio=propdf.T.sort_index(axis=1)
ax=month_ratio.plot.bar(title='Monthly Reception Ratio',rot=30)
ax.set_xlabel('Month')
ax.set_ylabel('Ratio')
plot_legend_setting(len(propdf.T.columns))
plt.show(ax)
