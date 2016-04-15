# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import roburger
import os

API_TOKEN = os.environ['API_TOKEN']

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start','freebk'])
def send_welcome(message):
    bot.reply_to(message, roburger.burgermain())


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()
