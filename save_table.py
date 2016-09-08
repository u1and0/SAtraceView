## __BUILT-IN MODULES_________________________ 
import pandas as pd
## __USER MODULES__________________________ 
import param
param=param.param()
path=param['in']   #Data Source
import read_table



df=read_table.dataframe(path,'*')
df.to_csv(param['out']+'SAtraceViewResult/SN.csv')
