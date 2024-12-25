"""Задача "Потоки гостей в кафе":
Table - стол, хранит информацию о находящемся за ним гостем (Guest).
Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
Примечания:
Для проверки значения на None используйте оператор is (table.guest is None).
Для добавления в очередь используйте метод put, для взятия - get.
Для проверки пустоты очереди используйте метод empty.
Для проверки выполнения потока в текущий момент используйте метод is_alive.
"""
import time
from queue import Queue
import threading
from threading import Thread
from random import randint


class Table:  # Объекты этого класса должны создаваться следующим способом - Table(1)
    # стол, хранит информацию о находящемся за ним гостем (Guest).
    def __init__(self, number):
        self.number = number  # номер стола
        self.guest = None  # гость, по умолчанию отсутствует


class Guest(Thread):  # наследуется от класса Thread, является ПОТОКОМ;
    # Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
    # гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)  # имя гостя

    def run(self):  # происходит ожидание случайным образом от 3 до 10 секунд.
        time.sleep(randint(3, 10))


class Cafe:  # Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
    # кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей и их обслуживания
    def __init__(self, *tables):
        self.queue = Queue()  # атрибут queue - очередь (объект класса Queue)
        self.tables = tables  # столы в этом кафе (любая коллекция)

    def guest_arrival(self, *guests):  # прибытие гостей
        """Должен принимать неограниченное кол-во гостей (объектов класса Guest). Далее, если есть свободный стол,
        то сажать гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку
         "<имя гостя> сел(-а) за стол номер <номер стола>". Если же свободных столов для посадки не осталось,
         то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди"."""
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}.')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        """Этот метод имитирует процесс обслуживания гостей.
        Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
         Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
         то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и
          "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
          Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу
        присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла)
        из очереди и сел(-а) за стол номер <номер стола>" Далее запустить поток этого гостя (start)"""
        for table in self.tables:
            while not self.queue.empty() or not table.guest is None:
                if not table.guest is None and table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(-а).\n'
                          f'Стол номер {table.number} свободен.')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-а) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()


# создание столов
tables = (Table(number) for number in range(1, 6))
# создание гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
# заполнение кафе столами
cafe = Cafe(*tables)
# прием гостей
cafe.guest_arrival(*guests)
# обслуживание гостей
cafe.discuss_guests()
