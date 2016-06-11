import discord
import random
from discord.ext import commands

class beatrice:
    """Commands for Beatrice. *cackle*cackle*cackle*"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def beatoquote(self):
        """Random Beatrice Ushiromiya quotes"""
        quote=int(random.randint(1,4))
        #Your code will go here
        if quote==1:
            await self.bot.say("You are incompetent!!")
        elif quote==2:
            await self.bot.say("Too bad, witches don't refo~rm!" )
        elif quote==3:
            await self.bot.say("This itself is a miracle. Magic. The proof of my existence!")
        elif quote==4:
            await self.bot.say("Yes, that expression fits you the most. That caring expression of yours really doesn't match me after all. My back was itching, and I was frantically trying to wishtand it. *cackle* *cackle* *cackle*!!")

    @commands.command()
    async def beatosmirk(self):
        """My own smirk."""

        #Your code will go here
        await self.bot.say('http://shounen.chungyc.org/wp-content/uploads/2009/09/next.jpg')

    @commands.command()
    async def beatolaugh(self):
        """My own laugh."""

        #Your code will go here
        await self.bot.say('http://i.imgur.com/vzrnRZo.png')

    @commands.command()
    async def beatodetermined(self):
        """My own determination."""
        await self.bot.say('http://media.animevice.com/uploads/0/2262/137719-vlcsnap_40273_super.png')

    @commands.command()
    async def beatosmile(self):
        """My own smile."""
        await self.bot.say('https://kakeracomplex.files.wordpress.com/2011/05/beatrce.jpg')

    @commands.command()
    async def beatotroll(self):
        """Did someone say 'small bombs' here?"""

        #Your code will go here
        await self.bot.say('http://static.tvtropes.org/pmwiki/pub/images/D_1684.png')

    @commands.command()
    async def beatostare(self):
        """My own stare."""

        #Your code will go here
        await self.bot.say('http://i.imgur.com/R8ziwXI.jpg')

    @commands.command()
    async def beatoportrait(self):
        """My portrait."""

        #Your code will go here
        await self.bot.say('http://vignette1.wikia.nocookie.net/politicsandwar/images/2/2c/Beatrice_Portrait.png/revision/latest?cb=20150425193618')

def setup(bot):
    bot.add_cog(beatrice(bot))

