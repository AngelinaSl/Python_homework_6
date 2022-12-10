# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

# вариант 1

# number = int(input('Введите число: '))
# my_list = [round((1 + 1 / i) ** i, 2) for i in range(1, number + 1)]
# print(f' {my_list}  Сумма = {round(sum(my_list), 3)}', end=" ")

# вариант 2

number = int(input('Введите число: '))
print(f' {[round((1 + 1 / i) ** i, 2) for i in range(1, number + 1)]}    '
      f'Сумма = {round(sum([(1 + 1 / i) ** i for i in range(1, number + 1)]), 3)}', end=" ")