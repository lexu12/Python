import sys
rate, prize = sys.argv[1:]
salary = ((int(input('Введите количество отработанных часов')) * int(rate)) + int(prize))
print('Ваша заработная плата', salary, 'рублей')