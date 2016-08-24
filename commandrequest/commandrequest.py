from discord.ext import commands
from cogs.utils import checks
from .utils.dataIO import fileIO
import json
import os


class CommandRequest:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def commandrequest(self, ctx, *, command):
        """Sends a request for a new command.
        A modified version of the debug command, with help from Calebj."""
        channelid = loadauth()
        if channelid == '':
            return await self.bot.say("You haven't set the channel ID for " +
                                      "command requests correctly. Use " +
                                      "`[p]savechannelid [your channel ID " +
                                      "here]` to set the command request " +
                                      "channel. Use Discord's Developer " +
                                      "Mode to copy the ID of the channel" +
                                      "you wish to set for receiving " +
                                      "command requests.")
        author = ctx.message.author
        server = ctx.message.server
        command = command + " -- Command requested by " + \
            author.name + " from " + "{}".format(server.name)
        command = command.replace("\'", "\\\'")
        channelid = self.bot.get_channel(str(channelid))
        return await self.bot.send_message(channelid, command)

    @commands.command()
    @checks.is_owner()
    async def savechannelid(self, channelid):
        """Saves this channel for commandrequests."""
        saveauth(channelid)
        channelidstring = loadauth()
        return await self.bot.say("Saved. Now using " + channelidstring +
                                  " as the channel id for command " +
                                  "requests.")

# GLOBAL JSON FUNCTIONS

DATADIR = "data/commandrequests"
SETTINGS = DATADIR + "/data.json"


def saveauth(channelid):
    channelid = channelid
    with open(SETTINGS, 'w') as f:
        json.dump(channelid, f)
    return


def loadauth():
    channelid = ''
    with open(SETTINGS, 'r') as f:
        channelid = json.load(f)
    return channelid


def check_folders():
    if not os.path.exists(DATADIR):
        print("Creating data directory for Command Request cog")
        os.mkdir(DATADIR)


def check_files():
    if not fileIO(SETTINGS, "check"):
        channelid = ''
        print("Creating blank data file for Command Request cog")
        fileIO(SETTINGS, "save", channelid)

# BOT SETUP


def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(CommandRequest(bot))
