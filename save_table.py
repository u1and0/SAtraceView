## __BUILT-IN MODULES_________________________ 
import pandas as pd
## __USER MODULES__________________________ 
import param
param=param.param()
path=param['in']   #Data Source
import read_table


def save_table(inpath,regex,outpath):
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
		inpath:データソースのある場所
		regex:ファイル名(正規表現)
		outpath:保存するcsvのフルパス
	戻り値:
		dft:カラム:周波数、インデックス:日付(pandas.DataFrame形式)
		本来の使い他ではないが、一応return設けておく。
	'''
	df=read_table.dataframe(inpath,regex)
	dft=df.T
	dft.index.name='DateTime'
	dft.to_csv(outpath)
	return dft



save_table(path,'20160101_01*',param['view_out']+'SN201601.csv')