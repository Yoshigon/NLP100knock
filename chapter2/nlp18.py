import pandas as pd
df = pd.read_table('./popular-names.txt', header=None, names=['name', 'sex', 'number', 'year'])

df = df.sort_values('number')
print(df)
