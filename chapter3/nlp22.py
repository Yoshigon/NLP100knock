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
        uk_text = res[i][0]['text'].split()

for line in uk_text:
    if '[[Category' in line:
        idx = line.find('Category')
        print(line[idx+9:-2])
