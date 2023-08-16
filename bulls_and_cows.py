import random
import tkinter as tk

def new_number(hard):
    numb = set()
    while len(numb) != hard:
        n = random.randrange(0, 10)
        numb.add(str(n))
    return ''.join(list(numb))


def get_num():
    return user.get()

win = tk.Tk()
win.geometry('500x500')


label = tk.Label(win, text='Введи число').pack()
user = tk.Entry(win)
user.pack()
btn1 = tk.Button(win, text='get', command=get_num).pack()


#start_game = input('Выбери уровень сложности: Легко, нажми - 3, Средне - 4, Сложно - 5')
#hidden_number = new_number(int(start_game))
#user = input(f'Введи {len(hidden_number)}-значное число: ')
#while len(user) != len(hidden_number) or user.isalpha():
#    user = input('Введи корректное число: ')




