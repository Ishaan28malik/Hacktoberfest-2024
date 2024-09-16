#!/usr/bin/env python
# coding: utf-8

# In[1]:


from siuba import *
import pandas as pd

import matplotlib.pyplot as plt

import warnings
import plotnine
import numpy as np


# In[2]:


data = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-10-13/datasaurus.csv")


# In[3]:


data


# # Print data into csv

# In[21]:


data.to_csv(r'The Datasaurus data package.csv',index=False)


# In[4]:


data.columns

#data >> summarize(dataset =('dino'))


# In[20]:


df1=data['dataset'].value_counts()['dino']
#no of columns that have dino as dataset name 
df1


# In[6]:





# In[7]:


#building scatter plot with all the data
catagory = (data.groupby('dataset'))

#tuples=hash(tuple(np.array(catagory)))
plt.scatter(data['x'],data['y'])




# In[8]:


#plotting data with respectto colours toshapes it have
import plotly.express as px
import plotly.graph_objects as go


fig = px.scatter(data, x="x", y="y",color="dataset",
                     hover_name="dataset", log_x=True, size_max=30)
fig.show()


# # split a pandas DataFrame into multiple DataFrames by column value in Python

# In[25]:


#using group by grouped the data in the data fram to parts
grouped = data.groupby(data.dataset)

#get the grouped data that have datset as dino
dino1 = grouped.get_group("dino")
#dino1


# In[24]:


#plotted the data accodding o in dino1
fig = px.scatter(dino1, x="x", y="y",color="dataset",
                     hover_name="dataset", log_x=False, size_max=1)
fig.show()


# In[36]:


h_lines1 = grouped.get_group("h_lines")
v_lines1 = grouped.get_group("v_lines")
x_shape1 = grouped.get_group("x_shape")
star1 = grouped.get_group("star")
bullseye1 = grouped.get_group("bullseye")


# In[37]:


fig = px.scatter(star1, x="x", y="y",color="dataset",
                     hover_name="dataset", log_x=False, size_max=1)
fig.show()


# In[38]:


fig = px.scatter(h_lines1, x="x", y="y",color="dataset",
                     hover_name="dataset", log_x=False, size_max=1)
fig.show()


# In[39]:


fig = px.scatter(v_lines1, x="x", y="y",color="dataset",
                     hover_name="dataset", log_x=False, size_max=1)
fig.show()


# In[40]:


fig = px.scatter(x_shape1, x="x", y="y",color="dataset",
                     hover_name="dataset", log_x=False, size_max=1)
fig.show()


# In[41]:


fig = px.scatter(bullseye1, x="x", y="y",color="dataset",
                     hover_name="dataset", log_x=False, size_max=1)
fig.show()


# In[ ]:




