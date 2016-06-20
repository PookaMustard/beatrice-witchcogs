import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
from discord.ext import commands
import datetime
import time
import aiohttp
import asyncio

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
    async def nope(self):
        """No. Just no."""

        #Your code will go here
        nope = ["https://cdn.discordapp.com/attachments/173967012123377664/192449277249716226/Ck8hjiJUYAA9bKl.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/192450306016018433/ExtremeNope.gif"]
        return await self.bot.say(randchoice(nope))
        
    @commands.command()
    async def shantae(self):
        """Ever dreamed of bathing with your clothes on?"""

        #Your code will go here
        nope = ["http://i.imgur.com/FyUAAw0.png",
               "http://i.imgur.com/n74nqYR.png"]
        return await self.bot.say(randchoice(nope))
        
    @commands.command()
    async def salt(self):
        """Have salt?"""

        #Your code will go here
        salt = ["http://vignette1.wikia.nocookie.net/kancolle/images/9/9a/Want_some_salt.jpg",
               "https://cdn.meme.am/instances/500x/55031607.jpg",
               "https://media.makeameme.org/created/well-then-you-q1b8n1.jpg"]
        return await self.bot.say(randchoice(salt))
        
    @commands.command()
    async def OvO(self):
        """Bingo!"""

        #Your code will go here
        ovo = ["https://cdn.discordapp.com/attachments/173967012123377664/190571971564666881/Screen_Shot_2015-10-30_at_6.22.16_PM.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/190572657270456321/IMG_0670.jpg",
               "https://cdn.discordapp.com/attachments/173967012123377664/190607662881308683/Bingo_in_FP_CS_Icon_OvO.png",
               "https://cdn.discordapp.com/attachments/173967012123377664/190607776324517890/BstayR_OvO.png"]
        return await self.bot.say(randchoice(ovo))
        
    @commands.command(hidden=True)
    async def weegee(self):
        """Weegeesquare!"""

        #Your code will go here
        weegee = ["https://lh6.googleusercontent.com/-dWUzHO0twIQ/V1n-efytS3I/AAAAAAAACUM/pPozGcXTDSIwdvhzRVQSoqJFq5v43jMzQCL0B/w48-h64-no/DLonk_idle_0.png",
               "https://lh6.googleusercontent.com/-O2H_nPtZ_lM/V1n-jhEoz9I/AAAAAAAACUM/WkewVrDQQcAWXJs2o2koF24gg2pWVBdYQCL0B/w88-h57-no/Weegee%2527s%2BRequest%252C%2Bwith%2Ba%2Btweak_20160319_190508.jpg",
               "https://lh5.googleusercontent.com/-7Lg4VvNReMA/V1n-kzsdwOI/AAAAAAAACUM/SupCobm8h5QP3_XCE0qc2_W6PKgq3L7gQCL0B/w47-h51-no/2_20160417_202903.jpg",
               "https://lh6.googleusercontent.com/-QEW_5_hdVj8/V1n-tSioO0I/AAAAAAAACUM/PYwEpkGMFLwjXU-RsebrZWgB1A3yND-vACL0B/s32-no/spr_Deb_0.png",
               "https://lh3.googleusercontent.com/-IjEvwALlGyg/V1n-zXJA5iI/AAAAAAAACUU/Li32CfrZ4oMl_cXBq8lPvXKcErZ8GsNuACL0B/w48-h50-no/spr_RyanBAS2_12.png"]
        return await self.bot.say(randchoice(weegee))
        
    @commands.command()
    async def kfl(self):
        """Kentucky Fried Luigi!"""

        #Your code will go here
        kfl = ["https://lh4.googleusercontent.com/-oexhXFIUcws/V1n---gChkI/AAAAAAAACUU/sAMqbgqIDrclqFldgu6vx25FAKyPQ_O0QCL0B/w48-h64-no/KFC_specN_3.png",
               "https://lh4.googleusercontent.com/-JD0NJULjAzg/V1n-8msS0_I/AAAAAAAACUU/SMUkD1JDxHQ-BKRz99Apg1m5YbTjFLdoQCL0B/w48-h64-no/KFC_specD_7.png"]
        return await self.bot.say(randchoice(kfl))
        
    @commands.command()
    async def bsod(self):
        """The Ultimate Screen."""

        #Your code will go here
        bsod = ["http://f.fwallpapers.com/images/bsod-xp.jpg",
               "http://thewindowsclub.thewindowsclubco.netdna-cdn.com/wp-content/uploads/2015/09/Blue-Screen-of-Death-Windows-10.png"]
        return await self.bot.say(randchoice(bsod))

    @commands.command(pass_context=True)
    async def darules(self, ctx):
        """The loopholes are strong."""

        #Your code will go here
        server = ctx.message.server
        await self.bot.say('http://vignette2.wikia.nocookie.net/fairlyoddparents/images/6/65/Abracatastrophe0793.jpg/revision/latest?cb=20160526203432&path-prefix=en')
        if server.id=='181225160622342144':
            await self.bot.say('Check server rules in ' + '<#181228813982760960>' +'!')
        elif server.id=='173965999744221185':
            await self.bot.say('Check server rules in ' + '<#173967163344945152>' +'!')

    @commands.command(pass_context=True)
    async def elrules(self, ctx):
        """The loopholes are sexy."""

        #Your code will go here
        server = ctx.message.server
        await self.bot.say('http://vignette4.wikia.nocookie.net/fairlyoddparents/images/9/99/FairyFairyQuiteContrary094.jpg/revision/latest?cb=20110404231200&path-prefix=en')
        if server.id=='181225160622342144':
            await self.bot.say('Check server rules in ' + '<#181228813982760960>' +'!')
        elif server.id=='173965999744221185':
            await self.bot.say('Check server rules in ' + '<#173967163344945152>' +'!')

    @commands.command()
    async def lilac(self):
        """She's a dragon dragon."""

        #Your code will go here
        await self.bot.say('http://vignette3.wikia.nocookie.net/freedomplanet/images/0/05/Lilac_Sketch_by_Stephen_DiDuro.png/revision/latest?cb=20140803235415')
        
    @commands.command()
    async def carol(self):
        """She's a wildcat wildcat."""

        #Your code will go here
        await self.bot.say('http://vignette4.wikia.nocookie.net/freedomplanet/images/a/a7/Carol_Sketch_by_Stephen_DiDuro.jpg/revision/latest?cb=20140805001110')
        
    @commands.command()
    async def milla(self):
        """She's a dog dog."""

        #Your code will go here
        await self.bot.say('http://vignette1.wikia.nocookie.net/freedomplanet/images/9/90/Milla_Basset_Sketch_by_Stephen_DiDuro.png/revision/latest?cb=20140805001350')

    @commands.command()
    async def graphics(self):
        """The stupidity of graphics arguments"""

        #Your code will go here
        await self.bot.say('http://i.imgur.com/5m3zGue.jpg')
        
    @commands.command()
    async def thumbsup(self):
        """Going overboard, aren't we?"""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/193897410664202241/Megalike.gif')
        
    @commands.command()
    async def okay(self):
        """I approve of this."""

        #Your code will go here
        await self.bot.say('http://i.makeagif.com/media/10-04-2015/f0UVsa.gif')
        
    @commands.command()
    async def puru(self):
        """Japanese stuff..."""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192355333035786242/PuruProtocultureJoke.PNG')
        
    @commands.command()
    async def rekt(self):
        """Poor stormtrooper..."""

        #Your code will go here
        await self.bot.say('http://i.imgur.com/9sKSRFD.gifv')

    @commands.command()
    async def yay(self):
        """I love it!"""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/192751917770866689/Yay.gif')
 
    @commands.command()
    async def niccage(self):
        """Featuring Nicolas Cage!"""

        #Your code will go here
        await self.bot.say('https://i.ytimg.com/vi/G8GVWhviw8s/hqdefault.jpg') 
        
    @commands.command()
    async def tobecontinued(self):
        """Coming Soon!"""

        #Your code will go here
        await self.bot.say('https://img0.etsystatic.com/059/0/10858326/il_570xN.762412812_ccx3.jpg')    
        
    @commands.command()
    async def escalated(self):
        """Escalators are fun. Also boring."""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173967012123377664/193499284899889153/b93f0e354df1d3a803f8e47adaae7651.png')    
        
    @commands.command()
    async def zerosystem(self):
        """Startup initiation commence!"""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/189389254093307905/191661403596259330/tumblr_zerosystem.gif')
        
    @commands.command()
    async def examwarning(self):
        """Beware the exam!"""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192311643969945601/EXAM_System_-_Activated.jpg')

    @commands.command()
    async def android(self):
        """THE Google Android"""

        #Your code will go here
        await self.bot.say('http://crackberry.com/sites/crackberry.com/files/styles/large/public/topic_images/2013/ANDROID.png?itok=xhm7jaxS')
        
    @commands.command()
    async def tumbleweed(self):
        """Pure abandonement."""

        #Your code will go here
        await self.bot.say('https://brittnyhabibti.files.wordpress.com/2014/10/tumbleweed.jpg')
        
    @commands.command()
    async def headdesk(self):
        """When the fail is even stronger."""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192431766726901761/Headdesk_Violent.gif')
        
    @commands.command()
    async def burnheal(self):
        """You're going to need it."""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192432102313164801/4313739.png')
        
    @commands.command()
    async def spoileralert(self):
        """Massive spoilers incoming!"""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192432214238167042/Spoiler_Alert.jpg')
        
    @commands.command()
    async def supertorque(self):
        """He's a super alien alien."""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192432139415977985/IMG_16052016_111115.png')
        
    @commands.command()
    async def technicallycorrect(self):
        """Correctly correct!"""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/173965999744221185/192432893694443522/TBKOC.jpg')
        
    @commands.command()
    async def steamnazis(self):
        """Steam in a nutshell."""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/178247098737754133/189429160525955073/aynA4ZY_700b_v1.jpg')
        
    @commands.command()
    async def dealwithit(self):
        """Cool glasses."""

        #Your code will go here
        await self.bot.say('http://imgur.com/HuoQG53')
        
    @commands.command()
    async def objection(self):
        """Cool pose."""

        #Your code will go here
        await self.bot.say('https://cdn.discordapp.com/attachments/167706685715120129/189796749420789763/objection.jpg')

    @commands.command()
    async def youdied(self):
        """Back to Dark Souls."""

        #Your code will go here
        await self.bot.say("http://img4.wikia.nocookie.net/__cb20130515050459/darksouls/images/6/63/You-Died.jpg")
        
    @commands.command()
    async def aerisisdead(self):
        """SPOILER ALERT! And I don't care about 'Aerith'."""

        #Your code will go here
        await self.bot.say("https://geekgirlmagazine.files.wordpress.com/2012/02/aeris-death.jpg")

    @commands.command()
    async def jojo(self):
        """Move out."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/2f19khz.gif")
        
    @commands.command()
    async def confoundthem(self):
        """Don't drink THAT much!"""

        #Your code will go here
        await self.bot.say("http://imgur.com/wDKwqN0")

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
    async def undersans(self):
        """(comic sans font): undertale sans"""

        #Your code will go here
        await self.bot.say("http://i2.kym-cdn.com/photos/images/newsfeed/001/021/889/68d.gif")
        
    @commands.command()
    async def smug(self):
        """Smugging hard."""

        #Your code will go here
        await self.bot.say("https://cdn.discordapp.com/attachments/184816492838256640/190986742227009538/IMG_0291.JPG")
        
    @commands.command()
    async def smugmode(self):
        """Smugging harder."""

        #Your code will go here
        await self.bot.say("https://v.dreamwidth.org/27224/52508")
        
    @commands.command()
    async def muda(self):
        """Another anime punch GIF."""

        #Your code will go here
        await self.bot.say("http://imgur.com/6zcE2Vz")
        
    @commands.command()
    async def zawurado(self):
        """Flashing images. Please consult your doctor."""

        #Your code will go here
        await self.bot.say("http://38.media.tumblr.com/c2d4006f53aa908b6de083ee4a7672d3/tumblr_n5xz2qbEmM1r6mrcio3_250.gif")

    @commands.command()
    async def barvon(self):
        """Duke Arktivus Barvon at your service."""

        #Your code will go here
        await self.bot.say("https://cdn.discordapp.com/attachments/173965999744221185/192621822108237825/barvon.png")

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
    async def animesucks(self):
        """Use this before it enters 'Murica."""

        #Your code will go here
        await self.bot.say("http://i1.kym-cdn.com/photos/images/newsfeed/000/708/423/caf.jpg")
        
    @commands.command()
    async def fuckanime(self):
        """Use this after it enters 'Murica."""

        #Your code will go here
        await self.bot.say("http://www.meh.ro/original/2009_11/meh.ro2857.jpg")

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
    async def boo(self):
        """ULTRA SCARY."""

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
    async def praisethesun(self):
        """Praise it."""

        #Your code will go here
        await self.bot.say("http://i.imgur.com/YA2WFS8.png")
        
    @commands.command()
    async def sun(self):
        """We all love her."""

        #Your code will go here
        await self.bot.say("http://solarsystemexplore.com/wp-content/uploads/2012/11/The-Sun.jpg")

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
    async def drm(self):
        """The pirates are badass, too."""

        #Your code will go here
        await self.bot.say("http://static.fjcdn.com/gifs/Drm+sucks+drm+is+not+good+for+anyone_2de156_4485223.gif")

    @commands.command()
    async def gooddaysir(self):
        """Presented by Willy Wonka."""

        #Your code will go here
        await self.bot.say("http://giphy.com/gifs/reaction-angry-gFjbkip9OIIuI")

    @commands.command()
    async def fetish(self):
        """That is my fetish."""

        #Your code will go here
        await self.bot.say("http://imgur.com/LiRYZeY")
        
    @commands.command()
    async def killthoseponies(self):
        """Bring them back to death."""

        #Your code will go here
        await self.bot.say("http://www.dailyfreegames.com/images/thumbsfree/KTPON150.jpg")     

    @commands.command()
    async def itsover9000(self):
        """What does the scouter say about their power level?"""

        #Your code will go here
        await self.bot.say("http://blog.sheasilverman.com/wp-content/uploads/2014/05/tumblr_lwhv2roIab1qd47jqo1_500.gif")    
        
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
        await self.bot.say("http://i.imgur.com/EUChYKI.gifv")
        
    @commands.command()
    async def finalcountdown(self):
        """Venus isn't a good place to live."""

        #Your code will go here
        await self.bot.say("http://b.vimeocdn.com/ts/234/533/234533071_640.jpg")

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
    async def bendgate(self):
        """Yes, iPhone 6+s are still bent to this day."""

        #Your code will go here
        await self.bot.say("http://pbs.twimg.com/media/By90YiIIcAAeyYh.jpg")

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
        
    @commands.command()
    async def clap(self):
        """And it's Snow White clapping!"""

        #Your code will go here
        await self.bot.say("http://cdn2.business2community.com/wp-content/uploads/2014/02/SnowWhiteClapping8.gif")

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
