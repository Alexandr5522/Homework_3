first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

"""список состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов."""
first_result = [len(line) for line in first_strings if len(line) >= 5]

"""Список состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из списка first_strings 
должно сравниваться с каждым из second_strings."""
second_result = [(line_first, line_second) for line_first in first_strings
                 for line_second in second_strings if len(line_first) == len(line_second)]

"""Словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки.
Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
Условие записи пары в словарь - чётная длина строки."""
third_result = {line: len(line) for line in first_strings + second_strings if len(line) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
