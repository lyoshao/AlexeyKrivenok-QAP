import math_utils

# Task1
print("----------------")
n = int(input("Введите число N: "))

results = [str(n * i) for i in range(1, 11)]

print(" | ".join(results))

# Task2
print("----------------")
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

print(f"Через 10 лет тебе будет {age + 10} лет, {name}!")

# Task3
print("----------------")
items = ["хлеб", "молоко", "кофе"]
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2

prices_rub = list(map(lambda x: round(x * rate, 1), prices_usd))

result_price = dict(zip(items, prices_rub))

print(result_price)

# Task4
print("----------------")


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


result_fizz = list(map(fizzbuzz, range(1, 21)))
print(result_fizz)

# Task5
print("----------------")


def my_stats(*args):
    if not args:
        return None, None, None

    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)

    return minimum, maximum, average


# Task6
print("----------------")


def build_profile(**kwargs):
    profile = kwargs.copy()
    profile["registered"] = True
    return profile


user = build_profile(name="Алексей", age=22, city="Минск")
print(user)

# task7
print("----------------")

def math():
    try:
        user_input = input("Введите целое число: ")
        num = int(user_input)

        sq = math_utils.square(num)
        cb = math_utils.cube(num)
        even = math_utils.is_even(num)

        print(f"Число: {num}")
        print(f"Квадрат: {sq}")
        print(f"Куб: {cb}")
        print(f"Четное: {'Да' if even else 'Нет'}")

    except ValueError:
        print("Ошибка: введите корректное целое число.")


if __name__ == "__main__":
    math()
