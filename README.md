# SAtraceView

SAtraceで収集したデータの分析
収集したデータを可視化し、分析を容易にします。




## 使い方

メインとなるファイルはSAtraceView.pyのPlotfitクラス。
これをipynb形式のファイル(SAtraceView.ipynb)で進めていく。

* 起動方法は「バッチを使用する」か「コマンドを打つ」
	* バッチで起動
		* SAtraceView.batをダブルクリック
	* コマンドを打つ
		* 好きなターミナル開く
		* `jupyter notebook SAtraceView.ipynb`と打つ
		> バッチの中身はこれが書いてあるだけ
* ipynbファイルに従い、Shift+Enterで進めていく




### ImportErrorが生じるとき、必要なモジュールをインポートする

以下のモジュールはanacondaに標準インストールされていない。
`conda install <モジュール名>`でインストールする。

* seaborn
























## SAtraceView ver1.0

__USAGE__

### jupyter notebookを起動

cmdなどで``jupyter notebook SAtraceView.ipynb`と打つ




### モジュールのインポート

最初のセルに`%load SAtraceView`と打ち込む
データのロードが完了すると
ロードしたデータフレームが表示される


### データの代入

`x=Plotfit(df)`


#### 解説

* データはソース内で指定したcsvから読み込まれ`df`というオブジェクトに格納されている。
* `x`などといったオブジェクトにクラスPlotfit(* データフレーム型の引数)を代入する。


### データの選択方法

```
dft=df.ix['20160211':'20160310',[0,4]]  # 選択したものをdftに代入する
x=Plotfit(dft)
```

* 2016年2月11日から2016年3月10日までの行
* 0番目、4番目の列
* 0,4...といった列番号ではなく、列名('xxxkHz')を指定しても良い。
> クォーテーションでくくること
* xというオブジェクトに`dft`を使用したクラスを代入する


__INTRODUCTION__

プロットする


__ACTION__

### クラスの外側

* モジュールをインポート
* パラメータをロード(param=...)
* 使用するファイルの指定(file = ...)
* データフレームをロード(df=...)

### クラス Plotfit

self.df : 引数にしたデータフレーム
self.title : データフレームの日時の最初と最後


__UPDATE1.0__

* count_agg追加
* README追加


__UPDATE0.1__
First commit


__TODO__
None













# データ形式
* ファイル名
	* タイムスタンプ`%Y%m%d_%H%M%S.txt`
	* 一日5分間隔
	* .txt形式


* ファイルの内容
	* 4列、1001行+ヘッダーフッター
	* サンプルデータはヘッダーフッター省略
	* 1列目はインデックス1~1000
	* 2,3,4列目はガウシアン分布に従う適当な値
	* x,y軸の順に1,2列目、1,3列目、1,4列目のペアで描くとガウシアン描く
	* 空白詰め


```ファイルの内容
<ヘッダー>
1       3.72665317e-06   3.91752688e-06   4.11776507e-06 
2    ...............
3
4
.
.
.
1001.......................
<フッター>
```





____________________________
# データの読み込み

## read_table.py

データの読み込みを行う

* 読み込んだデータをpandas.DataFrame形式にして返す関数:glob_dataframe()
* globしたリストを返す関数:dataglob()
+ globに時間がかかるので、イテレータを返すiglobにしようか



**ユーザーが指定するデータ選択の方法**
* 指定したディレクトリのリストから読み込む
* なければglobする>>>ユーザーにinput施す
	* 引数1つ
		* glob.glob(regex)
	* 引数2つ
		* pd.date_range(start,end)
	* 引数3つ
		* pd.date_range(start,end,freq='D||H')



```python:gob_dataframe(allfiles)
* 通常の使い方:
	* `glob_dataframe(dataglob())`としてpathからファイル名(フルパス)を読み込む

* 自分でリスト選択
	`glob_dataframe([path+'20160225_001023.txt',path+'20160225_000523.txt'])`みたいにしてリストを与えてやっても可

* 引数:
	* allfiles:ファイルのフルパス(リスト形式)

* 戻り値：
	* df:allfilesから取得した(pandas.DataFrame形式)
