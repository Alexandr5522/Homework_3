import logging
import asyncio
import time


async def start_strongman(name, power):
    if power <= 0:
        raise ValueError(f'Значение не может быть меньше или равно нулю. Введено {power}')
    if not isinstance(power, int):
        raise TypeError(f'Введена не цифра. Введено {power}.')
    if not isinstance(name, str):
        raise TypeError(f'Введена не строка. Введено {name}.')
    print(f'Силач {name} начал соревнования.')
    ball = 0
    while ball != 5:
        await asyncio.sleep(power - 1)
        ball += 1
        print(f'Силач {name} поднял {ball} шар(а).')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    try:
        task1 = asyncio.create_task(start_strongman('Vsevolod', 3))
        task2 = asyncio.create_task(start_strongman('Demyan', 4))
        task3 = asyncio.create_task(start_strongman(6, 5))
        await task1
        await task2
        await task3
        logging.info('Start_strongman выполнен успешно.', exc_info=True)
    except:
        logging.warning('Введено не верное значение.', exc_info=True)


logging.basicConfig(level=logging.INFO, filemode='w', filename='test_log_13_1.log',
                    format="%(asctime)s|%(levelname)s|%(message)s", encoding='UTF-8')

start = time.time()
asyncio.run(start_tournament())
end = time.time()
print(f'Время работы метода {round(end - start, 3)}')
