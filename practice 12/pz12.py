# Вариант 11.
# 1.В последовательности на n целых чисел найти и вывести:
# 1. минимальный среди положительных
# 2. элементы кратные пяти
# 3. их среднее арифметическое
# 2.Иззаданнойстрокиотобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"


import string
from random import randint

n = int(input("Введите количество чисел: "))
numbers = [randint(-100, 100) for _ in range(n)]
print(f'Список чисел: {numbers}')
min_posit = min((x for x in numbers if x > 0))
print(f"Минимальный среди положительных: {min_posit}")


del_for_five = [x for x in numbers if x % 5 == 0]
print(f'Элементы кратные пяти: {del_for_five}')


if del_for_five:
    average = sum(del_for_five) / len(del_for_five)
    print(f"Среднее арифметическое кратных пяти: {average}")


stroka =  '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}'

punctuation = [char for char in stroka if char in string.punctuation]
print(f"Символы пунктуации:, {' '.join(punctuation)}")
