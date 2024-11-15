# Task3
1.1.Создайте класс Геометрическая фигура. Которая имеет функцию расчета площади.
1.2.Создайте классы прямоугольник, круг и ромб, класс геометрическая фигура должен быть их родительским классом. Добавьте им необходимые атрибуты и перепишите функцию родительского класса.

# Solution
```python
import math

# Родительский класс Геометрическая фигура
class GeometricFigure:
    def area(self):
        # Метод расчета площади, если метод не переопределён в подклассе, выбрасывается исключение
        raise NotImplementedError("Этот метод должен быть переопределён в подклассе")

# Класс Прямоугольник, наследующий от Геометрической фигуры
class Rectangle(GeometricFigure):
    def __init__(self, width, height):
        # Инициализация атрибутов ширины и высоты
        self.width = width
        self.height = height

    def area(self):
        # Переопределение метода для расчета площади прямоугольника
        return self.width * self.height

# Класс Круг, наследующий от Геометрической фигуры
class Circle(GeometricFigure):
    def __init__(self, radius):
        # Инициализация атрибута радиуса
        self.radius = radius

    def area(self):
        # Переопределение метода для расчета площади круга
        return math.pi * (self.radius ** 2)

# Класс Ромб, наследующий от Геометрической фигуры
class Rhombus(GeometricFigure):
    def __init__(self, diagonal1, diagonal2):
        # Инициализация атрибутов диагоналей
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        # Переопределение метода для расчета площади ромба
        return (self.diagonal1 * self.diagonal2) / 2


rectangle = Rectangle(4, 5)
print("Площадь прямоугольника:", rectangle.area())

circle = Circle(3)
print("Площадь круга:", circle.area())

rhombus = Rhombus(6, 8)
print("Площадь ромба:", rhombus.area())
```
