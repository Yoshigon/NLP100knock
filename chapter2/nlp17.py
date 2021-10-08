import pandas as pd
df = pd.read_table('./popular-names.txt', header=None, names=['name', 'sex', 'number', 'year'])

print(len(df['name'].unique()))
