from cogs.utils import checks
import discord
from discord.ext import commands

class Echo:
    """I'll repeat what you said."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def echo(self, *text):
        """I'll repeat what you said."""

        text = " ".join(text)
        await self.bot.say(text)

    @commands.command()
    @checks.is_owner()
    async def sonar(self, channelid, *, text):
        """I'll repeat what you said and where you want it.
        A modified version of the debug command, with help from Calebj."""

        text = text.replace("\'", "\\\'")
        channelid = self.bot.get_channel(str(channelid))
        return await self.bot.send_message(channelid, text)

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def channelidget(self, ctx):
        """Gets current channel ID immediately."""
        channel = ctx.message.channel
        return await self.bot.say(channel.id)

def setup(bot):
    bot.add_cog(Echo(bot))
