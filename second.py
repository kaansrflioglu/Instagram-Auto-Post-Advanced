import os

from instabot import Bot
import requests


def getLink(link):
    r = requests.get(link)
    with open('00.jpeg', 'wb') as f:
        f.write(r.content)


def share(username, password, artist, location, date):
    bot = Bot()
    bot.login(username=username,password=password)
    tags = "#photo #sunset #moon"
    bot.upload_photo("00.jpeg",caption=artist+"\n\n"+location+"\n\n"+date+"\n\n"+tags)

def delete():
    os.remove("00.jpeg.REMOVE_ME")