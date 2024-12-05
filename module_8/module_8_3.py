class Car:
    """Класс создает автомобиль по данным: модель автомобиля, вин авто, номер автомобиля"""

    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        """Принимает vin_number и проверяет его на корректность. Возвращает True, если корректный,
         в других случаях выбрасывает исключение. Уровень доступа private."""
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber(f'У автомобиля {self.model} неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        """Принимает numbers и проверяет его на корректность. Возвращает True,
        если корректный, в других случаях выбрасывает исключение."""
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'У автомобиля {self.model} некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers(f'У автомобиля {self.model} неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    """Класс обрабатывает исключения, возникающие при создании данных автомобиля"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    """Класс обрабатывает исключения, возникающие при создании данных автомобиля"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


try:
    first = Car('AUDI', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('TOYOTA', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('FORD', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
