numbers = [input('Введите числа через пробел')]
with open('text_4.txt', 'w') as f:
    for numbers_1 in numbers:
        f.write(numbers_1)
with open('text_4.txt') as f:
    list_1 = f.read().split()
    list_2 = list(list_1)
    sum_1 = 0
    for i in list_2:
        sum_1 += int(i)
print(sum_1)
