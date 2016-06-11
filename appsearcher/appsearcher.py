import discord
import re
from bs4 import BeautifulSoup
import aiohttp
from discord.ext import commands

class appsearcher:
    """Search for apps on popular application stores"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gog(self, *text):
        """Returns GOG search results using game name
            Type %gog gamecount for the number of games"""

        #Your code will go here
        if text[0]=='gamecount':
            url = "https://www.gog.com/games?sort=bestselling&page=1" #build the web adress
            async with aiohttp.get(url) as response:
                soupObject = BeautifulSoup(await response.text(), "html.parser") 
            try:
                count_unabridged = soupObject.find(class_='header__title').get_text()
                count = count_unabridged.replace('  DRM-FREE GAMES     ', '')
                count = count.replace('\n        ', '')
                await self.bot.say("There are " + count + " games on GOG today.")
            except:
                await self.bot.say("Couldn't load amount of DRM-free games on GOG. There must be an error.")
        else:
            text = " ".join(text)
            query=text.replace(" ", "%20")
            await self.bot.say("https://www.gog.com/games?sort=bestselling&search="+query)

    @commands.command()
    async def itch(self, *text):
        """Returns itch.io search results using item name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "+")
        await self.bot.say("https://itch.io/search?q="+query)

    @commands.command()
    async def steamid(self, text):
        """Returns Steam game page using the steam appid"""

        #Your code will go here
        await self.bot.say("http://store.steampowered.com/app/"+text+"/")
        
    @commands.command()
    async def steamuser(self, *text):
        """Returns Steam user page using custom user ID"""

        #Your code will go here
        text = " ".join(text)
        await self.bot.say("http://steamcommunity.com/id/"+text+"/")

    @commands.command()
    async def steamsearch(self, *text):
        """Returns Steam search results using game name"""

        #Your code will go here
#        if text=='gamecount':
#            url = "http://store.steampowered.com/search/#sort_by=_ASC&tags=-1&category1=998&page=1"
#            async with aiohttp.get(url) as response:
#                soupObject = BeautifulSoup(await response.text(), "html.parser") 
#            try:
#                count_unabridged = soupObject.find(class_='search_pagination_left').get_text()
#                count = count_unabridged.replace('				showing 1 - 25 of ', '')
#                await self.bot.say("There are " + count + " apps on Steam today.")
#            except:
#                await self.bot.say("Couldn't load amount of apps on Steam. There must be an error.")
#        else:
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("http://store.steampowered.com/search/?snr=1_4_4__12&term="+query)

    @commands.command()
    async def humbundle(self, *text):
        """Returns Humble Bundle search results using game name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://www.humblebundle.com/store/search/search/"+query)

    @commands.command()
    async def origin(self, *text):
        """Returns Origin search results using game name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://www.origin.com/en-ie/store/browse?q="+query)

    @commands.command()
    async def gplay(self, *text):
        """Returns Google Play search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://play.google.com/store/search?q="+query)

    @commands.command()
    async def ios(self, *text):
        """Returns Apple Appstore search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "-")
        await self.bot.say("http://www.apple.com/us/search/"+query)

    @commands.command()
    async def winstore(self, *text):
        """Returns Windows Store search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "+")
        await self.bot.say("https://www.microsoft.com/en-us/newsearch/result.aspx?q="+query+"&form=apps")

    @commands.command()
    async def xb(self, *text):
        """Returns Xbox Store search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "+")
        await self.bot.say("http://www.xbox.com/en-us/Search?q="+query)

    @commands.command()
    async def ps(self, *text):
        """Returns PlayStation search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://store.playstation.com/#!/en-us/search/q="+query)

    @commands.command()
    async def nintendo(self, *text):
        """Returns Nintendo eShop search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "+")
        await self.bot.say("http://www.nintendo.com/search/#/results/"+query+"/1")


def setup(bot):
    bot.add_cog(appsearcher(bot))
