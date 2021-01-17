my_list = input('Введите список элементов через пробел')
my_list2 = my_list.split()
m = my_list2
k=0
for i in range((len(m)//2)):
    m[k], m[k + 1] = m[k + 1], m[k]
    k = k + 2
print(m)