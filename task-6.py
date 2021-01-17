n = 1
catalog = []
while True:
    a = input('Введите название товара')
    try:
        b = int(input('Введите цену товара цифрами'))
    except ValueError:
        print('Введино не число')
        b = int(input('Введите цену товара цифрами'))
    try:
        c = int(input('Введите количество товара цифрами'))
    except ValueError:
        print('Введино не число')
        c = int(input('Введите количество товара цифрами'))
    e = input('Введите единицу измерения')
    f = input('Нажмите "Enter" если хотите продолжить или введите "конец" если хотите закончить')
    d = dict(название=a, цена=b, количество=c, ед=e)
    catalog1 = [n, d]
    n += 1
    h = tuple(catalog1)
    catalog.append(h)
    if f == "конец":
        break
print(list(catalog))
t = [x[1] for x in catalog]
p = []
for h in t:
    y = h.get('название')
    p.append(y)
L = []
for h in t:
    y = h.get('цена')
    L.append(y)
q = []
for h in t:
    y = h.get('количество')
    q.append(y)
r = []
for h in t:
    y = h.get('ед')
    r.append(y)
my_dict = {'название': p, 'цена': L, 'количество': q, 'ед': r}
print(my_dict)