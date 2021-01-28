with open('text_1.txt') as f:
    list_1 = f.readlines()
print('В файле', len(list_1), 'строка(и)')
for i in range(0, len(list_1)):
    print('В', i+1, 'строке', len(list_1[i].split()), 'слова')
