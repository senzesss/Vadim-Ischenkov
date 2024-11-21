# Дано число R и список A размера N. Найти элемент списка, который наиболее близок
# к числу R (то есть такой элемент Aк, для которого величина |Aк - R| является
# минимальной).

# Запрашиваем у пользователя количество элементов в списке
n = input("Введите кол-во элементов в списке >> ")

# Обработка исключений
while True:
    try:
        n = int(n)
        if n > 0:
            break
        else:
            print("Число должно быть положительным")
            n = input("Введите кол-во элементов в списке >> ")
    except ValueError:
        print("Неправильно ввели число!")
        n = input("Введите кол-во элементов в списке >> ")

# Запрашиваем у пользователя число R для поиска ближайшего элемента
r = input("Введите число чтобы найти наиболее близкое к нему >> ")

# Обработка исключений
while type(r) != int:
    try:
        r = int(r)
    except ValueError:
        print("Неправильно ввели число!")
        r = input("Введите число чтобы найти наиболее близкое к нему >> ")

# Создаем список A из элементов от 1 до N
listA = list(range(1, n + 1))

# Инициализируем минимальную разницу как бесконечность
min_diff = float('inf')

# Перебираем все элементы списка A
for el in listA:
    diff = abs(el - r)  # Вычисляем абсолютную разницу между элементом и R
    if diff < min_diff:
        min_diff = diff  # Обновляем минимальную разницу
        closest_el = el  # Запоминаем текущий элемент как ближайший

# Выводим список A и ближайший элемент к числу R
print(f'Список A: {listA}')
print(f'Ближайшее число к R: {closest_el}')

