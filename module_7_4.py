name1_team = 'Мастера кода'
name2_team = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result1 = 'Победа команды Волшебники данных!'
# challenge_result2 = 'Победа команды Мастера кода'

# использование %
print('В команде %s участников: %s!' % (name1_team, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

# Использование format():
print("Команда {} решила задач: {}!".format(name2_team, score_2))
print("{} решили задачи за {} с.!".format(name2_team, team2_time))

# Использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')

# исход соревнования
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды {name1_team}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды {name2_team}'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')

tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 1)
print(f'Сегодня было решено {tasks_total} задач,'
      f' в среднем по {time_avg} секунды на задачу!')
