with open('text_3.txt', encoding='utf-8') as f:
    list_1 = f.read()
list_2 = list_1.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре')
print(list_2)
with open('text_5.txt', 'w', encoding='utf-8') as f:
    for text1 in list_2:
        f.write(text1)
