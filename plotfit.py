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
csv_files=['S2015_11',
	'S2015_11',
	'S2016_01',
	'S2016_02',
	'S2016_03',
	'S2016_04',
	'S2016_05',
	'S2016_06',
	'S2016_07',
	'S2016_08',
	# 'S2016_09',
	# 'S2016_10',
	# 'S2016_11',
	]
df=rt.fitfile_all(param['out']+'CSV/','S????_??.csv')
print('df')
print(df)
print('_'*20+'\n')


print('df.count()')
print(df.count())   #全columnを集計
print('_'*20+'\n')

prop=df.count()/len(df)   #全dfに対して、いくつ値が入っているかの比率
print('prop')
print(prop)
print('_'*20+'\n')

prop.plot.bar()
plt.show()



# codf=pd.DataFrame(np.where(df,1,0),index=df.index,columns=df.columns)   #使えない,NaNも1にしてしまうので。



# key=lambda x:x.date   #日ごとに集計
# dfd=codf.groupby(key).sum()
# print(dfd)
# print('_'*20+'\n')

# dfd.plot.bar()
# plt.show()
