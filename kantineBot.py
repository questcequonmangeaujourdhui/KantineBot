#!/usr/bin/python3

import sys
import locale
import time
from datetime import date
import requests
import telepot
from pprint import pprint

# locale
locale.setlocale(locale.LC_ALL,'fr_FR')

# today
d = date.today()
filename = d.strftime("%A %-d %B") + '.txt'

# get http
r = requests.get("https://questcequonmangeaujourdhui.github.io/menus/" + filename)

# on weekdays only
if(r.status_code != 200):
    sys.exit(0)

# telegram bot
bot = telepot.Bot('******************************')

try:
    sys.argv[1]
except IndexError:
    response = bot.getUpdates()
    pprint(response)
    sys.exit(0)

bot.sendMessage(sys.argv[1], r.content)
