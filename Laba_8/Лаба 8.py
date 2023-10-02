"""Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной
реализации (л.р. №7) разработать реализацию с использованием графического интерфейса. Допускается использовать любую
графическую библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка."""

import itertools
import random as r
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class selection:
    def __init__(self, main):
        self.first_click = True

        self.main = main
        self.main_label = Label(main, text='Люди у которых возраст превышает 30 лет не'
                                           'допускаются к участию в соревновании.\nНужно вывести составы команд, их '
                                           'параметры и команду с наибольшим суммарным рейтингом игроков.\n')

        self.label = Label(text='\nВведите кол-во игроков в турнире:')
        self.entry = ttk.Entry(width=30, justify='center')

        self.main_button = ttk.Button(text='Вывести', command=self.result)

        self.main_label.pack()
        self.label.pack()
        self.entry.pack()
        self.main_button.pack(expand=True)

    def result(self):
        self.m = []
        self.mp = {}
        self.string = ''
        self.rating = []
        self.player = []
        self.table = []
        self.player_parameters = {}

        try:
            self.conditions = True
            self.point = int(self.entry.get())

            if self.point < 4:
                messagebox.showwarning(title='Ошибка', message='Минимум четыре игрока.')
                self.conditions = False
            if self.point > 400:
                messagebox.showwarning(title='Ошибка', message='Вы ввели слишком большое число.')
                self.conditions = False

            if self.conditions:
                self.calculations()

                if self.first_click:
                    self.result_window()
                    self.first_click = False
                else:
                    self.purchases_window.destroy()
                    self.result_window()
        except ValueError:
            messagebox.showwarning(title='Ошибка', message='Введите число.')

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

        self.table += ['Игроки подавшие заявку:', f'{self.string[2::]}', '', 'Составы команд:', f'|{"¯" * 83}|',
                       '|{:^11}|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format('№ команды', 'Игрок № 1', 'Игрок № 2',
                                                                           'Возраст № 1', 'Возраст № 2', 'Рейтинг'),
                       f'|{"-" * 83}|']

        for j, n in enumerate(self.mp.items()):
            p1, p2 = (str(n[0])[1:-1]).split(', ')
            r1, r2 = (str(n[1])[1:-1]).split(', ')
            self.table += ['|{:^23}|{:^18}|{:^18}|{:^21}|{:^24}|{:^15}|'.format(j + 1, p1, p2, r1, r2, self.rating[j])]

        self.table += [f'|{"_" * 83}|', ' ', 'Команда с наивысшим рейтингом:', f'|{"¯" * 68}|',
                       '|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format('Игрок № 1', 'Игрок № 2', 'Возраст № 1',
                                                                    'Возраст № 2', 'Рейтинг'), f'|{"-" * 68}|']
        # Разделение списка на составляющие
        key = list(self.mp.items())[self.rating.index(max(self.rating))]
        p1, p2 = (str(key[0])[1:-1]).split(', ')
        r1, r2 = (str(key[1])[1:-1]).split(', ')
        self.table += ['|{:^21}|{:^19}|{:^19}|{:^19}|{:^18}|'.format(p1, p2, r1, r2, max(self.rating)),
                       f'|{"_" * 68}|']

    def result_window(self):
        self.purchases_window = Toplevel()
        self.purchases_window.title('Вывод')
        self.purchases_window.geometry('720x480')

        self.purchases_list = Listbox(self.purchases_window)
        self.purchases_list.pack(side='left', fill='both', expand=1)

        for i in self.table:
            self.purchases_list.insert('end', i)

        self.scrollbar = Scrollbar(self.purchases_window, command=self.purchases_list.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.purchases_list.config(yscrollcommand=self.scrollbar.set)


root = Tk()
root.title('Лабораторная № 8')
root.geometry('720x240')
root.resizable(False, False)

selection(root)

root.mainloop()
