# Importing the required modules from the telebot library
import telebot
from telebot import types

# Telegram bot token obtained from the BotFather
with open('tele_token.txt', 'r') as f:
    token = f.read().strip()

# Creating an instance of the TeleBot class using the provided token
bot = telebot.TeleBot(token)

# That's me (:
bot_creator = "@IMYdev"
