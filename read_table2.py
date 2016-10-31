# __BUILT-IN MODULES_________________________
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import glob
import json
from tqdm import tqdm


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

def spectrum(fullpath: str, columns: str ='Mean') -> pd.core.frame.DataFrame:
    '''
    txtデータからの読み込み
    引数:
        fullpath: txtデータのフルパス(str型)
        columns: txtデータの何列目をデータとして使うか。
                 デフォルトは'Mean': 0から始まっての2行目()(str型)
    戻り値:
        se: txtのうちの１列(pandasシリーズ型)
    '''
    use = {'Min': 1, 'Mean': 2, 'Max': 3}  # .txtの何列目を使うか
    columns_name = pd.to_datetime(fullpath[-19:-4],
                                  format='%Y%m%d_%H%M%S')
    se = pd.read_table(fullpath,
                       names=[columns_name],
                       sep='\s+',
                       header=0,
                       skipfooter=1,
                       usecols=[use[columns]],
                       engine='python')
    index_start = freq_center - freq_span / 2
    index_end = freq_center + freq_span / 2
    se.index = np.linspace(index_start, index_end, len(se))
    return se


def spectrum_table(regex: str, columns: str ='Mean') -> pd.core.frame.DataFrame:
    """
    txtデータからの読み込み
    regexのファイル名をglobで拾って、
    横にマージして一つのデータフレームにして返す

    引数:
        regex: globで拾う正規表現
    戻り値:
        df: spectrumで返されたデータフレームを横つなぎにする
    """
    print('.txt形式からのロード...少々時間がかかります。')
    df = pd.DataFrame()
    for fullpath in tqdm(glob.glob(regex)):
        se = spectrum(fullpath, columns)
        df[se.columns] = se
    return df


def noisefloor(df, axis: int=0):
    """
    1/4 medianをノイズフロアとし、各列に適用して返す
    引数:
        df: 行が周波数、列が日時(データフレーム型)
        axis: 0 or 1.
            0: 列に適用(デフォルト)
            1: 行に適用
    戻り値:
        df: ノイズフロア(データフレーム型)
    """
    return df.apply(lambda x: stats.scoreatpercentile(x, 25), axis)


def pltmod(title, columns):
    """
    plotの修飾

    * ラベル名
    * 凡例なし
    * タイトル名
    * 縦軸の最大/最小値(横軸はロードするときに決まってる)
    """
    plt.ylabel('S/N ratio [dBm]')
    con = pd.to_datetime(title, format='%Y%m%d')
    plt.title('S/N ratio %s in 1day %s' % (columns, con.isoformat()[:10]))
    plt.ylim(param['ylim_mean'])


def groupmean(regex: str, func: str, columns: str) -> pd.core.frame.DataFrame:
    """
    aggfuncでグループ化

    引数:
        regex:日付を表したファイル名(str型　正規表現　%Y%m%d)
        func: 日付 -> date
              月 -> month
              時間 -> hour
    戻り値:
        groupmean.T
        日にちで平均化したデータフレーム
        (データフレーム型)
    """
    df = spectrum_table(regex + '*', columns)  # globでファイル名マッチするものをデータフレーム化
    df -= noisefloor(df)  # powerからS/N比に変換
    groupfunc = 'lambda x: x.%s' % func
    groupmean = df.T.groupby(eval(groupfunc)).mean()  # 日にちで平均化したデータフレーム
    return groupmean.T


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

    """
    # TEST spectrum_table()
    regex = '20161028_18*'
    df = spectrum_table(param['in'] + regex)
    print(df)
    print(noisefloor(df))
    print(noisefloor(df, 1))
    """

    """
    # TEST
    regex = '20161028_18*'
    df = spectrum_table(param['in'] + regex)
    df -= noisefloor(df)
    print(df.T)
    """
