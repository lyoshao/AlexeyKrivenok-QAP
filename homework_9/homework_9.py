import math
from typing import Any, Self
from dataclasses import dataclass


#Task1
print("-----------------")
"""
Создай класс Circle с protected атрибутом _radius. 
Добавь @property для radius (с проверкой: радиус > 0), и вычисляемые свойства area и perimeter через @property - они должны пересчитываться автоматически при изменении радиуса.
"""


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Радиус должен быть больше 0.")
        self._radius = value

    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

circle = Circle(5)
print(f"Радиус: {circle.radius}")
print(f"Площадь: {circle.area:.2f}")

circle.radius = 10
print(f"Новая площадь: {circle.area:.2f}")
print(f"Новый периметр: {circle.perimeter:.2f}")


#Task2
print("-----------------")
"""
Создай класс Vector с атрибутами x и y. 
Реализуй магические методы __add__ (сложение двух векторов), __str__ (вывод в формате "Vector(x, y)"), и __eq__ (сравнение). 
Проверь: Vector(1, 2) + Vector(3, 4) должен давать Vector(4, 6).
"""


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return self.__str__()

v1 = Vector(1, 2)
v2 = Vector(3, 4)
result = v1 + v2

print(f"Результат сложения: {result}")
print(f"Проверка на равенство: {result == Vector(4, 6)}")


#Task3
print("-----------------")
"""
Создай класс Temperature с @property для celsius, fahrenheit и kelvin. 
При установке значения через любое свойство должны автоматически пересчитываться остальные. 
Хранить следует только одно внутреннее значение.
"""


class Temperature:
    def __init__(self, celsius: float = 0.0) -> None:
        self._celsius: float = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float) -> None:
        self._celsius = value - 273.15

    def __repr__(self) -> str:
        return f"Temperature(C={self.celsius:.2f}, F={self.fahrenheit:.2f}, K={self.kelvin:.2f})"

temp = Temperature(25)
print(f"Исходная: {temp}")

temp.fahrenheit = 100
print(f"После изменения F: {temp.celsius:.2f}°C")

temp.kelvin = 0
print(f"После изменения K: {temp.celsius:.2f}°C")


#Task4
print("-----------------")
"""
Используй @dataclass для создания класса Point с полями x: float и y: float. 
Добавь метод distance_to(other: Point) - расстояние до другой точки. 
Затем создай дочерний @dataclass класс Point3D, добавив поле z: float, и переопредели distance_to.
"""


@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

@dataclass
class Point3D(Point):
    z: float

    def distance_to(self, other: 'Point3D') -> float:  #type: ignore
        return math.sqrt(
            (self.x - other.x)**2 + 
            (self.y - other.y)**2 + 
            (self.z - other.z)**2
        )

p1 = Point(0, 0)
p2 = Point(3, 4)
print(f"Расстояние 2D: {p1.distance_to(p2)}")  # 5.0

p3d_1 = Point3D(0, 0, 0)
p3d_2 = Point3D(1, 1, 1)
print(f"Расстояние 3D: {p3d_1.distance_to(p3d_2):.2f}")  # ~1.73


#Task5
print("-----------------")
"""
Создай класс-итератор Countdown, который при итерации возвращает числа от start до 0. 
Реализуй __iter__ и __next__ (при исчерпании бросай StopIteration). Проверь в цикле for и через list().
"""


class Countdown:
    def __init__(self, start: int) -> None:
        self.current: int = start

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        
        number = self.current
        self.current -= 1
        return number

print("Цикл for:")
for num in Countdown(3):
    print(num)

print("\nПреобразование в list:")
numbers = list(Countdown(5))
print(numbers)