import pandas as pd
import numpy as np
dict={
    'name':["eee","uuu","ask","ram"],
    'marks':[32,45,99,100],
    'city':["Noida","delhi","singapore","baku"]

}
df=pd.DataFrame(dict)
print(df)
df.to_csv('marks.csv')
df.to_csv('marks_noind.csv',index=False)
df.head(1)
df.tail(1)
print(df.describe())
rd=pd.read_csv("marks.csv")
#print(rd)
#print(rd['name'][2])
rd['name'][3]="Mr. wimbot"
print(rd)
rd.to_csv('marks.csv')
rd.index=[1,2,3,4]
print(rd)
ser=pd.Series(np.random.rand(34))
print(ser)

print(df.T) #transpose
df.loc[0,2]=987 # 2 indicates column name
print(df)
df=df.drop(2,axis=1) # axis=0->row, axis=1->column
print(df)
#queries
print(df.loc[(df['marks']>50)])
print(df.iloc[0,2]) #columns will be traversed by index iterations irrespective of column names