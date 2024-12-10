import random

first = 'Мама мыла раму'

second = 'Рамена мало было'

result = list(map(lambda i, j: True if i == j else False, first, second))
print(result)


def get_advanced_writer(file_name):  # принимает название файла для записи
    def write_everything(*data_set):  # принимает неограниченное количество данных любого типа
        with open(file_name, 'w', encoding='utf-8') as file:  # запись данных в file_name
            for element in data_set:
                file.write(f'{element}\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:

    def __init__(self, *words):  # атрибут words хранящий коллекцию строк
        self.words = words

    def __call__(self):
        # случайным образом выбирает слово из words и возвращает его.
        # Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можно
        # использовать функцию choice из модуля random
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
