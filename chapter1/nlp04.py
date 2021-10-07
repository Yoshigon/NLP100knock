text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. ' \
       'Arthur King Can.'
dic = {}
table = str.maketrans({
    ',': '',
    '.': ''
})
text = text.translate(table)
words = text.split()

for i in range(len(words)):
    if i in {0, 4, 5, 6, 7, 8, 14, 15, 18}:
        dic[words[i][0]] = i+1
    else:
        dic[words[i][:2]] = i+1

print(dic)
