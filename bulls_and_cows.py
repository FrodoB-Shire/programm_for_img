import random
import tkinter as tk


def new_number():
    numb = set()
    while len(numb) != 4:
        n = random.randrange(0, 10)
        numb.add(str(n))
    return ''.join(list(numb))

def click_count():
    global count
    count += 1 
    return str(count)


def print_result():
    count = click_count()
    list_b = []
    list_c = []
    ut = user.get()
    if len(ut) != 4 or ut.isalpha():
        finish.insert(0.0, f'''{count}. Можно ввести только 4 цифры,
Да, это тоже считается за ход:)\n''')
    else:
        for i in ut:
            if i in number and ut.index(i) == number.index(i):
                list_b.append('B')
            elif i in number and ut.index(i) != number.index(i):
                list_c.append('C')
        if ut == number:
            finish.insert(0.0, f'''{count}. Угадал! Число - {ut}. Попыток - {count}
Если хочешь отгадать новое число, закрой это окно и открой снова)''')
            btn = tk.Button(win, text='Проверить  ->', bg='#717875', height=2, width=33).place(x=5, y=200)
        elif len(list_b) == 0 and len(list_c) == 0:
            finish.insert(0.0, f'{count}. {ut} Ничего нет.\n')
        else:
            finish.insert(0.0, f'{count}. {ut} Коров - {len(list_c)}, Быков - {len(list_b)}.\n')
            list_b.clear()
            list_c.clear()
    user.delete(0, tk.END)


global count
count = 0
global number
number = new_number()

win = tk.Tk()
win.geometry('500x600+500+100')
win.config(bg='#0b4a18')
win.resizable(False, False)
win.title('Быки и Коровы')

label_start = tk.Label(win, height=2, width=33, bg='#94a184', text='Введи число')
label_start.place(x=5, y=110)

user = tk.Entry(win, width=30)
user.place(x=30, y=160)

btn = tk.Button(win, text='Проверить  ->', bg='#72b099', height=2, width=33, command=print_result)
btn.place(x=5, y=200)

user_experiments = tk.Text(win, width=61, height=3)
user_experiments.place(x=5, y=5)


global finish
finish = tk.Text(win, width=30, height=30, wrap='word')
finish.place(x=250, y=110)


win.mainloop()
