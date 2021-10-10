import json
decoder = json.JSONDecoder()
res = []
with open('jawiki-country.json', 'r') as f:
    line = f.readline()
    while line:
        res.append(decoder.raw_decode(line))
        line = f.readline()

for i in range(len(res)):
    if res[i][0]['title'] == 'イギリス':
        print(res[i][0]['text'])
