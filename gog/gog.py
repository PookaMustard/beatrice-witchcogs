from discord.ext import commands
import discord
import html
import urllib.request
import json
import datetime


class GOG:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def magog(self, ctx, *, text):
        query = "http://www.an-ovel.com/cgi-bin/magog.cgi?ver=772" + \
            "&scp=gdspuio&dsp=ipgfsorcmbaS&ord=&flt=tcs~{}~" + \
            "&opt=nj&myf=MonJan92310072017_empty_VYXnZcKoKJFTY"
        query = query.format(text.replace(' ', '~tcs~'))
        data = self.extractdata(query, 'magog')
        await self.factorize(ctx, data, 'magog')

    @commands.command(pass_context=True)
    async def gog(self, ctx, *, text):
        query = "https://www.gog.com/games/ajax/" + \
                "filtered?limit=10&search=" + text.replace(" ", "%20")
        data = self.extractdata(query, 'gog')
        await self.factorize(ctx, data, 'gog')

    def extractdata(self, query, type):
        r = urllib.request.urlopen(query).read().decode('utf-8')
        data = json.loads(html.unescape(r))
        if type == 'gog':
            return data['products']
        else:
            return data['magog_search_results']

    async def factorize(self, ctx, data, type):
        try:
            title = data[0]['title']
        except:
            return await self.bot.say("No such game found.")

        message = ctx.message
        if len(data) == 1:
            num = 0
        else:
            games = "```"
            for count, i in enumerate(data):
                if count >= 10:
                    break
                if count != len(data):
                    games = games + "\n"
                number = str(count + 1)
                games = games + number + ") " + data[count]['title']
            games = games + "```"
        if len(data) != 1:
            await self.bot.say("Found the following games on GOG:\n" +
                               games + "Please send the number of " +
                               "the game you want. Type `cancel` to " +
                               "cancel.")
            rp = await self.bot.wait_for_message(
                channel=message.channel, author=message.author)
            if rp.content.lower() == "cancel":
                return await self.bot.say("Search cancelled.")
            try:
                num = int(rp.content) - 1
                if (num >= len(data)) or (num >= 10) or (num < 0):
                    await self.bot.say("Chosen number invalid. " +
                                       "Assuming first search " +
                                       "result.")
                    num = 0
            except:
                await self.bot.say("Cannot accept strings for " +
                                   "choosing search results. " +
                                   "Assuming first search result.")
                num = 0
        else:
            num = 0

        title = data[num]['title']

        if ", The" in title:
            title = "The " + title.replace(", The", "")

        if type == 'gog':
            url, image, bottext = await self.gog_search(data, num)
        else:
            url, image, bottext = await self.magog_search(data, num)

        em = discord.Embed(title=title, url=url, description=bottext)
        em.set_image(url=image)

        # Sending the final result
        return await self.bot.send_message(message.channel, embed=em)

    async def magog_search(self, data, num):
        image = data[num]['image'].replace("_100.jpg", ".png")
        url = data[num]['link']
        os = data[num]['os']
        genres = data[num]['genres']
        filesize = data[num]['file_size']
        features = data[num]['features']

        # Extracting release dates and formatting them
        gogdate = data[num]['add_date']
        reldate = data[num]['rls_date']
        if gogdate == reldate:
            datetext = "\n**Release Date:** {}".format(reldate)
        else:
            datetext = "\n**Original Release Date:** {}" + \
                "\n**GOG Release Date:** {}"
            datetext = datetext.format(reldate, gogdate)

        # Extracting publisher and developer
        companies = data[num]['companies'].split(' / ')
        dev = companies[0]
        pub = companies[1]
        if pub == dev:
            comtext = "Published and developed by **{}**".format(
                dev)
        else:
            comtext = "Published by **{}** and developed by **{}**".format(
                pub, dev)

        # Extracting goodies count
        goodies = data[num]['bonuses']
        if goodies == '':
            boncount = 'None'
        else:
            boncount = str(len(goodies.split(',')))

        # Extracting pricing
        curprice = data[num]['cur_price']
        savings = data[num]['you_save']
        if savings != 0:
            fullprice = curprice + savings
            price = "${} (discounted by {}, base price is {})".format(
                curprice, savings, fullprice)
        else:
            price = "${}".format(curprice)

        # Extracting coming soon or released status
        soon = data[num]['is_upcoming']
        if soon:
            rating = 0
            price = price + ", coming soon!"
        else:
            rating = data[num]['stars']

        # Extracting whether the game is NOT on Steam
        steam = data[num]['steam']
        if steam == 'NOT':
            steam = "\nThis game is NOT on Steam."
        else:
            steam = ''

        # Extracting blocked regions, if any
        regblock = data[num]['reg_block_str']
        if regblock != '':
            regblock = "\n**Blocked in the following regions:** {}".format(
                regblock)

        # Defining what the bot will say and formatting it
        bottext = "{}\n**Price:** {}\n**Genres:** {}\n**Rating:** {}/5" + \
            "\n**Operating Systems:** {}\n**Features:** {}" + \
            "\n**File Size:** {}\n**Goodies included:** {}" + \
            "{}{}{}"
        bottext = bottext.format(
            comtext, price, genres, rating, os, features, filesize, boncount,
            datetext, steam, regblock)
        return url, image, bottext

    async def gog_search(self, data, num):
        platformtext = ""
        image = "http:" + data[num]['image'] + ".png"
        genre = data[num]['originalCategory']
        url = 'http://www.gog.com' + \
            data[num]['url']

        # Loading platform support and formatting platform information
        windows_support = data[num]['worksOn']['Windows']
        linux_support = data[num]['worksOn']['Linux']
        mac_support = data[num]['worksOn']['Mac']
        platcount = windows_support + linux_support + mac_support

        for platnum in range(0, platcount):
            if windows_support:
                platformtext = platformtext + "Windows"
                windows_support = 0
            elif linux_support:
                platformtext = platformtext + "Linux"
                linux_support = 0
            elif mac_support:
                platformtext = platformtext + "Mac"
                mac_support = 0
            if platcount == 3 and platnum == 0:
                platformtext = platformtext + ", "
            if platcount == 3 and platnum == 1 or \
                    platcount == 2 and platnum == 0:
                platformtext = platformtext + " and "

        # Loading price details

        isdiscounted = data[num]['isDiscounted']
        discount = data[num]['price']['discountDifference']
        baseprice = data[num]['price']['baseAmount']
        iscomingsoon = data[num]['isComingSoon']
        isfree = data[num]['price']['isFree']
        price = data[num]['price']['symbol'] + \
            data[num]['price']['finalAmount']
        pricesymbol = data[num]['price']['symbol']
        buyable = data[num]['buyable']
        rating = str(data[num]['rating']) + "/50"

        timeraw = data[num]['releaseDate']
        if timeraw is not None:
            reldate = datetime.datetime.fromtimestamp(int(timeraw)) \
                .strftime("%B %d, %Y")
        else:
            reldate = "Unknown"

        if isfree:
            pricetext = 'Free'
        else:
            if not buyable:
                pricetext = 'Not buyable yet'
            else:
                pricetext = price
        if isdiscounted:
            pricetext = pricetext + \
                " (discounted by " + pricesymbol + discount + \
                ", base price is " + pricesymbol + baseprice + ")"
        if iscomingsoon:
            pricetext = pricetext + ", coming soon!"

        bottext = "Limited information is available about this title." + \
            "You can use `magog` to obtain more information if available." + \
            "\n**Original Release:** {}\n**Genre:** {}\n" + \
            "**Platforms:** {}\n**Rating:** {}\n**Price:** {}"
        bottext = bottext.format(
            reldate, genre, platformtext, rating, pricetext)
        return url, image, bottext


def setup(bot):
    bot.add_cog(GOG(bot))
