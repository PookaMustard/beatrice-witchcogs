import discord
from discord.ext import commands

class ThePirateBay:
    """Search for files on thepiratebay.org"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tpb(self, *text):
        """Returns TPB torrent search results using item name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(".", "")
        query=query.replace(" ", "%20")
        await self.bot.say("***WARNING:*** May or may not include NSFW content\nhttps://thepiratebay.org/search/" + query + "/0/99/0")

def setup(bot):
    bot.add_cog(thepiratebay(bot))
