import pandas as pd
import numpy as np


arr = np.arange(0,100).reshape(10,10)
# print(arr)
df = pd.DataFrame(data=arr,index=["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10"], columns=["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"])
# print(df) 
# print(df[['c1','c5']])
df['newC'] = df['c1'] + df['c2']
# print(df)
row = np.random.randint(1,100,11)
df.loc[len(row)] = row
# print(df)

# delete column from dataframe
# df.drop(['newC'], axis=1, inplace=True)
# print(df)

# delete row from dataframe
# df.drop(['r1'], axis=0, inplace=True)
# print(df)

# access row by label/name
# print(df.loc[['r5', 'r2']])

# access row by index
# print(df.iloc[[2,3]])


# grabbing a single element in dataframe
# print(df)
# print(df.loc['r2','c3'])

# grab a sub-set of dataframe
# result = df.loc[['r3','r5'], ['c1','c4']]
# print(result)

# print(df.loc[['r1','r3']])

# print(df > 5)

# print(df[df % 2 == 0])

# print(df.info())

print(df.describe())