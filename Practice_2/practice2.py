#  Дано двузначное число. Вывести вначале его левую цифру (десятки),
#  а затем — его правую цифру (единицы). Для нахождения десятков использовать операцию
#  деления нацело, для нахождения единиц — операцию взятия остатка от деления

number = input("Введите двухзначное число: ")

while True:
    try:
        # Проверка на целое число
        number = int(number)

        # Проверка на двузначное число
        if number < 10 or number > 99:
            print("Число должно быть двузначным.")
            number = input("Попробуйте снова: ")
            continue

        # Поиск десятков и единиц
        des = number // 10
        ost = number % 10

        # Вывод результата
        print("Десятки:", des)
        print("Единицы:", ost)
        break

    except ValueError:
        print("Неправильно ввели число! Введите целое число.")
        number = input("Попробуйте снова: ")
