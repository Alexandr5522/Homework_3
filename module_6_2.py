class Vehicle:  # любое транспортное средство
    # owner(str) - владелец транспорта (владелец может меняться)
    # __model(str) - модель(марка) транспорта (мы не можем менять название модели)
    # __engine_power(int) - мощность двигателя (мы не можем менять мощность двигателя самостоятельно)
    # __color(str) - название цвета (мы не можем менять цвет автомобиля своими руками)
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):  # тип машины

    __PASSENGERS_LIMIT = 5  # в седан может поместиться только 5 пассажиров


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Demyan', 'Audi A8', 345, 'white')

# проверяем изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч., вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vsevolod'
# Проверяем, что поменялось
vehicle1.print_info()
