# __BUILT-IN MODULES_________________________
import pandas as pd
import numpy as np
# __USER MODULES__________________________
import read_table as rt
import param
param = param.param()
path = param['in']  # Data Source


def save_table(df, outfullpath):
	'''
	dfをcsvとして保存する。
	引数:
		df:保存するDataFrame(pd.DataFrame形式)
		outfullpath:保存するcsvのフルパス(string形式)
		'''
	df.to_csv(outfullpath)


def make_table(sourcepath, regex):
	'''
	pd.dataframeをcsvとして保存する
	concatで後から追加できるように以下の形式で保存

	```dataframe.csv
	                     24507  24518  24529  24630  24641  24652  24663
	DateTime
	2016-01-01 01:27:41   5465   1333   -4097   -4133   -2280    1334    1460
	2016-01-01 01:32:43   4604   -4544   -4578    0.031   -0.45   -454   -4540
	2016-01-01 01:37:41   4605   -4644   -4578   -0.032    0.55    455   -4541
	2016-01-01 01:42:43   4606   -4744   -4578    0.033    0.65   -456    4542
	2016-01-01 01:47:45   4607   -4844   -4578   -0.034   -0.75    457    4543
	2016-01-01 01:52:45   4608   -4944    4578   -0.035   -0.85    458   -4544
	2016-01-01 01:57:43   4609   -5044   -4578   -0.036   -0.95   -459   -4545
	```

	引数:
		sourcepath:データソースのある場所
		regex:ファイル名(正規表現)
	戻り値:
		dft:カラム:周波数、インデックス:日付(pandas.DataFrame形式)
	'''
	df = rt.dataframe(sourcepath, regex)
	dft = df.T  # dfを転置する
	dft.index.name = 'DateTime'  # indexに名前付ける
	print('\n__Makeing DataFrame --> CSV')
	print(dft)
	print('\n__Making END...')
	return dft
'''TEST save_table()
df=make_table(path,'20160101_00*')
save_table(df,param['view_out']+'SN201601.csv')
'''


def concat_table(sourcepath, regex, read_csvpath):
	'''
	csvに保存されているdfと新たに追加するdfをpd.concatで縦につなげる

	引数:
		sourcepath:Data source、ファイルの入ったパス(string)
		regex:ファイル名(正規表現)
		read_csvpath:保存されたcsvのフルパス(string)
	戻り値:
		df_concat:csvから読み込まれたdfと追加するために読み込んだdfを縦につなげた(concat)df
	'''
	dfcsv = rt.fitfile(read_csvpath)  # 追加されるdf
	dfcsv.columns = np.linspace(param['freq_start'], param['freq_stop'], param['number_of_rows'])

	dft = make_table(sourcepath, regex)  # 追加するdf
	dft.columns = np.linspace(param['freq_start'], param['freq_stop'], param['number_of_rows'])

	df_concat = pd.concat([dfcsv, dft]).sort_index()  # dfの縦つなぎ
	print('\n__Concat DataFrame')
	print(df_concat)
	print('\n__Concat END...')
	return df_concat
'''TEST concat_table
'''
df = concat_table(path, '2016*', param['view_out'] + 'average_SN.csv')
save_table(df, param['view_out'] + 'average_SN.csv')
