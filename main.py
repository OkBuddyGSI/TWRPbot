from botcommands import *
from telebot import util

@bot.message_handler(commands=['start', 'request'])
def command_handler(m):
    command(m)

telebot.apihelper.RETRY_ON_ERROR = True

bot.infinity_polling()
