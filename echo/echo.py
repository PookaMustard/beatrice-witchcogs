import discord
from discord.ext import commands
from cogs.utils import checks
from __main__ import set_cog, send_cmd_help, settings
import importlib
import traceback
import logging
import asyncio
import threading
import datetime
import glob
import os
import time

log = logging.getLogger("red.owner")

class CogNotFoundError(Exception):
    pass

class CogLoadError(Exception):
    pass

class NoSetupError(CogLoadError):
    pass

class CogUnloadError(Exception):
    pass

class OwnerUnloadWithoutReloadError(CogUnloadError):
    pass

class echo:
    """I'll repeat what you said."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def echo(self, *text):
        """I'll repeat what you said."""

        #Your code will go here
        text = " ".join(text)
        await self.bot.say(text)

    @commands.command()
    @checks.is_owner()
    async def sonar(self, serv, *, text):
        """I'll repeat what you said and where you want it.
        
        A modified version of the debug command, with help from Calebj."""

        #Your code will go here
        text = "".join(text)
        text = text.replace("\'", "\\\'")
        local_vars = locals().copy()
        local_vars['bot'] = self.bot
        code = "bot.send_message(bot.get_channel(serv),'"+text+"')"
        python = '```py\n{}\n```'
        result = None

        try:
            result = eval(code, globals(), local_vars)
        except Exception as e:
            await self.bot.say(python.format(type(e).__name__ + ': ' + str(e)))
            return
                    
        if asyncio.iscoroutine(result):
            result = await result

        result = python.format(result)
        censor = (settings.email, settings.password)
        r = "[EXPUNGED]"
        for w in censor:
            if w != "":
                result = result.replace(w, r)
                result = result.replace(w.lower(), r)
                result = result.replace(w.upper(), r)

def setup(bot):
    bot.add_cog(echo(bot))
