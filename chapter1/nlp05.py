def word_ngram(text: str, n: int):
    table = str.maketrans({
        ',': '',
        '.': ''
    })
    text = text.translate(table)
    words = text.split()
    ret = []
    for i in range(len(words)-n+1):
        ret.append(words[i] + ' ' + words[i+1])
    return ret


def char_ngram(text: str, n: int):
    table = str.maketrans({
        ',': '',
        '.': '',
        ' ': ''
    })
    text = text.translate(table)
    ret = []
    for i in range(len(text)-n+1):
        ret.append(text[i]+text[i+1])
    return ret


if __name__ == '__main__':
    print('単語n-gram')
    print(word_ngram('I am an NLPer', 2))
    print('文字n-gram')
    print(char_ngram('I am an NLPer', 2))
