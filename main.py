number = input("Введите число >> ") # Ввод двухзначного числа

while type(number) != int: # обработка исключений
    try:
        number = int(number)
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите первое число: ")
# Поиск десятков и единиц
des = number // 10
ost = number % 10

# Вывод результата
print("Десятки: ", des)
print("Единицы: ", ost)