## __BUILT-IN MODULES_________________________ 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
# import sys
# import matplotlib.dates as pltd
# from datetime import datetime, timedelta
# import time
## __USER MODULES__________________________ 
import param


## __READ PARAMETER__________________________
param=param.param()

path=param['in']
freq_start=param['freq_start']
freq_stop=param['freq_stop']
num=param['number_of_rows']
outpath=param['out']


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






def dataglob(regex=False,start=0,stop=None):
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


def dataframe(regex):
	'''
	正規表現を元にデータフレーム返す関数
	引数:
		rergex:正規表現(str形式)
	戻り値:
		df:データフレーム(pd.DataFrame形式)
	'''
	frequency=pd.Series(np.linspace(freq_start,freq_stop,num))   #横軸はSeriesで定義
	df=glob_dataframe(dataglob(regex))   #データフレーム;テストのときはfullpath[1], リリースのときはfullpath[0]
	df.index=frequency   #インデックス(横軸)を振りなおす
	return df



def dataframe_fit():
	pass