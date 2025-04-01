import pandas as pd
#Making dataframe of six rows with 3 columns index of a,b,c
#df=pd.DataFrame([[0,1,2],[3,4,5],[6,7,8],[9,10,8],[6,2,5],[0,4,1]],columns=["A","B","C"],index=['a','b','c','a','b','c'])

df = pd.read_csv('https://raw.githubusercontent.com/dgrtwo/tidy-text-mining/master/data/juliasilge_tweets.csv')
# df =pd.read_excel('data.xlsx')

#print 5 rows from the top and 5 rows from the bottom
print(df)

head=df.head(6) #default or empty head() will show 5 rows from top but you can specify how many row you want row from top of list
print(head)
tail=df.tail(3) #default or empty head() will show 5 rows from bottom but you can specify how many row you want row from bottom of list
print(tail)


print(df.to_string())   #print entire dataFrame

pd_max_row = pd.options.display.max_rows
print(pd_max_row)
data_info=df.info()
print(data_info)

#prining specific list of rows with one column
print(df["id"])
#prining specific rows with multiple column
print(df[["id","text"]])

# new dataframe from data
newdf=df[["created_at","retweets","text"]]
#print(newdf.head())
# put conditions in python
newmdf=newdf[newdf["retweets"]>0]

print(newmdf.iloc[0])
print(newmdf.iloc[:,0])
print(newmdf.loc[0])
print(newmdf.loc[:,'retweets'])


