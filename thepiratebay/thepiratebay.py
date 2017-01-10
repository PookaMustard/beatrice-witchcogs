import discord
from discord.ext import commands
import requests
try:
    from bs4 import BeautifulSoup
    bs4ava = True
except:
    bs4ava = False


class ThePirateBay:
    """Search for files on the Pirate Bay"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def tpb(self, ctx, *, text):
        """Returns Pirate Bay torrent search results using item name"""

        # Initializing variables and URLs, loading search into memory
        message = ctx.message
        initm = '```'
        url = 'http://thepiratebay.org'
        searchurl = url + '/search/{}/0/99/0'.format(text.replace(" ", "%20"))
        search = requests.get(searchurl).content
        soup = BeautifulSoup(search)

        # Searching for all torrent links found on the search page
        var = soup.find_all(class_='detLink')

        # Identifying amount of results, determining the message to send users
        # First clause will send a message for no results
        # Second clause will pick the only search result for usage
        # Third clause will ask the user which of the results to choose from
        # If there are more than five results, send the search URL
        # In cases of found results, link, title and description extracted
        if len(var) == 0:
            return await self.bot.say("No results found.")
        elif len(var) == 1:
            title = var[0].get_text()
            finalurl = str(url) + str(var[0].get('href'))
            desc = soup.find(class_='detDesc').get_text()
        else:
            for count, i in enumerate(var):
                if count > 4:
                    count = 4
                    break
                numcount = count + 1
                initm = initm + str(numcount) + ". " + \
                    var[count].get_text() + "\n"
            initm = initm + '```'
            if len(var) > 4:
                initm = initm + "More results found here: <" + \
                    searchurl + ">\n"
            initm = initm + "Please type the number of the item you want." + \
                " Type `cancel` to cancel the search."
            await self.bot.say(initm)
            rp = await self.bot.wait_for_message(
                author=message.author, channel=message.channel)
            try:
                index = int(rp.content) - 1
                if (index >= count + 1) or (index < 0):
                    await self.bot.say("Chosen number invalid. " +
                                       "Assuming first search " +
                                       "result.")
                    index = 0
            except:
                if str(rp.content).lower() == 'cancel':
                    return await self.bot.say("Search cancelled.")
                await self.bot.say("Cannot accept strings for " +
                                   "choosing search results. " +
                                   "Assuming first search result.")
                index = 0
            title = var[index].get_text()
            finalurl = str(url) + str(var[index].get('href'))
            desc = soup.find_all(class_='detDesc')[index * 2].get_text()

        # Preparing information to send in a Discord embed
        desc = desc + "\n***WARNING:*** May or may not include NSFW content"
        em = discord.Embed(title=title, url=finalurl, description=desc)

        # Finally sending the message
        return await self.bot.say(embed=em)


def setup(bot):
    if not bs4ava:
        raise RuntimeError("You need to run 'pip install bs4' to run the cog")
    else:
        bot.add_cog(ThePirateBay(bot))
