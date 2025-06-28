# 11. Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во"


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Название: {self.name}, Цена: {self.price}, Количество: {self.quantity}")

product1 = Product("Apple", 50, 10)
product1.display_info()



# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class Figura:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Pryamougolnik(Figura):
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Kvadrat(Figura):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 4 * self.width


rect = Pryamougolnik(4, 5)
print(f"Прямоугольник: площадь = {rect.area()}, периметр = {rect.perimeter()}")
square = Kvadrat(4)
print(f"Квадрат: площадь = {square.area()}, периметр = {square.perimeter()}")
