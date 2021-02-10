from random import randint


def generate_numbers(count, minbound, maxbound):
    ret = []
    while len(ret) < count:
        new = randint(minbound, maxbound)
        if new not in ret:
            ret.append(new)
    return ret


class Keg:
    __num = None

    def __init__(self):
        self.__num = randint(1, 90)

    @property
    def num(self):
        return self.__num

    def __str__(self):
        return str(self.__num)


class Card:
    __data = None

    def __init__(self):
        uniques = generate_numbers(15, 1, 90)

        self.__data = []
        for i in range(0, 3):
            tmp = sorted(uniques[5 * i: 5 * (i + 1)])
            for j in range(0, 4):
                index = randint(0, len(tmp))
                tmp.insert(index, 0)
            self.__data += tmp

    def __str__(self):
        line = '--------------------------'
        ret = line + '\n'
        for index, num in enumerate(self.__data):
            if num == 0:
                ret += '  '
            elif num == -1:
                ret += ' -'
            elif num < 10:
                ret += f' {str(num)}'
            else:
                ret += str(num)

            if (index + 1) % 9 == 0:
                ret += '\n'
            else:
                ret += ' '

        return ret + line

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = -1

    def closed(self) -> bool:
        return set(self.__data) == {0, -1}


class Game:
    __usercard = None
    __compcard = None
    __kegs = []
    __gameover = False

    def __init__(self):
        self.__usercard = Card()
        self.__compcard = Card()
        self.__kegs = generate_numbers(90, 1, 90)

    def play_round(self) -> int:
        """
        :return:
        0 - game must go on
        1 - user wins
        2 - computer wins
        """

        keg = self.__kegs.pop()
        print(f'Новыйй бачонок: {keg} (осталось {len(self.__kegs)})')
        print(f'----- Ваша карточка ------\n{self.__usercard}')
        print(f'-- Карточка компьютера ---\n{self.__compcard}')

        useranswer = input('Зачеркнуть цифру? (y/n)').lower().strip()
        if useranswer == 'y' and not keg in self.__usercard or \
                useranswer != 'y' and keg in self.__usercard:
            return 2

        if keg in self.__usercard:
            self.__usercard.cross_num(keg)
            if self.__usercard.closed():
                return 1
        if keg in self.__compcard:
            self.__compcard.cross_num(keg)
            if self.__compcard.closed():
                return 2

        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('You win')
            break
        elif score == 2:
            print('You lose')
            break
