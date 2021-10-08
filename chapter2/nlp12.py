import pandas as pd
df = pd.read_table('./popular-names.txt', header=None, names=['name', 'sex', 'number', 'year'])

col1 = df['name']
col2 = df['sex']

col1.to_csv('col1.txt', sep=",")
col2.to_csv('col2.txt', sep=",")
