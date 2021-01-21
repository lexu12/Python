def devi_func(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'На 0 делить нельзя'


print(devi_func(num1=int(input('Введите первое число')), num2=int(input('Введите второе число'))))
