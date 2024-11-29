import math


class Figure:  # класс фигур
    sides_count = 0  # количество сторон фигуры

    def __init__(self, color, *sides):
        self.filled = False  # изначально не закрашенный (bool)
        self.__color = color  # список цветов в формате RGB

        # Проверка на количество сторон
        if len(sides) != self.sides_count:  # Если количество сторон не совпадает
            self.__sides = [1] * self.sides_count  # Создаём массив с единичными сторонами
        else:
            self.__sides = list(sides)  # Если всё верно, принимаем переданные стороны

    def get_color(self):  # возвращает список RGB цветов
        self.filled = True
        return self.__color

    def __is_valid_color(self, r, g, b):
        # Служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
        # перед установкой нового цвета. Корректным цвет: все значения
        # r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255:
            self.filled = True
            return r, g, b  # цвет корректный
        else:
            self.filled = False
            return self.__color

    def set_color(self, r, g, b):
        # Принимает параметры r, g, b - числа и изменяет атрибут __color
        # на соответствующие значения, предварительно проверив их на корректность.
        # Если введены некорректные данные, то цвет остаётся прежним.
        new_color = self.__is_valid_color(r, g, b)
        self.__color = list(new_color)
        return self.__color

    def __is_valid_sides(self, *new_sides):
        # Служебный, принимает неограниченное кол-во сторон, возвращает True,
        # если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
        # False - во всех остальных случаях.
        for sides in new_sides:
            if sides > 0 and len(new_sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):  # должен возвращать значение атрибута __sides.
        return self.__sides

    def set_sides(self, *new_sides):
        # должен принимать новые стороны, если их количество не равно sides_count,
        # то не изменять, в противном случае - менять.
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        return self.__sides

    def __len__(self):  # должен возвращать периметр фигуры.
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = self.get_sides()[0] / (2 * math.pi)
        # рассчитать исходя из длины окружности(одной единственной стороны).


    def get_square(self):  # возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        s = math.pi * (self.__radius ** 2)
        return math.ceil(s)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):  # площадь треугольника (формула Герона)
        sides = self.get_sides()
        a, b, c = sides[0], sides[1], sides[2]
        s = (a + b + c) / 2  # полупериметр
        return int(math.sqrt(s * (s - a) * (s - b) * (s - c)))  # по формуле Герона


class Cube(Figure):
    sides_count = 12 # у куба 12 ребер

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # Если стороны заданы корректно, берём их
        self.__sides = self.get_sides()

    def get_volume(self):  # объём куба
        side = self.__sides[0]  # сторона куба
        return math.ceil(side ** 3)


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(circle1.get_square()) # площадь круга
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(3)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
#
tri = Triangle((0, 0, 0,), 2, 4, 5)
print(tri.get_square())
tri.set_color(0, 0, 0)
print(tri.get_color())
print(len(tri))
print(tri.get_sides())
