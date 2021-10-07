def cipher(text: str):
    ret = ''
    for char in text:
        if char.islower():
            ret += chr(219 - ord(char))
        else:
            ret += char
    return ret


def decipher(text: str):
    ret = ''
    for char in text:
        if char.islower():
            ret += chr(219 - ord(char))
        else:
            ret += char
    return ret


print('暗号化:')
print(cipher('NLP is fun!'))
print('復号化:')
print(decipher(cipher('NLP is fun!')))
