class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.thickness = 5

    def method(self):
        self.method = self._width * self.thickness * self._length * self.weight
        print('Для покрытия', self._length, 'км дороги, необходимо', self.method, 'кг асфальта.')


r = Road((int(input('Введите длину дороги в километрах'))),
         int(input('Введите толщину дорожного покрытмя в сантиметрах')))
r.method()