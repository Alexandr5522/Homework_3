class House:
    pass

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor < self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Жилой комплекс: {self.name}, {self.number_of_floors} эт.'


residential1 = House('Виктория', 18)
residential2 = House('Акварели', 2)
print(residential1)
print(residential2)
print(f'Количество этажей: {len(residential1)}')
print(f'Количество этажей: {len(residential2)}')
residential1.go_to(5)
residential2.go_to(3)
