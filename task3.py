class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        self.get_full_name = self.name + ' ' + self.surname

    def get_total_income(self):
        self.get_total_income = self._income['wage'] + self._income['bonus']
        print(self.position, self.get_full_name, 'имеет доход', self.get_total_income, 'рублей')

r = Position(input('Введите имя\n',), input('Введите фамилию\n'), input('Введите должность\n'), input('Введите сумму оклада\n'), input('Введите сумму премии\n'))
r.get_full_name()
r.get_total_income()