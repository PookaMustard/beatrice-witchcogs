import discord
import requests
from discord.ext import commands

headers = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36"

class isitdown:
    """Checks if a website is down or up."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def isitdown(self, url):
        """Checks if a website is down or up."""
        if url=="":
                await self.bot.say("You haven't entered a website to check.")
        if "http://" in url:
                x=2
        elif "https://" in url:
                x=3
        else:
                url ="http://" + url
        try:
                while True:
                        response = requests.get(url, headers={'user_agent': headers}, timeout=15)
                        if response.status_code==200:
                                    await self.bot.say("The website is up and running.")
                                    break
                        await self.bot.say("The website is down.")
                        break
        except requests.exceptions.Timeout:
                await self.bot.say("The website is down.")
        except requests.exceptions.ConnectionError:
                await self.bot.say("The website is down.")
        

def setup(bot):
    bot.add_cog(isitdown(bot))
