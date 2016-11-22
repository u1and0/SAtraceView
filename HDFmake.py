
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


# In[5]:

pi.to_pickle(rt.param['view_out']+'average_SN.pkl')


# In[6]:

pkl = pd.read_pickle(rt.param['view_out']+'average_SN.dump');pkl


# In[ ]:

pi.to_hdf(rt.param['view_out']+'average_SN.h5', 'mean')


# In[ ]:

hdf = pd.read_hdf(rt.param['view_out']+'average_SN.h5'); hdf


# In[ ]:



