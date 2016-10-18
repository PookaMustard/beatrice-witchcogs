from discord.ext import commands

class Appsearcher:
    """Search for apps on popular application stores"""

    def __init__(self, bot):
        self.bot = bot

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
    bot.add_cog(Appsearcher(bot))
