import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__(name=name)
        self.power = power

    def run(self):
        enemies = 100
        day = 0
        print(f'{self.name} на нас напали.')
        while enemies != 0:
            day += 1
            enemies -= self.power
            print(f'{self.name} сражается {day} день(дня), осталось {enemies} врагов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня).')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
