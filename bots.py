# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 18:54:32 2016

@author: slid3r
"""
from twx.botapi import TelegramBot, ReplyKeyboardMarkup

"""
Setup the bot 2
"""

bot = TelegramBot('207164701:AAF_WoXS9fkYyYJW5y5lfM_XS1wpNDmKqwk')
bot.update_bot_info().wait()
print(bot.username)

"""
Send a message to a user
"""
text = open("newfile.txt",'w')
user_id = int(1368847)

result = bot.send_message(user_id, 'Fuck off').wait()
print >> text,result



"""
Get updates sent to the bot
"""
updates = bot.get_updates(offset=609555499).wait()
for update in updates:
    print >> text, update

"""
Use a custom keyboard
"""
keyboard = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
         ['0']
]
reply_markup = ReplyKeyboardMarkup.create(keyboard)

bot.send_message(user_id, 'please enter a number', reply_markup=reply_markup).wait()


flag = True