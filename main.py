import json
import openpyxl
import sqlite3 as sq


def open_json():
    with open('result.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
    return text


def chek_city():
    json_file = open_json()
    return json_file['name']


def create_database():
    with sq.connect('dates.db') as con:   # Создает таблицу bot_voisa
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS bot_voisa_msk(
                numbers_m TEXT,
                message_m TEXT)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS bot_voisa_spb(
                numbers_s TEXT,
                message_s TEXT)""")


# Достает все номера из БД
def take_from_database():
    create_database()
    numbers_from_sql = []
    with sq.connect('dates.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT numbers_m , message_m, numbers_s, message_s
                    FROM bot_voisa_msk, bot_voisa_spb""")
        for a in cur:
            number, none_value = a
            numbers_from_sql.append(number)
    return numbers_from_sql


def text_handler():
    num_list = []
    messages_list = []
    text = open_json()
    for i in text['messages']:
        if i['text'] == '':
            print(i)
        else:
            number, *client = i['text']
            for y in client:
                if type(y) == dict:
                    client.remove(y)
            num_list.append(number)
            messages_list.append(client)
# Делает список строк. 1 строка - 1 сообщений
    messages_list_str = []
    for i in messages_list:
        message_str = ''.join(i)
        messages_list_str.append(message_str)
# Удаляет лишние символы из сообщения клиента
    chars_to_remove = ['BOT', 'CLIENT', '\n',
                       'Контроль', 'Перезвон', 'менеджером']
    for index, i in enumerate(messages_list_str):
        for chars in chars_to_remove[0:3:]:
            i = i.replace(chars, ' ')
            messages_list_str[index] = i
# Оставляет только номер телефона
    for index, i in enumerate(num_list):
        list_i = i.split()
        number = list_i[0]
        num_list[index] = number
    tuple_num_message = num_list, messages_list_str
    return tuple_num_message


def search_in_db():
    nums = []
    mess = []
    numbers, messages = text_handler()
    for index in range(len(numbers)):
        if numbers[index] not in take_from_database():
            nums.append(numbers[index])
            mess.append(messages[index])
    return nums, mess


def add_xlsx(num_mes):   # Создает и заполняет excel файл
    column_A, column_B = num_mes
    book = openpyxl.Workbook()
    sheet = book.create_sheet('BOT_Numbers')
    book.remove(book.active)
    for i, name in enumerate(column_A):
        sheet[f'A{i+1}'] = name
    for i, name in enumerate(column_B):
        sheet[f'B{i+1}'] = name
    book.save('numbers.xlsx')
    book.close()


# Добавляет в БД последнюю дату из обрабатываемой выгрузки и дату сейчас
def add_info_to_db_msk():
    info = text_handler()
    numbers, messages = info
    for i in range(0, len(numbers)):
        for_database = numbers[i], messages[i]
        with sq.connect('dates.db') as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO bot_voisa_msk
                        VALUES(?, ?)""", for_database)


def add_info_to_db_spb():
    info = text_handler()
    numbers, messages = info
    for i in range(0, len(numbers)):
        for_database = numbers[i], messages[i]
        with sq.connect('dates.db') as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO bot_voisa_spb
                        VALUES(?, ?)""", for_database)
