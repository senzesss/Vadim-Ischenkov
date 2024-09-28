number = int(input()) # Ввод двухзначного числа

# Поиск десятков и единиц
des = number // 10
ost = number % 10

# Вывод результата
print("Десятки: ", des)
print("Единицы: ", ost)