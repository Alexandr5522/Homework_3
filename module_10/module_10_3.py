import threading
import time
from random import randint


class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        """Будет совершать 100 транзакций пополнения средств.
        Пополнение - это увеличение баланса на случайное целое число от 50 до 500. Если баланс больше
         или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
         После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
         Также после всех операций поставьте ожидание в 0.001 секунды,
          тем самым имитируя скорость выполнения пополнения."""
        transaction1 = 100
        while transaction1 != 0:
            transaction1 -= 1
            number1 = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += number1
            print(f'Пополнение: {number1}. Баланс: {self.balance}.')
            time.sleep(0.001)

    def take(self):
        """Будет совершать 100 транзакций снятия. Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
В начале должно выводится сообщение "Запрос на <случайное число>". Далее производится проверка:
если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на соответствующее число
 и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>". Если случайное число оказалось больше
 баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquiere."""
        transaction2 = 100
        while transaction2 != 0:
            transaction2 -= 1
            number2 = randint(50, 500)
            print(f'Запрос на снятие суммы: {number2}.')
            if number2 <= self.balance:
                self.balance -= number2
                print(f'Снятие: {number2}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонен, недостаточно средств.')
                self.lock.acquire()
            time.sleep(0.001)





bk = Bank(0)
thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
thread2 = threading.Thread(target=Bank.take, args=(bk,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(f'Итоговый баланс: {bk.balance}')