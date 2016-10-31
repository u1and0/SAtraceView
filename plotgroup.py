'''
aggregare___関数を使って集計したpd.DataFrameを可視化するモジュール
'''

# __MATH MODULES__________________________
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# __USER MODULES__________________________
import read_table as rt
param=rt.load_parameter()

path = param['in']
freq_start = param['freq_start']
freq_stop = param['freq_stop']
freq_num = param['number_of_rows']
freq_index = np.linspace(freq_start, freq_stop, freq_num)   # 周波数範囲


def aggregate(path):
	'''
	DataSource上のtxtデータから読み込んで周波数ごとに集計してpd.DataFrameで返す

	**save_table.pyでcsvを作ってあるなら、aggregate_csvから読み込むほうが早い**

	引数:
	 path: Data Source(string型)
	戻り値:
	 sub: (pd.DataFrame型)
	'''
	li = ['201511', '201512'] + [str(x) for x in range(201601, 201609)]
	sub = pd.DataFrame([], columns=['Temp'])

	for i in li:
		df = rt.dataframe(path, i)
		sub[i] = df.T.max()

	del sub['Temp']
	return sub


'''TEST aggregate()
df=aggregate(path)
'''


# df.plot(subplots=True,layout=(3,3),figsize=(6,6),sharex=False);plot.show()
# plt.savefig(param['out']+'SAtraceViewResult/sub.png')


def aggregate_csv(csv_fullpath, list_of_tuple):
	'''
	"csvfullpath"の中のファイルに対して、datelist(tuple of list形式)で区切って集計を行う(max,meanなど)
	dfを周波数ごとに集計
	集計範囲はlist_of_tupleに記載
	データフレームに取り出しやすいcsvデータから読み込む場合
	**集計方法(mean, maxなど)はココで変える！**


	引数:
	 path: Data Source
	 list_of_tuple: 集計の日付(yyyymmddの値が二つ入ったタプル形式のリスト)
	戻り値:
	 sub: 値は集計値(pd.DataFrame形式)
	'''
	print('Now loading from %s...' % csv_fullpath)
	sub = pd.DataFrame([], columns=['Temp'])

	df = rt.fitfile(csv_fullpath)
	for std, end in list_of_tuple:
		print('Date aggregation from %s to %s.' % (std, end))
		sub[std + '_' + end] = df.loc[std:end].max()

	del sub['Temp']
	sub.index = np.linspace(freq_start, freq_stop, freq_num)
	return sub


def eachplot(series, freq_list):
	'''
	plt.subplots()を使用してline plotとmarker plotを共存させる

	1. pd.DataFrameから切り出したpd.Seriesなどを引数にする。
	2. np.whereで特定のindexだけ値、それ以外はNanのpd.Seriesを作る。
	3. subplots()で切り出したpd.Seriesをline plot
	4. subplots()で作ったNan入りpd.Seriesをmarker plot
	5. label, title limitの設定

	引数:
	 series:
	 freq_list:注目周波数のリスト

	戻り値:なし
	'''
	print('plot %s' % series.name)
	fig, ax1 = plt.subplots()
	ax1.plot(series.index, series, color='gray', linewidth=0.5)   # spectrum plot
	for freq in freq_list:
		ax1.plot(freq, series.ix[freq],
                    linestyle='',
                    marker='D',
                    markeredgewidth=1,
                    fillstyle='none',
                    label=param['country'][str(freq)])   # 注目周波数plot as marker

	# __MAKE LABEL, TITLE, LIMIT__________________________
	plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center',
	           borderaxespad=0, fontsize='small', ncol=3)   # 別枠にラベルを書く
	plt.subplots_adjust(bottom=0.25)


def plot_marker(df, datelist):
	'''
	引数:
		df: csvをdateでグループ化したものpandas dataframe
	matplotlib.pyplot.subplots()を使って、スペクトラムは黒線、注目周波数は色つきマーカーでplotする
		datelist: csvから抜き出す日付(始りの日、終わりの日)yyyymmdd形式

	freq_list: 注目周波数、param.pyに記載
	freq_index: 周波数
	'''

	country_keys = list(param['country'].keys())  # 注目周波数
	freq_list = sorted([i for i in country_keys])  # 注目周波数をタイトルに使えるようにkHz抜いた

	for start, end in datelist:
		column_name = '%s_%s' % (start, end)   # dataframeのcolumn nameになる("yyyymmdd_yyyymmdd"の形のstring型)

		eachplot(df[column_name], freq_list)
		def dateiso(x):
			return pd.to_datetime(x, format='%Y%m%d').isoformat()[:10]   # yyyymmddの文字列に直してくれる
		plt.title('S/N ratio Max in 1month from %s to %s' % (dateiso(start), dateiso(end)))
		plt.ylabel('S/N ratio [dBm]')
		plt.ylim(param['ylim_max'])

		# __SHOW GRAPH or SAVE GRAPH__________________________
		plt.show()
		# plt.savefig(param['view_out'] + 'SNmax%s.png' % column_name, size=(5.12, 2.56))
		# plt.close()


if __name__ == '__main__':
	csv_fullpath = param['view_out'] + 'average_SN.csv'   # データソースを整理して収めたcsvファイルの場所(save_table参照)
	datelist = [
		('20151111', '20151210'),
		('20151211', '20160110'),
		('20160111', '20160210'),
		('20160211', '20160310'),
		('20160311', '20160410'),
		('20160411', '20160510'),
		('20160511', '20160610'),
		('20160611', '20160710'),
		('20160711', '20160810'),
	]
	plot_marker(aggregate_csv(csv_fullpath, datelist), datelist)
