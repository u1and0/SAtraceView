
# coding: utf-8

# In[ ]:




# In[26]:

get_ipython().magic('matplotlib inline')
import plottxt as pt


# In[9]:

path = pt.param['in']; path


# In[4]:

file = '20151125_004904.txt'


# In[20]:

pt.spectrum(path + file).plot()


# # 複数ファイルの処理
# ファイルを()の中にくくって複数指定する。
# 

# In[19]:

files = ('20151125_002404.txt',
        '20151214_225858.txt',
        '20161013_091345.txt')


# pythonの内包表記使ってpathを足したフルパスのリストを作成し、
# それを`spectrum_many`へ渡す。

# In[21]:

pt.spectrum_many([path + i for i in files]).plot()


# In[24]:

df.noisefloor()


# In[22]:

df = pt.spectrum_many([path + i for i in files])
dff = df - df.noisefloor()
dff.plot()


# In[23]:

dff.max(axis=1).plot()


# In[ ]:



