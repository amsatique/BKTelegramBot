import telepot
import roburger
import mongo_interact
import os
import time
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton

# Emojis and cute stuff
hourglass = u'\U0000231B'
hamburger = u'\U0001F354'
okHandSign = u'\U0001F44C'
star = u'\U00002B50'
thumbsUpSign = u'\U0001F44D'
clappingHandSign = u'\U0001F44D'
button1 = hamburger+" "+hamburger
button2 = star+star+star+star+star
burgerNumber = 999

# Interaction Strings
welcomeText = """ Hi ! This bot generate a code for some free """ + button1 + """!
# - 1) Press """ + button1 + """, get a code!
# - 2) Press """ + button2 + """, give your feedback!
# - Bon Appetit ! """
aboutText = """Over """ + str(burgerNumber) + ' ' + hamburger + """ has been generated ! """+thumbsUpSign+"""
Like our bot? please give """ + button2 + """ on StoreBot :
>> http://telegram.me/storebot?start=bkcodebot <<"""

API_TOKEN = os.environ['API_TOKEN']
bot = telepot.Bot(API_TOKEN)


def handle(message):
    content_type, chat_type, chat_id = telepot.glance(message)
    print(content_type, chat_type, chat_id)

    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=button1), KeyboardButton(text=button2)]
    ])

    if content_type != 'text':
        return

    feedback = message['text'].lower()
    global burgerNumber
    if feedback == '/freebk':
        holding_burger_generation(chat_id, keyboard)
    elif feedback == button1:
        holding_burger_generation(chat_id, keyboard)
    elif feedback == button2:
        burgerNumber = mongo_interact.MongoInteract().countAllBurgerGenerated()
        bot.sendMessage(chat_id, aboutText, reply_markup=keyboard)
    elif feedback == '/start':
        bot.sendMessage(chat_id, welcomeText, reply_markup=keyboard)
    elif feedback == '/about':
        burgerNumber = mongo_interact.MongoInteract().countAllBurgerGenerated()
        bot.sendMessage(chat_id, aboutText, reply_markup=keyboard)
    else:
        bot.sendMessage(chat_id, "Press " + button1 + ", get burgers!", reply_markup=keyboard)


def have_a_good_meal_string():
    return "\n    " + hamburger + "    Bon appetit!   " + hamburger


def holding_burger_generation(chat_id, keyboard):
    e = mongo_interact.MongoInteract()
    q = roburger
    g = e.codecountavailable
    if g == 0:
        print('g0')
        bot.sendMessage(chat_id, q.burgermain(1)[0] + have_a_good_meal_string(), reply_markup=keyboard)
        u = q.burgermain(5)
        print(u)
        e.insertANewCode(u)
        e.updateGeneratedNumber(1)
    elif 0 < g < 5:
        print('g14')
        r = e.getACode()
        bot.sendMessage(chat_id, r + have_a_good_meal_string(), reply_markup=keyboard)
        u = q.burgermain(2)
        e.insertANewCode(u)
    elif g > 4:
        print('g5or+')
        r = e.getACode()
        bot.sendMessage(chat_id, r + have_a_good_meal_string(), reply_markup=keyboard)
    else:
        print("Else? ")
        bot.sendMessage(chat_id, q.burgermain(1)[0] + have_a_good_meal_string(), reply_markup=keyboard)
        e.updateGeneratedNumber(1)

bot.message_loop(handle)
print('Ready to serve..')
while 1:
    time.sleep(10)