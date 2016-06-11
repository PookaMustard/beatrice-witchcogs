import discord
from discord.ext import commands

class randvideos:
    """Random videos!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dchipmunk(self):
        """The one and only dramatic chipmunk."""

        #Your code will go here
        await self.bot.say('https://www.youtube.com/watch?v=a1Y73sPHKxw')

    @commands.command()
    async def nostrongfeelings(self):
        """I am neutral."""

        #Your code will go here
        await self.bot.say('https://www.youtube.com/watch?v=CxK_nA2iVXw')

    @commands.command()
    async def godno(self):
        """PLEASE NO!!!"""

        #Your code will go here
        await self.bot.say('https://www.youtube.com/watch?v=umDr0mPuyQc')
        
def setup(bot):
    bot.add_cog(randvideos(bot))
