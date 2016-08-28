## __MATH MODULES__________________________ 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
# import seaborn as sns

## __USER MODULES__________________________
import read_table as rt
import makedata


df=makedata.make_dummy_dataframe()
print(df)


print(df.count())   #全columnを集計

prop=df.count()/len(df)   #全dfに対して、いくつ値が入っているかの比率
print(prop)
prop.plot.bar()
plt.show()
