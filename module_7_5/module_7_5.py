import os
import time

""" Научиться применять методы 
    os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize 
    и использование модуля time для корректного отображения времени."""

directory = '.'

for root, dirs, files in os.walk(directory):  # обход каталога, путь к которому указывает переменная directory
    for file in files:
        file_path = os.path.join(__file__)  # формирование полного пути к файлам

        file_time = os.path.getmtime(file)  # получение и отображения времени последнего изменения файла

        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(file_time))

        file_size = os.path.getsize(file)  # получение размера файла

        parent_dir = os.path.dirname(file_path)  # получение родительской директории файла

        print(f'Обнаружен файл: {file}\nПуть: {file_path}\nРазмер: {file_size} байт\n'
              f'Время изменения: {formatted_time}\nРодительская директория: {parent_dir}')
