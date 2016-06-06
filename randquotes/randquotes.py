 import discord 
 from random import randint 
 from random import choice as randchoice 
 from discord.ext import commands 
 
 
 class randquotes: 
     """Random quotes!""" 
 
 
     def __init__(self, bot): 
         self.bot = bot 
 
     @commands.command() 
     async def steam(self): 
         """No. Ice.""" 
 
         #Your code will go here 
         return await self.bot.say("In order to use Steam, you have to sign yourself into a contract which basically says \"YOU OWN NOTHING.\" The end result is that you end up buying licenses to games, which they can revoke anytime they wanted. They require the internet for the validation of licenses, which shouldn't be a requirement to play single player games. This results in an ecosystem that basically controls the titles you owned and gives you none of it, forcing you to stay into the ecosystem through the client to play the games you bought even if you don't want the client.")
         return await self.bot.say("The best part about all of this is that they can change their contract terms and retroactively apply it onto all the games bought under the previous term. If you don't accept the changes, your account is terminated along with the licenses you've bought under the old terms. You only get to keep the licenses you bought under the old terms IF you agree to them retroactively applying the new terms onto them.\nThe end.")

def setup(bot):
    bot.add_cog(randquotes(bot))
