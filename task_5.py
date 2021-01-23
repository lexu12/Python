from functools import reduce


def my_func(num1, num2):
    return num1 * num2


print(reduce(my_func, [i for i in range(100, 1001) if i % 2 == 0]))
