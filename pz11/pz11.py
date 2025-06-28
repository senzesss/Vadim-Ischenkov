# Вариант 11.
#+ 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Количество положительных элементов в первой половине:
# 2. Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое, количество знаков препинания. Сформировать новый файл, в который поместить строку наименьшей длины.


import string

listing = ['-1', '12', '17', '-5', '20', '92', '-33']

with open('textfile.txt', 'w') as file:
    for el in listing:
        file.write(f'{el}\n')

with open('textfile.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

count = len(numbers)
min_element = min(numbers)
first_half = numbers[:count // 2]
positive_count = sum(1 for num in first_half if num > 0)

with open('newfile.txt', 'w') as new_file:
    new_file.write(f'Исходные данные:{numbers}\n')
    new_file.write(f'Количество элементов: {count}\n')
    new_file.write(f'Минимальный элемент: {min_element}\n')
    new_file.write(f'Количество положительных элементов в первой половине: {positive_count}\n')




with open('text18-11.txt', 'r') as f1:
    lines = f1.readlines()

alltext = ''.join(lines)
punct = sum(1 for el in alltext if el in string.punctuation)
clean_lines = [line.strip() for line in lines if line.strip()]
sorts = sorted(clean_lines, key=len)
shortest = sorts[0]

with open('shortest.txt', 'w') as f:
    f.write(shortest)

print('Содержимое файла:')
print(alltext)
print(f'Количество знаков препинания: {punct}')
print(f'Строка наименьшей длины записана в файл shortest.txt')
