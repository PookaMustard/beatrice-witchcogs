import discord 
from discord.ext import commands 
 
class intercommands: 
     """Random interactive commands!""" 
 
    def __init__(self, bot): 
         self.bot = bot 
 
    @commands.command(pass_context=True)
    async def riprespect(self, ctx): 
        """Pay your respects. Or not."""
        message = ctx.message
 
        #Your code will go here 
        await self.bot.say("Send \"F\" to pay respects.")
        response = await self.bot.wait_for_message(author=message.author)
        if response.content.lower().strip() == "f":
            await self.bot.say("Rest in Peace.")
        else:
            await self.bot.say("I'm sorry. :_(")
              
    @commands.command()
    async def praise(self, user : discord.Member):
        """Praises the mentioned member"""
        praise = [user.mention + " is great!!", "Praise " + user.mention + "!", user.mention + "? That person is great!",
                 "We can all agree that we all love you, " + user.mention + ".", "You're a happy person, " + user.mention + ".", "May praise be upon " + user.mention + "!"]
        await self.bot.say(randchoice(praise))

def setup(bot):
    bot.add_cog(intercommands(bot))
