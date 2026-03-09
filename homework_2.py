#task1
print("--------------")

a = -1.6
b = 2.99
a = round(a)
b = round(b)

print(a, b)

#task2
print("--------------")

c = "www.my_site.com#about"

print(c.replace("#", "/"))

#task3
print("--------------")

g = "stroka"
h = "ing"

print(g + h)

#task4
print("--------------")

name = "Ivanou Ivan"
name_words = name.split()
name_result = " ".join(reversed(name_words))

print(name_result)

#task5
print("--------------")

text = " Ivan Ivanou "
text_result = text.strip()

print(f"'{text_result}'")

#task6
print("--------------")

school = {"1a": 10, "1b": 11, "2a": 15, "2b": 16, "3a": 16,
           "3b": 17, "4a": 15, "4b": 16, "5a": 17, "5b": 20}

print(school)

#task7
print("--------------")

list_h = ["homework1", "homework2"]

print(list_h[1])

#task8
print("--------------")

str1 = "employ"
str2 = "employment"

if str1 in str2:
    print(f"Yes, '{str1}' into in '{str2}'")
else:
    print(f"No, '{str1}' not into in '{str2}'")

#task9
print("--------------")

x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:16:3]) #nesgt

#task10
print("--------------")

numbers = [1, 5, 2, 9, 2, 9, 1]
unique = 0

for num in numbers:
    unique ^= num

print(unique)

print("--------------")