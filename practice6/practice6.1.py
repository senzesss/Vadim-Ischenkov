# Дан список A размера N (N — четное число). Вывести его элементы с четными номерами в порядке возрастания номеров: A2, A4, A6, ..., AN. Условный оператор не использовать. 

n = input("Введите чётное положительное число >> ")

while True:
    try:
        n = int(n)
        if n > 0 and (n % 2)==0:
            break  # Если все условия выполнены, выходим из цикла
        else:
            print("Число должно быть положительным и чётным")
            n = input("Введите чётное положительное число >>")
    except ValueError:
        print("Неправильно ввели число!")
        n = input("Введите чётное положительное число >>")

listA = []

listA = list(range(n))

even = listA[::2]

print(listA)
print(even)