# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib(n):
    match n:
        case 1 | 2:
            return 1
        case _:
            return fib(n - 1) + fib(n - 2)


def negafibonacci(my_list: list):
    neg_list = []
    i = len(my_list)
    while 0 < i:
        match i:
            case i if i % 2 == 0:
                neg_list.append((-my_list[i - 1]))
            case _:
                neg_list.append((my_list[i - 1]))
        i -= 1
    i = 0
    new_list = neg_list + [0] + [my_list[i] for i in range(0, len(my_list))]
    return new_list


number = int(input('Введите число: '))
print(f'k = {number}, Негафибоначчи: {negafibonacci([fib(e) for e in range(1, number + 1)])}')