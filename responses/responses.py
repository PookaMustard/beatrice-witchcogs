import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import time

class sao:
    """Positive response to SAO comments"""
    
    def __init__(self, bot):
        self.bot = bot
        self.timecheck = {}
        self.cooldown = 60*3 #60 seconds times the required minutes

    async def check_sao(self, message):
        saocheck = ['sao', 'sword art online', 'sword art offline']
        if 'sao' in message.content.split() or 'sword art online' in str(message.content) or 'sword art offline' in str(message.content) and message.author.id != self.bot.user.id:
            if message.channel.id not in self.timecheck or (time.time() - self.timecheck[message.channel.id]) > self.cooldown:
                self.timecheck[message.channel.id] = time.time()
                sao = ["SAO? Why don't you read Umineko no Naku Koro ni instead?", "I won't mute you for five minutes for mentioning SAO.",
                    "On another server, you'd be muted for mentioning SAO. Talk about it a lot here!"]
                await self.bot.send_message(message.channel, randchoice(sao))

def setup(bot):
    n = sao(bot)
    bot.add_listener(n.check_sao, "on_message")
    bot.add_cog(n)
