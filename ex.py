from tkinter import *


def qwer():
    user_inp = user.get()
    if user_inp == '1':
        text_win.insert(0.1, f'{type(user_inp)} - 1\n')
    elif user_inp == '2':
        text_win.insert(0.0, f'{type(user_inp)} - 2\n')
    else:
        text_win.insert(0.0, f'Вы ввели текст {type(user_inp)}\n')



win = Tk()
win.geometry('500x500')

user = Entry(win)
user.pack()

btn = Button(win, text='проверить', command=qwer)
btn.pack()

global text_win
text_win = Text(win)
text_win.pack()

win.mainloop()