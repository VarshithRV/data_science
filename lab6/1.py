import pandas as pd

raw_data = {'first_name': ['Sheldon', 'Raj', 'Leonard', 'Howard', 'Amy'],
            'last_name': ['Copper', 'Koothrappali', 'Hofstadter', 'Wolowitz', 'Fowler'],
            'age': [42, 38, 36, 41, 35],
            'Comedy_Score': [9, 7, 8, 8, 5],
            'Rating_Score': [25, 25, 49, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age',
                                       'Comedy_Score', 'Rating_Score'])
print(df)

#print(df['Comedy_Score'].where(df['Rating_Score'] < 50))
#print(df.shape())
#df.groupby('Outcome').size()
#df.info

#df2 = df['Comedy_Score'].where(df['Rating_Score'] < 50)

## columns
#print(df.columns)

## select column  -- returns data series 
#print(df['Comedy_Score'])
#print(df.Comedy_Score)

## select multiple columns -- returns data frame
#print(df[['first_name','Comedy_Score']])

## interger location
#print(df.iloc[[0,1]]) # print row
#print(df.iloc[[0,1],2]) ## print row with column

## label location
#print(df.loc[[0,1],'first_name'])

## update value
#x = df.at[0,'age']
#print(x)

## return the rows where the column matches the value
#x = df.loc[df['age'] == 42]
#print(x)
#print(type(x))

## return the index where the column matches the value
x = df[df['age']==42].index.values
print(x[0])

