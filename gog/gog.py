from discord.ext import commands
import urllib.request
import discord
import html
import re
import json
import datetime


class GOG:
    """Searches for games sold on GOG.com"""

    def __init__(self, bot):
        self.bot = bot

    def unhtml(self, str):
        return re.sub("<.*?>", "", str)

    def alphanum(self, str):
        str = str.replace(' ', '0987vcxz')
        str = re.sub(r'\W+', '', str)
        return str.replace('0987vcxz', '_').lower()

    def productCount(self, type, count):
        if type.lower() == "dlc":
            if count > 1:
                return "DLCs"
            else:
                return "DLC"
        elif type.lower() == "goodies":
            if count > 1:
                return "goodies"
            else:
                return "goodie"

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

    def apicheck(self, query):
        try:
            r = urllib.request.urlopen(query).read().decode()
            return json.loads(html.unescape(r))
        except:
            return self.bot.say(
                "An error has occured. Either the search term" +
                " is invalid or the API is down. Please try again later.")

    @commands.command(pass_context=True)
    async def gogcount(self, ctx):
        """Checks how many games are on GOG.com's library"""
        message = ctx.message
        await self.bot.send_typing(message.channel)
        query = "https://www.gog.com/games/ajax/filtered"

        # Checking if API is responding
        data = self.apicheck(query)

        msg = "There are " + str(data['totalGamesFound']) + \
              " games found on GOG.com as of now."
        em = discord.Embed(title="Games on GOG.com",
                           url="https://www.gog.com/games?" +
                           "sort=popularity&page=1",
                           description=msg,
                           color=discord.Color.gold())
        em.set_author(name="GOG.com", url="https://www.gog.com")
        em.set_thumbnail(url="https://images.gog.com/844bac20026" +
                         "bcb6faf3d308fe9ad38365b3df6d1b5c4b" +
                         "74d0db309b426c997c5.jpg")
        return await self.bot.send_message(message.channel, embed=em)

    @commands.command(pass_context=True)
    async def gog(self, ctx, *, search):
        """Searches for games on GOG.com"""
        message = ctx.message
        await self.bot.send_typing(message.channel)

        messageCheck = 0

        search, numParameter = self.parameterProcess(search)

        # Preparing search query and message context

        query = "https://www.gog.com/games/ajax/filtered?limit=10" +\
                "&search=" + search.replace(' ', '%20')

        # Checking if API is responding
        data = self.apicheck(query)

        # Isolate search results into its own variable
        info = data['products']

        # If only one result was returned, immediately choose it.
        if len(info) == 0:
            return await self.bot.say("No search results found.")
        elif len(info) == 1:
            num = 0
        elif numParameter != -1:
            if numParameter == -2:
                num = 0
                await self.bot.say(
                    "Invalid parameter. Assuming first search result.")
            else:
                num = numParameter - 1
                try:
                    id = info[num]['id']
                except IndexError:
                    num = 0
                    await self.bot.say(
                        "Parameter is out of bounds. Assuming first " +
                        "search result.")
        else:
            # Otherwise, ask the user for which product to seek.
            msg = "Found the following results: \n```"
            msg += ""
            for index, item in enumerate(info):
                if index > 9:
                    break
                nmb = index + 1
                if index < 9:
                    msg += " "
                msg += str(nmb) + ") " + info[index]['title'] + "\n"
            msg += "```"
            if int(data['totalResults']) > 10:
                st = "https://www.gog.com/games?sort=popularity&search=" + \
                     search.replace(' ', '%20')
                msg += "There are more than 10 products. View them " + \
                       "[here](" + st + ").\n"
            msg += "Please type the number of the item you want to view." + \
                   " Type `cancel` to cancel."
            em2 = discord.Embed(
                description=msg,
                color=discord.Color.gold())
            botmessage = await self.bot.say(embed=em2)
            messageCheck = 1
            rp = await self.bot.wait_for_message(
                channel=message.channel, author=message.author)
            if rp.content.lower() == "cancel":
                return await self.bot.say("Search cancelled.")
            editMsg = "Here is the search result you requested."
            try:
                num = int(rp.content) - 1
                if (num >= len(info)) or (num >= 10) or (num < 0):
                    num = 0
                    editMsg = "Chosen number invalid. Assuming first " + \
                              "search result."

            except:
                editMsg = "Cannot accept strings for choosing" + \
                          " search results. Assuming first search result."
                num = 0

        # Obtaining more data by using the ID of the game and Galaxy APIs
        id = info[num]['id']
        query = "http://api.gog.com/products/" + str(id) + \
                "?expand=description,downloads,related_products"

        # Checking if API is down while retrieving data
        info2 = self.apicheck(query)

        # Obtaining data from first set
        title = info[num]['title']
        developer = info[num]['developer']
        publisher = info[num]['publisher']
        basePrice = info[num]['price']['baseAmount']
        finalPrice = info[num]['price']['finalAmount']
        priceSymbol = info[num]['price']['symbol']
        isDiscounted = info[num]['price']['isDiscounted']
        discount = info[num]['price']['discountDifference']
        isFree = info[num]['price']['isFree']
        isDevelopment = info[num]['isInDevelopment']
        isComingSoon = info[num]['isComingSoon']
        isBuyable = info[num]['buyable']
        image = "http:" + info[num]['image'] + ".png"
        genre = info[num]['category']
        rating = info[num]['rating']
        worksOn = info[num]['worksOn']
        timeraw = info[num]['releaseDate']

        # Obtaining data from second set
        description = info2['description']['lead']
        languages = info2['languages']
        gameType = info2['game_type']
        buyLink = info2['links']['purchase_link']
        supportLink = info2['links']['support']
        forumLink = info2['links']['forum']
        try:
            # Only applies to the first OS
            size = info2['downloads']['installers'][0]['total_size']
        except IndexError:
            size = -1
        try:
            # Also only applies to the first OS
            version = info2['downloads']['installers'][0]['version'].upper()
        except AttributeError:
            version = ""
        bonusCount = len(info2['downloads']['bonus_content'])
        url = info2['links']['product_card'].replace("http://", "https://")
        try:
            dlcCount = len(info2['dlcs']['products'])
        except TypeError:
            dlcCount = 0

        # Organizing data (regex required to remove specials)

        # If game is inDev, add suffix to game title embed
        if isDevelopment:
            title = title + " [IN DEVELOPMENT]"

        # Link to games by developer and publisher
        if publisher == developer:
            devLink = "https://www.gog.com/games?devpub=" + \
                      self.alphanum(developer) + "&sort=title&page=1"
            devPubText = "**Developed and published by [" + \
                         developer + "](" + devLink + ")**"
        else:
            devLink = "https://www.gog.com/games?devpub=" + \
                      self.alphanum(developer) + "&sort=title&page=1"
            pubLink = "https://www.gog.com/games?devpub=" + \
                      self.alphanum(publisher) + "&sort=title&page=1"
            devpubLink = "https://www.gog.com/games?devpub=" + \
                self.alphanum(developer) + "," + \
                self.alphanum(publisher) + "&sort=title&page=1"
            devPubText = "**Developed by [" + developer + "](" + \
                         devLink + ") " + "and published by [" + \
                         publisher + "](" + pubLink + ")**\n" + \
                         "([view games by both developer and publisher](" + \
                         devpubLink + "))"
        msg = devPubText + "\n====\n"

        # Filling information into message, starting with description lead
        if description:
            msg += description + "\n====\n"
        elif info2['description']['full']:
            msg = info2['description']['full'][:400] + "...\n====\n"

        # Adding bonus and DLC counts
        if gameType == 'dlc':
            msg += "**This product is a DLC.**\n"
        if dlcCount > 0 and bonusCount > 0:
            msg += "**This product has " + str(dlcCount) + " potential" + \
                   " *" + self.productCount("dlc", dlcCount) + "* and " + \
                   str(bonusCount) + " *" + \
                   self.productCount("goodies", bonusCount) + "*.**\n"
        elif dlcCount > 0:
            msg += "**This product has " + str(dlcCount) + \
                   " potential *" + self.productCount("dlc", dlcCount) + \
                   "*.**\n"
        elif bonusCount > 0:
            msg += "**This product has " + str(bonusCount) + \
                   " *" + self.productCount("goodies", bonusCount) + "*.**\n"

        # Adding pricing
        if isFree:
            if not isBuyable:
                pricetext = "Not buyable yet"
            else:
                pricetext = "**Price:** Free"
        else:
            if not isBuyable:
                pricetext = "Not buyable yet"
            else:
                pricetext = "**Price:** " + priceSymbol + finalPrice
        if isDiscounted:
            pricetext = pricetext + \
                " (discounted by " + priceSymbol + str(discount) + \
                ", base price is " + priceSymbol + str(basePrice) + ")"
        if isComingSoon:
            pricetext = pricetext + ", coming soon!"
        msg += pricetext + "\n"

        # Adding original release date
        if timeraw is not None:
            reldate = datetime.datetime.fromtimestamp(int(timeraw)) \
                .strftime("%B %d, %Y")
        else:
            reldate = "Unknown"
        msg += "**Original release date:** " + reldate + "\n"

        # Adding genre and rating
        msg += "**Genre:** " + genre + "\n"
        msg += "**Rating:** " + str(rating) + "/50\n"

        # Adding languages
        lang = "**Languages:** "
        for index, language in enumerate(languages):
            lang += language.upper()
            if (index + 1) != len(languages):
                lang += ", "
        msg += lang + "\n"

        # Adding operating systems
        compatMsg = "**Supported platforms:** "
        i = 0
        compatWindows = worksOn['Windows']
        compatLinux = worksOn['Linux']
        compatMac = worksOn['Mac']
        trueCompats = compatWindows + compatLinux + compatMac
        for os in worksOn:
            if worksOn[os]:
                compatMsg += os
                i += 1
                if (trueCompats == 2 and i == 1) or \
                        (trueCompats == 3 and i == 2):
                    compatMsg += " and "
                if trueCompats == 3 and i == 1:
                    compatMsg += ", "
                if trueCompats == 1:
                    compatMsg += " only"
        msg += compatMsg + "\n"

        # Adding game size and version, if they exist
        if size != -1:
            if size > 1073741824:
                processedSize = str(round(size / pow(1024, 3), 2))
                if processedSize.endswith('.0'):
                    processedSize = processedSize[:-2]
                processedSize += "GB"
            else:
                processedSize = str(int((size / pow(1024, 2)))) + "MB"
            msg += "**Installer:** " + processedSize
            if version != "":
                msg += ", version " + version + "\n"
            else:
                msg += ", version unknown\n"

        if isBuyable:
            msg += "**[Buy now](" + buyLink + ") -** "
        msg += "**[View Support](" + supportLink + ") - " + \
               "[View Forums](" + forumLink + ")**"

        # Preparing embed
        authorAvatar = "https://images.gog.com/9b1aae00838bf648d83b01780" + \
                       "1d926f025abf226278d1263e20fd8d0df154445.jpg"
        em = discord.Embed(title=title, url=url,
                           description=self.unhtml(msg),
                           color=discord.Color.gold())
        em.set_author(name="GOG.com", url="https://www.gog.com",
                      icon_url=authorAvatar)
        em.set_image(url=image)
        em.set_footer(text="Sold on GOG.com -- Game ID: " + str(id))

        # Sending embed to Discord
        if messageCheck == 1:
            return await self.bot.edit_message(botmessage,
                                               str(editMsg),
                                               embed=em)
        else:
            return await self.bot.send_message(message.channel, embed=em)


def setup(bot):
    bot.add_cog(GOG(bot))
