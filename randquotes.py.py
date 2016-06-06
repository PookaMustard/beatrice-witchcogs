 import discord 
 from random import randint 
 from random import choice as randchoice 
 from discord.ext import commands 
 
 
 class randquotes: 
     """Random quotes!""" 
 
 
     def __init__(self, bot): 
         self.bot = bot 
 
     @commands.command() 
     async def randquotes(self): 
        """Random Quote""" 
 
         #Your code will go here 
         return await self.bot.say("Insert Something Here.) 
