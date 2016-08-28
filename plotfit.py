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

## __DATA__________________________
df=rt.fitfile_all(param['out']+'CSV/','S????_??.csv')
print(df)
columns=df.columns
prop=df[columns].count/len(df[columns[0]])
.plot