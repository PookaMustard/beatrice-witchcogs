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
    async def steam(self): 
        """No. Ice.""" 
        await self.bot.say("In order to use Steam, you have to sign yourself into a contract which basically says \"YOU OWN NOTHING.\" The end result is that you end up buying licenses to games, which they can revoke anytime they wanted. They require the internet for the validation of licenses, which shouldn't be a requirement to play single player games. This results in an ecosystem that basically controls the titles you owned and gives you none of it, forcing you to stay into the ecosystem through the client to play the games you bought even if you don't want the client.")
        await self.bot.say("The best part about all of this is that they can change their contract terms and retroactively apply it onto all the games bought under the previous term. If you don't accept the changes, your account is terminated along with the licenses you've bought under the old terms. You only get to keep the licenses you bought under the old terms IF you agree to them retroactively applying the new terms onto them.")
        await self.bot.say("The end.")
        
    @commands.command() 
    async def callforhelp(self): 
        """I hate Flowey.""" 
        await self.bot.say("But nobody came.")
        
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
                   "Mighty? Yes. Mega? No.", "http://lvl30psy.thecomicseries.com/images/comics/64/e1fc6f772a6cd154c3b027e3a26671f9948643108.png"
                   ]
            return await self.bot.say(randchoice(mn9))
        

def setup(bot):
    bot.add_cog(randquotes(bot))
