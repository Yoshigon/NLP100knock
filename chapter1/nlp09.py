import random


def typoglycemia(text: str):
    ret = []
    words = text.split()
    for w in words:
        if len(w) < 5:
            ret.append(w)
        else:
            tmp = list(w[1:-1])
            random.shuffle(tmp)
            body = ''.join(tmp)
            ret.append(w[0] + body + w[-1])
    return ret


sample_text = 'I couldn’t believe that I could actually understand what I was reading : ' \
       'the phenomenal power of the human mind .'

print(' '.join(typoglycemia(sample_text)))
