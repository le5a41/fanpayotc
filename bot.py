import os
import telebot

TOKEN = os.environ['BOT_TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Бот работает на Render')

print('Бот успешно запущен!')
bot.infinity_polling()
