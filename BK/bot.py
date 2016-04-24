import telebot
import roburger
import os

# Emojis and cute stuff
hourglass = u'\U0000231B'
hamburger = u'\U0001F354'
okhandsign = u'\U0001F44C'
star = u'\U00002B50'
thumbsupsign = u'\U0001F44D'
clappinghandsign = u'\U0001F44D'


API_TOKEN = os.environ['API_TOKEN']
bot = telebot.TeleBot(API_TOKEN)


# Handle '/start and /help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, """ Hi ! This bot generate a code for some free """ + hamburger + """ """ + hamburger + """!
# - Type /freebk
# - """+hourglass+""" for 10 sec """+hourglass+"""
# - Bon appetit ! """)


# Handle '/freebk', our main stuff
@bot.message_handler(commands=['freebk'])
def send_code(message):
    bot.reply_to(message, roburger.burgermain() + "\n    "+hamburger+"    Bon appetit!   " + hamburger)


# Handle '/about', giving people informations
@bot.message_handler(commands=['about'])
def send_welcome(message):
    burgernumber = roburger.generated_burger()
    bot.reply_to(message, """Over """ + str(burgernumber) + ' ' + hamburger + """ has been generated ! """+thumbsupsign+""" If you like our bot, please put """ + star + star + star + star + star + """ here :
http://telegram.me/storebot?start=bkcodebot""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, """Type /freebk, get burgers!""")

bot.polling()
