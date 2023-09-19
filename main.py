import telebot
import requests
import json
import webbrowser
from telebot import types
# import sqlite3

API = '924ead372bd558bf00894360020ad829'

name = None

bot = telebot.TeleBot('6578683615:AAHviIwc0llgJLFvH3j1OGSYnp29MoBKQP8')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi! Enter a city:')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp} градусов Цельсия.')
        image = 'sunny.jpeg' if temp > 5.0 else 'cloudy.jpeg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Введено неверное название города.')



# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('http://vitaminpersik.pythonanywhere.com/')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('database.sql')
#     cur = conn.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users (id int auto_increment PRIMARY KEY, name varchar(50), pass varchar(50))''')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'Hello! Enter your name for registration: ')
#     bot.register_next_step_handler(message, user_name)
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Enter your password: ')
#     bot.register_next_step_handler(message, user_pass)
#
#
# def user_pass(message):
#     password = message.text
#     conn = sqlite3.connect('database.sql')
#     cur = conn.cursor()
#     cur.execute(
#         '''INSERT INTO users (name, pass) VALUES (?, ?)''', (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('User list', callback_data='users'))
#     bot.send_message(message.chat.id, f'User {name} is registered.', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     conn = sqlite3.connect('database.sql')
#     cur = conn.cursor()
#     cur.execute('''SELECT * FROM users''')
#     users = cur.fetchall()
#     info = ''
#     for el in users:
#         info += f'Name: {el[1]}, password: {el[2]}\n'
#     cur.close()
#     conn.close()
#     bot.send_message(call.message.chat.id, info)



# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Search')
#     btn2 = types.KeyboardButton('Delete photo')
#     btn3 = types.KeyboardButton('Edit message')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     file = open('bumblebee.jpg', 'rb')
#     # bot.send_photo(message.chat.id, file, reply_markup=markup)
#     bot.send_message(message.chat.id, "Ссылка для скачивания: http://vitaminpersik.pythonanywhere.com/", reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)


# def on_click(message):
#     if message.text == 'Search':
#         bot.send_message(message.chat.id, "I'm searching!")
#     elif message.text == 'Delete photo':
#         bot.send_message(message.chat.id, "All is deleted!")
#     elif message.text == 'Edit message':
#         bot.send_message(message.chat.id, "All is edited!")
#
#
#
# @bot.message_handler(commands=['help'])
# def start_message(message):
#     bot.send_message(message.chat.id, '<b>Help</b> <em>info</em>', parse_mode='html')
#
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Search', url='https://duckduckgo.com/')
#     btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Edit message', callback_data='edit')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Nice photo!', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edited text', callback.message.chat.id, callback.message.message_id)
#
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)