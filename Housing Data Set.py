#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np

import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use("fivethirtyeight")


import warnings
warnings.filterwarnings("ignore")


# In[2]:


data = pd.read_csv("Housing.csv")
data


# In[3]:


data.shape


# In[4]:


data.info()


# In[5]:


data.isna().sum()


# In[6]:


data["bedrooms"].value_counts()


# In[7]:


data["bathrooms"].value_counts()


# In[8]:


data["stories"].value_counts()


# In[9]:


data["furnishingstatus"].unique()


# In[11]:


data["parking"].value_counts()


# In[12]:


data[["mainroad","hotwaterheating","guestroom"]]


# In[21]:


data["area"].unique().max()


# In[24]:


data["price"].max()


# #### --------------------------------------------------------------------------------------------

# ## EDA

# In[30]:


data


# In[37]:


sns.countplot(x = "bedrooms" , data =data , hue = "guestroom")


# In[41]:


sns.relplot(y = "price" , x  = "area" ,hue = "basement" , data = data)


# In[46]:


x = data.corr()


# In[48]:


sns.heatmap(x , annot = True)


# In[52]:


sns.jointplot(x = "price" , y = "area" , kind = "reg",data = data)


# In[53]:


y = data["furnishingstatus"].value_counts()


# In[63]:


myexplode = [0.2, 0, 0, 0]


# In[70]:


plt.pie(y , labels = y.index   , autopct='%.0f%%',pctdistance=0.6,
    shadow= True,
    labeldistance=1.1,
    startangle=0,
    radius=1,
    counterclock=True,
    wedgeprops=None,
    textprops=None,
    center=(0,0),
    frame=False,
    rotatelabels=False,)
plt.show()


# In[ ]:





# In[73]:


sns.catplot(x ="bathrooms" , y = "area" , kind = "swarm" ,data = data)


# In[78]:


data.hist(figsize = (10,10))
plt.show()


# In[ ]:





# In[83]:


sns.catplot(x = "bedrooms" , y ="area" ,kind= "bar", data = data)


# In[ ]:




