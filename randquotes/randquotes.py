import discord 
from discord.ext import commands
from random import randint
from random import choice as randchoice
from cogs.utils import checks
from __main__ import set_cog, send_cmd_help, settings
 
class randquotes: 
    """Random quotes!""" 
 
    def __init__(self, bot): 
        self.bot = bot 
 
    @commands.command() 
    async def steamrant(self): 
        """No. Ice.""" 
        await self.bot.say("In order to use Steam, you have to sign yourself into a contract which basically says \"YOU OWN NOTHING.\" The end result is that you end up buying licenses to games, which they can revoke anytime they wanted. They require the internet for the validation of licenses, which shouldn't be a requirement to play single player games. This results in an ecosystem that basically controls the titles you owned and gives you none of it, forcing you to stay into the ecosystem through the client to play the games you bought even if you don't want the client.")
        await self.bot.say("The best part about all of this is that they can change their contract terms and retroactively apply it onto all the games bought under the previous term. If you don't accept the changes, your account is terminated along with the licenses you've bought under the old terms. You only get to keep the licenses you bought under the old terms IF you agree to them retroactively applying the new terms onto them.")
        await self.bot.say("The end.")
        
    @commands.command() 
    async def callforhelp(self): 
        """I hate Flowey.""" 
        await self.bot.say("But nobody came.")
        
    @commands.command() 
    async def badtime(self): 
        """Sans Strikes Back.""" 
        badtime = ["You don't really want to click this link!\nhttps://jcw87.github.io/c2-sans-fight/",
                   "You don't really want to click this link!\nhttps://joezeng.github.io/endless-sans/"]
        await self.bot.say(randchoice(badtime))
        
    @commands.command()
    async def fairdyne(self):
        """The Undying"""
        await self.bot.say("NGAHHH!!\nhttps://joezeng.github.io/fairdyne/")

    @commands.command() 
    async def ia(self): 
        """INDIE ASSAULTED""" 
        ia = ["I would like to report this game for Indie Sexual Assault", "Spade was based off Sonic right? Then why is everyone complaining that he has a spindash?",
              "https://youtu.be/5XsLEXSyINs"]
        await self.bot.say(randchoice(ia))
        
    @commands.command() 
    async def fi(self): 
        """And you thought Navi was bad?""" 
        fi = ["YOUR BATTERIES ARE LOW, LINK.", "GOTTA BUY NEW BATTERIES, LINK!",
              "LINK, IT APPEARS YOUR BATTERIES ARE AT 75%. IT WOULD BE A GOOD IDEA TO PAUSE THE GAME AND CHANGE THEM NOW."]
        await self.bot.say(randchoice(fi))
         
    @commands.command(pass_context=True) 
    async def mn9(self, ctx): 
        """Mighty No. 9: Thoughts"""
        server = ctx.message.server
        if server.id=='174932651201921024':
            return
        else:
            mn9 = ["MIGHTY NO. 9 IS GETTING MIGHTIED OUTTA THE PLANET.", "Mighty No. 9? My pizza is late!!", "Mighty No. 9? How *unmighty*.",
                   "A thousand years would pass and still Mighty No. 9 would be quite the laughing stock...don't you think?", "Even Lambdadelta hates Mighty No. 9.", "4 million dollars did not save this game from turning into a flipping flop.",
                   "https://cdn.discordapp.com/attachments/174932651201921024/194933396621885452/13516359_666046493542630_5062462651910223041_n.png",
                   "https://images-2.discordapp.net/.eJwNx8ERwiAQAMBeKAA4EjnI30-aYJAgiSYeA5fx4di77m8_4my7mMTKXPuk1LL1RG2RnanFkmUhKnuOdesy0aEic0zrkV_cFeDgLWowYIYB0dpRgR_dPxY9OIcODSg-j9veArlE7_t85Q7NWMAnmdAgXLSWj1rE9wcErysP.1U6QQakVUAaZnjyk_Asamb9Bx5Y.jpg?width=287&height=300",
                   "https://67.media.tumblr.com/4fe613d88b23c4f10bc0194409aaf68e/tumblr_nommbxz03Q1qfb2lao1_540.png", "Mighty No. NEIN",
                   "Why buy the game if you can get it for free? Why buy games when you can get them for free, either? https://drive.google.com/folderview?id=0B7NlRHZE9SWSc2hucUlhdmhmMVU&usp=sharing",
                   "If Shovel Knight is the Good, and Azure Gunner Striker is the bad, then Mighty No 9 must be the ugly...", "Hello? Is this Keiji Inafune? Yeah? I'd like to order some pizza.",
                   "Should be called Mighty No. 69'd instead!", "7/10 Not Enough Pizza Explosions -IGN", "I tried to eat some of Mighty No. 9, but I couldn't.",
                   "Asgore didn't hesitate to banish Mighty No. 9 from the Underworld. You must be **THAT BAD** for *Asgore* to do this!", "Seraphna banned this command? Outrageous!", "8.5 Too Much Dashing.",
                   "Mighty No. 9 has been convicted of murdering Megaman in the past. Be careful around it.", "MN9 is the best horror game around...at least according to Steam's 'community'.",
                   "Delivery of pizza has been halted for an unknown reason.", "So yeah, got your money's worth out of the game yet? Oh, wait, this...thing isn't even worth 4 million.",
                   "In the future, someone will burn Scuttle Town again, but with Mighty No. 9 copies.", "Battler tried to play Mighty No. 9...before Jessica smashed the screen...",
                   "Crash Bandicoot wants your love.", "https://cdn.discordapp.com/attachments/173967012123377664/196816534864134155/69087288.jpg", "Spyro is better.",
                   "I once made a pizza out of Mighty No. 9 copies.", "Mighty No. 9 has killed Spongebob. IT IS A HERO!", "Timmy wished that Vicky wouldn't use medieval tools for torturing him. She tortures him with Mighty No. 9 instead.",
                   "Can't wait for Mighty No. 9 creepypasta!", "Where's Mighty No. 8, 7, 6, 5, 4, 3, 2 and 1?! 0/10 bad game.", "Lord Arktivus Brevon was caught with a copy of Mighty No. 9 in his Dreadnought. It must be a horrible game.",
                   "The last time Shantae fought Mighty No. 9, she fainted before the battle even started.", "Mighty No. 9 started the apocalypse. Run.",
                   "Meanwhile at Nintendo Studios...:\nSakura: Why should you be in Smash?\nShantae: Because I think I would be a valuable fighter in your roster\nSakura: Oh ok. What about you?\nBeck: I CAN JUMP AND SHOOT...\nSakura: Oh okayyyyy\nBeck: AND DASH! smiles and winks\nSakura whispers: can someone get him outta here?",
                   "Call's lack of personality makes her the perfect contender for a sex toy", "Mighty No. 9 killed the cat.",
                   "https://images-1.discordapp.net/.eJwFwdsNwyAMAMBdGADHPAxkG0QQSZXUCLtfVXfv3dd81m12c6pO2QGOSxqvw4ryqqPbwTzuXucltvEDVbW28-lvFcDkC6UNHTrvUyIKgIUyUvQhU0AfMEagsuXkcravOczvDxhKIXs.Kkw3TpBf_cvTw3G3CXAsgcI5CX4.jpg",
                   "The Mighty No. 9 Pizza! Is the Pizza! For you and me!", "http://i0.kym-cdn.com/photos/images/newsfeed/001/139/678/2d2.png",
                   "This game is quite dashing..........in a bad way", "Announcing Domino's new special edition pizza: the Mighty Meaty No. 9",
                   "Don't you mean 'Meh'ty Number No. 9?", "When you install a Mighty No. 9 function on your buster\nhttps://cdn.discordapp.com/attachments/173965999744221185/197744572514828289/unknown.png",
                   "I once heard Alex Kidd beat up Beck.", "Damn, that playthrough of MN9 made me hungry for some pizza.",
                   "As much as I give it flak, it's better than FNaF anyday, everyday. *cackles*", "Mighty No. 9 does what Megamandon't.",
                   "Mighty? Yes. Mega? No.", "http://lvl30psy.thecomicseries.com/images/comics/64/e1fc6f772a6cd154c3b027e3a26671f9948643108.png",
                   "I'd rather have Rock and Roll at my Beck and Call", "poor roahmmythril hes gonna have to perfect run this game someday",
                   "Look at my codpiece! You know you want to.\nhttp://media1.gameinformer.com/filestorage/CommunityServer.Components.SiteFiles/imagefeed/featured/comcept/mightyno9/release-date/MightyNo9RD-610.jpg",
                   "http://i.imgur.com/byQgSDr.png","https://cdn.discordapp.com/attachments/173967012123377664/201530405877186560/did-you-mean-0686f1224818a4a6520cd99c626f74ee.png",
                   "I like my Mighty No. 9 with extra anchovies and a garlic cheese stuffed crust.","http://i1.kym-cdn.com/photos/images/newsfeed/001/147/617/a31.png"
                   ]
            return await self.bot.say(randchoice(mn9))
        
    @commands.command() 
    async def sjw(self): 
        """And you thought Navi was bad?""" 
        sjw = ["You're an SJW? So you're a salty juvenile wiener?","SJW: Shameful Jackass Whiner",
               "SJW: Supreme Jackass Whiner","SJW: Super-triggered Justiceless Wanker",
               "https://didyoumean-generator.com/did-you-means/20160714/did-you-mean-66fab343163deb1bac408f4fb30587b4.png"]
        await self.bot.say(randchoice(sjw))
        
    @commands.command()
    async def navyseal(self):
        """You read this already, probably."""
        await self.bot.say("```What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.```")

    @commands.command()
    async def redrant(self):
        """Salt, RedScarf-style"""
        await self.bot.say("```well, that's what happens when blah blah blah battleaxe blah blah blah broken promises blah blah blah abuse of power blah blah blah```")
        
    @commands.command() 
    async def gametheory(self):
        """The study of mathematical models of conflict and cooperation between intelligent rational decision-makers. Apparently.""" 
        gametheory = ["Game Theory: MatPat is a SHAMELESS MONEYGRABBING CUNT?!?!","Why i gave the pope bayonetta"]
        await self.bot.say(randchoice(gametheory))

    @commands.command()
    async def giga(self):
        """Salami the Multivitamin"""
        await self.bot.say("MMMMMMMMMMH :heart:")
        
    @commands.command()
    async def sonic(self):
        """GOTTAGOFAST"""
        sonic = ["***YOU'RE TOO SLOW!***","Let's do it to it!","Hands off my chilli dogs!","Way past cool!","Catch you later, Eggman!"]
        await self.bot.say(randchoice(sonic))

def setup(bot):
    bot.add_cog(randquotes(bot))
