import os
import random
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def dismiss(win):
    win.grab_release()
    win.destroy()


def openfile():
    try:
        text = open(r'C:\py\test.txt', 'r+')
        return text
    except FileNotFoundError:
        try:
            os.mkdir(r'C:\py')
            text = open(r'C:\py\test.txt', 'w')
            text.close()
            text = open(r'C:\py\test.txt', 'r+')
            return text
        except FileNotFoundError:
            text = open(r'C:\py\test.txt', 'r+')
            return text


class game:
    def __init__(self, main):
        s = ttk.Style()
        s.configure('my.TButton', font='Arial 20 bold')
        a = ttk.Style()
        a.configure('my1.TButton', font='Arial 22')

        self.count = 0
        self.main = main
        self.account = {}
        self.first_click = True
        self.login = ttk.Entry(width=20, justify='center', font='Arial 20 bold')
        self.password = ttk.Entry(width=20, justify='center', font='Arial 20 bold', show='*')
        self.txtl = Label(text='Логин', font='Arial 30 bold')
        self.txtp = Label(text='Пароль', font='Arial 30 bold')
        self.txt = Label(text='Для игры введите ваш логин и пароль', font='Arial 36 bold')
        self.blur = ttk.Button(text='🫣', style='my1.TButton', command=lambda: self.bluring(self.password, self.blur))
        self.button_reg = ttk.Button(text='Зарегистрироваться', style='my.TButton', command=lambda: self.regist())
        self.button_avt = ttk.Button(text='Авторизоваться', style='my.TButton', command=lambda: self.authorization())

        self.txt.place(x=90, y=40)
        self.txtl.place(x=330, y=170)
        self.txtp.place(x=330, y=260)
        self.login.place(x=510, y=175, height=40)
        self.password.place(x=510, y=265, height=40)
        self.blur.place(x=774, y=265, width=42, height=42)
        self.button_avt.place(x=260, y=380)
        self.button_reg.place(x=540, y=380)

    def bluring(self, pas, but):
        if self.count % 2 == 0:
            pas.config(show='')
            but.config(text='🧐')
        else:
            pas.config(show='*')
            but.config(text='🫣')
        self.count += 1

    def authorization(self):
        s_l = self.login.get()
        s_p = self.password.get()

        if len(s_l) == 0 or len(s_p) == 0:
            messagebox.showwarning(title='Ошибка', message='Поле заполнения пусто')

        else:
            file = openfile()
            a = file.readline()[:-1].split(' ')

            while True:
                if a != ['']:
                    self.account[a[0]] = a[1]
                    a = file.readline()[:-1].split(' ')
                else:
                    break

            f_reg = False
            f_p = True
            for i in self.account.items():
                l, p = i
                if s_l == l and s_p == p:
                    f_reg = True
                    break
                elif s_l == l and s_p != p:
                    f_p = False

            if f_reg:
                for widget in self.main.winfo_children():
                    widget.destroy()

                Label(self.main, text=f'Вы успешно авторизовались!', font='Arial 36 bold').place(x=210, y=160)
                button = ttk.Button(self.main, text='Играть', style='my.TButton', command=lambda: self.games())
                button.place(x=460, y=340)

            elif not f_p:
                messagebox.showwarning(title='Ошибка', message='Неверный пароль')
            else:
                messagebox.showwarning(title='Ошибка', message='Такого аккаунта не существует')

    def regist(self):
        win = Toplevel()
        win.geometry('1080x520+430+250')
        win.title('Регистрация')
        win.resizable(False, False)
        win.protocol('WM_DELETE_WINDOW', lambda: dismiss(win))
        win.grab_set()

        login = ttk.Entry(win, width=20, justify='center', font='Arial 20 bold')
        password = ttk.Entry(win, width=20, justify='center',font='Arial 20 bold', show='*')
        txtl = Label(win, text='Логин', font='Arial 30 bold')
        txtp = Label(win, text='Пароль', font='Arial 30 bold')
        txt = Label(win, text='Введите желаемые логин и пароль', font='Arial 36 bold')
        blur = ttk.Button(win, text='🫣', style='my1.TButton', command=lambda: self.bluring(password, blur))
        button_reg = ttk.Button(win, text='Зарегистрироваться', style='my.TButton', command=lambda: registrate())

        txt.place(x=120, y=40)
        txtl.place(x=300, y=170)
        txtp.place(x=300, y=260)
        login.place(x=470, y=175, height=40)
        password.place(x=470, y=265, height=40)
        blur.place(x=735, y=265, width=42, height=42)
        button_reg.place(x=405, y=380)

        def registrate():
            s_l = login.get()
            s_p = password.get()

            if len(s_l) == 0 or len(s_p) == 0:
                messagebox.showwarning(title='Ошибка', message='Поле заполнения пусто')
            else:
                file = openfile()
                a = file.readline()[:-1].split(' ')

                while True:
                    if a != ['']:
                        self.account[a[0]] = a[1]
                        a = file.readline()[:-1].split(' ')
                    else:
                        break

                f_reg = False

                for i in self.account.items():
                    l, p = i
                    if s_l == l:
                        f_reg = True

                if not f_reg:
                    file = openfile()
                    file.seek(0, os.SEEK_END)
                    file.write(f'{s_l} {s_p}\n')
                    file.close()

                    for widget in win.winfo_children():
                        widget.destroy()

                    Label(win, text='Вы успешно зарегистрировались', font='Arial 36 bold').place(x=140, y=200)
                    win.after(2000, lambda: (win.destroy(), win.grab_release()))
                else:
                    messagebox.showwarning(title='Ошибка', message='Такой аккаунт уже существует')

    def games(self):
        for widget in self.main.winfo_children():
            widget.destroy()
        Label(text='Игра', font='Arial 48 bold').place(x=460, y=200)


root = Tk()
root.title('Авторизация')
root.geometry('1080x520+430+250')
root.resizable(False, False)

game(root)

root.mainloop()