```

データフレームを返す。
dataglob()によってglobするファイル名をユーザーに入力を施す。
入力する値は正規表現で入力。

例えば

```
2016*   #2016年のデータ
201612*   #2016年12月のデータ
20161225*   #2016年12月25日のデータ
20161225_12*   #2016年12月25日12時のデータ
20161225_1[12]*   #2016年12月25日11時か12時のデータ
20161225_1?5*   #2016年12月25日10,11,12時50分台のデータ
```








### fitfile(fullpath)
fitされた1ファイルをデータフレームとして出力



### fitfile_all(path,regex)
fitされたすべてのファイル(dataglob()で取得)を行方向に追加してデータフレームを返す

引数:
	path:ファイルの詰まったパス
	regex:ファイル名(正規表現)

戻り値:
	df:path+regexで指定したすべてのファイルを行方向に連結したデータフレーム(pd.DataFrame形式)




## TODO read_table

* ~~glob系の関数の引数をregex一つにまとめる`glob(regex)`~~ 
> regexは独立していなきゃいけない
>> read_table.dataglob内でinput()できいてくるので。







# データの書き込み
## save_table

pd.DataFrameをcsvで保存する
データはまだ収集され続けるので、addできる形にする
以下のような形式のCSV

```dataframe.csv
2016-01-01 00:00:00,2016-01-01 00:05:00,2016-01-01 00:10:00,2016-01-01 00:15:00,
freq1,435  354,634,456,
freq2,465  283,665,488,
freq3,468  243,668,491,
   
