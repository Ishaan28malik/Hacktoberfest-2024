#!/usr/bin/env python
# coding: utf-8

# # Iris Dataset - SVM

# In[2]:


# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[13]:


#Importing dataset
data = pd.read_csv(r'C:\Users\Dell\Desktop\Machine Learning\Sample Dataset\IRIS.csv')
data.shape


# In[14]:


data.head(5)


# In[15]:


#Check if any null value is present
data.isnull().values.any()


# In[16]:


#Correlation
import seaborn as sns
import matplotlib.pyplot as plt
cormat = data.corr()
top_corr_features = cormat.index
plt.figure(figsize=(20,20))

#Plotting heat map
g = sns.heatmap(data[top_corr_features].corr(), annot = True)


# In[17]:


data.corr()


# In[18]:


#Splitting Training and Testing datset
from sklearn.model_selection import train_test_split
features_column = [ 'sepal_length', 'sepal_width', 'petal_length', 'petal_width' ]
prediction_class = ['species']

X = data[features_column].values
Y = data[prediction_class].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.30, random_state = 10)
(X, Y)


# In[19]:


X_train.shape


# In[20]:


X_test.shape


# In[21]:


Y_train.shape


# In[22]:


Y_test.shape


# In[23]:


#Checking null values
print("Total no of rows : {0}".format(len(data)))
print("Number of missing rows in sepal_length : {0}" .format(len(data.loc[data['sepal_length'] ==0 ])))
print("Number of missing rows in sepal_width : {0}" .format(len(data.loc[data['sepal_width'] ==0 ])))
print("Number of missing rows in petal_length : {0}" .format(len(data.loc[data['petal_length'] ==0 ])))
print("Number of missing rows in petal_width : {0}" .format(len(data.loc[data['petal_width'] ==0 ])))


# In[24]:


#Applying SVM to model - Most Accurate
from sklearn import svm
model = svm.SVC()
model.fit(X_train, Y_train.ravel())
#Predicting Accuracy of model
predict = model.predict(X_test)
from sklearn import metrics
print("Accuracy of SVM = {0:.3f}".format(metrics.accuracy_score(Y_test, predict)))


# In[ ]:





# In[ ]:




