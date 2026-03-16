#Task1
print("-------------")

number = int(input("Введите число: "))

if number > 0:
    number += 1

print(number)

#Task2
print("-------------")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

count = 0  # счетчик положительных чисел

if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1

print("Количество положительных чисел:", count)

#Task3
print("-------------")

year = int(input("Введите год: "))

# Проверяем условия високосного года
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days = 366
else:
    days = 365

print(f"Количество дней: {days}")

#Task4
print("-------------")

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

total_sum = 0
for i in range(A, B + 1):
    total_sum += i

print(f"Сумма чисел от {A} до {B} равна {total_sum}")

#Task5
print("-------------")

product_pos = 1
sum_neg = 0
count_neg = 0
has_positive = False

for i in range(10):
    num = int(input(f"Введите число {i+1}: "))
    
    if num > 0:
        product_pos *= num
        has_positive = True
    elif num < 0:
        sum_neg += num
        count_neg += 1

final_product = product_pos if has_positive else 0

print(f"Произведение положительных: {final_product}")
print(f"Сумма отрицательных: {sum_neg}")
print(f"Количество отрицательных: {count_neg}")

#Task6
print("-------------")

n = int(input("Введите число N: "))
product = 1

for i in range(1, n + 1):
    product *= i

print(f"Произведение чисел от 1 до {n} равно {product}")

#Task7
print("-------------")

s1 = float(input("Введите площадь первого сорта (S1): "))
s2 = float(input("Введите площадь второго сорта (S2): "))

years = 0

while s1 >= 0.1 * s2:
    s1 *= 2
    s2 *= 3
    years += 1

print(f"Через {years} лет площадь первого сорта будет меньше 10% от второго.")

#Task8
print("-------------")

def is_happy(n):
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
        
    return n == 1

n = int(input("Введите число: "))
print(is_happy(n))

print("-------------")