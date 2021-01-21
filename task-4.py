def my_func(x, y):
    return x ** y


print(my_func(4, -2))



def my_func(x, y):
    result =1
    for i in range(abs(y)):
        result *= x
    return 1/result


print(my_func(4, -2))