import nlp05

char_x = 'paraparaparadise'
char_y = 'paragraph'

X = set(nlp05.char_ngram(char_x, 2))
Y = set(nlp05.char_ngram(char_y, 2))

print(f'和集合: {X | Y}')
print(f'積集合: {X & Y}')
print(f'差集合 (X-Y): {X - Y}')
print(f'差集合 (X-Y): {Y - X}')


def check_included(target_string: str, target_set: set, set_name: str):
    if target_string in target_set:
        print(f'{target_string}は{set_name}に含まれています')
    else:
        print(f'{target_string}は{set_name}に含まれていません')


check_included('se', X, 'X')
check_included('se', Y, 'Y')
