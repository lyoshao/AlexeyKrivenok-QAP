from typing import List, Any, Optional


#Task1
print("-----------------")
"""
Создай класс Library с атрибутом класса books = [] и методами add_book(title), remove_book(title) и show_books().
Продемонстрируй, что список книг общий для всех объектов класса.
"""


class Library:
    books: List[str] = []

    def add_book(self, title: str) -> None:
        Library.books.append(title)

    def remove_book(self, title: str) -> None:
        if title in Library.books:
            Library.books.remove(title)

    def show_books(self) -> List[str]:
        return Library.books

lib1 = Library()
lib2 = Library()

lib1.add_book("1984")

print(f"Книги в lib1: {lib1.show_books()}")
print(f"Книги в lib2: {lib2.show_books()}")

lib2.add_book("Brave New World")

print(f"Общий список после добавления в lib2: {lib1.show_books()}")


#Task2
print("-----------------")
"""
Создай иерархию: базовый класс Employee с атрибутами name и salary, методом get_info(). 
Дочерние классы Manager (добавляет department) и Developer (добавляет language). Каждый переопределяет get_info().
"""


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def get_info(self) -> str:
        return f"Сотрудник: {self.name}, Зарплата: {self.salary}"

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str) -> None:
        # Вызов конструктора базового класса
        super().__init__(name, salary)
        self.department = department

    def get_info(self) -> str:
        return f"Менеджер: {self.name}, Отдел: {self.department}, Зарплата: {self.salary}"

class Developer(Employee):
    def __init__(self, name: str, salary: float, language: str) -> None:
        super().__init__(name, salary)
        self.language = language

    def get_info(self) -> str:
        return f"Разработчик: {self.name}, Язык: {self.language}, Зарплата: {self.salary}"

mgr = Manager("Алиса", 120000, "IT")
dev = Developer("Иван", 100000, "Python")

print(mgr.get_info())
print(dev.get_info())


#Task3
print("-----------------")
"""
Реализуй класс Stack (стек) с протектед атрибутом _items = [] и методами push(item), pop(), peek() (посмотреть верхний элемент), is_empty() и size().
"""


class Stack:
    def __init__(self) -> None:
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Optional[Any]:
        if not self.is_empty():
            return self._items.pop()
        return None

    def peek(self) -> Optional[Any]:
        if not self.is_empty():
            return self._items[-1]
        return None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

stack = Stack()
stack.push("Первый")
stack.push("Второй")

print(f"Верхний элемент: {stack.peek()}")
print(f"Размер: {stack.size()}")
print(f"Извлечено: {stack.pop()}")
print(f"Пуст? {stack.is_empty()}")


#Task4
print("-----------------")
"""
Создай класс Vehicle с методом move(), выводящим "Moving...". Создай дочерние классы Car, Boat и Plane, каждый переопределяет move() по-своему. 
Напиши функцию start_journey(vehicle), которая вызывает move() у любого переданного транспорта - продемонстрируй полиморфизм.
"""


class Vehicle:
    def move(self) -> None:
        print("Moving...")

class Car(Vehicle):
    def move(self) -> None:
        print("Машина едет по дороге")

class Boat(Vehicle):
    def move(self) -> None:
        print("Лодка плывет по воде")

class Plane(Vehicle):
    def move(self) -> None:
        print("Самолет летит в небе")

def start_journey(vehicle: Vehicle) -> None:
    vehicle.move()

vehicles = [Car(), Boat(), Plane(), Vehicle()]

for v in vehicles:
    start_journey(v)


#Task5
print("-----------------")
"""
Создай класс Student с атрибутами name и grades (список оценок). 
Добавь методы add_grade(grade), average() (средняя оценка), highest() и lowest(). Защити grades через одиночное подчёркивание.
"""


class Student:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._grades: List[int] = []

    def add_grade(self, grade: int) -> None:
        if 1 <= grade <= 10:
            self._grades.append(grade)
        else:
            print("Ошибка: Оценка должна быть в диапазоне от 1 до 10.")

    def average(self) -> float:
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def highest(self) -> Optional[int]:
        return max(self._grades) if self._grades else None

    def lowest(self) -> Optional[int]:
        return min(self._grades) if self._grades else None

student = Student("Алексей")
student.add_grade(8)
student.add_grade(10)
student.add_grade(7)

print(f"Студент: {student.name}")
print(f"Средний балл: {student.average():.2f}")
print(f"Лучшая оценка: {student.highest()}")
print(f"Худшая оценка: {student.lowest()}")
