# SAtraceView

SAtraceで収集したデータの分析
収集したデータを化しかし、分析を容易にします。


## 使い方
方法は「バッチを使用する」か「コマンドを打つ」

* バッチで起動
	* SAtraceView.batをダブルクリック
* コマンドを打つ
	* 好きなターミナル開く
	* `python plot2d.py`と打つ
	> バッチの中身はこれが書いてあるだけ



## データ形式
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



# データの読み込み

## read_table.py

データの読み込みを行う
主な関数

* あらかじめグラフ化したいデータのフルパスを格納しておくfililistをリストとして読み込み:read_filelist(filelist_path)
* globしたリストを返す関数:dataglob(path, regex=False)
* 読み込んだデータをpandas.DataFrame形式にして返す関数:glob_dataframe(allfiles)

**ユーザーが指定するデータ選択の方法** は関数dataglob()の説明を読むこと。



### onefile(fullpath):
Read single file
Store dataframe


### manyfile(start, stop):
Read multiple files
Store dataframe


### spectrum(fullpath, columns='Ave'):
Make dataframe as ploting spectrums.
indexをnp.linspaceにできないかなぁ




### python:filelist_header()
fililist.txtの説明文を返す





### read_filelist()
globするときの手順

1. 引数0個
	1.1. ユーザーに入力させる
	1.2. `input()`
		1.2.1. なおも0個の場合、`filelist.txt`から読み込む
2. 引数1個
	2.1. 正規表現として受け取り、globに渡す
	2.2. `glob. glob()`
3. 引数2個
	3.1. それぞれstringとして受け取り、pd.date_range()の引数に使う
	3.2. `pd.date_range(start,end)`
4. 引数3個
	4.1. それぞれstringとして受け取り、pd.date_range()の引数に使う
	4.2. 3つめの引数はfreq(D or H)
	4.3. `pd.date_range(start,end,freq='H')`
5. 1.2.1以外の結果は`filelist.txt`に上書き
	5.1. 次回に1.2.1のようにした場合、結果を再利用できる。
	5.2. もしくは自作のリストを使用できる。



### dataglob(path, regex=False):
* 引数:
	* path:データソースのディレクトリ
	* regex: ファイル名の正規表現
		* 空の入力=>コンソールからユーザにインプット施す
* 戻り値:
	* path内のファイルのフルパス
* 内容:
	* 指定したディレクトリ(path)から正規表現(regex)をもとにglobして、ファイルのフルパスを返す
	* regexがない(False, Noneなどの空の入力)とき、ユーザーにinput求める
		* input 0個(求められたinputが尚も空, Noneの時)
			* fililist.txtに登録されたファイルのフルパスを返す
		* input 1個(path内の正規表現を入力する)
			* glob.glob(regex)で返されたフルパスをfilelistに書き込み
			* fililist.txtに登録されたファイルのフルパスを返す
まだここまでしかできていない
_________________________
		* input 2個(pandas.date_rangeの引数を入力する'start','end')
			* pd.date_range(start,end)
			* ↑で生成された値を正規表現としてglobし、
			* 結果をfilelistに書き込み
			* fililist.txtに登録されたファイルのフルパスを返す
		* input 3個(pandas.date_rangeの引数を入力する'start','end','D' or 'H')
			* pd.date_range(start,end,freq='D||H')
			* ↑で生成された値を正規表現としてglobし、
			* 結果をfilelistに書き込み
			* fililist.txtに登録されたファイルのフルパスを返す




### glob_dataframe(allfiles)
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















## plot2d.py

データ選択してグラフ化するするモジュール

やっていること

1. パラメータを読み込む
	`param.param()`
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
