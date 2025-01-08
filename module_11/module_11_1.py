import multiprocessing as mp
from PIL import Image, ImageFilter
from queue import Empty

"""Модуль PIL"""
# with Image.open('nature0.jpg') as im:
#     im = im.resize((2000, 2000))
#     im.save('nature0.1._new.jpg')

# def change(filename, delta):
#     """Функция меняет содержимое по заданным параметрам"""
#     with Image.open(filename) as im:
#         x_size, y_size = im.size
#
#         delta = delta % x_size
#         if delta == 0:
#             return im
#
#         part1 = im.crop((0, 0, delta, y_size))  # метод обрезает картинку по указанным координатам
#         part2 = im.crop((delta, 0, x_size, y_size))
#         im.paste(part1, (x_size - delta, 0, x_size, y_size)) # метод вставляет одно изображение в другое
#         im.paste(part2, (0, 0, x_size - delta, y_size))
#         im.save('im_new.jpg')
#     return im
#
"""Реализация с помощью multiprocessing"""
# def resize_image(image_paths, queue):
#     """Функция берет из списка картинку, изменяет ей размер и ставит в очередь"""
#     for image_path in image_paths:
#         image = Image.open(image_path)
#         image = image.resize((500, 500))
#         queue.put((image_path, image))
#
# def change_color(queue):
#     """Функция берет картинку из очереди, изменяет цвет и сохраняет"""
#     while True:
#         try:
#             image_path, image = queue.get(timeout=2) # ставим таймаут, когда закончится очередь цикл остановится
#         except Empty:
#             break
#         image = image.convert('L') # метод делает картинку черно-белой
#         image.save(image_path)
#
# def show_image(): # функция показывает картинку
#     im = Image.open('../images/nature24.jpg')
#     im.show()
#
#
# if __name__ == "__main__":
#     data = []
#     queue = mp.Queue()
#
#     for image in range(20, 25): # формируем список из картинок
#         data.append(f'../images/nature{image}.jpg')
#
#     resize_process = mp.Process(target=resize_image, args=(data, queue, ))
#     change_process = mp.Process(target=change_color, args=(queue, ))
#
#     resize_process.start()
#     change_process.start()
#
#     resize_process.join()
#     change_process.join()
#
#     show_image()

"""Модуль pandas"""
import zipfile
import pandas as pd
import glob

with zipfile.ZipFile('./trades.zip', 'r') as zip_ref: # распаковка zip-файла
    zip_ref.extractall()

csv_files = glob.glob('./trades/*.csv')

zero_volatility = []
all_volatility = []

for file in csv_files: # чтение файлов из папки trades
    df = pd.read_csv(file, sep=',')
    ticker = df['SECID'][0] # данные из файла столбец SECID
    max_price = df['PRICE'].max() # максимальное значение столбца PRICE
    min_price = df['PRICE'].min() # минимальное значение столбца PRICE
    average_price = (max_price + min_price) / 2 # среднее значение столбца PRICE
    if average_price == 0:
        raise ZeroDivisionError("Средняя цена равна 0")
    else:
        volatility = round(((max_price - min_price) / average_price) * 100, 2) # определяем волатильность ТИКЕРА

    if volatility == 0:
        zero_volatility.append(ticker) # добавляем в список нулевые ТИКЕРВ
    else:
        all_volatility.append((volatility, ticker)) # добавляем в список волатильность и наименование ТИКЕРА

zero_volatility.sort()
all_volatility.sort(reverse=True)
max_volatility = all_volatility[0:3]
min_volatility = all_volatility[-3::]
print('Максимальная волатильность ТИКЕРОВ:')
for element in max_volatility:
    print(element[0], element[1])
print('Минимальная волатильность ТИКЕРОВ:')
for element in min_volatility:
    print(element[0], element[1])
print(f"Нулевая волатильность ТИКЕРОВ:\n{zero_volatility}")


# """Модуль matplotlib"""
# import matplotlib.pyplot as plt
#
# # Данные для графика
# x = [2, 4, 6, 8, 10]
# y = [3, 5, 6, 10, 12]
#
#
# # Создание графика
# plt.plot(x, y)
#
# # Добавление заголовка и подписей осей
# plt.title("Линейный график")
# plt.xlabel("Ось X")
# plt.ylabel("Ось Y")
#
# # Отображение графика
# plt.show()

"""Модуль requests"""

# from pprint import pprint
# from queue import Queue
# from threading import Thread, Event
# import requests
#
# ACCESS_TOKEN = '6wd4LkvBHN4TPRHMsxU61WwL-pl1ABnMR2N-AjxAz3bvA4-KNqs1mBsm1KjmPtc_'
# RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
# GENIUS_API_URL = 'https://api.genius.com/search'
# GENIUS_URL = 'https://genius.com'
#
# all_sounds = []
# class GetGenre(Thread):
#     """Класс выбирает на сервере по ссылке случайным образом жанры музыки """
#
#     def __init__(self, queue, stop_event):
#         self.queue = queue
#         self.stop_event = stop_event  # останавливает поиск
#         super().__init__()
#
#     def run(self):
#         print(queue.qsize())
#         while not stop_event.is_set():
#             genre = requests.get(RANDOM_GENRE_API_URL).json()
#             self.queue.put(genre)
#
#
# class Genius(Thread):
#     """Класс выбирает музыку по жанру"""
#
#     def __init__(self, queue):
#         self.queue = queue
#         super().__init__()
#
#     def run(self):
#         genre = self.queue.get()
#         data = requests.get(GENIUS_API_URL, params=({'access_token': ACCESS_TOKEN, 'q': genre}))
#         data = data.json()
#         try:
#             sound_id = data['response']['hits'][0]['result']['api_path']
#             all_sounds.append({'genre': genre, 'songs': f'{GENIUS_URL}{sound_id}/apple_music_player'})
#         except IndexError as exc:
#             self.run()
#
#
# queue = Queue()
# stop_event = Event()
#
# genre_list = []
# genius_list = []
#
# for i in range(6):
#     tr = GetGenre(queue, stop_event)
#     tr.start()
#     genre_list.append(tr)
#
# for i in range(10):
#     tr = Genius(queue)
#     tr.start()
#     genius_list.append(tr)
#
# for tr in genius_list:
#     tr.join()
# stop_event.set()
#
# print(queue.qsize())
# pprint(all_sounds)
# print(len(all_sounds))
#
#
