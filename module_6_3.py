class Animal:  # класс описывающий животных
    live = True  # живёт
    sound = None  # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        """Меняет соответствующие координаты в _cords на dx, dy, dz в том же порядке, где множителем
        будет являться speed. Если при попытке изменения координаты z в _cords значение будет меньше 0,
        то выводить сообщение "It s too deep, i can't dive :(", при этом изменения не вносятся"""
        self._cords[0] = self.speed * dx
        self._cords[1] = self.speed * dy
        if dz * self.speed >= 0:
            self._cords[2] = self.speed * dz
        elif dz * self.speed < 0:
            print("It's too deep, i can't dive :(")

    def get_cords(self):  # выводит координаты
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):  # выводит строку со звуком sound
        print(f'{self.sound}')


class Bird(Animal):  # класс описывающий птиц.
    beak = True  # наличие клюва

    def lay_eggs(self, number):
        # выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
        print(f'Here are(is) {number} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        """Где dz изменение координаты z в _cords. Должен изменять в отрицательную сторону координату z уменьшенную
в 2 раза с учётом скорости. С каким бы знаком не был передан параметр dz, внутри метода используйте
         его значение по модулю(функция abs)."""
        delta_z = abs(dz * self.speed) / 2
        new_z = self._cords[2] - delta_z
        self._cords[2] = max(0, new_z)


class PoisonousAnimal(Animal):  # класс описывающий ядовитых животных.
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):  # класс описывающий утконоса.
    sound = "Click-click-click"  # звук, который издаёт утконос


db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in()
db.get_cords()
db.lay_eggs(3)
