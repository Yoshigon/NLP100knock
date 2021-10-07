text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
table = str.maketrans({
    ',': '',
    '.': ''
})
text = text.translate(table)
words = text.split()

words_len = []
for w in words:
    words_len.append(len(w))

print(words_len)
