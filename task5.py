class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(' ', self.title, 'пишет')


class Pensil(Stationery):
    def draw(self):
        print(' ', self.title, 'рисует')


class Handle(Stationery):
    def draw(self):
        print(' ', self.title, 'разукрашивает')


p = Pen('Ручка')
p1 = Pensil('Карандаш')
h = Handle('Маркер')
p.draw()
p1.draw()
h.draw()
