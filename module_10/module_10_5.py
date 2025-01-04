import multiprocessing
import threading
from datetime import datetime
from threading import Thread
from multiprocessing import Pool


def read_info(name):
    """Функция read_info(name), где name - название файла. Функция должна: Создавать локальный список all_data.
    Открывать файл name для чтения. Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
    Во время считывания добавлять каждую строку в список all_data."""
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


filenames = [f'./file {number}.txt' for number in range(1, 5)] # список файлов

# start_time = datetime.now()

# read_info(filenames[0]) # линейный запуск функции поочередно для каждого файла
# read_info(filenames[1])
# read_info(filenames[2])
# read_info(filenames[3])

# thread1 = Thread(target=read_info, args=(filenames[0], )) # потоковый запуск функции
# thread2 = Thread(target=read_info, args=(filenames[1], ))
# thread3 = Thread(target=read_info, args=(filenames[2], ))
# thread4 = Thread(target=read_info, args=(filenames[3], ))
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()

# finish_time = datetime.now()
# print(finish_time - start_time)

if __name__ == "__main__":
    start_time = datetime.now()
    with Pool() as p: # многопроцессный запуск функции
        p.map(read_info, filenames)

#     process1 = multiprocessing.Process(target=read_info, args=(filenames[0], ))
#     process2 = multiprocessing.Process(target=read_info, args=(filenames[1], ))
#     process3 = multiprocessing.Process(target=read_info, args=(filenames[2], ))
#     process4 = multiprocessing.Process(target=read_info, args=(filenames[3], ))
#     process1.start()
#     process2.start()
#     process3.start()
#     process4.start()
#     process1.join()
#     process2.join()
#     process3.join()
#     process4.join()

    finish_time = datetime.now()
    print(finish_time - start_time)