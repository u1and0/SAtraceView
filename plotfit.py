'''
fittingされて出てきたCSVの解析、可視化
集計方法はcountからのパーセンテージ
'''
# __MATH MODULES__________________________
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# __USER MODULES__________________________
import read_table as rt
import json
with open('parameter.json', 'r') as f:
	param = json.load(f)

df = rt.fitfile(param['out'] + 'CSV/' + 'SN20151211_20160110.csv')
# df = rt.fitfile_all(param['out'] + 'CSV/', 'S????_??.csv')

# std,end='20160111','20160210'
# df_loc=df.loc[std:end]   #std~endまでのインデックスを選択


def prop_plot(df_loc):
	print('読み込んだデータフレーム')
	print(df_loc)

	print('全columnを集計')
	print(df_loc.count())  # 全columnを集計

	prop = df_loc.count() / len(df_loc)  # 全dfに対して、いくつ値が入っているかの比率
	print('値が入っている比率')
	print(prop)

	return prop.plot.bar(title='%s-%s' % (std, end), rot=30)


'''TEST prop_plot()
plt.show(prop_plot(df_loc))
'''


def prop_date(df_loc):
	df_cnt = df_loc.groupby(lambda x: x.date).count()  # 日ごとに集計
	print('__count__')
	print(df_cnt)

	print('__sum__')
	print(df_cnt.sum())  # 周波数ごとに合計する

	print('__ratio__')
	prop = df_cnt.sum() / len(df_loc)  # 月ごとの比率はdf_locで割り算
	print(prop)
	return prop


'''TEST
prop_date(df_loc)
'''


def plot_legend_setting(plot_element):
	'''データ12コまでなら凡例表示'''
	if plot_element <= 12:
		plt.legend(bbox_to_anchor=(0.5, -0.3), loc='center', borderaxespad=0, fontsize='small', ncol=3)
		plt.subplots_adjust(bottom=0.25)


def propdf(df, name):
	propdf = pd.DataFrame([])
	propdf[name] = prop_date(df)
	return propdf


def plot_propdf(propdf):
	month_ratio = propdf.sort_index(axis=1)
	month_ratio_index = [float(i[:-3]) for i in month_ratio.index]
	month_ratio.index = np.linspace(month_ratio_index[0], month_ratio_index[-1], 37)
	ax = month_ratio.plot.bar(title='Monthly Reception Ratio')
	ax.set_xlabel('Frequency')
	ax.set_ylabel('Ratio')
	plot_legend_setting(len(propdf.T.columns))
	return ax


def propdf_all(df):
	csvlist = [
	    ('20151111', '20151210'),
	    ('20151211', '20160110'),
	    ('20160111', '20160210'),
	    ('20160211', '20160310'),
	    ('20160311', '20160410'),
	    ('20160411', '20160510'),
	    ('20160511', '20160610'),
	    ('20160611', '20160710'),
	    ('20160711', '20160810')
	]
	propdf = pd.DataFrame([], columns=['temp'])
	for std, end in csvlist:
		df_loc = df.loc[std:end]  # std~endまでのインデックスを選択
		propdf['%s/%s' % (std[:4], std[4:6])] = prop_date(df_loc)
	del propdf['temp']
	print(propdf)

	month_ratio = propdf.T.sort_index(axis=1)
	# month_ratio.columns=param['country'][month_ratio.columns]
	ax = month_ratio.plot.bar(title='Monthly Reception Ratio', rot=30)
	ax.set_xlabel('Month')
	ax.set_ylabel('Ratio')
	plot_legend_setting(len(propdf.T.columns))
	# plt.show(ax)
	plt.savefig(param['view_out'] + 'allratio%s_%s.png' % (std, end))


# __MAIN__________________________

propdf = propdf(df, '2015/12/11-2016/01/10')
print(propdf)


ax = plot_propdf(propdf)
# plt.show(ax)
plt.savefig(param['view_out'] + 'allratio20151211_20160110.png')
