"""Вариант 9.
Нечетные четырехричные числа, не превышающие 1024, у которых вторая справа цифра равна 3. Выводит на
экран цифры числа, исключая тройки. Вычисляется среднее число между минимальным и максимальным и выводится прописью. """

import re

m = []


def slovo(x):
    z = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
         '8': 'восемь', '9': 'девять'}
    return z[x]


f = open('test.txt')
buffer = f.readline().split()
if not buffer:
    print('Файл пустой.')
    quit()
else:
    while True:
        if not buffer:
            break
        for i in buffer:
            work_buffer = re.findall(r'\b[0-3]{0,3}3[13]\b', i)
            if work_buffer:
                m += [int(work_buffer[0])]
                l = work_buffer[0].replace('3', '')
                print(f'Вывод: {l}')
        buffer = f.readline().split()

if m:
    sred = (max(m) + min(m)) // 2
    k = ''
    for i in range(len(str(sred))):
        g = slovo(str(sred)[i])
        k += g + ' '
    print(f'Среднее значение: {sred} - {k}')
else:
    print('В файле нет подходящих значений.')
