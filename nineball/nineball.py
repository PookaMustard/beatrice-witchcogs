import discord
from random import randint
from random import choice as randchoice
from discord.ext import commands

class nineball:
    """Asks Beatrice's 9-Ball a question"""

    def __init__(self, bot):
        self.bot = bot
        self.ball = ["As I see it, yes!", "According to Lambdadelta, it is certain!", "It is decidedly so!", "Most likely.", "The outlook is good.",
             "Yes. That's where the signs point!", "Without a doubt!", "Yes.", "Yes, definitely!", "You may rely on it.", 
             "Don't count on it.", "My reply is no!! *cackles*", "My sources say no.", "The outlook is not good.", "Very doubtful.",
             "Not a chance in hell!", "I refuse.", "The odds of that happening are...zero!", "The truth of the matter, is no." "Lambdadelta certainly says no."]

    @commands.command(name="9", aliases=["9ball"])
    async def _9ball(self, *question):
        """Asks Beatrice's 9-Ball a question

        Question must end with a question mark.
        """
        question = " ".join(question)
        if question.endswith("?") and question != "?":
            return await self.bot.say("`" + randchoice(self.ball) + "`")
        else:
            return await self.bot.say("That doesn't look like a question.")

def setup(bot):
    bot.add_cog(nineball(bot))
