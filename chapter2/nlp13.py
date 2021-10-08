import pandas as pd
col1 = pd.read_csv('./col1.txt', index_col=0)
col2 = pd.read_csv('./col2.txt', index_col=0)

df = pd.concat([col1, col2], axis=1)
df.to_csv('col1-col2.txt', sep='\t')
