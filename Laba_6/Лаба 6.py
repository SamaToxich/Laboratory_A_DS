"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 9:
В команду для участия в турнире по теннису в смешанном разряде подали заявку 3 женщины и 5 мужчин.
Вывести все возможные варианты состава команды.
"""

import itertools
import random as r


def parameters(x):
    global mp
    a, b = x
    a1, b1 = r.randint(1, 10), r.randint(1, 10)
    mp[a, b] = participants_parameters[a], participants_parameters[b]
    rating.append(a1 + b1)


m = []
mp = {}
rating = []
participants = ['Ж1', 'Ж2', 'Ж3', 'М1', 'М2', 'М3', 'М4', 'М5']
participants_parameters = {'Ж1': 19, 'Ж2': 27, 'Ж3': 35, 'М1': 24, 'М2': 38, 'М3': 21, 'М4': 18, 'М5': 43}

try:
    a = int(input('Запустить обычную версию программы или усложнённую? ( Обычную = 0 | Усложнённую = 1 ): '))
    while a != 0 and a != 1:
        a = int(input('Принимаются только значения "0" и "1": '))
    # Первая часть задания
    if a == 0:
        for i in itertools.combinations(participants, 2):
            m.append(i)

        print('\nСоставы команд:')
        for i in m:
            print(' Игрок № 1: {}, Игрок № 2: {} '.format(*i))
    # Вторая часть задания
    else:
        print('\nДополнительным условием будет ограничение по возрасту.\nЛюди у которых возраст превышает 30 лет не'
              'допускаются к участию в соревновании.\nНужно вывести составы команд и их параметры и команду с'
              ' наибольшим суммарным рейтингом игроков.\n')
        y = 0
        for i, n in enumerate(participants_parameters.items()):
            a, b = n
            if int(b) > 30:
                i -= y
                y += 1
                participants.pop(i)
        for i in itertools.combinations(participants, 2):
            parameters(i)
        # Заготовки для таблицы
        table = []
        a = '¯' * 73
        b = '_' * 73
        c = '-' * 73
        # Разделение списка на составляющие
        for i, n in enumerate(mp.items()):
            p1, p2 = (str(n[0])[1:-1]).split(', ')
            r1, r2 = (str(n[1])[1:-1]).split(', ')
            table.append([i + 1, p1, p2, r1, r2, rating[i]])
        # Вывод таблицы
        print('Составы команд:')
        print(f'|{a}|')
        print('|{:^11}|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format('№ команды', 'Игрок № 1', 'Игрок № 2', 'Возраст № 1',
                                                                  'Возраст № 2', 'Рейтинг'))
        print(f'|{c}|')
        for value in table:
            print('|{:^11}|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format(value[0], value[1], value[2], value[3], value[4],
                                                                      value[5]))
        print(f'|{b}|')
        # Заготовки для таблицы
        a = '¯' * 61
        b = '_' * 61
        c = '-' * 61
        # Разделение списка на составляющие
        key = list(mp.items())[rating.index(max(rating))]
        p1, p2 = (str(key[0])[1:-1]).split(', ')
        r1, r2 = (str(key[1])[1:-1]).split(', ')
        # Вывод таблицы
        print('\nКоманда с наивысшим рейтингом:')
        print(f'|{a}|')
        print('|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format('Игрок № 1', 'Игрок № 2', 'Возраст № 1',
                                                           'Возраст № 2', 'Рейтинг'))
        print(f'|{c}|')
        print('|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format(p1, p2, r1, r2, max(rating)))
        print(f'|{b}|')

    print('\nРабота программы завершена успешно.')
except ValueError:
    print('\nВы ввели символ, а не число, перезапустите программу и введите нужное число.')
