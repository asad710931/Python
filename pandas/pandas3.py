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

#renaming columns
df=df.rename(columns={'name':'student','score':'marks'})
print(f"Rename columns:\n{df}")

#change datatype 
df=df.fillna(0.0)
df['age']=df['age'].astype('int')
print(f"Change datatype :\n{df}")

df['age']=df['age'].astype('float')
print(f"Change datatype :\n{df}")


#change data raw to datetime
df['marks']=pd.to_datetime(df['marks'])
print(f'================\n{df}')
