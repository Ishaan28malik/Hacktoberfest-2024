# Importing Pandas Library
import pandas as pd
"""
Making a dictionary of data with key-value pairs
, Keys are Column names written outside Square Brackets
and Values are the data written in lists
"""
dict={'Name':['Silvi','Shreya','Shaina','Shan'],'Roll No':[72,70,45,29],'Eng_Marks':[96,67,89,74],'Maths_Marks':[99,88,77,67]}
# Data Frame function/method in pandas is used to create a dataframe of given data(dictionary) 
df=pd.DataFrame(dict)
print(df)
