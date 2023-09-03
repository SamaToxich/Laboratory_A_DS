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
                                           'допускаются к участию в соревновании.\nНужно вывести составы команд и их '
                                           'параметры и команду с наибольшим суммарным рейтингом игроков.\n')

        self.label1 = Label(text='\nВведите название таблицы:')
        self.entry1 = ttk.Entry(width=30, justify='center')

        self.main_button = ttk.Button(text='Вывести', command=self.result)

        self.main_label.pack()
        self.label1.pack()
        self.entry1.pack()
        self.main_button.pack(expand=True)

    def parameters(self, x):
        self.a, self.b = x
        self.a1, self.b1 = r.randint(1, 10), r.randint(1, 10)
        self.mp[self.a, self.b] = self.participants_parameters[self.a], self.participants_parameters[self.b]
        self.rating.append(self.a1 + self.b1)

    def result(self):
        self.m = []
        self.mp = {}
        self.rating = []
        self.participants = ['Ж1', 'Ж2', 'Ж3', 'М1', 'М2', 'М3', 'М4', 'М5']
        self.participants_parameters = {'Ж1': 19, 'Ж2': 27, 'Ж3': 35, 'М1': 24, 'М2': 38, 'М3': 21, 'М4': 18, 'М5': 43}

        self.conditions = True

        if self.conditions:
            self.calculations()

            if self.first_click:
                self.result_window()
                self.first_click = False
            else:
                self.purchases_window.destroy()
                self.result_window()

    def calculations(self):
        self.y = 0
        for i, n in enumerate(self.participants_parameters.items()):
            self.a, self.b = n
            if int(self.b) > 30:
                i -= self.y
                self.y += 1
                self.participants.pop(i)
        for j in itertools.combinations(self.participants, 2):
            self.parameters(j)
        # Заготовки для таблицы
        self.table = []
        # Разделение списка на составляющие
        self.table.append(['№ команды', 'Игрок № 1', 'Игрок № 2', 'Возраст № 1', 'Возраст № 2', 'Рейтинг'])
        for j, n in enumerate(self.mp.items()):
            self.p1, self.p2 = (str(n[0])[1:-1]).split(', ')
            self.r1, self.r2 = (str(n[1])[1:-1]).split(', ')
            self.table.append([j + 1, self.p1, self.p2, self.r1, self.r2, self.rating[j]])

        # Заготовки для таблицы
        self.a = '¯' * 83
        self.b = '_' * 83
        self.c = '-' * 83
        # Разделение списка на составляющие
        self.key = list(self.mp.items())[self.rating.index(max(self.rating))]
        self.p1, self.p2 = (str(self.key[0])[1:-1]).split(', ')
        self.r1, self.r2 = (str(self.key[1])[1:-1]).split(', ')

    def result_window(self):
        self.purchases_window = Toplevel()
        self.purchases_window.title('Вывод')
        self.purchases_window.geometry('720x480')

        self.label2 = Label(self.purchases_window, text=self.entry1.get())
        self.label2.pack()
        self.label3 = Label(self.purchases_window, text=f'|{self.a}|')
        self.label3.pack()
        self.label4 = Label(self.purchases_window, text='|{:^11}|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format(
            self.table[0][0], self.table[0][1], self.table[0][2], self.table[0][3],
            self.table[0][4], self.table[0][5]))
        self.label4.pack()
        self.label5 = Label(self.purchases_window, text=f'|{self.c}|')
        self.label5.pack()
        for i in self.table[1::]:
            self.label6 = Label(self.purchases_window, text='|{:^23}|{:^18}|{:^18}|{:^21}|{:^24}|{:^15}|'.format(
                i[0], i[1], i[2], i[3], i[4], i[5]))
            self.label6.pack()
        self.label7 = Label(self.purchases_window, text=f'|{self.b}|')
        self.label7.pack()
        self.label8 = Label(self.purchases_window, text='\nКоманда с наивысшим рейтингом:')
        self.label8.pack()
        self.label9 = Label(self.purchases_window, text=f'|{"¯" * 68}|')
        self.label9.pack()
        self.label10 = Label(self.purchases_window,
                             text='|{:^11}|{:^11}|{:^13}|{:^13}|{:^9}|'.format('Игрок № 1', 'Игрок № 2', 'Возраст № 1',
                                                                               'Возраст № 2', 'Рейтинг'))
        self.label10.pack()
        self.label11 = Label(self.purchases_window, text=f'|{"-" * 68}|')
        self.label11.pack()

        key = list(self.mp.items())[self.rating.index(max(self.rating))]
        p1, p2 = (str(key[0])[1:-1]).split(', ')
        r1, r2 = (str(key[1])[1:-1]).split(', ')

        self.label12 = Label(self.purchases_window,
                             text='|{:^21}|{:^19}|{:^19}|{:^19}|{:^18}|'.format(p1, p2, r1, r2, max(self.rating)))
        self.label12.pack()
        self.label13 = Label(self.purchases_window, text=f'|{"_" * 68}|')
        self.label13.pack()


root = Tk()
root.title('Лабораторная № 8')
root.geometry('720x320')
root.resizable(False, False)

selection(root)

root.mainloop()
