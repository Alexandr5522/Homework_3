def custom_write(file_name, strings):
    # функция принимает аргументы file_name - название файла для записи, strings - список строк для записи
    strings_positions = {}
    num = 0
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        position = file.tell()
        num += 1
        file.write(f'{i}\n')
        strings_positions.update({(num, position): i})
    #file.close()
    return strings_positions


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

print(result)