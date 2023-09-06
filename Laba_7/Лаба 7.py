"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

Вариант 9:
В команду для участия в турнире по теннису в смешанном разряде подали заявку 3 женщины и 5 мужчин.
Вывести все возможные варианты состава команды.

Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода."""

import itertools
import random as r


class selection:
    try:
        def __init__(self):
            self.m = []
            self.mp = {}
            self.string = ''
            self.rating = []
            self.player = []
            self.table = []
            self.player_parameters = {}

            self.calculations()
            self.result()

        def players(self, x):
            cntplayers = 1

            for _ in range(x):
                self.player.append(f'{r.choice("МЖ")}{cntplayers}')
                cntplayers += 1

            for j in self.player:
                self.player_parameters[j] = r.randint(18, 35)

            for i in self.player_parameters.items():
                a, b = i
                self.string = f'{self.string}, {a} {b}'

        def parameters(self, x):
            a, b = x
            a1, b1 = r.randint(1, 50), r.randint(1, 50)
            self.mp[a, b] = self.player_parameters[a], self.player_parameters[b]
            self.rating.append(a1 + b1)

        def calculations(self):
            a = int(input('Запустить обычную версию программы или усложнённую? ( Обычную = 0 | Усложнённую = 1 ): '))
            while a != 0 and a != 1:
                a = int(input('Принимаются только значения "0" и "1": '))

            self.point = int(input('Введите кол-во игроков в турнире: '))
            while self.point < 4:
                self.point = int(input('Введите кол-во игроков в турнире (минимум четыре игрока): '))

            y = 0

            self.players(self.point)

            for i, n in enumerate(self.player_parameters.items()):
                a, b = n
                if int(b) > 30:
                    i -= y
                    y += 1
                    self.player.pop(i)
            for j in itertools.combinations(self.player, 2):
                self.parameters(j)

            self.table += ['\nИгроки подавшие заявку:', f'{self.string[2::]}', '', 'Составы команд:', f'|{"¯" * 73}|',
                           '|{:^11}|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format('№ команды', 'Игрок № 1', 'Игрок № 2',
                                                                               'Возраст № 1', 'Возраст № 2', 'Рейтинг'),
                           f'|{"-" * 73}|']

            for j, n in enumerate(self.mp.items()):
                p1, p2 = (str(n[0])[1:-1]).split(', ')
                r1, r2 = (str(n[1])[1:-1]).split(', ')
                self.table += ['|{:^11}|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format(j + 1, p1, p2, r1, r2, self.rating[j])]

            self.table += [f'|{"_" * 73}|', ' ', 'Команда с наивысшим рейтингом:', f'|{"¯" * 61}|',
                           '|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format('Игрок № 1', 'Игрок № 2', 'Возраст № 1',
                                                                        'Возраст № 2', 'Рейтинг'), f'|{"-" * 61}|']
            # Разделение списка на составляющие
            key = list(self.mp.items())[self.rating.index(max(self.rating))]
            p1, p2 = (str(key[0])[1:-1]).split(', ')
            r1, r2 = (str(key[1])[1:-1]).split(', ')
            self.table += ['|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format(p1, p2, r1, r2, max(self.rating)),
                           f'|{"_" * 61}|']

        def result(self):
            for i in self.table:
                print(i)

    except ValueError:
        print('\nВы ввели символ, а не число, перезапустите программу и введите нужное число.')


selection()
