import warnings
import functools
from functools import wraps
from typing import Callable, Any, List, Optional


#Task1
"""
Напишите рекурсивную функцию palindrome(s), которая проверяет, является ли строка палиндромом.
Без срезов и reversed(), только рекурсия.
"""


def palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return palindrome(s[1:-1])


#Task2
"""
Напишите функцию make_validator(min_val, max_val), которая возвращает функцию-валидатор.
Валидатор принимает число и возвращает True если оно в диапазоне, иначе False.
"""


def make_validator(min_val: int, max_val: int) -> Callable[[int], bool]:
    def validator(number:int) ->bool:
        return min_val <= number <= max_val
    return validator

is_adult: Callable[[int], bool] = make_validator(18, 100)

print(is_adult(25))  # True
print(is_adult(15))  # False


#Task3
"""
Напишите декоратор @retry(n), который при возникновении любого исключения повторяет вызов функции до n раз.
Если все попытки провалились — пробрасывает последнее исключение.
"""


def retry(n: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception: Exception
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator


#Task4
"""
Напишите декоратор @deprecated(message), который выводит предупреждение при вызове функции (через warnings.warn) и всё равно выполняет её.
Сохраняйте метаданные через functools.wraps.
"""


def deprecated(message: str) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(
                f"Функция {func.__name__} устарела. {message}",
                category=DeprecationWarning,
                stacklevel=2
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator


#Task5
"""
Напишите рекурсивную функцию binary_search(lst, target) (бинарный поиск числа в списке), 
оберните её декоратором @logger, который логирует каждый вызов с параметрами.
"""


def logger(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_repr: list[str] = [repr(a) for a in args]
        kwargs_repr: list[str] = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature: str = ", ".join(args_repr + kwargs_repr)

        print(f"Вызов {func.__name__}({signature})")
        return func(*args, **kwargs)
    
    return wrapper

@logger
def binary_search(
    lst: List[int], 
    target: int, 
    low: int = 0, 
    high: Optional[int] = None
) -> int:
    if high is None:
        high = len(lst) - 1
    
    if low > high:
        return -1
    
    mid: int = (low + high) // 2
    
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, low, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, high)
