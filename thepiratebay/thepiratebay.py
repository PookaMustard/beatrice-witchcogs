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

    @commands.command(pass_context=True)
    async def tpbcat(self, ctx, categories, *, search):
        """Returns Pirate Bay torrent search results using item name
           and under specific categories. The categories are as follows:
                *100 - Audio
                *200 - Video
                *300 - Applications
                *400 - Games
                *500 - Porn
                *600 - Other
           And many more categories. See the website for more details.
           You can add as many categories as you wish, seperated by commas
           and without any spaces inbetween the category numbers.
           For example:
           [p]tpbcat 300,600 linux mint

           You can use parameters to select a certain result, e.g. the
           first. An example:

           [p]tpb linux mint --1"""

        # Fetching info about the command user message
        message = ctx.message

        # This variable will come in handy if there are multiple results
        messageCheck = 0

        # Send typing status to inform the user of a response
        await self.bot.send_typing(message.channel)

        # Obtain parameter status
        search, numParameter = self.parameterProcess(search)

        # Querying and scraping the website with multiple categories
        url = 'http://thepiratebay.org'
        searchurl = url + '/search/{}/0/99/{}'.format(
            search.replace(" ", "%20"), categories)
        query = requests.get(searchurl).content
        soup = BeautifulSoup(query)
        await self.process(soup, numParameter, url, messageCheck, message,
                           searchurl)

    @commands.command(pass_context=True)
    async def tpb(self, ctx, *, search):
        """Returns Pirate Bay torrent search results using item name.

           You can use parameters to select a certain result, e.g. the
           first. An example:

           [p]tpb linux mint --1"""

        # Same comments as above
        message = ctx.message
        messageCheck = 0
        await self.bot.send_typing(message.channel)

        search, numParameter = self.parameterProcess(search)

        # Querying and scraping with all categories
        url = 'http://thepiratebay.org'
        searchurl = url + '/search/{}/0/99/0'.format(
            search.replace(" ", "%20"))
        query = requests.get(searchurl).content
        soup = BeautifulSoup(query)
        await self.process(soup, numParameter, url, messageCheck, message,
                           searchurl)

    async def process(self, soup, numParameter, url, messageCheck, message,
                      searchurl):
        try:
            results = soup.find(
                'table', id='searchResult').find_all('tr')[1:9]
        except AttributeError:
            return await self.bot.say("No search results found.")

        # If only one result was returned, immediately choose it.
        if len(results) == 1:
            num = 0
        elif numParameter != -1:
            # Take into account the user parameter if stated
            if numParameter == -2:
                num = 0
                await self.bot.say(
                    "Invalid parameter. Assuming first search result.")
            else:
                num = numParameter - 1
                try:
                    info = results[num].find_all('td')[1].find(
                        "a", class_="detLink").get_text()
                except IndexError:
                    num = 0
                    await self.bot.say(
                        "Parameter is out of bounds. Assuming first " +
                        "search result.")
        else:
            # Otherwise, ask the user for which product to seek.
            msg = "Found the following results: "
            msg += "```bash\n"
            for index, item in enumerate(results):
                if index > 8:
                    index = 8
                    break
                nmb = index + 1
                # if index != 7:
                #    msg += " "
                msg += str(nmb) + ") " + results[index].find_all(
                    'td')[1].find("a", class_="detLink").get_text() + "\n"
                msg += "\t\t\t\t# " + \
                    results[index].find_all('td')[0].find_all('a')[
                        0].get_text()
                msg += " - (" + results[index].find_all('td')[
                    0].find_all('a')[1].get_text() + ")"
                msg += " - (S: " + results[index].find_all('td')[2].get_text(
                ) + " - L: " + \
                    results[index].find_all('td')[3].get_text() + ")\n"

            msg += "```"
            shortResults = soup.find(
                'table', id='searchResult').find_all('tr')
            if len(shortResults) > 8:
                # If there are more than 8 results, post a link to the search
                msg += "There are more than 8 results. View them [here](" + \
                    searchurl + ")\n"
            msg += "Please type the number of the item you want to view." + \
                   " Type `cancel` to cancel."
            # Prepare a new message with embed and remember it for later
            em2 = discord.Embed(
                description=msg,
                color=discord.Color.gold())
            botmessage = await self.bot.say(embed=em2)
            messageCheck = 1
            rp = await self.bot.wait_for_message(
                channel=message.channel, author=message.author)
            if rp.content.lower() == "cancel":
                return await self.bot.say("Search cancelled.")
            try:
                num = int(rp.content) - 1
                if (num >= len(results)) or (num >= 10) or (num < 0):
                    await self.bot.say("Chosen number invalid. " +
                                       "Assuming first search " +
                                       "result.")
                    num = 0
            except:
                await self.bot.say("Cannot accept strings for " +
                                   "choosing search results. " +
                                   "Assuming first search result.")
                num = 0

        # Collecting data from the second column (which has the most data)
        data = results[num].find_all('td')[1]
        magnet = data.find_all("a")[1].get("href")
        link = url + data.find("a", class_="detLink").get("href")
        info = data.find("font", class_="detDesc").get_text().replace(
            "\xa0", " ")
        title = data.find("a", class_="detLink").get_text()
        finalInfo = BeautifulSoup(requests.get(link).content)

        # Collect data from the other columns
        seeders = results[num].find_all('td')[2].get_text()
        leechers = results[num].find_all('td')[3].get_text()
        category = results[num].find_all('td')[0].find_all('a')[0].get_text()
        subCat = results[num].find_all('td')[0].find_all('a')[1].get_text()

        # Preparing description
        description = finalInfo.find(
            "div", class_="nfo").find("pre").get_text()
        if len(description) > 280:
            description = description[:277] + "..."

        # Prepare embed message
        msg = "====\n" + description + "\n====\n"
        msg += info + "\n" + \
            "**Seeders:** " + seeders + " - **Leechers:** " + leechers
        msg += "\t\t\t\t**Category:** " + category + " (" + subCat + ")\n"
        msg += "**[Magnet link](" + magnet + ")**"

        # Prepare the embed
        # If the result is from the Porn category, reflect the NSFW nature
        # of the content
        em = discord.Embed(title=title, url=link,
                           description=msg, color=discord.Color.gold())
        em.set_author(name="The Pirate Bay", url="https://thepiratebay.org/")
        if category == "Porn":
            em.set_footer(
                text="This torrent includes not safe for work content.")

        # If the bot sent a message for choice selection before, edit it
        # Otherwise, just send a message
        if messageCheck == 1:
            return await self.bot.edit_message(botmessage,
                                               str("Here is the search " +
                                                   "result you requested."),
                                               embed=em)
        else:
            return await self.bot.send_message(message.channel, embed=em)


def setup(bot):
    if not bs4ava:
        raise RuntimeError("You need to run 'pip install bs4' to run the cog")
    else:
        bot.add_cog(ThePirateBay(bot))
