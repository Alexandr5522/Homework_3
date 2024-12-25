from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__(name=name)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables  # столы в кафе
        self.queue = Queue()  # очередь

    def guest_arrival(self, *guests):  # прибытие гостей
        """Принимает неограниченное кол-во гостей (объектов класса Guest). Далее, если есть свободный стол,
        то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку
         "<имя гостя> сел(-а) за стол номер <номер стола>". Если же свободных столов для посадки не осталось,
         то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди"."""
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    # self.queue.get(guest)
                    table.guest = guest
                    table.guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}.')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        """Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
        Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
        то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".
         Так же текущий стол освобождается (table.guest = None). Если очередь ещё не пуста (метод empty) и стол один из
          столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()).
          Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
          Далее запустить поток этого гостя (start)"""
        while not self.queue.empty():
            for table in self.tables:
                if (not table.guest is None) and (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла).')
                    print(f'Стол номер {table.number} свободен.')
                    table.guest = None
                if (not self.queue.empty()) and (table.guest is None):
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.')
                    table.guest.start()


tables = [Table(number) for number in range(1, 6)]  # Создание столов

guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']  # Имена гостей

guests = [Guest(name) for name in guests_names]  # Создание гостей

cafe = Cafe(*tables)  # Заполнение кафе столами

cafe.guest_arrival(*guests)  # Приём гостей

cafe.discuss_guests()  # Обслуживание гостей
