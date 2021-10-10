import json
import re

decoder = json.JSONDecoder()
res = []
with open('jawiki-country.json', 'r') as f:
    line = f.readline()
    while line:
        res.append(decoder.raw_decode(line))
        line = f.readline()

uk_text = []
for i in range(len(res)):
    if res[i][0]['title'] == 'イギリス':
        uk_text = res[i][0]['text'].split(sep='\n')

for line in uk_text:
    if re.match('\[\[ファイル:.*\|', line):
        tmp = re.search('\[\[ファイル:.*?\|', line).group()  # 非貪欲マッチ
        print(tmp[7:-1])
