# __BUILT-IN MODULES_________________________
import pandas as pd
import numpy as np
from scipy import stats
import glob
from datetime import datetime
import json


# __READ PARAMETER__________________________
def load_parameter(file='parameter.json'):
    """
    parameter.jsonからディレクトリやファイル情報、周波数などの情報をロードしてくる。
    """
    with open(file, 'r') as f:
        param = json.load(f)
    return param


param = load_parameter()
path = param['in']
# freq_start = param['freq_start']
# freq_stop = param['freq_stop']
freq_center = param['freq_center']
freq_span = param['freq_span']
num = param['number_of_rows']


# __MAIN FUNCTIONS__________________________

def spectrum(fullpath: str, columns: str ='Ave') -> pd.core.frame.DataFrame:
    '''
    txtデータからの読み込み
    引数:
        fullpath: txtデータのフルパス(str型)
        columns: txtデータの何列目をデータとして使うか。
                 デフォルトは'Ave': 0から始まっての2行目()(str型)
    戻り値:
        se: txtのうちの１列(pandasシリーズ型)
    '''
    use = {'Min': 1, 'Ave': 2, 'Max': 3}  # .txtの何列目を使うか
    columns_name = pd.to_datetime(fullpath[-19:-4],
                                  format='%Y%m%d_%H%M%S')
    se = pd.read_table(fullpath,
                       names=[columns_name],
                       sep='\s+',
                       header=0,
                       skipfooter=1,
                       usecols=[use[columns]],
                       engine='python')
    # se['Frequency']=np.linspace(freq_start,freq_stop,len(se))
    # se.append(stats.scoreatpercentile(se, 25))  # fix at 1/4median
    index_start = freq_center - freq_span / 2
    index_end = freq_center + freq_span / 2
    se.index = np.linspace(index_start, index_end, len(se))
    return se


def spectrum_table(regex: str) -> pd.core.frame.DataFrame:
    """
    txtデータからの読み込み
    regexのファイル名をglobで拾って、
    横にマージして一つのデータフレームにして返す

    引数:
        regex: globで拾う正規表現
    戻り値:
        df: spectrumで返されたデータフレームを横つなぎにする
    """
    df = pd.DataFrame()
    for fullpath in glob.iglob(regex):
        se = spectrum(fullpath)
        df[se.columns] = se
    return df


def noisefloor(df):
    """
    1/4 medianをノイズフロアとし、各列に適用して返す
    引数:
        df: 行が周波数、列が日時(データフレーム型)
    戻り値:
        df: ノイズフロア(データフレーム型)
    """
    return df.apply(lambda x: stats.scoreatpercentile(x, 25))


if __name__ == '__main__':

    """
    # TEST spectrum()
    regex = '20161028_18*'
    for fullpath in glob.iglob(param['in'] + regex):
        print(spectrum(fullpath))
    """

    """
    # TEST spectrum_table()
    regex = '20161028_18*'
    df = spectrum_table(param['in'] + regex)
    print(df)
    print('読み込んだデータのカラム\n', df.columns)
    print('読み込んだデータのインデックス\n', df.index)
    """

    regex = '20161028_18*'
    df = spectrum_table(param['in'] + regex)
    print(df)
    print(noisefloor(df))
