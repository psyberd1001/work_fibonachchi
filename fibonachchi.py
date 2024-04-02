n = int(input('Введите номер числа для вывода конечного числа Фибоначчи: '))
def fibonachchi(number3):
    number_fib_1 = 1
    number_fib_2 = 1
    for i in range(2, number3):
        number_fib_1, number_fib_2 = number_fib_2, number_fib_1 + number_fib_2
        print('Номенр итерации: ', {i - 1}, 'Первое число Фибоначчи:', number_fib_1, 'Второе число Фибоначчи:', number_fib_2)
    return number_fib_2


def fibonachchi_1(number4):
    number_fib_rec_1 = 1
    number_fib_rec_2 = 1
    i = 2
    while i < number4:
        number_fib_rec_1, number_fib_rec_2 = number_fib_rec_2, number_fib_rec_1 + number_fib_rec_2
        i = i + 1
        print('Номенр итерации: ', {i - 2}, 'Первое число Фибоначчи:', number_fib_rec_1, 'Второе число Фибоначчи:', number_fib_rec_2)
    return number_fib_rec_2

def fibonachchi_2(number5):
    if number5 in (1, 2):
        return 1
    return fibonachchi_2(number5 - 1) + fibonachchi_2(number5 - 2)

print('Итоговое число Фибоначчи', fibonachchi(n))
print('Итоговое число Фибоначчи', fibonachchi_1(n))
print('Итоговое число Фибоначчи', fibonachchi_2(n))