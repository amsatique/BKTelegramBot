# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import roburger
import os

API_TOKEN = os.environ['API_TOKEN']

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, """ Hi !
    This bot generate a code for some free burgers !
    Type /freebk, *wait 10 sec* while your code is generated and Bon appetit ! """)


# Handle '/start' and '/help'
@bot.message_handler(commands=['freebk'])
def send_code(message):
    bot.reply_to(message, roburger.burgermain() + ". Bon appetit!")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, """Type /freebk, get burgers!""")

bot.polling()
