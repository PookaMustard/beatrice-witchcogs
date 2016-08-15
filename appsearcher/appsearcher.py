import discord
import re
import json
import requests
from bs4 import BeautifulSoup
import aiohttp
from discord.ext import commands

class appsearcher:
    """Search for apps on popular application stores"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gog(self, *text):
        """Returns GOG search results using game name
            Type %gog gamecount for the number of games"""

        #Your code will go here
        if text[0]=='gamecount':
            url = "https://www.gog.com/games?sort=bestselling&page=1" #build the web adress
            async with aiohttp.get(url) as response:
                soupObject = BeautifulSoup(await response.text(), "html.parser") 
            try:
                count_unabridged = soupObject.find(class_='header__title').get_text()
                count = count_unabridged.replace('  DRM-FREE GAMES     ', '')
                count = count.replace('\n        ', '')
                return await self.bot.say("There are " + count + " games on GOG today.")
            except:
                return await self.bot.say("Couldn't load amount of DRM-free games on GOG. There must be an error.")
        else:
            text = " ".join(text)
            text = text.replace(" ", "%20")
            query = 'https://www.gog.com/games/ajax/filtered?limit=5&search=' + text
            #Loading ajax search URL into variable r
            r = requests.get('https://www.gog.com/games/ajax/filtered?limit=5&search=')
            #Loading the text of ajax search URL into variable data
            data = json.loads(r.text)
            
            #Checking if game exists
            try:
            	check = data['products'][0]
            except IndexError:
            	return await self.bot.say("No games found under that name on GOG.com. Try another search result.")
            	
            #Loading all required details into variables
            
            #Loading game details
            
            image = 'https' + data['products'][0]['image'] + '.png'
            title = data['products'][0]['title']
            genre = data['products'][0]['originalCategory']
            url = 'https://www.gog.com' + data['products'][0]['url']
            
            #Loading platform support
            platcount = 0
            platformtext = 'ready! to die'
            windows_support = data['products'][0]['worksOn']['Windows']
            linux_support = data['products'][0]['worksOn']['Linux']
            mac_support = data['products'][0]['worksOn']['Mac']
            if windows_support == True:
            	platcount = platcount + 1
            if linux_support == True:
            	platcount = platcount + 1
            if mac_support == True:
            	platcount = platcount + 1
            
            #Loading price details
            
            isdiscounted = data['products'][0]['isDiscounted']
            iscomingsoon = data['products'][0]['isComingSoon']
            isfree = data['products'][0]['price']['isFree']
            price = data['products'][0]['price']['symbol'] + data['products'][0]['price']['finalAmount']
            buyable = data['products'][0]['buyable']
            
            #THE REAL CODE BEGINS.
            # Formatting platform text. If platcount = 3, all platforms are added into the text. If 1, only one platform is added. If two, the first platform is added, followed by a ' and ' string, and then by the second platform finally.
            if platcount == 3:
            	platformtext = 'Windows, Linux and Mac.'
            elif platcount == 2:
            	if windows_support == True:
            		windows_checked == True
            		platformtext = platformtext + 'Windows'
            	elif linux_support == True:
            		linux_checked == True
            		platformtext = platformtext + 'Linux'
            	elif mac_support == True:
            		mac_checked == True
            		platformtext == platformtext + 'Mac'
            	platformtext == platformtext + ' and '
            	if (windows_support == True and windows_checked != True):
            		platformtext = platformtext + 'Windows'
            	elif (linux_support == True and linux_checked != True):
            		platformtext = platformtext + 'Linux'
            	elif (mac_support == True and mac_checked != True):
            		platformtext = platformtext + 'Mac'
            elif platcount == 1:
            	if windows_support == True:
            		platformtext = platformtext + 'Windows'
            	elif linux_support == True:
            		platformtext = platformtext + 'Linux'
            	elif mac_support == True:
            		platformtext == platformtext + 'Mac'
            	platformtext == platformtext + ' only'
            
            #Formatting price text.
            if isfree == True:
            	pricetext = 'Free'
            else:
            	if buyable == False:
            		pricetext = 'Not buyable yet.'
            	else:
            		pricetext = price
            if iscomingsoon == True:
            	pricetext = pricetext + ", coming soon!"
            
            bottext = 'null'
            bottext = "Title: " + title + "\n" + "Game URL: " + url + "\n" + "Game Image URL: " + image + "\n" + "Genre: " + genre + "\n" + "Platforms: " + platformtext + "\n"  + "Price: " + pricetext
            return await self.bot.say(bottext)


#            await self.bot.say("https://www.gog.com/games?sort=bestselling&search="+query)

    @commands.command()
    async def itch(self, *text):
        """Returns itch.io search results using item name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "+")
        await self.bot.say("https://itch.io/search?q="+query)

    @commands.command()
    async def steamid(self, text):
        """Returns Steam game page using the steam appid"""

        #Your code will go here
        await self.bot.say("http://store.steampowered.com/app/"+text+"/")
        
    @commands.command()
    async def steamuser(self, *text):
        """Returns Steam user page using custom user ID"""

        #Your code will go here
        text = " ".join(text)
        await self.bot.say("http://steamcommunity.com/id/"+text+"/")

    @commands.command()
    async def steamsearch(self, *text):
        """Returns Steam search results using game name"""

        #Your code will go here
#        if text=='gamecount':
#            url = "http://store.steampowered.com/search/#sort_by=_ASC&tags=-1&category1=998&page=1"
#            async with aiohttp.get(url) as response:
#                soupObject = BeautifulSoup(await response.text(), "html.parser") 
#            try:
#                count_unabridged = soupObject.find(class_='search_pagination_left').get_text()
#                count = count_unabridged.replace('				showing 1 - 25 of ', '')
#                await self.bot.say("There are " + count + " apps on Steam today.")
#            except:
#                await self.bot.say("Couldn't load amount of apps on Steam. There must be an error.")
#        else:
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("http://store.steampowered.com/search/?snr=1_4_4__12&term="+query)

    @commands.command()
    async def humbundle(self, *text):
        """Returns Humble Bundle search results using game name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://www.humblebundle.com/store/search/search/"+query)

    @commands.command()
    async def origin(self, *text):
        """Returns Origin search results using game name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://www.origin.com/en-ie/store/browse?q="+query)

    @commands.command()
    async def gplay(self, *text):
        """Returns Google Play search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://play.google.com/store/search?q="+query)

    @commands.command()
    async def ios(self, *text):
        """Returns Apple Appstore search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "-")
        await self.bot.say("http://www.apple.com/us/search/"+query)

    @commands.command()
    async def winstore(self, *text):
        """Returns Windows Store search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "+")
        await self.bot.say("https://www.microsoft.com/en-us/newsearch/result.aspx?q="+query+"&form=apps")

    @commands.command()
    async def xb(self, *text):
        """Returns Xbox Store search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "+")
        await self.bot.say("http://www.xbox.com/en-us/Search?q="+query)

    @commands.command()
    async def ps(self, *text):
        """Returns PlayStation search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://store.playstation.com/#!/en-us/search/q="+query)

    @commands.command()
    async def nintendo(self, *text):
        """Returns Nintendo eShop search results using app name"""

        #Your code will go here
        text = " ".join(text)
        query=text.replace(" ", "+")
        await self.bot.say("http://www.nintendo.com/search/#/results/"+query+"/1")


def setup(bot):
    bot.add_cog(appsearcher(bot))
