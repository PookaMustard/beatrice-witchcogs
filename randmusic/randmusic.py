import discord
from discord.ext import commands

class randmusic:
    """Random music!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def highqualityrip(self):
        """Only the best for SilvaGunner."""
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/205762542004469760/Freedom_Planet_Pangu_Lagoon_2_High_Quality_Rip.mp3')

    @commands.command()
    async def elevatormusic(self):
        """All your favorite tunes, played on a $4.99 synth."""
        await self.bot.say('https://soundcloud.com/brianlindner/asriel-rides-an-elevator')

def setup(bot):
    bot.add_cog(randmusic(bot))
