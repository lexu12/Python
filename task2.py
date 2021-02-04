from abc import ABC, abstractmethod
import re


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        pass


class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Абстрактность'


class Costume(Clothes):

    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(400)
costume = Costume(55)
print(coat.consumption())
print(costume.consumption())
p = re.compile(r'\d+\.\d+')
coat1 = [float(i) for i in p.findall(coat.consumption())]
costume1 = [float(i) for i in p.findall(costume.consumption())]
clothes = coat1[0] + costume1[0]
print('Для пошива костюма и польто нужно:', clothes, 'ткани')

print(coat.abstract())
