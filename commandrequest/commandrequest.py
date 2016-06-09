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


class commandrequest:

    def __init__(self, bot):
        self.bot = bot
        self.setowner_lock = False

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def commandrequest(self, ctx, *, command):
        """Sends a request for a new command."""

        local_vars = locals().copy()
        local_vars['bot'] = self.bot
        code = "bot.send_message(bot.get_channel('190590897480663040'),'"+command+"')"
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
        if not ctx.message.channel.is_private:
            censor = (settings.email, settings.password)
            r = "[EXPUNGED]"
            for w in censor:
                if w != "":
                    result = result.replace(w, r)
                    result = result.replace(w.lower(), r)
                    result = result.replace(w.upper(), r)


def setup(bot):
    bot.add_cog(commandrequest(bot))
