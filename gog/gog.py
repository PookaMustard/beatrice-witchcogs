from discord.ext import commands
import requests
import json
import html
import discord


class GOG:
    """Search for games and movies on GOG.com"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def gog(self, ctx, *, text):
        """Returns GOG search results using game name"""

        # First, defining variables, query included
        message = ctx.message
        retries, retriesnum, = 0, 1
        gamename = []
        othergames = ''
        query = "http://www.an-ovel.com/cgi-bin/magog.cgi?ver=772" + \
            "&scp=gdspuio&dsp=ipgfsorcmbaS&ord=&flt=tcs~{}~" + \
            "&opt=nj&myf=MonJan92310072017_empty_VYXnZcKoKJFTY"
        query = query.format(text)

        # Loading query into memory
        r = requests.get(query)
        data = json.loads(html.unescape(r.text))
        data = data['magog_search_results']

        # Loading at maximum 10 games into memory
        while retries <= 10:
            try:
                gamene = data[retries]['title']
                gamename.append(gamene)
                othergames = othergames + "\n" + \
                    str(retriesnum) + ") " + gamename[retries]
                retries = retries + 1
                retriesnum = retriesnum + 1
            except:
                if retries == 0:
                    return await self.bot.say("No games found " +
                                              "under that name on " +
                                              "GOG.com. Try another " +
                                              "search result.")
                maxnum = retries
                break

        # If there were more than one game, ask user to choose from them
        if maxnum != 1:
            await self.bot.say("Found the following games on GOG:" +
                               othergames + "\n\nPlease type the " +
                               "number of the game you want, " +
                               "then send.")
            rp = await self.bot.wait_for_message(author=message.author)
            try:
                num = int(rp.content) - 1
                if (num >= maxnum) or (num < 0):
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

        # Extracting basic data
        title = data[num]['title']
        url = data[num]['link']
        image = data[num]['image'].replace("_100.jpg", ".png")
        os = data[num]['os']
        genres = data[num]['genres']
        gogdate = data[num]['add_date']
        reldate = data[num]['rls_date']
        filesize = data[num]['file_size']
        features = data[num]['features']

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
            rating = 'Not rated yet.'
            price = price + ", coming soon!"
        else:
            rating = data[num]['stars']

        # Extracting whether the game is NOT on Steam
        steam = data[num]['steam']
        if steam == 'NOT':
            steam = "\nThis game is NOT on Steam."
        else:
            steam = ''

        # Defining what the bot will say and formatting it
        bottext = "{}\n**Price:** {}\n**Genres:** {}\n**Rating:** {}" + \
            "\n**Operating Systems:** {}\n**Features:** {}" + \
            "\n**File Size:** {}\n**Goodies included:** {}" + \
            "\n**Original Release Date:** {}\n**GOG Release Date:** {}{}"
        bottext = bottext.format(
            comtext, price, genres, rating, os, features, filesize, boncount,
            reldate, gogdate, steam)

        # Finally embedding all the acquired information into an embed
        em = discord.Embed(title=title, url=url, description=bottext)
        em.set_image(url=image)

        # Sending the final result
        return await self.bot.say(embed=em)


def setup(bot):
    bot.add_cog(GOG(bot))
