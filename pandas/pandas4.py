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

#Combine mulitple dataframe into one

combined=pd.concat([df,df1]) #default axis=0
combined=pd.concat([df,df1],axis=1)
print(combined)

#marged into one
marged=pd.merge(df, df1, on="age")
marged=pd.merge(df, df1, how="left", on="age")
marged=pd.merge(df, df1, how="inner", on="age")
print(marged)

#join dataframes
joined=df.join(df1, how="outer",lsuffix='A',rsuffix='B')

print(joined)