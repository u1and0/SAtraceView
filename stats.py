'''
統計を行う
まずはnoisefloor
'''

## __MATH MODULES__________________________ 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
# import seaborn as sns

## __USER MODULES__________________________
import makedata




df=makedata.gaussian_dataframe()
noisef=stats.scoreatpercentile(df, 25)	#fix at 1/4median
df['NoiseFloor']=pd.DataFrame([noisef for i in df.index])

print(df)
df.plot(ylim=(-1,1))
plt.show()
