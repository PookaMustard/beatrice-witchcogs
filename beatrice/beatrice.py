import discord
import random
from random import randint
from random import choice as randchoice
from discord.ext import commands

class beatrice:
    """Commands for Beatrice. *cackle*cackle*cackle*"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uminekochars(self):
        """Random Umineko character images!"""
        char = ["Beatrice (A.K.A. me, you idiot.)\nhttp://vignette2.wikia.nocookie.net/umineko/images/0/02/Bea_a11_akuwarai5.png/revision/latest/scale-to-width-down/270?cb=20120227220630",
                "Bernkastel\nhttp://vignette2.wikia.nocookie.net/umineko/images/1/18/Ber_a24_akuwarai3.png/revision/latest/scale-to-width-down/270?cb=20130925011239",
                "Lambdadelta\nhttp://vignette1.wikia.nocookie.net/umineko/images/f/f0/Lambdadelta1.png/revision/latest/scale-to-width-down/270?cb=20110805145404",
                "Featherine Augustus Aurora\nhttp://vignette4.wikia.nocookie.net/umineko/images/4/47/Fea_b11_warai2.png/revision/latest/scale-to-width-down/270?cb=20120127223228",
                "Kanon\nhttp://vignette3.wikia.nocookie.net/umineko/images/e/ee/Kan_a12_default_2.png/revision/latest/scale-to-width-down/252?cb=20111219174303",
                "Genji Ronoue\nhttp://vignette2.wikia.nocookie.net/umineko/images/c/c9/Gen_a11_default_1.png/revision/latest/scale-to-width-down/270?cb=20120124012905",
                "Ronove\nhttp://vignette2.wikia.nocookie.net/umineko/images/a/a3/Ron_a11_default_1.png/revision/latest/scale-to-width-down/270?cb=20111219174603",
                "Sakutarou\nhttp://vignette4.wikia.nocookie.net/umineko/images/b/b1/Sak_a13_warai1.png/revision/latest/scale-to-width-down/270?cb=20130925000007",
                "Zepar (gender unknown)\nhttp://vignette4.wikia.nocookie.net/umineko/images/0/0c/Zep_a12_def1.png/revision/latest/scale-to-width-down/270?cb=20120127220404",
                "Furfur (gender unknown)\nhttp://vignette3.wikia.nocookie.net/umineko/images/6/6d/Fur_a12_def1.png/revision/latest/scale-to-width-down/270?cb=20120127220804",
                "Goat Butlers\nhttp://vignette4.wikia.nocookie.net/umineko/images/7/7e/Goats.png/revision/latest/scale-to-width-down/270?cb=20111112021420",
                "Virgillia\nhttp://vignette1.wikia.nocookie.net/umineko/images/3/39/Virgilia5.png/revision/latest/scale-to-width-down/270?cb=20111212210826",
                "Battler Ushiromiya (A.K.A. my future hasband)\nhttp://vignette2.wikia.nocookie.net/umineko/images/c/c0/Ushiromiya_Battler2.png/revision/latest/scale-to-width-down/270?cb=20111212210826",
                "Kinzo Ushiromiya (A.K.A. the person whom I gave 10 tons of gold)\nhttp://vignette4.wikia.nocookie.net/umineko/images/1/1c/Ep5_1_kin_EP5_1_kin.png/revision/latest/scale-to-width-down/270?cb=20131115080450",
                "Asmodeus (A.K.A. one of the Stakes of Purgatory)\nhttp://vignette4.wikia.nocookie.net/umineko/images/0/08/Asmodeus1.png/revision/latest/scale-to-width-down/270?cb=20110915143350",
                "Satan (A.K.A. one of the Stakes of Purgatory)\nhttp://vignette2.wikia.nocookie.net/umineko/images/1/1c/Satan1.png/revision/latest/scale-to-width-down/270?cb=20111219202833",
                "Krauss Ushiromiya\nhttp://vignette1.wikia.nocookie.net/umineko/images/9/95/Cla_a11_default_1.png/revision/latest/scale-to-width-down/270?cb=20120125200822",
                "Gaap\nhttp://vignette1.wikia.nocookie.net/umineko/images/0/08/Gaap3.png/revision/latest/scale-to-width-down/270?cb=20111219200336",
                "Maria Ushiromiya\nhttp://vignette1.wikia.nocookie.net/umineko/images/d/de/Ushiromiya_Maria3.png/revision/latest/scale-to-width-down/270?cb=20111112020834",
                "George Ushiromiya\nhttp://vignette1.wikia.nocookie.net/umineko/images/9/92/Ushiromiya_George2.png/revision/latest/scale-to-width-down/270?cb=20111013015611",
                "Belphegor (A.K.A. one of the Stakes of Purgatory)\nhttp://vignette2.wikia.nocookie.net/umineko/images/8/82/Stakes_Belphegor2.png/revision/latest/scale-to-width-down/270?cb=20111112015426",
                "Cornelia\nhttp://vignette2.wikia.nocookie.net/umineko/images/f/fe/Cor_a11_def1.png/revision/latest/scale-to-width-down/270?cb=20120127221610",
                "Dlanor A. Knox\nhttp://vignette2.wikia.nocookie.net/umineko/images/b/b3/Dla_a11_def1.png/revision/latest/scale-to-width-down/270?cb=20140125150839",
                "Rudolf Ushiromiya\nhttp://vignette2.wikia.nocookie.net/umineko/images/1/16/Rudolf.png/revision/latest/scale-to-width-down/270?cb=20120102184452",
                "Ange Ushiromiya\nhttp://vignette2.wikia.nocookie.net/umineko/images/1/1e/129868919028.png/revision/latest/scale-to-width-down/270?cb=20111129115935",
                "Lucifer (A.K.A. one of the Stakes of Purgatory)\nhttp://vignette4.wikia.nocookie.net/umineko/images/8/84/Lucifer2.png/revision/latest/scale-to-width-down/270?cb=20111219201651",
                "Chiester 00\nhttp://vignette2.wikia.nocookie.net/umineko/images/7/78/Siesta00.png/revision/latest/scale-to-width-down/270?cb=20111215225332",
                "Gertrude\nhttp://vignette2.wikia.nocookie.net/umineko/images/f/ff/Ger_a11_def1.png/revision/latest/scale-to-width-down/270?cb=20120127221451",
                "Leviathan (one of the Stakes of Purgatory)\nhttp://vignette2.wikia.nocookie.net/umineko/images/9/96/Leviathan1.png/revision/latest/scale-to-width-down/270?cb=20111219202125",
                "Mammon (one of the Stakes of Purgatory)\nhttp://vignette4.wikia.nocookie.net/umineko/images/3/3a/Mammon2.png/revision/latest/scale-to-width-down/270?cb=20111219203528",
                "Beelzebub (one of the Stakes of Purgatory)\nhttp://vignette1.wikia.nocookie.net/umineko/images/8/81/Beelzebub1.png/revision/latest/scale-to-width-down/270?cb=20111219203922",
                "EVA-Beatrice\nhttp://vignette1.wikia.nocookie.net/umineko/images/b/b2/Eva-Beatrice7.png/revision/latest/scale-to-width-down/270?cb=20111113145537",
                "Chiester 410\nhttp://vignette1.wikia.nocookie.net/umineko/images/3/3e/Siesta_410_2.png/revision/latest/scale-to-width-down/258?cb=20111214203655",
                "Chiester 45\nhttp://vignette1.wikia.nocookie.net/umineko/images/a/a7/Siesta451.png/revision/latest/scale-to-width-down/270?cb=20111227180647",
                "Chiester 556\nhttp://vignette1.wikia.nocookie.net/umineko/images/5/50/Siesta556.png/revision/latest/scale-to-width-down/270?cb=20111227181023",
                "Eva Ushiromiya\nhttp://vignette1.wikia.nocookie.net/umineko/images/9/93/Ushiromiya_Eva3.png/revision/latest/scale-to-width-down/205?cb=20111212210826",
                "Rosa Ushiromiya\nhttp://vignette4.wikia.nocookie.net/umineko/images/3/3f/Rosa1.png/revision/latest/scale-to-width-down/240?cb=20111227175537",
                "Dr. Terumasa Nanjo\nhttp://vignette1.wikia.nocookie.net/umineko/images/6/63/Terumasa_Nanjo2.png/revision/latest/scale-to-width-down/270?cb=20111214204050",
                "Kasumi Sumadera\nhttp://vignette1.wikia.nocookie.net/umineko/images/3/3a/Kas_a11_default_1.png/revision/latest/scale-to-width-down/265?cb=20120124202806",
                "Hideyoshi Ushiromiya\nhttp://vignette1.wikia.nocookie.net/umineko/images/f/f8/Ushiromiya_Hideyoshi2.png/revision/latest/scale-to-width-down/270?cb=20111214202158",
                "Kyrie Ushiromiya\nhttp://vignette1.wikia.nocookie.net/umineko/images/6/67/Kir_a27_futeki1.png/revision/latest/scale-to-width-down/270?cb=20140115052519",
                "Shannon\nhttp://vignette1.wikia.nocookie.net/umineko/images/e/e7/Shannon4.png/revision/latest/scale-to-width-down/270?cb=20111112015425",
                "Natsuhi Ushiromiya\nhttp://vignette4.wikia.nocookie.net/umineko/images/2/29/Nat_a11_default_1.png/revision/latest/scale-to-width-down/270?cb=20120123222020",
                "Jessica Ushiromiya\nhttp://vignette2.wikia.nocookie.net/umineko/images/4/48/Ushiromiya_Jessica9.png/revision/latest/scale-to-width-down/270?cb=20111113144749",
                "Erika Furudo\nhttp://vignette3.wikia.nocookie.net/umineko/images/8/8d/Eri_a11_akuwarai3.png/revision/latest/scale-to-width-down/270?cb=20120213095914",
                "Tetsuro Okonogi\nhttp://vignette2.wikia.nocookie.net/umineko/images/9/9d/Oko_a11_def1.png/revision/latest/scale-to-width-down/270?cb=20120127222048",
                "Toshiro Gohda\nhttp://vignette3.wikia.nocookie.net/umineko/images/f/f8/Goh_a11_default_1.png/revision/latest/scale-to-width-down/270?cb=20120124012503",
                "Masayuki Nanjo\nhttp://vignette2.wikia.nocookie.net/umineko/images/9/9b/Na2_a11_default_3.png/revision/latest/scale-to-width-down/243?cb=20120124014023",
                "Chiyo Kumasawa\nhttp://vignette3.wikia.nocookie.net/umineko/images/5/5b/Chiyo_Kumasawa.png/revision/latest/scale-to-width-down/270?cb=20111227180109",
                "Lion Ushiromiya\nhttp://vignette1.wikia.nocookie.net/umineko/images/8/81/Rio_a11_def1.png/revision/latest/scale-to-width-down/270?cb=20120822181702",
                "Clair Vaux Bernardus\nhttp://vignette1.wikia.nocookie.net/umineko/images/0/0e/Cur_a11_houshin3star.png/revision/latest/scale-to-width-down/270?cb=20120127222512",
                "Beatrice Castiglioni (A.K.A. my grandmother and not myself, you idiot.)\nhttp://vignette4.wikia.nocookie.net/umineko/images/1/1f/Bea_c11_def1.png/revision/latest?cb=20120127221305",
                "Willard H. Wright\nhttp://vignette2.wikia.nocookie.net/umineko/images/a/a6/Wil_a23_komaru1.png/revision/latest/scale-to-width-down/270?cb=20131010120041",
                "Beatrice Ushiromiya (A.K.A. my mother and even if she looks like me, she's not myself, you idiot.)\nhttp://vignette3.wikia.nocookie.net/umineko/images/d/d7/Bea_a15_1_hajirai1.png/revision/latest/scale-to-width-down/270?cb=20120127224010"]
        return await self.bot.say(randchoice(char))

    @commands.command()
    async def beatoquote(self):
        """Random Beatrice Ushiromiya quotes"""
        quote=int(random.randint(1,4))
        #Your code will go here
        if quote==1:
            await self.bot.say("You are incompetent!!")
        elif quote==2:
            await self.bot.say("Too bad, witches don't refo~rm!" )
        elif quote==3:
            await self.bot.say("This itself is a miracle. Magic. The proof of my existence!")
        elif quote==4:
            await self.bot.say("Yes, that expression fits you the most. That caring expression of yours really doesn't match me after all. My back was itching, and I was frantically trying to wishtand it. *cackle* *cackle* *cackle*!!")

    @commands.command()
    async def beatosmirk(self):
        """My own smirk."""

        #Your code will go here
        await self.bot.say('http://shounen.chungyc.org/wp-content/uploads/2009/09/next.jpg')

    @commands.command()
    async def beatolaugh(self):
        """My own laugh."""

        #Your code will go here
        await self.bot.say('http://i.imgur.com/vzrnRZo.png')

    @commands.command()
    async def beatodetermined(self):
        """My own determination."""
        await self.bot.say('http://media.animevice.com/uploads/0/2262/137719-vlcsnap_40273_super.png')

    @commands.command()
    async def beatosmile(self):
        """My own smile."""
        await self.bot.say('https://kakeracomplex.files.wordpress.com/2011/05/beatrce.jpg')

    @commands.command()
    async def beatotroll(self):
        """Did someone say 'small bombs' here?"""

        #Your code will go here
        await self.bot.say('http://static.tvtropes.org/pmwiki/pub/images/D_1684.png')

    @commands.command()
    async def beatostare(self):
        """My own stare."""

        #Your code will go here
        await self.bot.say('http://i.imgur.com/R8ziwXI.jpg')

    @commands.command()
    async def beatoportrait(self):
        """My portrait."""

        #Your code will go here
        await self.bot.say('http://vignette1.wikia.nocookie.net/politicsandwar/images/2/2c/Beatrice_Portrait.png/revision/latest?cb=20150425193618')

def setup(bot):
    bot.add_cog(beatrice(bot))

