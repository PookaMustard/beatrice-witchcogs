import discord
from cogs.utils import checks
from bs4 import BeautifulSoup
import aiohttp
from discord.ext import commands

class echo:
    """I'll repeat what you said"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def echo(self, *text):
        """I'll repeat what you said."""

        #Your code will go here
        text = " ".join(text)
        await self.bot.say(text)

def setup(bot):
    bot.add_cog(echo(bot))
