class Car:
    def __init__(self, name, speed, color, is_police=True):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(self.color, self.name, 'поехала')

    def stop(self):
        print(self.color, self.name, 'остановилась')

    def turn(self, derection):
        print(self.color, self.name, 'повернула на', derection)

    def show_speed(self):
        print('Скорость', self.color, self.name, self.speed, 'км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(self.color, self.name, 'привысила допустимую скорость на', self.speed - 60, 'км/ч')
        else:
            print(self.color, self.name, 'едит с допустимой скоростью')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(self.color, self.name, 'привысил допустимую скорость на', self.speed - 40, 'км/ч')
        else:
            print(self.color, self.name, 'едит с допустимой скоростью')


class PoliceCar(Car):
    pass


town = TownCar('Audi', 70, 'черная', False)
print(town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

sport = SportCar('AudiRS', 170, 'красная', False)
print(sport.go(), sport.show_speed(), sport.turn('лево'), sport.stop())

work = WorkCar('WAZ', 40, 'зеленый', False)
print(work.go(), work.show_speed(), work.turn('право'), work.stop())

police = PoliceCar('Kia', 100, 'желтый', True)
print(police.go(), police.show_speed(), police.turn('лево'), police.stop())