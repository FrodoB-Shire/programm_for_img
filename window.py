import tkinter as tk
from tkinter import *
from def_ex import add_xlsx, add_info_to_db_msk, add_info_to_db_spb, chek_city, search_in_db, text_handler
from from_db import xlsx_from_msk, xlsx_from_spb


def btn_msk():
    if chek_city() == 'ИМГ x Voicia Москва':
        data = search_in_db()
        add_xlsx(data)
        add_info_to_db_msk()
    else:
        Error_window = tk.Tk()
        Error_window.title('Ошибка')
        Error_window.geometry('300x100+650+390')
        Error_window.attributes("-topmost", True)
        Error_window.resizable(False, False)
        label = tk.Label(Error_window, text='Здесь номера СПб. Нажми другую кнопку')
        label.pack()


def btn_spb():
    data = search_in_db()
    if chek_city() == 'ИМГ x Voicia Санкт-Петербург':
        data = search_in_db()
        add_xlsx(data)
        add_info_to_db_spb()
    else:
        Error_window = tk.Tk()
        Error_window.title('Ошибка')
        Error_window.geometry('300x100+650+390')
        Error_window.attributes("-topmost", True)
        Error_window.resizable(False, False)
        label = tk.Label(Error_window, text='Здесь номера Мск. Нажми другую кнопку')
        label.pack()


def from_msk():
    xlsx_from_msk()


def from_spb():
    xlsx_from_spb()


def without_db():
    data = text_handler()
    add_xlsx(data)


def open_file():
    # fd.askopenfilename()
    pass


def save_file():
    pass



def win_info_voisa():
    info_voisa = tk.Tk()
    info_voisa.title("Инфо по воису")
    info_voisa.geometry('1000x200+300+300')
    info_voisa.resizable(False, False)
    info_voisa.config(bg='black')
    label_info = tk.Label(info_voisa,
                          bg='black',
                          foreground='white',
                          font=('Arial', 14),
                          text="""1. Кнопка 'Выгрузить с проверкой Мск/СПб'. Работает по принципу проверки на дубли в доке загрузки 
    базы.
    В файл xlsx попадают только уникальные номера, и подгружаются в бд. Не работает без result.json """)
    label_info.place(x=0, y=0)
    label_info_2 = tk.Label(info_voisa,
                            bg='black',
                            foreground='white',
                            font=('Arial', 14),
                            text="""2. Кнопка 'Выгрузка БД Мск/СПб' Выгружает все номера из бд по городу. result.json не нужен""")
    label_info_2.place(x=0, y=90)
    label_info_3 = tk.Label(info_voisa,
                            bg='black',
                            foreground='white',
                            font=('Arial', 14),
                            text="""3. Просто выгружает номера из result.json без взаимодействия с бд.""")
    label_info_3.place(x=0, y=120)


def voisa_win():
    win = tk.Tk()
    win.title('Voisa')
    win.geometry('370x123+650+390')
    btn_1 = tk.Button(win, text='Выгрузить с проверкой Мск',
                      width=25,
                      height=2,
                      command=btn_msk)
    btn_1.grid(row=0, column=0)
    btn_2 = tk.Button(win, text='Выгрузить без проверки',
                      width=53,
                      height=2,
                      command=without_db)
    btn_2.grid(row=2, column=0, columnspan=2)
    btn_3 = tk.Button(win, text='Выгрузка бд Мск',
                      width=25,
                      height=2,
                      command=from_msk)
    btn_3.grid(row=1, column=0)
    btn_4 = tk.Button(win, text='Выгрузить с проверкой СПб',
                      width=25,
                      height=2,
                      command=btn_spb)
    btn_4.grid(row=0, column=1)

    btn_6 = tk.Button(win, text='Выгрузка бд СПб',
                      width=25,
                      height=2,
                      command=from_spb)
    btn_6.grid(row=1, column=1)


def empty_func():
    Error_window = tk.Tk()
    Error_window.title('Тут пока ничего нет')
    Error_window.geometry('300x100+650+390')
    label = tk.Label(Error_window, text='Кнопка пока не работает:)')
    label.pack()


win_main = tk.Tk()
win_main.title("Тест")
win_main.geometry('532x250+500+300')
win_main.resizable(False, False)

mainmenu = Menu(win_main)
win_main.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
info = Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Open_file', command=open_file)
filemenu.add_command(label='Save_file', command=save_file)
info.add_command(label='info_voisa', command=win_info_voisa)

mainmenu.add_cascade(label='File', menu=filemenu)
mainmenu.add_cascade(label='Settings')
mainmenu.add_cascade(label='info', menu=info)

btn_vois = tk.Button(win_main, text='Бот Voisa',
                     bg='#737875',
                     width=15,
                     height=5,
                     relief=tk.RAISED,
                     command=voisa_win)
btn_vois.place(y=40, x=2)

btn_1 = tk.Button(win_main, text='Пусто',
                  width=15,
                  height=5,
                  relief=tk.RAISED,
                  command=empty_func)
btn_1.place(y=150, x=2)

btn_2 = tk.Button(win_main, text='Пусто',
                  width=15,
                  height=5,
                  relief=tk.RAISED,
                  command=empty_func)
btn_2.place(y=40, x=140)

btn_3 = tk.Button(win_main, text='Пусто',
                  width=15,
                  height=5,
                  relief=tk.RAISED,
                  command=empty_func)
btn_3.place(y=150, x=140)

btn_4 = tk.Button(win_main, text='Пусто',
                  width=15,
                  height=5,
                  relief=tk.RAISED,
                  command=empty_func)
btn_4.place(y=40, x=278)

btn_5 = tk.Button(win_main, text='Пусто',
                  width=15,
                  height=5,
                  relief=tk.RAISED,
                  command=empty_func)
btn_5.place(y=150, x=278)

btn_6 = tk.Button(win_main, text='Пусто',
                  width=15,
                  height=5,
                  relief=tk.RAISED,
                  command=empty_func)
btn_6.place(y=40, x=416)

btn_7 = tk.Button(win_main, text='Пусто',
                  width=15,
                  height=5,
                  relief=tk.RAISED,
                  command=empty_func)
btn_7.place(y=150, x=416)
win_main.mainloop()
