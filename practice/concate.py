import pandas as pd 
#convert the lists to series and get the counts
first_list = pd.Series(
    ["a", "b", "c", "d", "e", "a", "b", "c", "a", "b","n"]
).value_counts()

second_list = pd.Series(
    ["a","b","c","d", "e", "e","d","c","e","q"]
).value_counts()

#get the counts as a dataframe
df=pd.concat([first_list,second_list],axis=1)
df.columns=['first','second']

# melt the data frame so it has a "tidy" data format
df=df.reset_index().melt(id_vars=['index'])
print(df)
