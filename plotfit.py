## __MATH MODULES__________________________ 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
# import seaborn as sns

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


std,end='20160111','20160210'
df_loc=df.loc[std:end]   #std~endまでのインデックスを選択



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

prop_date(df_loc)