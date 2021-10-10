import json

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
    ' ': ''
})

for line in uk_text:
    if line.startswith('{{基礎情報 国'):
        flag = 1
    if flag:
        if line.startswith('}}'):
            break
        else:
            tmp = line.translate(table)
            if '=' in tmp:
                idx = tmp.find('=')
                key = tmp[:idx]
                value = tmp[idx+1:]
                dic[key] = value
                print(key, value)
