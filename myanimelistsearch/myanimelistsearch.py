import discord
from bs4 import BeautifulSoup
import aiohttp
from discord.ext import commands

class MyAnimeListSearch:
    """Commences a search on MyAnimeList"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def anime(self, *text):
        """Returns MAL anime search result using anime name"""

        #Your code will go here
        query=text.replace(" ", "%20")
        await self.bot.say("http://myanimelist.net/anime.php?q="+query)

    @commands.command()
    async def manga(self, text):
        """Returns MAL manga search result using manga name"""

        #Your code will go here
        query=text.replace(" ", "%20")
        await self.bot.say("http://myanimelist.net/manga.php?q="+query)

    @commands.command()
    async def malcharacter(self, text):
        """Returns MAL character search result using char name"""

        #Your code will go here
        query=text.replace(" ", "%20")
        await self.bot.say("http://myanimelist.net/character.php?q="+query)

    @commands.command()
    async def animelist(self, text):
        """Returns a user's MyAnimeList anime list"""

        #Your code will go here
        query=text
        await self.bot.say("http://myanimelist.net/animelist/"+query)

    @commands.command()
    async def mangalist(self, text):
        """Returns a user's MyAnimeList manga list"""

        #Your code will go here
        query=text
        await self.bot.say("http://myanimelist.net/mangalist/"+query)

    @commands.command()
    async def mal(self, text):
        """Returns MAL search result using search name"""

        #Your code will go here
        query=text.replace(" ", "%20")
        await self.bot.say(" http://myanimelist.net/search/all?q="+query)

def setup(bot):
    bot.add_cog(MyAnimeListSearch(bot))
