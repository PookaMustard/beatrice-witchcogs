import discord 
from discord.ext import commands 
 
class intercommands: 
     """Random quotes!""" 
 
     def __init__(self, bot): 
         self.bot = bot 
 
     @commands.command(pass_context=True)
     async def riprespect(self, ctx): 
         """No. Ice."""
         message = ctx.message
 
         #Your code will go here 
         await self.bot.say("Press F to pay respects.")
         response = await self.bot.wait_for_message(author=message.author)
         if response.content.lower().strip() == "f":
              await self.bot.say("Rest in Peace.")
         else:
              await self.bot.say("I'm sorry. :_(")

def setup(bot):
    bot.add_cog(intercommands(bot))
