
# coding: utf-8

# In[2]:

import read_table as rt


# In[3]:

from datetime import datetime
pi = pd.read_csv(rt.param['view_out']+'average_SN.csv',
                 header=0,
                 index_col='DateTime',
                 date_parser=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))


# In[4]:

pi


# In[9]:

picklefile = 'average_SN.pkl'
pi.to_pickle(rt.param['view_out']+picklefile)


# In[10]:

pkl = pd.read_pickle(rt.param['view_out'] + picklefile);pkl


# In[7]:

hdffile = 'average_SN.h5'
pi.to_hdf(rt.param['view_out']+hdffile, 'mean')


# In[8]:

hdf = pd.read_hdf(rt.param['view_out']+hdffile); hdf


# In[ ]:



