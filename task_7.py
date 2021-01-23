import math
my_list = []
def yield_func(n):
    z = 1
    for el in range(1, n + 1):
        z = math.factorial(el)
        yield z


n = int(input("Укажите факториал какого числа Вы хотели бы узнать?"))
fact = yield_func()
for el in fact:
    my_list.append(el)
print(my_list[len(my_list) - 1])