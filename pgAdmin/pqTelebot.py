import telebot
from telebot import types
from pgAdmin0 import tg_login
import time

TOKEN = '7955204064:AAHfmTZROEy740kQoGG_3kmQUO8fMhWnA8o'

bot = telebot.TeleBot(TOKEN)
user_states = {}
user_data = {}
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Купить подписку")
    btn2 = types.KeyboardButton("Войти в аккаунт")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f"Привет! Я телеграм-бот для оформления подписки.{message.chat.id}", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text == "Войти в аккаунт")
def ask_login(message):
    user_states[message.chat.id] = "waiting_for_login"
    bot.reply_to(message, "Пожалуйста, введите ваш логин:")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "waiting_for_login")
def handle_login(message):
    user_data[message.chat.id] = {'login': message.text.strip()}
    user_states[message.chat.id] = "waiting_for_password"
    bot.reply_to(message, "Теперь введите ваш пароль:")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "waiting_for_password")
def handle_password(message):
    login = user_data[message.chat.id]['login']
    password = message.text.strip()
    user_states[message.chat.id] = None

    correct_password = tg_login(login)  # tg_login возвращает пароль по логину
    if password == correct_password:
        bot.reply_to(message, "Вы успешно вошли в аккаунт!")
    else:
        bot.reply_to(message, "Неверный логин или пароль. Попробуйте ещё раз.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Купить подписку":
        bot.reply_to(message, "поздравляю, вы купили подписку!")
        start= time.time()
    else:
        bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)