import hashlib
from time import sleep


class User:
    # nickname(имя пользователя, str), hash(password), int)), age(возраст, int)
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
            """Хеширование пароля"""
            return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
            """Проверяем пароль через хэш"""
            return self.password == hashlib.sha256(password.encode()).hexdigest()

    # возврат имени пользователя
    def __str__(self):
        return f"Пользователь({self.nickname}, возраст {self.age})"


class Video:
    # title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки, изначально 0),
    # adult_mode(ограничение по возрасту, False по умолчанию)
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def str(self):
        return f"Видео({self.title}, продолжительность-{self.duration}сек., ограничение по возрасту{self.adult_mode})"

class UrTube:
    # users(список объектов User), videos(список видео Video), current_user(текущий пользователь User)
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    # метод добавления имени пользователя и пароля
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.check_password(password) == password:
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")
                return
        print("Неправильный логин или пароль.")

    # метод регистрации нового пользователя
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошёл в систему.")

    def log_out(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)
                print(f'Видео ({video.title}) добавлено.')
            else:
                print(f'Видео ({video.title}) уже существует.')

    def contains(self, video):
        """Магический метод для проверки наличия видео"""
        return video in self.videos

    # принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово, без учета регистра
    def get_videos(self, word):
        word_video = []
        for video in self.videos:
            if word.upper() in video.title.upper():
                word_video.append(video.title)
        return word_video

    # Метод принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится,
    # если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    # После текущее время просмотра данного видео сбрасывается.
    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу.")
                    return
                print(f"Начинаем просмотр видео: {video.title}")
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    sleep(1)  # Имитируем просмотр по одной секунде
                print("\nКонец видео")
                video.time_now = 0  # Сбрасываем время остановки после полного просмотра
                return
        print(f'Видео не найдено.')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
