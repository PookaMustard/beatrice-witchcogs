import discord 
from discord.ext import commands
from random import randint
from random import choice as randchoice
from cogs.utils import checks
from __main__ import set_cog, send_cmd_help, settings
 
class randquotes: 
    """Random quotes!""" 
 
    def __init__(self, bot): 
        self.bot = bot 
 
    @commands.command() 
    async def steam(self): 
        """No. Ice.""" 
 
        #Your code will go here 
        await self.bot.say("In order to use Steam, you have to sign yourself into a contract which basically says \"YOU OWN NOTHING.\" The end result is that you end up buying licenses to games, which they can revoke anytime they wanted. They require the internet for the validation of licenses, which shouldn't be a requirement to play single player games. This results in an ecosystem that basically controls the titles you owned and gives you none of it, forcing you to stay into the ecosystem through the client to play the games you bought even if you don't want the client.")
        await self.bot.say("The best part about all of this is that they can change their contract terms and retroactively apply it onto all the games bought under the previous term. If you don't accept the changes, your account is terminated along with the licenses you've bought under the old terms. You only get to keep the licenses you bought under the old terms IF you agree to them retroactively applying the new terms onto them.")
        await self.bot.say("The end.")
         
    @commands.command(pass_context=True) 
    async def mn9(self, ctx): 
        """Mighty No. 9: Thoughts"""
        server = ctx.message.server
        if server.id=='174932651201921024':
            return
        else:
            mn9 = ["MIGHTY NO. 9 IS GETTING MIGHTIED OUTTA THE PLANET.", "Mighty No. 9? My pizza is late!!", "Mighty No. 9? How *unmighty*.",
                   "A thousand years would pass and still Mighty No. 9 would be quite the laughing stock...don't you think?", "Even Lambdadelta hates Mighty No. 9.", "4 million dollars did not save this game from turning into a flipping flop.",
                   "https://cdn.discordapp.com/attachments/174932651201921024/194933396621885452/13516359_666046493542630_5062462651910223041_n.png",
                   "https://images-2.discordapp.net/.eJwNx8ERwiAQAMBeKAA4EjnI30-aYJAgiSYeA5fx4di77m8_4my7mMTKXPuk1LL1RG2RnanFkmUhKnuOdesy0aEic0zrkV_cFeDgLWowYIYB0dpRgR_dPxY9OIcODSg-j9veArlE7_t85Q7NWMAnmdAgXLSWj1rE9wcErysP.1U6QQakVUAaZnjyk_Asamb9Bx5Y.jpg?width=287&height=300",
                   "https://67.media.tumblr.com/4fe613d88b23c4f10bc0194409aaf68e/tumblr_nommbxz03Q1qfb2lao1_540.png", "Mighty No. NEIN",
                   "Why buy the game if you can get it for free? Why buy games when you can get them for free, either? https://drive.google.com/folderview?id=0B7NlRHZE9SWSc2hucUlhdmhmMVU&usp=sharing",
                   "Shovel Knight is the good; Azure Gunner Striker is the bad; Mighty Number 9 must be the ugly..."]
            return await self.bot.say(randchoice(mn9))
        

def setup(bot):
    bot.add_cog(randquotes(bot))
