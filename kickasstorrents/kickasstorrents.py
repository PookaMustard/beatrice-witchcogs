import discord
from discord.ext import commands

class kickasstorrents:
    """Search for files on kat.cr"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kat(self, *text):
        """Returns kat torrent search results using item name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(".", "")
        query=query.replace(" ", "%20")
        await self.bot.say("***WARNING:*** May or may not include NSFW content\nhttps://kat.cr/usearch/"+query)

def setup(bot):
    bot.add_cog(kickasstorrents(bot))
