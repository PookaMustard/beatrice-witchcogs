from discord.ext import commands
from __main__ import send_cmd_help
import discord
import base64
import requests
import json
from random import randint


class Minecraft:
    """Minecraft related commands such as profile or server check"""

    def __init__(self, bot):
        self.bot = bot

    def cleanspans(self, snippet):
        snippet = snippet.replace('</span>', '')
        snippet = snippet.replace(
            '<span class="searchmatch">', '')
        return snippet.replace('      ', ' - ')

    def parameterProcess(self, search):
        paraLen = 0
        if search[:-1].endswith("--"):
            paraLen = 1
        elif search[:-2].endswith("--"):
            paraLen = 2
        if paraLen:
            try:
                numParameter = int(search[len(search) - paraLen:len(search)])
                return search[:-(paraLen + 2)], (
                    numParameter if numParameter else 1)
            except ValueError:
                return search, -2
        else:
            return search, -1

    @commands.group(pass_context=True)
    async def minecraft(self, ctx):
        """Minecraft related commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @minecraft.command(pass_context=True)
    async def status(self, ctx):
        """Checks the status of Mojang's Minecraft servers"""
        # Initializing necessary variables
        query = 'https://status.mojang.com/check'
        message = ctx.message

        # Sending typing status
        await self.bot.send_typing(message.channel)

        # Checking if API is responding
        try:
            r = requests.get(query).text
            data = json.loads(r)
        except:
            return await self.bot.say(
                "An error has occured. API may be down.")

        # Organizing data from API into a single bot message
        msg = "**GREEN** means there are no issues"
        msg += "\n**YELLOW** means there are some issues"
        msg += "\n**RED** means the service is unavailable"
        msg += "\n```"
        msg += "\nMinecraft.net:                                  " + \
            data[0]['minecraft.net'].upper()
        msg += "\nMojang.com:                                     " + \
            data[9]['mojang.com'].upper()
        msg += "\nMojang API (api.mojang.com):                    " + \
            data[7]['api.mojang.com'].upper()
        msg += "\nMinecraft Sessions (session.minecraft.net):     " + \
            data[1]['session.minecraft.net'].upper()
        msg += "\nMojang Accounts (account.mojang.com):           " + \
            data[2]['account.mojang.com'].upper()
        msg += "\nMojang Authentication (auth.mojang.com):        " + \
            data[3]['auth.mojang.com'].upper()
        msg += "\nMojang Auth Server (authserver.mojang.com):     " + \
            data[5]['authserver.mojang.com'].upper()
        msg += "\nSkins (skins.minecraft.net):                    " + \
            data[4]['skins.minecraft.net'].upper()
        msg += "\nSession Server (sessionserver.mojang.com):      " + \
            data[6]['sessionserver.mojang.com'].upper()
        msg += "\nTextures (textures.minecraft.net):              " + \
            data[8]['textures.minecraft.net'].upper()
        msg += "\n```"

        # Send embed
        em = discord.Embed(title="Minecraft API Status", description=msg,
                           color=discord.Color.gold())
        em.set_author(name="Minecraft.net", url="https://minecraft.net",
                      icon_url="https://minecraft.gamepedia.com/media/" +
                      "minecraft.gamepedia.com/d/d4/Crafting_Table.png" +
                      "?version=c8b10ca0ed4cf44bf89423f3d371a2e4")
        return await self.bot.say(embed=em)

    @minecraft.command(pass_context=True)
    async def wiki(self, ctx, *, search):
        """Looks up the Gamepedia wiki for information about searched term

            Support is in beta. Some snippets may come out with garbage
            results. This is due to the API used by the official Minecraft
            Wiki and how it gathers information."""

        # Initializing variables
        message = ctx.message
        await self.bot.send_typing(message.channel)

        # Obtaining parameter and message edit info
        search, numParameter = self.parameterProcess(search)
        if not search:
            return await self.bot.say("Cannot accept just a parameter. " +
                                      "Please try again with a valid search.")
        messageCheck = 0

        # Preparing query URL
        query = 'https://minecraft.gamepedia.com/api.php?action=query' + \
            '&format=json&list=search&srsearch=' + \
            search.replace(' ', '_')

        # Checking if API is responding
        try:
            r = requests.get(query).text
            data = json.loads(r)
        except:
            return await self.bot.say(
                "An error has occured. API may be down.")

        # Validating existence of valid queries
        info = data['query']['search']
        if info == []:
            return await self.bot.say("No search results returned.")
        else:
            # Checking if it is a single query or multiple queries
            if len(info) == 1:
                title = info[0]['title']
                snippet = self.cleanspans(info[0]['snippet'])
            elif numParameter != -1:
                # If a parameter was provided, process it with respect to data
                if numParameter == -2:
                    num = 0
                    await self.bot.say(
                        "Invalid parameter. Assuming first search result.")
                else:
                    num = numParameter - 1
                    try:
                        title = info[0]['title']
                    except IndexError:
                        num = 0
                        await self.bot.say(
                            "Parameter is out of bounds. Assuming first " +
                            "search result.")
            else:
                # Prepare a bot function to receive the query the user intends
                # to view
                msg = "Found the following results: "
                msg += "```"
                for index, item in enumerate(info):
                    if index > 9:
                        break
                    nmb = index + 1
                    msg += str(nmb) + ") " + info[index]['title'] + "\n"
                msg += "```"
                msg += "Please type the number of the item you want to view."
                msg += "\nType `cancel` to cancel."
                msg += "\nType `random` for a random result"
                em2 = discord.Embed(description=msg,
                                    color=discord.Color.gold())
                botmessage = await self.bot.say(embed=em2)
                messageCheck = 1
                rp = await self.bot.wait_for_message(
                    channel=message.channel, author=message.author)
                if rp.content.lower() == "cancel":
                    return await self.bot.say("Search cancelled.")
                elif rp.content.lower() == "random":
                    num = randint(0, len(info) - 1)
                    editMsg = "Here's a random result."
                else:
                    try:
                        num = int(rp.content) - 1
                        editMsg = "Here is the search result you requested."
                        if (num >= len(info)) or (num >= 10) or (num < 0):
                            editMsg = "Chosen number invalid. Assuming " + \
                                      "first search result."
                            num = 0
                    except:
                        editMsg = "Cannot accept strings for choosing" + \
                                  " search results. Assuming first" + \
                                  " search result."
                        num = 0
            title = info[num]['title']
            snippet = self.cleanspans(info[num]['snippet'])

            # Preparing to post the information in an embed
            snippet = "..." + snippet + "..."
            url = "http://minecraft.gamepedia.com/" + title.replace(' ', '_')
            em = discord.Embed(title=title, url=url, description=snippet,
                               color=discord.Color.gold())
            em.set_footer(
                text="*Wiki snippet may be strange due to API limitations*")
            em.set_author(name="Official Minecraft Wiki",
                          url="https://minecraft.gamepedia.com",
                          icon_url="https://minecraft.gamepedia.com/media/" +
                          "minecraft.gamepedia.com/b/bc/Wiki.png")

            # Finally sending the message
            if messageCheck == 1:
                return await self.bot.edit_message(botmessage,
                                                   str(editMsg),
                                                   embed=em)
            else:
                return await self.bot.send_message(message.channel, embed=em)

    @minecraft.command(pass_context=True)
    async def player(self, ctx, playername):
        """Checks information about a player, such as skins and capes"""
        message = ctx.message
        query = 'https://api.mojang.com/users/profiles/minecraft/' + \
                playername

        await self.bot.send_typing(message.channel)

        # Checking if API is responding
        try:
            r = requests.get(query).text
            if r == '':
                return await self.bot.say(playername + " does not exist.")
            d1 = json.loads(r)
        except:
            return await self.bot.say(
                "An error has occured. API may be down.")

        # Obtaining the player's ID from profiles server, then looking it
        # up in the sessions server to obtain skin and cape information
        playerID = d1['id']
        query = 'https://sessionserver.mojang.com/session/' + \
                'minecraft/profile/' + playerID

        # Now testing against the sessions server to see if the bot is
        # allowed to obtain information from there.
        try:
            r = requests.get(query).text
            d2 = json.loads(r)
        except:
            return await self.bot.say(
                "Due to API limitations, you must wait a full minute" +
                " before requesting this username again. If the command" +
                " still doesn't work, the API may be down.")

        # Decoding the base64 value of the textures (skin and cape info)
        d3 = json.loads(
            base64.b64decode(
                d2['properties'][0]['value']).decode().replace("'", '"'))

        # Organizing the newly obtained data into a Discord embed
        msg = ""
        if d3['textures'] == {}:
            msg += "\nThis player has no custom skin or cape."
        else:
            if 'SKIN' not in d3['textures']:
                msg += "\nThis player has no custom skin."
                hasSkin = False
            else:
                if 'metadata' not in d3['textures']['SKIN']:
                    msg += "\n**Skin variant:** 'Steve?'/Classic"
                else:
                    msg += "\n**Skin variant:** 'Alex?'/Slim"
                skin = d3['textures']['SKIN']['url'].replace('http', 'https')
                hasSkin = True
                msg += "\n**[Skin Link](" + skin + ")**"
            if 'CAPE' not in d3['textures']:
                msg += "\nThis player has no custom cape."
            else:
                if not hasSkin:
                    msg += "\n"
                else:
                    msg += " - "
                cape = d3['textures']['CAPE']['url'].replace('http', 'https')
                msg += "**[Cape Link](" + cape + ")**"

        # Preparing embed
        em = discord.Embed(title=playername, description=msg,
                           color=discord.Color.gold())
        em.set_author(name="Minecraft.net", url="https://minecraft.net",
                      icon_url="https://minecraft.gamepedia.com/media/" +
                      "minecraft.gamepedia.com/d/d4/Crafting_Table.png" +
                      "?version=c8b10ca0ed4cf44bf89423f3d371a2e4")
        em.set_footer(text="Player ID: " + playerID)

        # Try to set a skin as image. If there are none, continue as normal
        if hasSkin:
            em.set_image(url=skin)

        # Sending embed
        return await self.bot.send_message(message.channel, embed=em)


def setup(bot):
    bot.add_cog(Minecraft(bot))
