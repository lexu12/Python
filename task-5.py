prof = int(input('Введите сумму прибыли'))
expen = int(input('Введите сумму расходов'))
if prof > expen:
    print('Прибыль')
    profitab = prof - expen
    pers = int(input('Сколько сотрудников работает в фирме'))
    n = profitab/pers
    print("Прибыль на каждого сотрудника фирмы", n)
elif expen > prof:
    print('Убыток')
else:
    print("Вы вышли в 0")
