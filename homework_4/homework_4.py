import math_utils
from typing import List, Dict, Tuple, Optional, Any

# Task1
print("----------------")
n: int = int(input("Введите число N: "))

results: list[str] = [str(n * i) for i in range(1, 11)]

print(" | ".join(results))

# Task2
print("----------------")
name: str = input("Введите ваше имя: ")
age: int = int(input("Введите ваш возраст: "))

print(f"Через 10 лет тебе будет {age + 10} лет, {name}!")

# Task3
print("----------------")
items: List[str] = ["хлеб", "молоко", "кофе"]
prices_usd: List[float] = [1.5, 2.0, 8.0]
rate: float = 3.2

prices_rub: List[float] = list(map(lambda x: round(x * rate, 1), prices_usd))

result_price: Dict[str, float] = dict(zip(items, prices_rub))

print(result_price)

# Task4
print("----------------")


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


result_fizz: List[str] = list(map(fizzbuzz, range(1, 21)))
print(result_fizz)

# Task5
print("----------------")


def my_stats(*args: float) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    if not args:
        return None, None, None

    minimum: float = min(args)
    maximum: float = max(args)
    average: float = sum(args) / len(args)

    return minimum, maximum, average


# Task6
print("----------------")


def build_profile(**kwargs: Any) -> Dict[str, Any]:
    profile: Dict[str, Any] = kwargs.copy()
    profile["registered"] = True
    return profile


user: Dict[str, Any] = build_profile(name="Алексей", age=22, city="Минск")
print(user)

# task7
print("----------------")

def math() -> None:
    try:
        user_input: str = input("Введите целое число: ")
        num: int = int(user_input)

        sq: int = math_utils.square(num)
        cb: int = math_utils.cube(num)
        even: bool = math_utils.is_even(num)

        print(f"Число: {num}")
        print(f"Квадрат: {sq}")
        print(f"Куб: {cb}")
        print(f"Четное: {'Да' if even else 'Нет'}")

    except ValueError:
        print("Ошибка: введите корректное целое число.")


if __name__ == "__main__":
    math()
