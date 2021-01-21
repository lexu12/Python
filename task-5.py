result = 0
try:
    while True:
        for i in map(int, input(' Введите числа через пробел или * для выхода из программы').split()):
            result += int(i)
        print(f'Сумма чисел равна {result}')
except ValueError:
    print(f' Сумма чисел равна {result}')


