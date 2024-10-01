import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import os

df=pd.read_csv('heart.csv')
df.isnull().sum()
from sklearn.model_selection import train_test_split
X = df.drop("target",axis=1).values
y = df["target"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)

from sklearn.metrics import accuracy_score
#Neural Network
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(20,activation='relu'))

model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(X_train,y_train,epochs=100)
pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,pred))
print('\n')
print(confusion_matrix(y_test,pred))

# Logistic Regression
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(X_train,y_train)

Y_pred_lr = lr.predict(X_test)
print(classification_report(y_test,Y_pred_lr))
print('\n')
print(confusion_matrix(y_test,Y_pred_lr))

