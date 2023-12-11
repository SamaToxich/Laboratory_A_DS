"""
Вариант 9:
Вычислить сумму знакопеременного ряда (|х^(2n+1)|)/(2n+1)!, где х-матрица ранга к (к и матрица, задаются случайным
образом), n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после
запятой. У алгоритма д.б. линейная var = сложность. Операция умножения –поэлементная. Знак первого слагаемого -
случайный.
"""

from random import choice, randint
import numpy as np
from decimal import Decimal, getcontext


def s_sum(x, t):
    # Задаем базовые параметры
    n = 1
    matrix = x * x * x
    factorial = 6
    res = 0
    sign = choice([-1, 1])

    while True:
        curr_term = Decimal(np.linalg.det(matrix) / factorial)
        # decimal, что позволяет сохранять числа после запятой, даже при больших значениях самого числа
        res += sign * curr_term

        if abs(curr_term) < 1 / (10 ** t):
            break

        # Для следующего слагаемого
        n += 1
        sign = -sign
        factorial *= (2*n)*(2*n+1)
        matrix *= x * x

    return res


try:
    t = int(input('Введите число t, являющееся кол-вом знаков после запятой: '))
    while t > 300 or t < 1:
        t = int(input('Введите число t, большее или равное 1:\n'))

    # Генерация случайного значения k и матрицы x
    k = randint(2, 5)
    x = np.round(np.random.uniform(-1, 1, (k, k)), 3)

    print('\nМатрица:\n', x)

    getcontext().prec = t + 100

    result = s_sum(x, t)

    print(f"\nСумма ряда с точностью {t} знаков после запятой: {result:.{t}f}".rstrip('0').rstrip('.'))

except ValueError:
    print('\nВведенный символ не является числом. Перезапустите программу и введите число.')
