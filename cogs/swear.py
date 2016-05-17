<<<<<<< HEAD
from discord.ext import commands
from datetime import datetime
import pytz
import discord
import asyncio
import aiohttp


import random
import simplify as s
# from main import bot as b


class Swear:
    def __init__(self, bot):
        """
        Here is where I should probably explain what this stuff does
        """
        self.bot = bot
        self.greylist = ["fuck", "shit", "cunt"]
        self.blacklist = ["nigga", "nigger", "kys", "fuck you", "fuck u"]
        self.warnings = ["Please don't swear!", "Don't swear, thanks!"]
        self.ignore = "<@181177004085739520>"

    """
    TO DO
    -----
    Add counting system to black list, on third trigger send message to idiotech via #admin
    ^^ potentially scrap that idea
    """

    async def on_message(self, message):
        print("message recieved")
        print(message.content)
        if message.author.id is not self.ignore:
            print("author id is not bots")
            for i in self.greylist:
                print("greylist checking: "+i)
                if i in message.content:
                    print("checked and found "+i+" from greylist")
                    await s.whisper(message.author, random.choice(self.warnings), self.bot)
                    break

            for j in self.blacklist:
                print("blacklist checking: "+j)
                if j in message.content:
                    print("blacklist triggered")
                    # admin = message.server.get_channel("176304607172100097") # for idiotech server
                    admin = message.server.get_channel("181233418099490826")  # for test server
                    customWarn = message.author.name + " sent a blacklisted phrase '" + j + "' in " \
                        + message.channel.name

                    await self.bot.send_message(admin, customWarn)


def setup(bot):
    bot.add_cog(Swear(bot))
    Swear.on_message = bot.event(Swear.on_message)
=======
import asyncio
import simplify as s


"""
DRAFT VERSION
"""

watchlist = {}
loop = asyncio.get_event_loop()


class Warns:
    def __init__(self, user, bot):
        self.user = user
        self.bot = bot
        self.points = 0
        watchlist.update({self.user: self})
        self.new()

    def new(self):
        self.points += 1
        self.point_check()
        loop.create_task(self.decay)

    async def decay(self):
        time = 120
        while True:
            if time > 0:
                time -= 1
                await asyncio.sleep(1)
            else:
                break
        self.points -= 1
        self.point_check()

    def point_check(self):
        if self.points >= 3:
            loop.create_task(self.warn_user)
        elif self.points == 0:
            del watchlist[self.user]

    async def warn_user(self):
        s.whisper(self.user, "I'm warning you", self.bot)


async def message(bot, message):
    """
    after you decide he used something for which you want to give him a point:

    if message.author in watchlist:
        watchlist['message.author'].new()
    else:
        Warns(message.author, bot)

    Only create the logic for detecting the bad words

    If you want grey words to have different weight than black words
    we can have new_grey and new_black methods instead of new, add different amount of points
    Then for every point loop.create_task(self.decay)
    """
    pass

>>>>>>> refs/remotes/iScrE4m/master
