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
     async def insult(self, user : discord.Channel):
         """Insults the mentioned member"""
 
         #Your code will go here
 #        quote=int(random.randint(1,2))
         if user.id == self.bot.user.id:
             return await self.bot.say("You cannot insult me!")
         quote=1
         if quote==1:
             await self.bot.say(user.mention + " is incompetent!")

def setup(bot):
    bot.add_cog(intercommands(bot))
