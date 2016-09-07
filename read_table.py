## __BUILT-IN MODULES_________________________ 
###__SCIENCE__________________________
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
# import matplotlib.dates as pltd
### __DATETIME__________________________
from datetime import datetime, timedelta
import time
###__STRING__________________________
import sys
import glob
import codecs
import re
## __USER MODULES__________________________ 
import param

## __READ PARAMETER__________________________
param=param.param()

path=param['in']
freq_start=param['freq_start']
freq_stop=param['freq_stop']
num=param['number_of_rows']


def onefile(fullpath):
	'''
	Read single file
	Store dataframe
	'''
	# fullpath='20160101_081243.txt'
	df=pd.read_table(fullpath,names=['Min','Ave','Max'],sep='\s+',header=0,skipfooter=1,usecols=[1,2,3],engine='python')
	df['Frequency']=np.linspace(freq_start,freq_stop,len(df))   #frequency column added
	df['Datetime']=pd.to_datetime(fullpath[-19:-4],format='%Y%m%d_%H%M%S')
	return df






def manyfile(start,stop):
	'''
	Read multiple files
	Store dataframe
	'''
	allfiles=glob.glob(path+'*.txt')[start:stop]
	pieces=[]
	for file in allfiles:
		pieces.append(onefile(file))
		data=pd.concat(pieces,ignore_index=True)
	return data


# print(onefile(path+'20160101_081243.txt'))
# print(manyfile(None,10))







def spectrum(fullpath,columns='Ave'):
	'''
	Make dataframe as ploting spectrums.
	indexをnp.linspaceにできないかなぁ
	'''
	use={'Min':1,'Ave':2,'Max':3}
	columns_name=pd.to_datetime(fullpath[-19:-4],format='%Y%m%d_%H%M%S')
	df=pd.read_table(fullpath,names=[columns_name],sep='\s+',header=0,skipfooter=1,usecols=[use['Ave']],engine='python')
	# df['Frequency']=np.linspace(freq_start,freq_stop,len(df))
	return df







def read_filelist(filelist_path):
	'''
	引数:ファイルパスが書かれたリストのフルパス。ファイル名は`filelist.txt`でなくてもよい。
	戻り値:filelistの中身。ただし行頭に#がついた行は飛ばす。

	filelist.txtから1行ずつ読み込み、リストに格納
	regex.compileで取り除きたい要素の文字を指定
	stripにより、改行、クォーテーションの削除
	re.searchでマッチするリストの要素は内法表記で返さない
	'''
	code=[]
	with codecs.open(filelist_path,'r','utf-8') as f:
			code+=f.readlines()   #filelist.txtから1行ずつ読み込み、リストに格納
	regex=re.compile('^#')   #regex.compileで取り除きたい要素の文字を指定
	return [i.strip('\n\r\'\"') for i in code if not regex.search(i)]
		   # stripにより、改行、クォーテーションの削除
		   # re.searchでマッチするリストの要素は内法表記で返さない






def dataglob(path,regex=False,start=0,stop=None):
	'''
	* 引数:
		* regex:globするファイル名(正規表現)
			* 空の入力=>コンソールからユーザにインプット施す
		* start:ファイルリストの最初の要素
		* stop:ファイルリストの最後の要素
	* 戻り値:
		* path内のファイルのリスト
	* 空の入力=引数なしはデフォルト引数'*'が入力され、path内のすべてのファイルを拾う
	'''
	if not regex:
		print('''
____________________________
<使い方>
グラフ化したいファイルベースネーム(拡張子抜きのファイル名)を入力
ワイルドカードも使えます！
"*"0文字以上の文字列
"?"1文字か0文字の文字列
"[]"の中に書いた文字列一文字ずつ(たとえば[135]は"1か3か5", [2-8]は"2,3,4,5,6,7,8のどれか")
使える正規表現一覧: http://docs.python.jp/3/library/re.html
(例)20151201_000344	<<<2015/12/01 00:03:44のデータ
(例)*151201_000344	<<<2015/12/01 00:03:44のデータ
(例)*151201_000344*	<<<2015/12/01 00:03:44のデータ
(例)*151201_001*	<<<2015/12/01 0時10分～19分のデータ
(例)*151201_00*		<<<2015/12/01 00時台のデータ
(例)*151201_0*		<<<2015/12/01 0～9時台のデータ
(例)*151201*		<<<2015/12/01のデータ
(例)201601??_21*	<<<2016年1月??日のデータのうち、21時台のデータ
(例)*1201_19??56	<<<？年12月1日のデータのうち、19時台で56秒で終わっているデータ
(例)201601??_2[13]*	<<<2016年01月のデータのうち、21時台か23時台のデータ
''')

		print('%s内のファイルを取得します。'%path)
		regex=input('正規表現で入力してください >> ')
		if not regex:
			return read_filelist('./filelist.txt')   #引数:読み込ませたいファイルのフルパス
		else:
			return glob.glob(path+regex)[start:stop]




