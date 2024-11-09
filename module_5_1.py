class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 < new_floor < self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break


residential1 = House('ЖК Виктория', 18)
residential2 = House('ЖК Акварели', 2)
residential1.go_to(5)
residential2.go_to(10)


