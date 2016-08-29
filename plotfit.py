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
df=rt.fitfile_all(param['out']+'CSV/','S????_??.csv')
print(df)
print('_'*20+'\n')


print(df.count())   #全columnを集計
print('_'*20+'\n')

prop=df.count()/len(df)   #全dfに対して、いくつ値が入っているかの比率
print(prop)
print('_'*20+'\n')

# prop.plot.bar()
# plt.show()



codf=pd.DataFrame(np.where(df,1,0),index=df.index,columns=df.columns)



key=lambda x:x.month
dfd=codf.groupby(key).sum()   #日ごとに集計
print(dfd)
print('_'*20+'\n')

dfd.plot.bar()
plt.show()
