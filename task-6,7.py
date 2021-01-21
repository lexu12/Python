def int_func(word):
    new_word = [word[0].title() + word[1:]]
    return ''.join(new_word)


words = input('Введите слова через пробел').split()
list_words = []
for word in words:
    list_words.append(int_func(word))
print(' '.join(list_words))