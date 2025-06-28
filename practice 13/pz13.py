# Вариант 11.
# 1. В двумерном списке найти сумму и произведение элементов строки N (N задать
# клавиатуры).
# 2. В двумерном списке найти сумму элементов второй половины матрицы


from functools import reduce

stroke = int(input("Введите количество строк: "))
stolb = int(input("Введите количество столбцов: "))

matrix = [[i * stolb + j + 1 for j in range(stolb)] for i in range(stroke)]


print("Созданная матрица:")
nl = '\n'
for row in matrix:
    print(row)

N = int(input('Введите строку в которой, вы хотите найти сумму и произведение элементов'))
half = len(matrix) // 2


print(f'Сумма элементов строки {N}: {sum(matrix[N-1])}{nl}Произведение элементов строки {N}:  {reduce(lambda x, y: x * y, matrix[N-1])}')
print(f'Сумма элементов второй половины матрицы: {sum(sum(row) for row in matrix[half:])}')