```



read_frame:以前に作られたcsvファイルから読み込むcsv
write_frameこれから作るdataframe(read_table利用する)


### save_table TODO

indexの重複はpass



____________________________
# データの可視化



## plot2d.py

データ選択してグラフ化するするモジュール

やっていること

1. パラメータを読み込む

	以下のようにすることで`param`に辞書形式で`parameter.json`の内容が入る。
	以降`param['hoge']`として変数を扱う。
	なお、`load_parameter()`の引数にファイルのフルパスを与えると、そのファイルをjsonとして読み込む。

	```python
		import readtable as rt
		param = rt.load_parameter()
	```

2. データフレームを作成する
	`df=rt.glob_dataframe(rt.dataglob())`
3. df.plotでプロットする
	`df.plot(grid=True,ylim=(-120,0),legend=False)`
4. プロットの設定をする
5. プロットを別ウィンドウで表示
	`plot.show()`

### plot2d TODO

クラス化する

* `plot2d.Plot2d.allplot()`とかで呼び出せたらな。
* `plot2d.Plot2d.hoge()`のところをユーザーに選択させる
* 引数はdate_range()かな
* date_range indexを勉強しよう



### allmean(df)
dfを周波数ごとに平均化して、平均値のプロット








## plotfit.py
filefile_allによってcsvをインポート、pd.DataFrameとして
dfm=df.loc[std,end]でdfを区切る
stdはttttmmdd形式


月ごとに集計(カウント)
groupbyを使う

```
dfm=df.loc[std:end]
key=lambda x:x.date   #日ごとに集計
dfd=dfm.groupby(key).count()
```

















# plotgroup.py

## aggregate(path)

DataSource上のtxtデータから読み込んで周波数ごとに集計してpd.DataFrameで返す

**save_table.pyでcsvを作ってあるなら、aggregate_csvから読み込むほうが早い**

* 引数:
 * path: Data Source(string型)
* 戻り値:
 * sub: (pd.DataFrame型)









## aggregate_cdv(csv_fullpath, list_of_tuple)

dfを周波数ごとに集計
集計範囲はlist_of_tupleに記載
データフレームに取り出しやすいcsvデータから読み込む場合

* 引数:
 * path: Data Source
 * list_of_tuple: 集計の日付(yyyymmddの値が二つ入ったタプル形式のリスト)
* 戻り値:
 * sub: 値は集計値(pd.DataFrame形式)









## eachplot(series, freq_list)

plt.subplots()を使用してline plotとmarker plotを共存させる

1. pd.DataFrameから切り出したpd.Seriesなどを引数にする。
2. np.whereで特定のindexだけ値、それ以外はNanのpd.Seriesを作る。
3. subplots()で切り出したpd.Seriesをline plot
4. subplots()で作ったNan入りpd.Seriesをmarker plot
5. label, title limitの設定

* 引数:
 * series:
 * freq_list:注目周波数のリスト
* 戻り値:なし














____________________________

# plottxt.py

.txtから読み込み
平均化、最大値だけ取得など
pd.DataFrame.groupbyを使用してグラフ化。

## load_parameter(file='parameter.json'):

parameter.jsonからディレクトリやファイル情報、周波数などの情報をロードしてくる。





## spectrum(fullpath: str, columns: str) -> pd.core.frame.DataFrame:

txtデータからの読み込み
引数:
    fullpath: txtデータのフルパス(str型)
    columns: txtデータの何列目をデータとして使うか。
             デフォルトは'Mean': 0から始まっての2行目()(str型)
戻り値:
    se: txtのうちの１列(pandasシリーズ型)



## spectrum_table(regex: str, columns: str) -> pd.core.frame.DataFrame:

txtデータからの読み込み
regexのファイル名をglobで拾って、
横にマージして一つのデータフレームにして返す

引数:
    regex: globで拾う正規表現
戻り値:
    df: spectrumで返されたデータフレームを横つなぎにする





## noisefloor(df, axis: int=0):

1/4 medianをノイズフロアとし、各列に適用して返す
引数:
    df: 行が周波数、列が日時(データフレーム型)
    axis: 0 or 1.
        0: 列に適用(デフォルト)
        1: 行に適用
戻り値:
    df: ノイズフロア(データフレーム型)







## pltmod(title, columns):

plotの修飾

* ラベル名
* 凡例なし
* タイトル名
* 縦軸の最大/最小値(横軸はロードするときに決まってる)

plt.ylabe







## groupmean(regex: str, ffunc: str, gfunc: str, columns: str) -> pd.core.frame.DataFrame:
aggfuncでグループ化

引数:
    regex:日付を表したファイル名(str型　正規表現　%Y%m%d)
    ffunc: 集計の関数
        Mean: 平均値
        Max: 最大値
    gfunc: groupの仕方
        date: 日付
        month: 月
        hour: 時間
    columns: .txtから読み取る行数
        Min: 最小値
        Mean: 平均値
        Max: 最大値
戻り値:
    groupmean.T
    日にちで平均化したデータフレーム
    (データフレーム型)











# TEST plottxt.py

## TEST spectrum()
regex = '20161028_18*'
for fullpath in glob.iglob(param['in'] + regex):
    print(spectrum(fullpath))

## TEST spectrum_table()
regex = '20161028_18*'
df = spectrum_table(param['in'] + regex)
print(df)
print('読み込んだデータのカラム\n', df.columns)
print('読み込んだデータのインデックス\n', df.index)

## TEST spectrum_table()
regex = '20161028_18*'
df = spectrum_table(param['in'] + regex)
print(df)
print(noisefloor(df))
print(noisefloor(df, 1))

## TEST spectrum_table()
regex = '20161028_18*'
df = spectrum_table(param['in'] + regex)
df -= noisefloor(df)
print(df.T)

## TEST groupmean()
regex = '20161030'
df = groupmean(param['in'] + regex, ffunc='Max', gfunc='date', columns='Mean')
eachplot(df.ix[:, 0], freq_list)
pltmod(regex, 'Max')
plt.show()










____________________________
# TODO

## Feature

* all average csvも使用して各時間のスペクトラムも表示
* ノイズフロアも解析


## Bugs

None


# indent to space
できるところまでまとめてからmasterにgit flow release
master v3.0にしてから
`gf hotfix start indent`してindent直す


# groupby Timeframe 
// * 時間軸でグループ化
// * 月ごと、週ごと、日ごと、時間ごとで集計

## 何に役立つか
曜日はどこが多く出ているのか









# noise floor 
* nose floorをdfに加えてプロット
* 第2軸にline plot


## 何のため？
noise floorの影響でSN隠れていないかの確認







# heatmap plot
* seaborn(sns)が良いのか？
* pandasだけじゃできないか？

