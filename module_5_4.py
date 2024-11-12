class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории.')

residential1 = House('ЖК Виктория', 10)
print(House.houses_history)
residential2 = House('ЖК Акварели', 20)
print(House.houses_history)
residential3 = House('ЖК Матрёшка', 20)
print(House.houses_history)

del residential2
del residential3

print(House.houses_history)

del residential1
