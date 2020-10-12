
Markdown
# This is a model where we will predict a football players's value with some given features from the dataset with the use of Artificial Neural Network
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
# IMPORTING AND CHECKING THE DATA FRAMES
df=pd.read_csv('football data.csv',index_col=0)
df.head()
#This is important to check how many unique features are there in you data input (here in form of descending order)
df.nunique().sort_values(ascending=False)
#CHECKING FOR ANY MISSING DATA . For training a model there should  not be any feature left behind
df.isnull().sum()
#FILLING THE MISSING VALUES WITH THEIR MEAN MOR MEDIANS
df['Weight']
# Using important features and filling their missing values either by their mean or median (as per model's convenience)
df['ShortPassing'].fillna(df['ShortPassing'].mean(), inplace = True)
df['Volleys'].fillna(df['Volleys'].mean(), inplace = True)
df['Dribbling'].fillna(df['Dribbling'].mean(), inplace = True)
df['Curve'].fillna(df['Curve'].mean(), inplace = True)
df['FKAccuracy'].fillna(df['FKAccuracy'], inplace = True)
df['LongPassing'].fillna(df['LongPassing'].mean(), inplace = True)
df['BallControl'].fillna(df['BallControl'].mean(), inplace = True)
df['HeadingAccuracy'].fillna(df['HeadingAccuracy'].mean(), inplace = True)
df['Finishing'].fillna(df['Finishing'].mean(), inplace = True)
df['Crossing'].fillna(df['Crossing'].mean(), inplace = True)
df['Weight'].fillna('165lbs', inplace = True)
df['Contract Valid Until'].fillna(2019, inplace = True)
df['Height'].fillna("5'11", inplace = True)
df['Loaned From'].fillna('None', inplace = True)
df['Joined'].fillna('Jul 1, 2018', inplace = True)
df['Jersey Number'].fillna(8, inplace = True)
df['Body Type'].fillna('Normal', inplace = True)
df['Position'].fillna('ST', inplace = True)
df['Club'].fillna('No Club', inplace = True)
df['Work Rate'].fillna('Medium/ Medium', inplace = True)
df['Skill Moves'].fillna(df['Skill Moves'].median(), inplace = True)
df['Weak Foot'].fillna(3, inplace = True)
df['Preferred Foot'].fillna('Right', inplace = True)
df['International Reputation'].fillna(1, inplace = True)
df['Wage'].fillna('€200K', inplace = True)

df.isnull().nunique().sum()
df.fillna(0, inplace = True)
#REPLACING THE STRING TO REQUIRED NUMERICAL VALUE FOR GETTING USE OF MORE COLUMNS 

df['Weight'].describe()

def extract_value_from(value):
  out = value.replace('lbs', '')
  return float(out)

df['Weight'] = df['Weight'].apply(lambda x : extract_value_from(x))

df['Weight'].head()

def extract_value_from(Value):
    out = Value.replace('€', '')
    if 'M' in out:
        out = float(out.replace('M', ''))*1000000
    elif 'K' in Value:
        out = float(out.replace('K', ''))*1000
    return float(out)
    
df['Value'] = df['Value'].apply(lambda x: extract_value_from(x))
df['Wage'] = df['Wage'].apply(lambda x: extract_value_from(x))


df['Wage'].head()

# SELECTING IMPORTANT COLUMNS OF DATASET

selected_columns = ['Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value',
                    'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot',
                    'Skill Moves', 'Work Rate', 'Body Type', 'Position', 'Height', 'Weight',
                    'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                    'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
                    'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
                    'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                    'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                    'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                    'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']
df_selected = pd.DataFrame(df, columns = selected_columns)
df_selected.columns
# CHECKING FOR SIMILAR CORELATED COLUMNS 

plt.figure(figsize=(16,10))
sns.heatmap(df_selected.corr(),cmap='coolwarm')
plt.ylim(10, 0)

sns.scatterplot(x='Value',y='Wage',data=df_selected)
# SOME MORE FEATURE ENGINEERING WITH HIGHLY CORRELATED COLUMNS CONVERTING THEM TO FLOAT DATA TYPE
df_selected['Club'].head()
sns.scatterplot(x='Age',y='Wage',data=df_selected)
# Position was highly corelated with value so replacing their string values to numerical so that they can be used in training model
forward = ["ST", "LW", "RW", "LF", "RF", "RS","LS", "CF"]
midfielder = ["CM","RCM","LCM", "CDM","RDM","LDM", "CAM", "LAM", "RAM", "RM", "LM"]
defender = ["CB", "RCB", "LCB", "LWB", "RWB", "LB", "RB"]

df_selected.loc[df["Position"] == "GK", "Position"] = 0.0
df_selected.loc[df["Position"].isin(defender), "Position"] = 1.0
df_selected.loc[df["Position"].isin(midfielder), "Position"] = 2.0
df_selected.loc[df["Position"].isin(forward), "Position"] = 3.0

sns.distplot(df_selected['Position'],bins=50,kde=False)
df_selected["Position"].value_counts()
sns.boxplot(x='Position',data=df_selected,y='Wage')
def hconversion(value):
        height = value.split("'")
        feet=int(height[0])
        inches=int(height[1])
        metre=((12*feet)+inches)*0.0254
        return metre
df_selected['Height'] = df_selected['Height'].apply(lambda x : hconversion(x))      
plt.figure(figsize=(14,10))
sns.boxplot(x='Position',y='Value',data=df_selected,hue='Preferred Foot')
#ADJUSTING SOME MORE COLUMNS
def extract_value_from(Value):
    Value=str(Value)
    out = Value.replace('€', '')
    if 'M' in out:
        out = float(out.replace('M', ''))*1000000
    elif 'K' in Value:
        out = float(out.replace('K', ''))*1000
    return float(out)
df_selected['Release Clause'] = df_selected['Release Clause'].apply(lambda x: extract_value_from(x))
sns.countplot(df_selected['Preferred Foot'])
foot=pd.get_dummies(df_selected['Preferred Foot'],drop_first=True)
df_selected=pd.concat([df_selected,foot],axis=1)
df_selected=df_selected.drop(['Preferred Foot','Name','Nationality','Club'],axis=1)
# CHECKING AND REMOVING THE PLAYERS WITH 0 VALUES
df_selected['Value'].sort_values(ascending=True)
c=df_selected[df_selected['Value']>0]
c['Value'].mean()
# TRAINING AND TESTING THE MODEL
c=c.drop(['Body Type','Work Rate'],axis=1)
X=c.drop('Value',axis=1).values
y=c['Value'].values
from sklearn.model_selection import train_test_split
 X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33)
 
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
# Importing neural network models from tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# Constructing the neural network 6 layers and 1 output layer(for value)
6 layers is because of data size (more datasize=more neural layers)
model=Sequential()
model.add(Dense(300,activation='relu'))
model.add(Dense(150,activation='relu'))
model.add(Dense(80,activation='relu'))
model.add(Dense(50,activation='relu'))
model.add(Dense(20,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='softplus'))
        
model.compile(optimizer='adam',loss= 'msle')

model.fit(x=X_train, 
          y=y_train, 
          epochs=400,
          batch_size=128,
          validation_data=(X_test, y_test), 
          )
losses=pd.DataFrame(model.history.history)
losses.plot()          


    

