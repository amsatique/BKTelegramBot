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



# API_TOKEN = os.environ['API_TOKEN']
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
    bot.reply_to(message, holding_burger_generation() + "\n    "+hamburger+"    Bon appetit!   " + hamburger)


# Handle '/about', giving people informations
@bot.message_handler(commands=['about'])
def send_welcome(message):
    print("# - Current cmd=about")
    burgernumber = roburger.generated_burger()
    bot.reply_to(message, """Over """ + str(burgernumber) + ' ' + hamburger + """ has been generated ! """+thumbsupsign+""" If you like our bot, please put """ + star + star + star + star + star + """ here :
http://telegram.me/storebot?start=bkcodebot""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print("# - Current cmd=none")
    bot.reply_to(message, """Type /freebk, get burgers!""")


def holding_burger_generation():
    e = mongo_interact.MongoInteract()
    u = roburger
    g = e.codecountavailable
    if g == 0:
        pass
    # TODO Generer un code, le renvoyer au user, lancer 5 generations, sauvegarder vers la base
    elif 0 < g < 5:
        pass
    # TODO prendre un code en db, lancer g+1 generations, sauvegarder vers la base
    elif g > 5:
        pass
    # TODO transmettre un code.
    else:
        print("Else?")
        pass
    # TODO Faire un code, just like before


bot.polling()
