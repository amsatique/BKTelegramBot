import telebot
import roburger
import mongo_interact
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
    print("# - Current cmd=freebk")
    holding_burger_generation(message)


# Handle '/about', giving people informations
@bot.message_handler(commands=['about'])
def send_welcome(message):
    print("# - Current cmd=about")
    burgernumber = mongo_interact.MongoInteract().countAllBurgerGenerated()
    bot.reply_to(message, """Over """ + str(burgernumber) + ' ' + hamburger + """ has been generated ! """+thumbsupsign+""" If you like our bot, please put """ + star + star + star + star + star + """ here :
http://telegram.me/storebot?start=bkcodebot""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print("# - Current cmd=none")
    bot.reply_to(message, """Type /freebk, get burgers!""")


def haveAGoodMealString():
    return "\n    " + hamburger + "    Bon appetit!   " + hamburger


def holding_burger_generation(message):
    e = mongo_interact.MongoInteract()
    q = roburger
    g = e.codecountavailable
    if g == 0:
        print('g0')
        bot.reply_to(message, q.burgermain(1)[0] + haveAGoodMealString())
        u = q.burgermain(5)
        print(u)
        e.insertANewCode(u)
        e.updateGeneratedNumber(1)
    elif 0 < g < 5:
        print('g14')
        r = e.getACode()
        bot.reply_to(message, r + haveAGoodMealString())
        u = q.burgermain(2)
        e.insertANewCode(u)
    elif g > 4:
        print('g5or+')
        r = e.getACode()
        bot.reply_to(message, r + haveAGoodMealString())
    else:
        bot.reply_to(message, q.burgermain(1)[0] + haveAGoodMealString())
        e.updateGeneratedNumber(1)
        print("Else? ")

bot.polling()
