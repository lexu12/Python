with open('text_2.txt', encoding='utf-8') as f:
    list_1 = f.read().split()
print(list_1)
dict_1 = dict(zip(list_1[::2], list_1[1::2]))
print('Зарплаты больше чем 20000 у следующих сотрудников:')
for key in dict_1:
    if float(dict_1[key]) > 20000:
        print(key)
dict_2 = dict_1.values()
sum1 = 0
for i in dict_2:
    sum1 += float(i)
print('Средняя зарплата предприятия равна', sum1/len(dict_2))
