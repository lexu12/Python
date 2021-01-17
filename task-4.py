my_list = input('Введите список элементов через пробел')
my_list2 = my_list.split()
for i, a in enumerate(my_list2, 1):
    b = a[:10]
    print(i, b)