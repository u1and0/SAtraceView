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

def spectrum(fullpath: str, columns: str ='Ave') -> pd.core.series.Series:
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
    columns_name = pd.to_datetime(fullpath[-19:-4], format='%Y%m%d_%H%M%S')
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


if __name__ == '__main__':
    regex = '20161028_18*'
    for fullpath in glob.iglob(param['in'] + regex):
        print(spectrum(fullpath))
