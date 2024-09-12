# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:43:26 2020

@author: Parikshit
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:26:23 2019

@author: parik
"""

import numpy as np
from sklearn import preprocessing , model_selection , naive_bayes
import pandas as pd
from sklearn.metrics import accuracy_score

df=pd.read_csv('cancer_data.txt')
df.replace('?',-99999,inplace=True)
df.drop('id',1,inplace=True)

x=np.array(df.drop(['class'],1))
y=np.array(df['class'])

x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.2)

clf=naive_bayes.GaussianNB()
clf.fit(x_train,y_train)
pre=clf.predict(x_test)

acc=accuracy_score(pre,y_test)
print(pre)
print(acc)