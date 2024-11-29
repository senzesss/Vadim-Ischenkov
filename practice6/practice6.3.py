# Дан список размера N. Осуществить сдвиг элементов списка влево на одну позицию
# (при этом AN перейдет в AN-1, AN-1 — в AN-2, .., A2 — в A1, a исходное значение
# первого элемента будет потеряно). Последний элемент полученного списка
# положить равным 0.

# Запрос ввода от пользователя
n = input("Введите кол-во элементов в списке >> ")

# Обработка исключений
while True:
    try:
        n = int(n)
        if n > 0:
            break
        else:
            print("Число должно быть положительным")
    except ValueError:
        print("Неправильно ввели число!")
    n = input("Введите кол-во элементов в списке >> ")

listA = list(range(1, n + 1))
print("Исходный список:", listA)

# Сдвиг элементов влево на одну позицию
listA = listA[1::]

# Установка последнего элемента равным 0
listA[-1] = 0
print("Изменённый список:", listA)
