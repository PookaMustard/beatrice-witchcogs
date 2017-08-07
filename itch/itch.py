import discord
from discord.ext import commands
import requests
from random import randint
try:
    from bs4 import BeautifulSoup
    bs4ava = True
except:
    bs4ava = False


class Itch:
    """Search for products on itch.io"""

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
    async def itch(self, ctx, *, search):
        """Search for a product on itch.io"""

        # Obtain calling message info and send typing to channel
        message = ctx.message
        await self.bot.send_typing(message.channel)

        # Useful for editing the list later
        messageCheck = 0

        # Obtain parameter status
        search, numParameter = self.parameterProcess(search)
        if not search:
            return await self.bot.say("Cannot accept just a parameter. " +
                                      "Please try again with a valid search.")

        # Scraping a search result
        url = "https://itch.io/search?q=" + search.replace(" ", "+")
        soup = BeautifulSoup(requests.get(url).content)
        results = soup.find("div", class_="grid_outer").find_all(
            "div", class_="game_cell")

        if len(results) == 0:
            # If no results, quit
            return await self.bot.say("No search results found.")
        elif len(results) == 1:
            # If only one result, set it automatically
            num = 0
        elif numParameter != -1:
            # If parameters are involved, see them
            if numParameter == -2:
                num = 0
                await self.bot.say(
                    "Invalid parameter. Assuming first search result.")
            else:
                num = numParameter - 1
                try:
                    link = results[num].find("a").get("href")
                except IndexError:
                    num = 0
                    await self.bot.say(
                        "Parameter is out of bounds. Assuming first " +
                        "search result.")
        else:
            # Otherwise, ask the user for which product to seek.
            msg = "Found the following results: \n```"
            msg += ""
            for index, item in enumerate(results):
                if index > 9:
                    break
                nmb = index + 1
                if index < 9:
                    msg += " "
                msg += str(nmb) + ") " + \
                    results[index].find(class_="title").get_text() + "\n"
            msg += "```"
            if len(results) > 10:
                # If there are more than 10 results, post search URL
                # Also remember the randomizer variable
                randomLimit = True
                msg += "There are more than 10 products. View them " + \
                       "[here](" + url + ").\n"
            msg += "Please type the number of the item you want to view." + \
                   "\nType `cancel` to cancel.\nType `random` to choose" + \
                   " a random result."
            em2 = discord.Embed(
                description=msg,
                color=discord.Color.gold())
            botmessage = await self.bot.say(embed=em2)
            messageCheck = 1
            rp = await self.bot.wait_for_message(
                channel=message.channel, author=message.author)
            if rp.content.lower() == "cancel":
                return await self.bot.say("Search cancelled.")
            elif rp.content.lower() == "random":
                if randomLimit:
                    num = randint(0, 9)
                else:
                    num = randint(0, len(results) - 1)
                editMsg = "Here's a random result."
            else:
                try:
                    num = int(rp.content) - 1
                    editMsg = "Here is the search result you requested."
                    if (num >= len(results)) or (num >= 10) or (num < 0):
                        num = 0
                        editMsg = "Chosen number invalid. Assuming first " + \
                                  "search result."
                except:
                    editMsg = "Cannot accept strings for choosing" + \
                              " search results. Assuming first search result."
                    num = 0

        # Obtain the necessary information
        link = results[num].find("a").get("href")
        id = results[num].get("data-game_id")
        title = results[num].find(class_="title").get_text()
        author = results[num].find(class_="game_author").find("a").get_text()
        authorLink = results[num].find(
            class_="game_author").find("a").get("href")
        platformText = ""

        # Obtain all variable information
        # Since they may or may not exist, they must be tried and excepted
        try:
            # Platforms must be formatted before usage
            platforms = results[num].find(
                "div", class_="game_platform").find_all("span")
            for index, item in enumerate(platforms):
                try:
                    if "Download for" in item.get("title"):
                        platformText += item.get("title")[13:]
                except TypeError:
                    pass
                try:
                    platformText += item.get_text()
                except TypeError:
                    pass
                if index != (len(platforms) - 1):
                    platformText += ", "
        except AttributeError:
            platformText = "Unknown"
        try:
            desc = results[num].find("div", class_="game_text").get("title")
        except AttributeError:
            desc = ""
        try:
            genre = results[num].find("div", class_="game_genre").get_text()
        except:
            genre = "Unknown"
        try:
            price = results[num].find("div", class_="price_value").get_text()
        except AttributeError:
            price = "Free"

        # Prepare embed message
        msg = "**Released by [" + author + "](" + authorLink + ")**"
        msg += "\n====\n"
        if desc:
            msg += desc + "\n====\n"
        msg += "**Price:** " + price
        msg += "\n**Genre:** " + genre
        msg += "\n**Platforms:** " + platformText

        # Prepare embed details
        siteUrl = "https://itch.io"
        em = discord.Embed(description=msg, title=title, url=link,
                           color=discord.Color.gold())
        em.set_author(name="itch.io", url=siteUrl,
                      icon_url="https://pbs.twimg.com/profile_images/" +
                      "877992944002899972/qCF6gLIY.jpg")
        em.set_footer(text="Product ID: " + id)

        # Prepare embed message
        imgStr = results[num].find("div", class_="game_thumb").get("style")
        if imgStr != "":
            image = imgStr[imgStr.find("url('") + 5:len(imgStr) - 2]
            em.set_image(url=image)

        # Edit if a list was sent, send new message otherwise
        if messageCheck == 1:
            return await self.bot.edit_message(botmessage,
                                               str(editMsg),
                                               embed=em)
        else:
            return await self.bot.send_message(message.channel, embed=em)


def setup(bot):
    if not bs4ava:
        raise RuntimeError("You need to run 'pip install bs4' to run the cog")
    else:
        bot.add_cog(Itch(bot))