def glob_dataframe(allfiles):
	'''
	* 通常の使い方:
		`glob_dataframe(dataglob())`
		としてpathからファイル名(フルパス)を読み込む

	* 自分でリスト選択
		`glob_dataframe([path+'20160225_001023.txt',path+'20160225_000523.txt'])`
		みたいにしてリストを与えてやっても可

	* 引数:
		* allfiles:ファイルのフルパス(リスト形式)

	* 戻り値：
		* df:allfilesから取得した(pandas.DataFrame形式)
	'''
	num=len(spectrum(allfiles[1]))   #
	df=pd.DataFrame(list(range(num)),columns=['Temp'])   #1001要素の仮のデータフレーム作製
	for file in allfiles:   #1ファイルを1columnとしてdfに追加
		filebasename=file[-19:-4]
		df[pd.to_datetime(filebasename,format='%Y%m%d_%H%M%S')]=spectrum(file)
		# df.plot(x=frequency,y=pd.Timestamp(pd.to_datetime(filebasename,format='%Y%m%d_%H%M%S')))
	del df['Temp']   #仮で作ったデータは消す
	print('Loading pandas DataFrame...\n\n',df)
	print('\n\n...Loading END.\n')
	return df
	# plt.show()   #それぞれ別のウィンドウで開く


def dataframe(path,regex):
	'''
	glob_dataframe()からcolumn:ファイル名、index:周波数のdataframeをもらう
	dataglob()から読み取るデータのフルパスが格納されたリストを受け取る
	正規表現を元にデータフレーム返す関数
	引数:
		rergex:正規表現(str形式)
	戻り値:
		df:データフレーム(pd.DataFrame形式)
	'''
	frequency=pd.Series(np.linspace(freq_start,freq_stop,num))   #横軸はSeriesで定義
	df=glob_dataframe(dataglob(path,regex))   #データフレーム;テストのときはfullpath[1], リリースのときはfullpath[0]
	df.index=frequency   #インデックス(横軸)を振りなおす
	return df






def fitfile(fullpath):
	'''fitされた1ファイルをデータフレームとして出力'''
	parse=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')   #インデックスを文字列からpd.Timestamp形式に変換
	df=pd.read_csv(fullpath,header=0,index_col='DateTime',date_parser=parse)
			   #1行目(0行目？)をヘッダー(=columns name)とし
			   # 'DateTime'と名前のついたcolumnをindexとする
	return df
'''TEST read_fitfile()
fullpath=param['out']+'CSV/P2015_12.csv'
df=fitfile(fullpath)
print(df)
print(df.index)
'''



def fitfile_all(path,regex):
	'''
	fitされたすべてのファイル(dataglob()で取得)を行方向に追加してデータフレームを返す

	引数:
		path:ファイルの詰まったパス
		regex:ファイル名(正規表現)

	戻り値:
		df:path+regexで指定したすべてのファイルを行方向に連結したデータフレーム(pd.DataFrame形式)
	'''
	allfiles=dataglob(path,regex)
	pieces=[]
	for file in allfiles:
		pieces.append(fitfile(file))
		df=pd.concat(pieces)
	return df
'''TEST fitfile_all()
df=fitfile_all(param['out']+'CSV/','S????_??.csv')
print(df)
'''
