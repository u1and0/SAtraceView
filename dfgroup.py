import pandas as pd
import read_table as rt
import simplejson
with open('parameter.json', 'r') as f:
    param = simplejson.load(f)


class Dgroup(df):
    """docstring for Dgroup"""

    def __init__(self, ]):
        self.path = param['out'] + 'CSV/allfit20151111_20160930.csv'
        self.df = rt.fitfile(path)
        self.start = pd.Timestamp('20160101')
        self.end = pd.Timestamp('20160201')
        self.freq = param['freq_choice']
        self.df = df.ix[start: end, :]

    def hour():
        return df.groupby(lambda x: x.hour).count()

    def hour():
        return df.groupby(lambda x: x.hour).count()




x = Dgroup(df)
x.hour()
