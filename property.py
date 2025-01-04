class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # вызываем метод как атрибут, без ()
    @property
    def area(self):
        return self._width * self._height

    # можно обращаться к защищенному атрибуту через метод width
    @property
    def width(self):
        return self._width

    # добавляем правило при обновлении значения атребута _width
    @width.setter
    def width(self, value):
        if value <= 0:
            self._width = 1
        else:
            self._width = value


r = Rectangle(10, 5)
print(r.area)
r.width = 0
print(r.width)
print(r.area)


# Декоратор датакласс (класс-словарь)
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str

