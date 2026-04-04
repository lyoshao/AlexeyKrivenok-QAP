import shutil
import os
from datetime import datetime
from file_utils import read_lines, write_lines, count_words # type: ignore
from typing import List, Dict, Callable

#Task1
print("-----------------")
"""
Напиши функцию copy_file(source: str, destination: str) -> bool которая читает содержимое файла source и записывает его в destination.
Возвращает True если успешно. Проверь что файл-копия создался.
"""


def copy_file(source: str, destination: str) -> bool:
    try:
        shutil.copy2(source, destination)
        return os.path.exists(destination)
    except (FileNotFoundError, PermissionError, IOError):
        return False

success: bool = copy_file('source.txt', 'backup.txt')
print(f"Копирование прошло успешно: {success}")


#Task2
print("-----------------")
"""
Создай файл grades.txt где каждая строка содержит имя студента и его оценку через запятую:
Анна,85
Иван,72
Петр,91
Напиши код который читает файл и добавляет в конец каждой строки статус: 'отлично' если оценка >= 90, 'хорошо' если >= 75, иначе 'удовлетворительно'.
Сохрани результат в новый файл grades_with_status.txt.
"""


try:
    with open('grades.txt', 'r', encoding='utf-8') as infile, \
         open('grades_with_status.txt', 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            line = line.strip()
            if not line or ',' not in line: 
                continue
            
            name, score_str = line.split(',')
            score = int(score_str)
            
            if score >= 90:
                status = 'отлично'
            elif score >= 75:
                status = 'хорошо'
            else:
                status = 'удовлетворительно'
            
            
            outfile.write(f"{name},{score},{status}\n")
            
    print("Готово! Проверьте файл grades_with_status.txt.")

except FileNotFoundError:
    print("Ошибка: Файл 'grades.txt' не найден в текущей папке.")
except ValueError:
    print("Ошибка: В файле есть некорректные данные (в оценке не число).")


#Task3
print("-----------------")
"""
Напиши функцию age_calculator(birth_date_str: str) -> int которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет. 
"""


def age_calculator(birth_date_str: str) -> int:
    birth_date: datetime = datetime.strptime(birth_date_str, '%d/%m/%Y')
    today: datetime = datetime.today()
    
    age: int = today.year - birth_date.year
    
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        
    return age
    

user_input: str = input("Введите дату рождения (дд/мм/гггг): ")
print(f"Ваш возраст: {age_calculator(user_input)}")


#Task4
print("-----------------")
"""
Напиши модуль file_utils.py с тремя полностью аннотированными функциями:

def read_lines(filename): ...
def write_lines(filename, lines): ...
def count_words(filename): ... # count_words считает сколько раз каждое слово встречается в файле и возвращает словарь. 
В main.py импортируй и протестируй все три.
"""


def run_test() -> None:
    test_file: str = 'test.txt'
    sample_text: List[str] = [
        "Python лучший",
        "Илья привет",
        "Я изучаю Python",
        "Как дела Илья",
        "Python лайк",
        "Пока Илья"
        ]

    write_lines(test_file, sample_text)
    print(f"Файл '{test_file}' успешно создан.")

    lines: List[str] = read_lines(test_file)
    print(f"Прочитанные строки: {lines}")

    counts: Dict[str, int] = count_words(test_file)
    print(f"Частота слов: {counts}")

if __name__ == "__main__":
    run_test()


#Task5
print("-----------------")
"""
Напиши функцию password_checker(correct_password) которая возвращает вложенную функцию check(password).
Вложенная принимает пароль и возвращает True если совпадает, иначе False.
"""


def password_checker(correct_password: str) -> Callable[[str], bool]:
    def check(password: str) -> bool:
        return password == correct_password
        
    return check

verify: Callable[[str], bool] = password_checker("1503")

print(verify("2004"))
print(verify("1503"))
