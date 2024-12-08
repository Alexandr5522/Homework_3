first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

"""Высчитывает разницу длин строк из списков first и second, 
если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip."""
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))

"""Содержит результаты сравнения длин строк в одинаковых позициях из списков first и second. 
Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len."""
second_result = ((len(first[i]) == len(second[i]) for i in range(len(first))))

print(list(first_result))
print(list(second_result))
