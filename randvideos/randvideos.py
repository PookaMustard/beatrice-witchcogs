import discord
from discord.ext import commands

class randvideos:
    """Random videos!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dchipmunk(self):
        """The one and only dramatic chipmunk."""
        await self.bot.say('https://www.youtube.com/watch?v=a1Y73sPHKxw')

    @commands.command()
    async def getready(self):
        """I said get ready."""
        await self.bot.say('https://www.youtube.com/watch?v=ArF8lrby8xY')

    @commands.command()
    async def nostrongfeelings(self):
        """I am neutral."""
        await self.bot.say('https://www.youtube.com/watch?v=CxK_nA2iVXw')

    @commands.command()
    async def godno(self):
        """PLEASE NO!!!"""
        await self.bot.say('https://www.youtube.com/watch?v=umDr0mPuyQc')
        
def setup(bot):
    bot.add_cog(randvideos(bot))
