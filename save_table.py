## __BUILT-IN MODULES_________________________ 
import pandas as pd
import numpy as np
## __USER MODULES__________________________ 
import param
param=param.param()
path=param['in']   #Data Source
import read_table as rt






def save_table(df,outfullpath):
	'''outfullpath:保存するcsvのフルパス'''
	df.to_csv(outfullpath)



def make_table(sourcepath,regex):
	'''
	pd.dataframeをcsvとして保存する
	concatで後から追加できるように以下の形式で保存

	```dataframe.csv
	2016-01-01 00:00:00,2016-01-01 00:05:00,2016-01-01 00:10:00,2016-01-01 00:15:00,
	freq1,435  354,634,456,
	freq2,465  283,665,488,
	freq3,468  243,668,491,
	   
	```

	引数:
		sourcepath:データソースのある場所
		regex:ファイル名(正規表現)
	戻り値:
		dft:カラム:周波数、インデックス:日付(pandas.DataFrame形式)
		本来の使い他ではないが、一応return設けておく。
	'''
	df=rt.dataframe(sourcepath,regex)
	dft=df.T
	dft.index.name='DateTime'
	print('\n__Makeing DataFrame --> CSV')
	print(dft)
	print('\n__Making END...')
	return dft


'''TEST save_table()
'''
df=make_table(path,'20160101_00*')
save_table(df,param['view_out']+'SN201601.csv')


def concat_table(sourcepath,regex,read_csvpath):
	dfcsv=rt.fitfile(read_csvpath)   #追加されるdf
	dfcsv.columns=np.linspace(22,26,1001)

	dft=make_table(sourcepath,regex)   #追加するdf
	dft.columns=np.linspace(22,26,1001)

	df_concat=pd.concat([dfcsv,dft])   #dfの縦つなぎ
	print('\n__Concat DataFrame')
	print(df_concat)
	print('\n__Concat END...')
	return df_concat

'''TEST concat_table
'''
df=concat_table(path,'20160101_01*',param['view_out']+'SN201601.csv')
save_table(df,param['view_out']+'SN201601.csv')