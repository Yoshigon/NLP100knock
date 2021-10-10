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

flag = 0
dic = {}
table = str.maketrans({
    '|': '',
    ' ': '',
    '\'''': '',
    '[': '',
    ']': ''
})

for line in uk_text:
    if line.startswith('{{基礎情報 国'):
        flag = 1
    if flag:
        if line.startswith('}}'):
            break
        if '=' not in line:
            continue
        else:
            tmp = line.translate(table)
            tmp = re.sub(r'\<.*\>', '', tmp)
            tmp = re.sub(r'\{\{lang..', '', tmp)
            tmp = re.sub(r'\{\{0', '', tmp)
            tmp = re.sub(r'\{\{enicon', '', tmp)
            tmp = re.sub(r'\{\{centerファイル:', '', tmp)
            tmp = re.sub(r'\{\{仮', '', tmp)
            tmp = re.sub(r':en:', '', tmp)
            tmp = re.sub(r'\}\}', '', tmp)
            idx = tmp.find('=')
            key = tmp[:idx]
            value = tmp[idx + 1:]
            dic[key] = value
            print(key, value)
