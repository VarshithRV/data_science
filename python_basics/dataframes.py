import pandas as pd
'''
class functions :
- columns - df.columns - returns the columns
- df[<column name>] - returns the column values, can select multiple columns
- iloc, df.iloc[[list_of_rows_index],[list_of_column_index]] -returns
a dataframe containing the following rows and columns
- loc, df.loc[listofrowsindex,listofcolumnkeys]
- df.at[row_index,column_key] returns the value of the cells
- index.values : x = df[df[<column>]==certainvalue].index.values returns a
list of index values
- df = df.drop(index) -- drops a row
- df = df.append(df2,ignore_index = True) -- appends a dataframe
'''

# everything about dataframes ;
d = {"column1":['value1'],"column2":['value2']}
df = pd.DataFrame(d)
df.to_csv('file1.csv',index = False)
print(df,"\n",type(df))


