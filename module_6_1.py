class Animal:
    alive = "Да"  # живой
    fed = "Да"  # накормленный

    def __init__(self, name):
        self.name = name  # индивидуальное название каждого животного

    def __str__(self):
        return f'Животное: {self.name}'

    def eat(self, food):  # метод, где food - это параметр, принимающий объекты классов растений
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
        else:
            print(f'{self.name} не стал есть {food.name}')
        self.alive = "Здоровый"
        self.fed = "Сытый"


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False  # съедобность

    def __init__(self, name):
        self.name = name  # индивидуальное название каждого растения

    def __str__(self):
        return f'Растение: {self.name}'


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True  # съедобность


predator = Predator('Волк')
mammal = Mammal('Заяц')
flower = Flower('Цветик семицветик')
fruit = Fruit('Морковь')
print(predator)
print(flower)
print(predator.alive)
print(mammal.fed)
predator.eat(flower)
print(predator.alive)
mammal.eat(fruit)
print(mammal.fed)

# вариант вывода
print(Predator('Волк'))
print(Flower('Морковь'))
Predator('Волк').eat(Flower('Цветик семицветик'))  # без атрибута класса '''predator'''
