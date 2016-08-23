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




## read_table.py

データの読み込みを行う

* 読み込んだデータをpandas.DataFrame形式にして返す関数:glob_dataframe()
* globしたリストを返す関数:dataglob()



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

