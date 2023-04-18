"""
С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B, C, D, E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.
Вид матрицы А:
D	Е
С	В
Каждая из матриц B, C, D, E имеет вид:
     4
  3     1
     2
Вариант 9:
Формируется матрица F следующим образом: если в "В" количество строк, состоящих из одних нулей в четных
столбцах в области 2 больше, чем сумма положительных элементов в четных строках в области 4,то поменять в С
симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После
чего вычисляется выражение: (К*F)*А – K * AT. Выводятся по мере формирования А, F и все матричные операции
последовательно.
"""

from math import ceil
import random as r


def print_matrix(matrix):  # функция вывода матрицы
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        c = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{c+1}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)


try:
    n = int(input('Введите число N: '))
    k = int(input('Введите число K: '))
    while n < 5:
        n = int(input('Введите число N больше 4: '))

    cnt_b2 = sum_ch4 = 0
    middle_n = n//2 + n % 2  # Середина матрицы
    A = [[r.randint(-10, 10) for i in range(n)] for j in range(n)]  # Задаём матрицу A
    AT = [[0 for i in range(n)] for j in range(n)]  # Заготовка под транспонированную матрицу А
    F = A.copy()  # Задаём матрицу F
    KF = [[0 for i in range(n)] for j in range(n)]  # Заготовка под результат умножения матрицы F на коэффициент K
    KFA = [[0 for i in range(n)] for j in range(n)]  # Заготовка под результат умножения матрицы KF на матрицу А
    KAT = [[0 for i in range(n)] for j in range(n)]  # Заготовка под результат умножения матрицы AT на коэффициент K
    result = [[0 for i in range(n)] for j in range(n)]  # Заготовка под результат вычитания двух матриц

    for i in range(n):  # Транспонируем матрицу А
        for j in range(n):
            AT[i][j] = A[j][i]

    print('\nМатрица А:')
    print_matrix(A)
    print('\nТранспонированная А:')
    print_matrix(AT)

    # Выделяем матрицы E C B
    if n % 2 == 1:
        E = [A[i][middle_n - 1:n] for i in range(middle_n)]
        C = [A[i][0:middle_n] for i in range(middle_n - 1, n)]
        B = [A[i][middle_n - 1:n] for i in range(middle_n - 1, n)]
    else:
        E = [A[i][middle_n:n] for i in range(0, middle_n)]
        C = [A[i][0:middle_n] for i in range(middle_n, n)]
        B = [A[i][middle_n:n] for i in range(middle_n, n)]

    for i in range(middle_n):  # Проверяем, что во 2 области в чётных столбцах в матрице "В" всё значения равны 0
        l_cnt = zero_cnt = 0
        for j in range(middle_n):
            if (i + j + 1) >= middle_n and (i >= j) and (j + 1) % 2 == 0:
                l_cnt += 1
                if B[i][j] == 0:  # Считаем кол-во подходящих строк
                    zero_cnt += 1
        if l_cnt == zero_cnt and l_cnt > 0:
            cnt_b2 += 1

    for i in range(middle_n):  # Считаем сумму положительных элементов в зоне 4 в чётных строках в матрице B
        for j in range(middle_n):
            if (i <= j) and ((i + j + 1) <= middle_n) and ((i + 1) % 2 == 0):
                if B[i][j] > 0:
                    sum_ch4 += B[i][j]

    if cnt_b2 > sum_ch4:
        print(f'\nВ матрице "В" количество строк с нулями на чётных позициях в области 2({cnt_b2})')
        print(f'больше чем сумма чётных строк в области 4({sum_ch4})')
        print('поэтому симметрично меняем местами области 1 и 2 в С.')
        for i in range(middle_n-1, ceil(middle_n / 2)-1, -1):
            for j in range(i):
                if (i + j + 1) >= middle_n:
                    C[i][j], C[j][i] = C[j][i], C[i][j]  # Симметрично меняем местами области 1 и 2 в С

        if n % 2 == 1:
            for i in range(middle_n - 1, n):
                for j in range(0, middle_n):
                    F[i][j] = C[i - (middle_n - 1)][j]  # Перезаписываем С
        else:
            for i in range(middle_n, n):
                for j in range(0, middle_n):
                    F[i][j] = C[i - middle_n][j]
    else:
        print(f'\nВ матрице "В" количеств строк с нулями на чётных позициях в области 2({cnt_b2})')
        print(f'меньше суммы чётных строк в области 4({sum_ch4}) или равно ей')
        print('поэтому несимметрично меняем местами подматрицы C и E:')
        C, E = E, C
        if n % 2 == 1:
            for i in range(middle_n - 1, n):  # Перезаписываем С
                for j in range(middle_n):
                    F[i][j] = C[i - (middle_n - 1)][j]
            for i in range(middle_n):  # Перезаписываем Е
                for j in range(middle_n - 1, n):
                    F[i][j] = E[i][j - (middle_n - 1)]
        else:
            for i in range(middle_n, n):
                for j in range(middle_n):
                    F[i][j] = C[i - middle_n][j]
            for i in range(0, middle_n):
                for j in range(middle_n, n):
                    F[i][j] = E[i][j - middle_n]

    # K * F и K * AT
    for i in range(n):
        for j in range(n):
            KF[i][j] = k * F[i][j]  # Производим умножение матрицы KF на коэффициент
            KAT[i][j] = k * AT[i][j]  # Производим умножение матрицы KAT на коэффициент

    # KF * A
    for i in range(n):
        for j in range(n):
            for m in range(n):
                KFA[i][j] += KF[i][m] * A[m][j]  # Производим умножение матрицы KFA на матрицу A

    # KFA - KAT
    for i in range(n):
        for j in range(n):
            result[i][j] = KFA[i][j] - KAT[i][j]  # Вычисляем разность двух матриц

    # Вывод всех операций
    print('\nМатрица F:')
    print_matrix(F)
    print('\nРезультат K * F:')
    print_matrix(KF)
    print("\nРезультат K * АT:")
    print_matrix(KAT)
    print('\nРезультат (К * F) * А:')
    print_matrix(KFA)
    print('\nРезультат (К * F) * А – K * AT:')
    print_matrix(result)
    print('\nРабота программы завершена.')
except ValueError:  # ошибка на случай введения не числа в качестве порядка или коэффициента
    print('\nВведенный символ не является числом. Перезапустите программу и введите число.')
