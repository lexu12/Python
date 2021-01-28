text = []

while True:
    text.append(input('Введите текст'))
    print()
    if text.count('') == 1:
        break

with open('text_1.txt', 'w') as f:
    for text1 in text:
        f.write(text1 + '\n')

with open('text_1.txt', 'r') as f:
    text2 = f.read()
    print(text2)




