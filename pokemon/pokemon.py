import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice

class pokemon:
    """Random Pokemon images!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pokemon(self):
        """Random Pokemon images!"""
        pokemonran = ["#0025 Pikachu\nhttp://cdn.bulbagarden.net/upload/thumb/0/0d/025Pikachu.png/250px-025Pikachu.png",
                      "#0150 Mewtwo\nhttp://cdn.bulbagarden.net/upload/thumb/7/78/150Mewtwo.png/250px-150Mewtwo.png",
                      "#0039 Jigglypuff\nhttp://cdn.bulbagarden.net/upload/thumb/3/3e/039Jigglypuff.png/250px-039Jigglypuff.png",
                      "#0151 Mew\nhttp://cdn.bulbagarden.net/upload/thumb/b/b1/151Mew.png/250px-151Mew.png",
                      "#0001 Bulbasaur\nhttp://cdn.bulbagarden.net/upload/thumb/2/21/001Bulbasaur.png/250px-001Bulbasaur.png",
                      "#0002 Ivysaur\nhttp://cdn.bulbagarden.net/upload/thumb/7/73/002Ivysaur.png/250px-002Ivysaur.png",
                      "#0003 Venusaur\nhttp://cdn.bulbagarden.net/upload/thumb/a/ae/003Venusaur.png/250px-003Venusaur.png",
                      "#0004 Charmander\nhttp://cdn.bulbagarden.net/upload/thumb/7/73/004Charmander.png/250px-004Charmander.png",
                      "#0005 Charmeleon\nhttp://cdn.bulbagarden.net/upload/thumb/4/4a/005Charmeleon.png/250px-005Charmeleon.png",
                      "#0006 Charizard\nhttp://cdn.bulbagarden.net/upload/thumb/7/7e/006Charizard.png/250px-006Charizard.png",
                      "#0007 Squirtle\nhttp://cdn.bulbagarden.net/upload/thumb/3/39/007Squirtle.png/250px-007Squirtle.png",
                      "#0008 Wartortle\nhttp://cdn.bulbagarden.net/upload/thumb/0/0c/008Wartortle.png/250px-008Wartortle.png",
                      "#0009 Blastoise\nhttp://cdn.bulbagarden.net/upload/thumb/0/02/009Blastoise.png/250px-009Blastoise.png",
                      "#0010 Caterpie\nhttp://cdn.bulbagarden.net/upload/thumb/5/5d/010Caterpie.png/250px-010Caterpie.png",
                      "#0011 Metapod\nhttp://cdn.bulbagarden.net/upload/thumb/c/cd/011Metapod.png/250px-011Metapod.png",
                      "#0012 Butterfree\nhttp://cdn.bulbagarden.net/upload/thumb/d/d1/012Butterfree.png/250px-012Butterfree.png",
                      "#0013 Weedle\nhttp://cdn.bulbagarden.net/upload/thumb/d/df/013Weedle.png/250px-013Weedle.png",
                      "#0014 Kakuna\nhttp://cdn.bulbagarden.net/upload/thumb/f/f0/014Kakuna.png/250px-014Kakuna.png",
                      "#0015 Beedrill\nhttp://cdn.bulbagarden.net/upload/thumb/6/61/015Beedrill.png/250px-015Beedrill.png",
                      "#0016 Pidgey\nhttp://cdn.bulbagarden.net/upload/thumb/5/55/016Pidgey.png/250px-016Pidgey.png",
                      "#0017 Pidgeotto\nhttp://cdn.bulbagarden.net/upload/thumb/7/7a/017Pidgeotto.png/250px-017Pidgeotto.png",
                      "#0018 Pidgeot\nhttp://cdn.bulbagarden.net/upload/thumb/5/57/018Pidgeot.png/250px-018Pidgeot.png",
                      "#0019 Rattata\nhttp://cdn.bulbagarden.net/upload/thumb/4/46/019Rattata.png/250px-019Rattata.png",
                      "#0020 Raticate\nhttp://cdn.bulbagarden.net/upload/thumb/f/f4/020Raticate.png/250px-020Raticate.png",
                      "#0021 Spearow\nhttp://cdn.bulbagarden.net/upload/thumb/8/8b/021Spearow.png/250px-021Spearow.png",
                      "#0022 Fearow\nhttp://cdn.bulbagarden.net/upload/thumb/a/a0/022Fearow.png/250px-022Fearow.png",
                      "#0023 Ekans\nhttp://cdn.bulbagarden.net/upload/thumb/f/fa/023Ekans.png/250px-023Ekans.png",
                      "#0024 Arbok\nhttp://cdn.bulbagarden.net/upload/thumb/c/cd/024Arbok.png/250px-024Arbok.png",
                      "#0026 Raichu\nhttp://cdn.bulbagarden.net/upload/thumb/8/88/026Raichu.png/250px-026Raichu.png",
                      "#0027 Sandshrew\nhttp://cdn.bulbagarden.net/upload/thumb/9/9e/027Sandshrew.png/250px-027Sandshrew.png",
                      "#0028 Sandslash\nhttp://cdn.bulbagarden.net/upload/thumb/0/0b/028Sandslash.png/250px-028Sandslash.png",
                      "#0029 Nidoran\nhttp://cdn.bulbagarden.net/upload/thumb/8/81/029Nidoran.png/250px-029Nidoran.png",
                      "#0030 Nidorina\nhttp://cdn.bulbagarden.net/upload/thumb/c/cd/030Nidorina.png/250px-030Nidorina.png",
                      "#0031 Nidoqueen\nhttp://cdn.bulbagarden.net/upload/thumb/b/bf/031Nidoqueen.png/250px-031Nidoqueen.png",
                      "#0032 Nidoran\nhttp://cdn.bulbagarden.net/upload/thumb/4/4a/032Nidoran.png/250px-032Nidoran.png",
                      "#0033 Nidorino\nhttp://cdn.bulbagarden.net/upload/thumb/9/9f/033Nidorino.png/250px-033Nidorino.png",
                      "#0034 Nidoking\nhttp://cdn.bulbagarden.net/upload/thumb/c/c6/034Nidoking.png/250px-034Nidoking.png",
                      "#0035 Clefairy\nhttp://cdn.bulbagarden.net/upload/thumb/f/f4/035Clefairy.png/250px-035Clefairy.png",
                      "#0036 Clefable\nhttp://cdn.bulbagarden.net/upload/thumb/a/a9/036Clefable.png/250px-036Clefable.png",
                      "#0037 Vulpix\nhttp://cdn.bulbagarden.net/upload/thumb/6/60/037Vulpix.png/250px-037Vulpix.png",
                      "#0038 Ninetales\nhttp://cdn.bulbagarden.net/upload/thumb/0/05/038Ninetales.png/250px-038Ninetales.png",
                      "#0040 Wigglytuff\nhttp://cdn.bulbagarden.net/upload/thumb/9/92/040Wigglytuff.png/250px-040Wigglytuff.png",
                      "#0041 Zubat\nhttp://cdn.bulbagarden.net/upload/thumb/d/da/041Zubat.png/250px-041Zubat.png",
                      "#0042 Golbat\nhttp://cdn.bulbagarden.net/upload/thumb/0/0c/042Golbat.png/250px-042Golbat.png",
                      "#0043 Oddish\nhttp://cdn.bulbagarden.net/upload/thumb/4/43/043Oddish.png/250px-043Oddish.png",
                      "#0044 Gloom\nhttp://cdn.bulbagarden.net/upload/thumb/2/2a/044Gloom.png/250px-044Gloom.png",
                      "#0045 Vileplume\nhttp://cdn.bulbagarden.net/upload/thumb/6/6a/045Vileplume.png/250px-045Vileplume.png",
                      "#0046 Paras\nhttp://cdn.bulbagarden.net/upload/thumb/d/d4/046Paras.png/250px-046Paras.png",
                      "#0047 Parasect\nhttp://cdn.bulbagarden.net/upload/thumb/8/80/047Parasect.png/250px-047Parasect.png",
                      "#0048 Venonat\nhttp://cdn.bulbagarden.net/upload/thumb/a/ad/048Venonat.png/250px-048Venonat.png",
                      "#0049 Venomoth\nhttp://cdn.bulbagarden.net/upload/thumb/d/d3/049Venomoth.png/250px-049Venomoth.png",
                      "#0050 Diglett\nhttp://cdn.bulbagarden.net/upload/thumb/3/31/050Diglett.png/250px-050Diglett.png",
                      "#0051 Dugtrio\nhttp://cdn.bulbagarden.net/upload/thumb/e/e5/051Dugtrio.png/250px-051Dugtrio.png",
                      "#0052 Meowth\nhttp://cdn.bulbagarden.net/upload/thumb/d/d6/052Meowth.png/250px-052Meowth.png",
                      "#0053 Persian\nhttp://cdn.bulbagarden.net/upload/thumb/1/13/053Persian.png/250px-053Persian.png",
                      "#0054 Psyduck\nhttp://cdn.bulbagarden.net/upload/thumb/5/53/054Psyduck.png/250px-054Psyduck.png",
                      "#0055 Golduck\nhttp://cdn.bulbagarden.net/upload/thumb/f/fe/055Golduck.png/250px-055Golduck.png",
                      "#0056 Mankey\nhttp://cdn.bulbagarden.net/upload/thumb/4/41/056Mankey.png/250px-056Mankey.png",
                      "#0057 Primeape\nhttp://cdn.bulbagarden.net/upload/thumb/9/9a/057Primeape.png/250px-057Primeape.png",
                      "#0058 Growlithe\nhttp://cdn.bulbagarden.net/upload/thumb/3/3d/058Growlithe.png/250px-058Growlithe.png",
                      "#0059 Arcanine\nhttp://cdn.bulbagarden.net/upload/thumb/b/b8/059Arcanine.png/250px-059Arcanine.png",
                      "#0060 Poliwag\nhttp://cdn.bulbagarden.net/upload/thumb/4/49/060Poliwag.png/250px-060Poliwag.png",
                      "#0061 Poliwhirl\nhttp://cdn.bulbagarden.net/upload/thumb/a/a9/061Poliwhirl.png/250px-061Poliwhirl.png",
                      "#0062 Poliwrath\nhttp://cdn.bulbagarden.net/upload/thumb/2/2d/062Poliwrath.png/250px-062Poliwrath.png",
                      "#0063 Abra\nhttp://cdn.bulbagarden.net/upload/thumb/6/62/063Abra.png/250px-063Abra.png",
                      "#0064 Kadabra\nhttp://cdn.bulbagarden.net/upload/thumb/9/97/064Kadabra.png/250px-064Kadabra.png",
                      "#0065 Alakazam\nhttp://cdn.bulbagarden.net/upload/thumb/c/cc/065Alakazam.png/250px-065Alakazam.png",
                      "#0066 Machop\nhttp://cdn.bulbagarden.net/upload/thumb/8/85/066Machop.png/250px-066Machop.png",
                      "#0067 Machoke\nhttp://cdn.bulbagarden.net/upload/thumb/8/8e/067Machoke.png/250px-067Machoke.png",
                      "#0068 Machamp\nhttp://cdn.bulbagarden.net/upload/thumb/8/8f/068Machamp.png/250px-068Machamp.png",
                      "#0069 Bellsprout\nhttp://cdn.bulbagarden.net/upload/thumb/a/a2/069Bellsprout.png/250px-069Bellsprout.png",
                      "#0070 Weepinbell\nhttp://cdn.bulbagarden.net/upload/thumb/9/9f/070Weepinbell.png/250px-070Weepinbell.png",
                      "#0071 Victreebel\nhttp://cdn.bulbagarden.net/upload/thumb/b/be/071Victreebel.png/250px-071Victreebel.png",
                      "#0072 Tentacool\nhttp://cdn.bulbagarden.net/upload/thumb/4/4e/072Tentacool.png/250px-072Tentacool.png",
                      "#0073 Tentacruel\nhttp://cdn.bulbagarden.net/upload/thumb/f/f6/073Tentacruel.png/250px-073Tentacruel.png",
                      "#0074 Geodude\nhttp://cdn.bulbagarden.net/upload/thumb/9/98/074Geodude.png/250px-074Geodude.png",
                      "#0075 Graveler\nhttp://cdn.bulbagarden.net/upload/thumb/7/75/075Graveler.png/250px-075Graveler.png",
                      "#0076 Golem\nhttp://cdn.bulbagarden.net/upload/thumb/f/f2/076Golem.png/250px-076Golem.png",
                      "#0077 Ponyta\nhttp://cdn.bulbagarden.net/upload/thumb/3/3b/077Ponyta.png/250px-077Ponyta.png",
                      "#0078 Rapidash\nhttp://cdn.bulbagarden.net/upload/thumb/3/3f/078Rapidash.png/250px-078Rapidash.png",
                      "#0079 Slowpoke\nhttp://cdn.bulbagarden.net/upload/thumb/7/70/079Slowpoke.png/250px-079Slowpoke.png",
                      "#0080 Slowbro\nhttp://cdn.bulbagarden.net/upload/thumb/8/80/080Slowbro.png/250px-080Slowbro.png",
                      "#0081 Magnemite\nhttp://cdn.bulbagarden.net/upload/thumb/6/6c/081Magnemite.png/250px-081Magnemite.png",
                      "#0082 Magneton\nhttp://cdn.bulbagarden.net/upload/thumb/7/72/082Magneton.png/250px-082Magneton.png",
                      "#0083 Farfetch'd\nhttp://cdn.bulbagarden.net/upload/thumb/f/f8/083Farfetch%27d.png/250px-083Farfetch%27d.png",
                      "#0084 Doduo\nhttp://cdn.bulbagarden.net/upload/thumb/5/54/084Doduo.png/250px-084Doduo.png",
                      "#0085 Dodrio\nhttp://cdn.bulbagarden.net/upload/thumb/9/93/085Dodrio.png/250px-085Dodrio.png",
                      "#0086 Seel\nhttp://cdn.bulbagarden.net/upload/thumb/1/1f/086Seel.png/250px-086Seel.png",
                      "#0087 Dewgong\nhttp://cdn.bulbagarden.net/upload/thumb/c/c7/087Dewgong.png/250px-087Dewgong.png",
                      "#0088 Grimer\nhttp://cdn.bulbagarden.net/upload/thumb/a/a0/088Grimer.png/250px-088Grimer.png",
                      "#0089 Muk\nhttp://cdn.bulbagarden.net/upload/thumb/7/7c/089Muk.png/250px-089Muk.png",
                      "#0090 Shellder\nhttp://cdn.bulbagarden.net/upload/thumb/4/40/090Shellder.png/250px-090Shellder.png",
                      "http://cdn.bulbagarden.net/upload/thumb/1/1d/091Cloyster.png/250px-091Cloyster.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/ca/092Gastly.png/250px-092Gastly.png",
                      "http://cdn.bulbagarden.net/upload/thumb/6/62/093Haunter.png/250px-093Haunter.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/c6/094Gengar.png/250px-094Gengar.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/9a/095Onix.png/250px-095Onix.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/3e/096Drowzee.png/250px-096Drowzee.png",
                      "http://cdn.bulbagarden.net/upload/thumb/0/0a/097Hypno.png/250px-097Hypno.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/a7/098Krabby.png/250px-098Krabby.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/71/099Kingler.png/250px-099Kingler.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/da/100Voltorb.png/250px-100Voltorb.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/84/101Electrode.png/250px-101Electrode.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/af/102Exeggcute.png/250px-102Exeggcute.png",
                      "http://cdn.bulbagarden.net/upload/thumb/2/24/103Exeggutor.png/250px-103Exeggutor.png",
                      "http://cdn.bulbagarden.net/upload/thumb/2/2a/104Cubone.png/250px-104Cubone.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/98/105Marowak.png/250px-105Marowak.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/32/106Hitmonlee.png/250px-106Hitmonlee.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/a3/107Hitmonchan.png/250px-107Hitmonchan.png",
                      "http://cdn.bulbagarden.net/upload/thumb/0/00/108Lickitung.png/250px-108Lickitung.png",
                      "http://cdn.bulbagarden.net/upload/thumb/1/17/109Koffing.png/250px-109Koffing.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/42/110Weezing.png/250px-110Weezing.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/9b/111Rhyhorn.png/250px-111Rhyhorn.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/47/112Rhydon.png/250px-112Rhydon.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/cd/113Chansey.png/250px-113Chansey.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/3e/114Tangela.png/250px-114Tangela.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/4e/115Kangaskhan.png/250px-115Kangaskhan.png",
                      "http://cdn.bulbagarden.net/upload/thumb/5/5a/116Horsea.png/250px-116Horsea.png",
                      "http://cdn.bulbagarden.net/upload/thumb/2/26/117Seadra.png/250px-117Seadra.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/7b/118Goldeen.png/250px-118Goldeen.png",
                      "http://cdn.bulbagarden.net/upload/thumb/6/6a/119Seaking.png/250px-119Seaking.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/4f/120Staryu.png/250px-120Staryu.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/cd/121Starmie.png/250px-121Starmie.png",
                      "http://cdn.bulbagarden.net/upload/thumb/e/ec/122Mr._Mime.png/250px-122Mr._Mime.png",
                      "http://cdn.bulbagarden.net/upload/thumb/b/ba/123Scyther.png/250px-123Scyther.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/7c/124Jynx.png/250px-124Jynx.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/de/125Electabuzz.png/250px-125Electabuzz.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/8c/126Magmar.png/250px-126Magmar.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/71/127Pinsir.png/250px-127Pinsir.png",
                      "http://cdn.bulbagarden.net/upload/thumb/b/b8/128Tauros.png/250px-128Tauros.png",
                      "http://cdn.bulbagarden.net/upload/thumb/0/02/129Magikarp.png/250px-129Magikarp.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/41/130Gyarados.png/250px-130Gyarados.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/ab/131Lapras.png/250px-131Lapras.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/36/132Ditto.png/250px-132Ditto.png",
                      "http://cdn.bulbagarden.net/upload/thumb/e/e2/133Eevee.png/250px-133Eevee.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/fd/134Vaporeon.png/250px-134Vaporeon.png",
                      "http://cdn.bulbagarden.net/upload/thumb/b/bb/135Jolteon.png/250px-135Jolteon.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/dd/136Flareon.png/250px-136Flareon.png",
                      "http://cdn.bulbagarden.net/upload/thumb/6/6b/137Porygon.png/250px-137Porygon.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/79/138Omanyte.png/250px-138Omanyte.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/43/139Omastar.png/250px-139Omastar.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/f9/140Kabuto.png/250px-140Kabuto.png",
                      "http://cdn.bulbagarden.net/upload/thumb/2/29/141Kabutops.png/250px-141Kabutops.png",
                      "http://cdn.bulbagarden.net/upload/thumb/e/e8/142Aerodactyl.png/250px-142Aerodactyl.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/fb/143Snorlax.png/250px-143Snorlax.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/4e/144Articuno.png/250px-144Articuno.png",
                      "http://cdn.bulbagarden.net/upload/thumb/e/e3/145Zapdos.png/250px-145Zapdos.png",
                      "http://cdn.bulbagarden.net/upload/thumb/1/1b/146Moltres.png/250px-146Moltres.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/cc/147Dratini.png/250px-147Dratini.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/93/148Dragonair.png/250px-148Dragonair.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/8b/149Dragonite.png/250px-149Dragonite.png"
                      ]
        return await self.bot.say(randchoice(pokemonran))
    
def setup(bot):
    bot.add_cog(pokemon(bot))
