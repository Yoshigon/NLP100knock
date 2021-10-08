import pandas as pd
df = pd.read_table('./popular-names.txt', header=None, names=['name', 'sex', 'number', 'year'])

N = int(input())
dfs = []
num_col = len(df) // N
for i in range(N-1):
    dfs.append(df[num_col * i: num_col * (i+1)])
dfs.append(df[num_col * (N-1):])
