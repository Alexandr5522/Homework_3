import threading
import time
from datetime import timedelta, datetime


def write_words(word_count, file_name):
    # word_count - количество записываемых слов
    # file_name - название файла, куда будут записываться слова.
    for line in range(1, word_count + 1):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово № {line}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


t_start1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
t_finish1 = datetime.now()
print(f'Работа потоков: {t_finish1 - t_start1}')  # время в часах, минутах, секундах

t_start2 = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()  # работа потоков
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
t_finish2 = time.time()
print(f'Работа потоков: {timedelta(seconds=t_finish2 - t_start2)}')
