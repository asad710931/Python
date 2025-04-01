import pandas as pd
import numpy as np


data={
    'name':['asad','sabed','ali','kamal','selim'],
    'age':[np.nan,15,28,30,np.nan],
    'score':[90,np.nan,75,np.nan,65],
}
data1={
    'name':['john','bob','tom','dick',np.nan],
    'age':[np.nan,25,38,32,np.nan],
    'score':[88,np.nan,75,68,np.nan],
}

df=pd.DataFrame(data)
df1=pd.DataFrame(data1)


#drop missing values 
#dropna will remove all rows that are empty contain no value or null
#remove any raw with missing value

df=df.dropna()
df=df.dropna(axis=0)

#remove columns with missing values
df=df.dropna(axis=1)

#filling empty values
d1=df1.fillna(0)
print(df1)

df1['age'] = df1['age'].fillna(df1['age'].median())
print(f'Age changed \n {df1}')

#ffill will fill data base on what is before it (forword fill)
df1['score']=df1['score'].ffill()

#put all data to forword fill
df1=df1.fillna(method='ffill')
print(df1)

#bfil9l will fill data base on what is after it(backword fill)
df1['score']=df1['score'].bfill()

#put all data to backword fill
df1=df1.fillna(method='bfill')

print(df1)

#interpolate
# data interpolation what interpolate does is calulate two value before and after then fill empty fill will middle value
df['score']=df['score'].interpolate()
print(df)

#dropna will remove all rows that are empty contain no value or null


