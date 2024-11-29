class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    __file_name = 'products.txt'

    def __init__(self, name, weight, category):
        super().__init__(name, weight, category)

    def get_products(self):
        # считывает всю информацию из файла __file_name,
        # закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        file = open(self.__file_name, 'r')
        reading = file.read()
        file.close()
        return reading

    def add(self, *products):
        # Принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый
        # продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, то не
        # добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
        for new_product in products:
            if str(new_product) in self.get_products():
                print(f'Продукт {new_product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{new_product}\n')
                file.close()


s1 = Shop(str, float, str)
p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')
print(f'{p1}\n{p2}\n{p3}'.__str__())  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
