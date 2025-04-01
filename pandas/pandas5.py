import pandas as pd
import numpy as np



#========Using Grouping data========
# reading data from local csv files
irisDf = pd.read_csv('iris.csv')


#grouping data by species names
grouped=irisDf.groupby('species')

#reading data with loops 
for group_names,group in grouped:
    print(group_names)
    print(group)

#grouping data by column category and getting specific value from numurical column
group_mean=irisDf.groupby('species')['sepal_length'].mean()
group_sum=irisDf.groupby('species')['sepal_length'].sum()
group_max=irisDf.groupby('species')['sepal_length'].max()

print(f'Mean : {group_mean}\nSum : {group_sum}\nMax : {group_max}')


#grouping data by column category and getting multitple value from numurical column
group_agg=irisDf.groupby('species').agg({'sepal_length':['mean','max','min']})
print(group_agg)


#using pivot_table
pivot=irisDf.pivot_table(values="sepal_length",index="species",aggfunc="min")
print(pivot)

#using custom aggregations
def myFun1(x):
    return x.max()
aggre1=irisDf.groupby('species')['sepal_length'].agg(myFun1)

print(f'Custom aggregations-2 : {aggre1}')
def myFun(x):
    return x.max()-2
aggre=irisDf.groupby('species')['sepal_length'].agg(myFun)

print(f'Custom aggregations : {aggre}')