import math
from typing import List, Callable, Generator, Iterator, TypeVar, Optional, Union, Any


#Task1
print("-----------------")
"""
Используя filter() и lambda, отфильтруйте из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа.
"""


numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers: List[int] = list(filter(lambda x: x % 2 != 0, numbers))

print(odd_numbers)


#Task2
print("-----------------")
"""
Напишите функцию apply_operations(numbers, *operations),
которая принимает список чисел и произвольное количество lambda-функций, последовательно применяя каждую ко всему списку.
"""


def apply_operations(numbers: List[int], *operations: Callable[[List[int]], List[int]]) -> List[int]:
    result: List[int] = numbers
    for op in operations:
        result = op(result)
    return result

nums: List[int] = [1, 2, 3, 4, 5]
final_list: List[int] = apply_operations(
    nums,
    lambda x: [i * 2 for i in x],
    lambda x: [i for i in x if i > 5]
)

print(final_list)


#Task3
print("-----------------")
"""
Напишите генератор chunked(lst, size), который разбивает список на куски заданного размера и поочередно их выдает.
Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5].
"""


def chunked(lst: List, size: int) -> Generator[List, None, None]:
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

for chunk in chunked([1, 2, 3, 4, 5], 2):
    print(chunk)


#Task4
print("-----------------")
"""
Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. Выведите первые 20.
"""


def prime_numbers() -> Iterator[int]:
    n: int = 2
    while True:
        if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            yield n
        n += 1

gen: Iterator[int] = prime_numbers()
primes: List[int] = [next(gen) for _ in range(20)]

print(primes)


#Task5
print("-----------------")
"""
Напишите функцию safe_convert(value, type_func), которая пытается преобразовать value с помощью переданной функции (например, int, float).
При ошибке возвращает None.
"""


T = TypeVar("T")

def safe_convert(value: Any, type_func: Callable[[int], Any]) -> Optional[int]:
    try:
        return type_func(value)
    except (ValueError, TypeError):
        return None

res_1: Optional[int] = safe_convert("123", int) #123
res_2: Optional[int] = safe_convert("abc", int) #None
res_3: Optional[float] = safe_convert([1, 2], float) #None

print(res_1)
print(res_2)
print(res_3)


#Task6
print("-----------------")
"""
Создайте собственный класс исключения NegativeNumberError.
Напишите функцию sqrt_safe(n), которая считает квадратный корень из числа, но при отрицательном n выбрасывает NegativeNumberError с понятным сообщением.
"""


class NegativeNumberError(Exception):
    pass

def sqrt_safe(n: Union[int, float]) -> float:
    if n < 0:
        raise NegativeNumberError(f"Ошибка: нельзя извлечь корень из {n}. Число должно быть >= 0.")
    return math.sqrt(n)

try:
    num1: float = sqrt_safe(16)
    print(num1)

    num2: float = sqrt_safe(5)
    print(num2)
except NegativeNumberError as e:
    print(e)


#Task7
print("-----------------")
"""
Напишите функцию-калькулятор calculator(a, b, op), где op — строка ("+", "-", "*", "/").
Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов.
"""


Number = Union[int, float]

def calculator(a: Number, b: Number, op: str) -> Union[Number, str]:
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        else:
            return f"Ошибка: неизвестная операция '{op}'"
            
    except ZeroDivisionError:
        return "Ошибка: деление на ноль невозможно."
    except TypeError:
        return "Ошибка: некорректные типы аргументов (ожидались числа)."
    except Exception as e:
        return f"Произошла непредвиденная ошибка: {e}"

calc1: Union[Number, str] = calculator(10, 0, "/") #Деление на ноль
calc2: Union[Number, str] = calculator(10, "5", "+") #Некорректный тип
calc3: Union[Number, str] = calculator(10, 5, "^") #Неизсветная операция

print(calc1)
print(calc2)
print(calc3)
