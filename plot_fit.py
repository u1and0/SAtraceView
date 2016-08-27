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
codf=pd.DataFrame(np.where(df,1,0),index=df.index,columns=df.columns)
print(codf)


count_foo=codf.foo.sum()   #fooの集計
print(count_foo)


# count=pd.DataFrame([codf[codf.columns]],col=df.columns)