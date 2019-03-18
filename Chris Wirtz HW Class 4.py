#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
path ='https://raw.githubusercontent.com/vikrambj2019/basic/master/Data/'
filename_read=os.path.join(path,"auto-mpg.csv")
df=pd.read_csv(filename_read,na_values=['NA','?'])


# In[13]:


df.to_csv('filename_read')


# In[15]:


pd.DataFrame(np.random.rand(20,5))


# In[17]:


pd.Series('filename_read')


# In[18]:


df.index = pd.date_range('1900/1/30',
periods=df.shape[0])


# In[20]:


df.head(10)


# In[21]:


df.tail(7)


# In[23]:


df.info()


# In[24]:


df.describe()


# In[28]:


df['mpg']


# In[29]:


df[['mpg', 'horsepower']]


# In[31]:


df.iloc[0,:]


# In[32]:


df.iloc[0,0]


# In[36]:


df.dropna()


# In[39]:


df.fillna('x')


# In[41]:


df.fillna(df.mean())


# In[42]:


df.iloc[0]


# In[45]:


df.replace([1,3],['one','three'])


# In[47]:


df.rename(columns={'mpg': 'miles per gallon'})


# In[50]:


df.set_index('name')


# In[55]:


df[df['cylinders'] > 7]


# In[57]:


df[(df['cylinders'] > 5) & (df['cylinders'] < 9)]


# In[63]:


df.sort_values(['horsepower','weight'],ascending=[True,False])


# In[64]:


df.groupby('cylinders')


# In[65]:


df.groupby('cylinders')['weight'].mean()


# In[67]:


df.pivot_table(index='cylinders',values=
['horsepower','weight'])


# In[68]:


df.groupby('cylinders').agg(np.mean)


# In[72]:


result=pd.DataFrame(df.groupby(['cylinders'])['horsepower'].aggregate('mean'))


# In[73]:


new_df=pd.merge(df,result, how='left',left_on=['cylinders'], right_on=['cylinders'])


# In[74]:


new_df.head()


# In[77]:


df.corr()


# In[78]:


df.count()


# In[79]:


df.max()


# In[80]:


df.std()


# In[119]:


df['horsepower']=df['horsepower'].fillna(df.groupby(['origin'])['cylinders'].transform('mean'))


# In[120]:


df.tail()


# In[103]:


table2=pd.DataFrame(df.groupby(['year'])['weight'].aggregate('std'))


# In[104]:


table2.head()


# In[113]:


df_2=pd.merge(df,table2, how='left',left_on=['year'], right_on=['year'])


# In[114]:


df_2.head()


# In[ ]:




