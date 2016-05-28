import discord
from random import randint
from random import choice as randchoice
from discord.ext import commands

class randimages:
    """Random images!"""

    def __init__(self, bot):
        self.bot = bot
        self.sonozaki = ["http://images4.fanpop.com/image/photos/22700000/Shion-Sonozaki-sonozaki-fans-22705531-704-396.jpg",
                         "http://img1.ak.crunchyroll.com/i/spire2/fc24e1a77e12e1e0007185cd42e750541371546895_full.jpg",
                         "http://img1.ak.crunchyroll.com/i/spire2/fc24e1a77e12e1e0007185cd42e750541371546895_full.jpg",
                         "http://img1.ak.crunchyroll.com/i/spire2/fc24e1a77e12e1e0007185cd42e750541371546895_full.jpg",]

        
    @commands.command()
    async def shion(self):
        """HAHAHAHAHAHAHAHAHAHAHA!"""

        #Your code will go here
        return await self.bot.say(randchoice(self.sonozaki))

    @commands.command()
    async def freiza(self):
        """This isn't even my final form!"""

        #Your code will go here
        freiza = ["http://img-9gag-fun.9cache.com/photo/a9PmRPm_700b.jpg",
               "http://brain-images.cdn.dixons.com/0/9/20163490/l_20163490_001.jpg"]
        return await self.bot.say(randchoice(freiza))

    @commands.command()
    async def graphics(self):
        """The stupidity of graphics arguments"""

        #Your code will go here
        await self.bot.say('http://i.imgur.com/5m3zGue.jpg')

    @commands.command()
    async def dealwithit(self):
        """Cool glasses."""

        #Your code will go here
        await self.bot.say('http://imgur.com/HuoQG53')

    @commands.command()
    async def youdied(self):
        """Back to Dark Souls."""

        #Your code will go here
        await self.bot.say("http://img4.wikia.nocookie.net/__cb20130515050459/darksouls/images/6/63/You-Died.jpg")

    @commands.command()
    async def jojo(self):
        """Move out."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/2f19khz.gif")

    @commands.command()
    async def iamyourfather(self):
        """The Father Strikes Back."""

        #Your code will go here
        await self.bot.say("http://i.perezhilton.com/wp-content/uploads/2015/11/star-wars-empire-strikes-back-movie-misquote.gif")

    @commands.command()
    async def rip(self):
        """Rest in Peace."""

        #Your code will go here
        await self.bot.say("http://www.spokeo.com/blog/wp-content/uploads/2011/05/RIP-Spokeo-Info-Bubble.jpg")

    @commands.command()
    async def facepalm(self):
        """When the fail is strong enough."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/iWKad22.jpg")

    @commands.command()
    async def doublefacepalm(self):
        """When the fail is even stronger."""

        #Your code will go here
        await self.bot.say("http://robinbrown.co.uk/wp-content/uploads/2012/02/double-facepalm1.jpg")

    @commands.command()
    async def pizza(self):
        """Oh boy I'm so hungry."""

        #Your code will go here
        await self.bot.say("http://www.tonysfoodphotos.com/data/photos/67_1stuffed_crust_pizza.jpg")
  
    @commands.command()
    async def disappointed(self):
        """I am disappoint."""

        #Your code will go here
        await self.bot.say("https://media.giphy.com/media/3oAt21Fnr4i54uK8vK/giphy.gif")      
        
    @commands.command()
    async def mandms(self):
        """Lambdadelta likes M&Ms."""

        #Your code will go here
        await self.bot.say("http://1.bp.blogspot.com/-rtC_BMawGH0/Tu6wXOwbZjI/AAAAAAAANCY/hmLDW8aOINc/s1600/6533753255_537c347d96_o.jpg")

    @commands.command()
    async def gowrong(self):
        """What could possibly go wrong?"""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/o1DnKkL.png")

    @commands.command()
    async def dance(self):
        """Dance."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/4HbsKX1.gif")

    @commands.command()
    async def doge(self):
        """Awww......"""

        #Your code will go here
        await self.bot.say("http://barkpost-assets.s3.amazonaws.com/wp-content/uploads/2013/11/dogesmall.jpg")

    @commands.command()
    async def limewire(self):
        """Do what you want cause a pirate is free."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/1h6HMiV.gifv")

    @commands.command()
    async def meteorstrike(self):
        """Presented by Sabin and Tom Slattery."""

        #Your code will go here
        await self.bot.say("http://static.fjcdn.com/gifs/What_a9d5b5_5443845.gif")
        
    @commands.command()
    async def suplex(self):
        """Presented by SABIN and TED WOOLSEY."""

        #Your code will go here
        await self.bot.say("http://www.gamingrebellion.com/wp-content/uploads/2015/09/FF6-Train-Suplex.gif?9d7bd4")

    @commands.command()
    async def genesisdoes(self):
        """What Nintendon't."""

        #Your code will go here
        await self.bot.say("http://static1.squarespace.com/static/550b8a2ae4b0558c356e47f5/t/55de6fa3e4b0b8c9e8eb629c/1440640932037/")

    @commands.command()
    async def nuke(self):
        """Wipe out everything."""

        #Your code will go here
        await self.bot.say("http://www.chrisewings.com/images/Misc/images/Nuke%203_jpg.jpg")

    @commands.command()
    async def gooddaysir(self):
        """Presented by Willy Wonka."""

        #Your code will go here
        await self.bot.say("http://giphy.com/gifs/reaction-angry-gFjbkip9OIIuI")

    @commands.command()
    async def awake(self):
        """I have a bad feeling about this."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/RqgiDtI.gif")
        
    @commands.command()
    async def weebstick(self):
        """Because we REALLY NEEDED an Overwatch GIF."""

        #Your code will go here
        await self.bot.say("http://imgur.com/PIpsc02")

    @commands.command()
    async def notprepared(self):
        """You are dead."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/Ch9TMSd.gif")

    @commands.command()
    async def dank(self):
        """Uhh."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/EUChYKI.gif")

    @commands.command()
    async def pcmr(self):
        """Glorious PC Master Race."""

        #Your code will go here
        await self.bot.say("https://i.ytimg.com/vi/jrxXyTHPPCw/hqdefault.jpg")

    @commands.command()
    async def ora(self):
        """Ora Ora Ora Ora!!!"""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/A2ZzU39.gif")

    @commands.command()
    async def ata(self):
        """ATATATATATATATA- *sigh* I'm tired."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/UC5EUda.gif")

    @commands.command()
    async def frustrated(self):
        """I hate my life."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/shlFpZM.gif")

    @commands.command()
    async def getgood(self):
        """...it means get good."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/XKw7Yot.gif")

    @commands.command()
    async def bye(self):
        """Goodbye!"""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/YXhYUud.gif")

    @commands.command()
    async def nom(self):
        """Eats-a-Otter"""

        #Your code will go here
        await self.bot.say("http://imgur.com/zMJ0ErL")

    #@commands.command()
    #async def meh(self):
   #     """Very mediocre."""
#
   #     #Your code will go here
   #     await self.bot.say("http://i.imgur.com/vsjdjje.webm")

    @commands.command()
    async def endlesseight(self):
        """15532"""

        #Your code will go here
        await self.bot.say("http://2.bp.blogspot.com/_uj_QeQVH3-g/TByp6OOnSRI/AAAAAAAAAX8/0PS_lfCcto4/s1600/Suzumiya+Haruhi+endless+eight!.jpg")

    @commands.command()
    async def megaman(self):
        """A NEW MEGAMAN GAME!!"""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/I5tpeYT.gif")

    @commands.command()
    async def justinbieber(self):
        """[Insert Bieber song here]"""

        #Your code will go here
        await self.bot.say("http://i3.kym-cdn.com/photos/images/newsfeed/000/628/701/e5f.gif")

    @commands.command()
    async def internet(self):
        """The internet? I thought it was a dinosaur?"""

        #Your code will go here
        await self.bot.say("https://cdn.discordapp.com/attachments/174932651201921024/180800690233409537/10172634_10152398016887929_353810091488771162_n.jpg")

    @commands.command()
    async def zerofucks(self):
        """I don't care enough."""

        #Your code will go here
        await self.bot.say("https://images-2.discordapp.net/.eJwVyEkOwyAMAMC_8ADMErHkN4hQg5TUCLuHqurf21zmMB_1WqfaVReZvAMcgyutQ7PQKtg0EuHZyhysK11QRErtV3sKg40x5exMssZZG30Od2Xjk9tM-OtTDIBj9rfG8VDfH8FeIes.-986DO-paeh4B02b83dM92oEf14.gif")

def setup(bot):
    bot.add_cog(randimages(bot))
