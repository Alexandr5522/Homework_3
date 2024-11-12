class House:
    def __init__(self, name, number_of_floors, ):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 < new_floor < self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Жилой комплекс: {self.name}, {self.number_of_floors} эт.'

    def __eq__(self, other):  # ==
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors and self.name == other.name

    def __lt__(self, other):  # <
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):  # >
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __le__(self, other):  # <=
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):  # >=
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):  # !=
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value
        else:
            print("Разные типы данных")

    def __iadd__(self, value):
        return self

    def __radd__(self, value):
        return value + self.number_of_floors


residential1 = House('Виктория', 10, )
residential2 = House('Акварели', 20, )
print(f'1. {residential1}')
print(f'2. {residential2}')

print(f'3. Количество этажей: {len(residential1)}')  # __len__
print(f'4. Количество этажей: {len(residential2)}')  # __len__
print(f'5. {residential1 == residential2}')  # __eg__

residential1.number_of_floors = residential1 + 10  # __add__
print(f'6. {residential1}')
print(f'7. {residential1 == residential2}')  # __eg__

residential1.number_of_floors += 10  # __iadd__
print(f'8. {residential1}')

residential2.number_of_floors = 10 + residential2  # __radd__
print(f'9. {residential2}')
print(f'10. {residential1 == residential2}')  # __eg__

print(f'11. {residential1 > residential2}')  # __gt__
print(f'12. {residential1 >= residential2}')  # __ge__
print(f'13. {residential1 < residential2}')  # __lt__
print(f'14. {residential1 <= residential2}')  # __le__
print(f'15. {residential1 != residential2}')  # __ne__

residential1.go_to(33)  # применения метода go_to()
residential2.go_to(3)
