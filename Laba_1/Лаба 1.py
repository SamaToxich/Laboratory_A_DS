"""Вариант 9.
Нечетные четырехричные числа, не превышающие 1024, у которых вторая справа цифра равна 3. Выводит на
экран цифры числа, исключая тройки. Вычисляется среднее число между минимальным и максимальным и выводится прописью. """

m = []
chisla = ['0', '1', '2', '3']
simvols = [' ', '!', '?', '.', ',', '\n', '', ':', '-', ';', '"', ')', '(']
buffer_len = 1 
work_buffer = ''


def chet(v):
    s = ''
    while v > 0:
        s += str(v % 4)
        v //= 4
    return int(s[::-1])


def slovo(x):
    z = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
    return z[x]


with open('test.txt') as f:
    buffer = f.read(buffer_len)
    if not buffer:
        print('Файл пустой.')
        quit()
    while buffer:
        while buffer not in simvols:
            work_buffer += buffer
            buffer = f.read(buffer_len)
        if len(work_buffer) > 0:
            flag = True
            for i in range(len(work_buffer)):
                if work_buffer[i] not in chisla:
                    flag = False
            if flag and len(work_buffer) > 1:
                if work_buffer[-2] == '3' and int(work_buffer) < chet(1025) and int(work_buffer) % 2 == 1:
                    m += [int(work_buffer)]
                    l = work_buffer.replace('3', '')
                    print(f'Вывод: {l}')
        work_buffer = ''
        buffer = f.read(buffer_len)

if m:
    sred = (max(m) + min(m)) // 2
    k = ''
    for i in range(len(str(sred))):
        g = slovo(str(sred)[i])
        k += g + ' '
    print(f'Среднее значение: {sred} - {k}.')
else:
    print('В файле нет подходящих значений.')
