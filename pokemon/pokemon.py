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
                      "#0091 Cloyster\nhttp://cdn.bulbagarden.net/upload/thumb/1/1d/091Cloyster.png/250px-091Cloyster.png",
                      "#0092 Gastly\nhttp://cdn.bulbagarden.net/upload/thumb/c/ca/092Gastly.png/250px-092Gastly.png",
                      "#0093 Haunter\nhttp://cdn.bulbagarden.net/upload/thumb/6/62/093Haunter.png/250px-093Haunter.png",
                      "#0094 Gengar\nhttp://cdn.bulbagarden.net/upload/thumb/c/c6/094Gengar.png/250px-094Gengar.png",
                      "#0095 Onix\nhttp://cdn.bulbagarden.net/upload/thumb/9/9a/095Onix.png/250px-095Onix.png",
                      "#0096 Drowzee\nhttp://cdn.bulbagarden.net/upload/thumb/3/3e/096Drowzee.png/250px-096Drowzee.png",
                      "#0097 Hypno\nhttp://cdn.bulbagarden.net/upload/thumb/0/0a/097Hypno.png/250px-097Hypno.png",
                      "#0098 Krabby\nhttp://cdn.bulbagarden.net/upload/thumb/a/a7/098Krabby.png/250px-098Krabby.png",
                      "#0099 Kingler\nhttp://cdn.bulbagarden.net/upload/thumb/7/71/099Kingler.png/250px-099Kingler.png",
                      "#0100 Voltorb\nhttp://cdn.bulbagarden.net/upload/thumb/d/da/100Voltorb.png/250px-100Voltorb.png",
                      "#0101 Electrode\nhttp://cdn.bulbagarden.net/upload/thumb/8/84/101Electrode.png/250px-101Electrode.png",
                      "#0102 Exeggcute\nhttp://cdn.bulbagarden.net/upload/thumb/a/af/102Exeggcute.png/250px-102Exeggcute.png",
                      "#0103 Exeggutor\nhttp://cdn.bulbagarden.net/upload/thumb/2/24/103Exeggutor.png/250px-103Exeggutor.png",
                      "#0104 Cubone\nhttp://cdn.bulbagarden.net/upload/thumb/2/2a/104Cubone.png/250px-104Cubone.png",
                      "#0105 Marowak\nhttp://cdn.bulbagarden.net/upload/thumb/9/98/105Marowak.png/250px-105Marowak.png",
                      "#0106 Hitmonlee\nhttp://cdn.bulbagarden.net/upload/thumb/3/32/106Hitmonlee.png/250px-106Hitmonlee.png",
                      "#0107 Hitmonchan\nhttp://cdn.bulbagarden.net/upload/thumb/a/a3/107Hitmonchan.png/250px-107Hitmonchan.png",
                      "#0108 Lickitung\nhttp://cdn.bulbagarden.net/upload/thumb/0/00/108Lickitung.png/250px-108Lickitung.png",
                      "#0109 Koffing\nhttp://cdn.bulbagarden.net/upload/thumb/1/17/109Koffing.png/250px-109Koffing.png",
                      "#0110 Weezing\nhttp://cdn.bulbagarden.net/upload/thumb/4/42/110Weezing.png/250px-110Weezing.png",
                      "#0111 Rhyhorn\nhttp://cdn.bulbagarden.net/upload/thumb/9/9b/111Rhyhorn.png/250px-111Rhyhorn.png",
                      "#0112 Rhydon\nhttp://cdn.bulbagarden.net/upload/thumb/4/47/112Rhydon.png/250px-112Rhydon.png",
                      "#0113 Chansey\nhttp://cdn.bulbagarden.net/upload/thumb/c/cd/113Chansey.png/250px-113Chansey.png",
                      "#0114 Tangela\nhttp://cdn.bulbagarden.net/upload/thumb/3/3e/114Tangela.png/250px-114Tangela.png",
                      "#0115 Kangaskhan\nhttp://cdn.bulbagarden.net/upload/thumb/4/4e/115Kangaskhan.png/250px-115Kangaskhan.png",
                      "#0116 Horsea\nhttp://cdn.bulbagarden.net/upload/thumb/5/5a/116Horsea.png/250px-116Horsea.png",
                      "#0117 Seadra\nhttp://cdn.bulbagarden.net/upload/thumb/2/26/117Seadra.png/250px-117Seadra.png",
                      "#0118 Goldeen\nhttp://cdn.bulbagarden.net/upload/thumb/7/7b/118Goldeen.png/250px-118Goldeen.png",
                      "#0119 Seaking\nhttp://cdn.bulbagarden.net/upload/thumb/6/6a/119Seaking.png/250px-119Seaking.png",
                      "#0120 Staryu\nhttp://cdn.bulbagarden.net/upload/thumb/4/4f/120Staryu.png/250px-120Staryu.png",
                      "#0121 Starmie\nhttp://cdn.bulbagarden.net/upload/thumb/c/cd/121Starmie.png/250px-121Starmie.png",
                      "#0122 Mr. Mime\nhttp://cdn.bulbagarden.net/upload/thumb/e/ec/122Mr._Mime.png/250px-122Mr._Mime.png",
                      "#0123 Scyther\nhttp://cdn.bulbagarden.net/upload/thumb/b/ba/123Scyther.png/250px-123Scyther.png",
                      "#0124 Jynx\nhttp://cdn.bulbagarden.net/upload/thumb/7/7c/124Jynx.png/250px-124Jynx.png",
                      "#0125 Electabuzz\nhttp://cdn.bulbagarden.net/upload/thumb/d/de/125Electabuzz.png/250px-125Electabuzz.png",
                      "#0126 Magmar\nhttp://cdn.bulbagarden.net/upload/thumb/8/8c/126Magmar.png/250px-126Magmar.png",
                      "#0127 Pinsir\nhttp://cdn.bulbagarden.net/upload/thumb/7/71/127Pinsir.png/250px-127Pinsir.png",
                      "#0128 Tauros\nhttp://cdn.bulbagarden.net/upload/thumb/b/b8/128Tauros.png/250px-128Tauros.png",
                      "#0129 Magikarp\nhttp://cdn.bulbagarden.net/upload/thumb/0/02/129Magikarp.png/250px-129Magikarp.png",
                      "#0130 Gyarados\nhttp://cdn.bulbagarden.net/upload/thumb/4/41/130Gyarados.png/250px-130Gyarados.png",
                      "#0131 Lapras\nhttp://cdn.bulbagarden.net/upload/thumb/a/ab/131Lapras.png/250px-131Lapras.png",
                      "#0132 Ditto\nhttp://cdn.bulbagarden.net/upload/thumb/3/36/132Ditto.png/250px-132Ditto.png",
                      "#0133 Eevee\nhttp://cdn.bulbagarden.net/upload/thumb/e/e2/133Eevee.png/250px-133Eevee.png",
                      "#0134 Vaporeon\nhttp://cdn.bulbagarden.net/upload/thumb/f/fd/134Vaporeon.png/250px-134Vaporeon.png",
                      "#0135 Jolteon\nhttp://cdn.bulbagarden.net/upload/thumb/b/bb/135Jolteon.png/250px-135Jolteon.png",
                      "#0136 Flareon\nhttp://cdn.bulbagarden.net/upload/thumb/d/dd/136Flareon.png/250px-136Flareon.png",
                      "#0137 Porygon\nhttp://cdn.bulbagarden.net/upload/thumb/6/6b/137Porygon.png/250px-137Porygon.png",
                      "#0138 Omanyte\nhttp://cdn.bulbagarden.net/upload/thumb/7/79/138Omanyte.png/250px-138Omanyte.png",
                      "#0139 Omaster\nhttp://cdn.bulbagarden.net/upload/thumb/4/43/139Omastar.png/250px-139Omastar.png",
                      "#0140 Kabuto\nhttp://cdn.bulbagarden.net/upload/thumb/f/f9/140Kabuto.png/250px-140Kabuto.png",
                      "#0141 Kabutops\nhttp://cdn.bulbagarden.net/upload/thumb/2/29/141Kabutops.png/250px-141Kabutops.png",
                      "#0142 Aerodactyl\nhttp://cdn.bulbagarden.net/upload/thumb/e/e8/142Aerodactyl.png/250px-142Aerodactyl.png",
                      "#0143 Snorlax\nhttp://cdn.bulbagarden.net/upload/thumb/f/fb/143Snorlax.png/250px-143Snorlax.png",
                      "#0144 Articuno\nhttp://cdn.bulbagarden.net/upload/thumb/4/4e/144Articuno.png/250px-144Articuno.png",
                      "#0145 Zapdos\nhttp://cdn.bulbagarden.net/upload/thumb/e/e3/145Zapdos.png/250px-145Zapdos.png",
                      "#0146 Moltres\nhttp://cdn.bulbagarden.net/upload/thumb/1/1b/146Moltres.png/250px-146Moltres.png",
                      "#0147 Dratini\nhttp://cdn.bulbagarden.net/upload/thumb/c/cc/147Dratini.png/250px-147Dratini.png",
                      "#0148 Dragonair\nhttp://cdn.bulbagarden.net/upload/thumb/9/93/148Dragonair.png/250px-148Dragonair.png",
                      "#0149 Dragonite\nhttp://cdn.bulbagarden.net/upload/thumb/8/8b/149Dragonite.png/250px-149Dragonite.png",
                      "#0152 Chikorita\nhttp://cdn.bulbagarden.net/upload/thumb/b/bf/152Chikorita.png/250px-152Chikorita.png",
                      "#0153 Bayleef\nhttp://cdn.bulbagarden.net/upload/thumb/c/ca/153Bayleef.png/250px-153Bayleef.png",
                      "#0154 Meganium\nhttp://cdn.bulbagarden.net/upload/thumb/d/d1/154Meganium.png/250px-154Meganium.png",
                      "#0155 Cyndaquil\nhttp://cdn.bulbagarden.net/upload/thumb/9/9b/155Cyndaquil.png/250px-155Cyndaquil.png",
                      "#0156 Quilava\nhttp://cdn.bulbagarden.net/upload/thumb/b/b6/156Quilava.png/250px-156Quilava.png",
                      "#0157 Typhlosion\nhttp://cdn.bulbagarden.net/upload/thumb/4/47/157Typhlosion.png/250px-157Typhlosion.png",
                      "#0158 Totodile\nhttp://cdn.bulbagarden.net/upload/thumb/d/df/158Totodile.png/250px-158Totodile.png",
                      "#0159 Croconaw\nhttp://cdn.bulbagarden.net/upload/thumb/a/a5/159Croconaw.png/250px-159Croconaw.png",
                      "#0160 Feraligatr\nhttp://cdn.bulbagarden.net/upload/thumb/d/d5/160Feraligatr.png/250px-160Feraligatr.png",
                      "#0161 Sentret\nhttp://cdn.bulbagarden.net/upload/thumb/c/c5/161Sentret.png/250px-161Sentret.png",
                      "#0162 Furret\nhttp://cdn.bulbagarden.net/upload/thumb/4/4b/162Furret.png/250px-162Furret.png",
                      "#0163 Hoothoot\nhttp://cdn.bulbagarden.net/upload/thumb/5/53/163Hoothoot.png/250px-163Hoothoot.png",
                      "#0164 Noctowl\nhttp://cdn.bulbagarden.net/upload/thumb/f/fa/164Noctowl.png/250px-164Noctowl.png",
                      "#0165 Ledyba\nhttp://cdn.bulbagarden.net/upload/thumb/b/bb/165Ledyba.png/250px-165Ledyba.png",
                      "#0166 Ledian\nhttp://cdn.bulbagarden.net/upload/thumb/5/5b/166Ledian.png/250px-166Ledian.png",
                      "#0167 Spinarak\nhttp://cdn.bulbagarden.net/upload/thumb/7/75/167Spinarak.png/250px-167Spinarak.png",
                      "#0168 Ariados\nhttp://cdn.bulbagarden.net/upload/thumb/7/76/168Ariados.png/250px-168Ariados.png",
                      "#0169 Crobat\nhttp://cdn.bulbagarden.net/upload/thumb/1/17/169Crobat.png/250px-169Crobat.png",
                      "#0170 Chinchou\nhttp://cdn.bulbagarden.net/upload/thumb/d/d9/170Chinchou.png/250px-170Chinchou.png",
                      "#0171 Lanturn\nhttp://cdn.bulbagarden.net/upload/thumb/9/9b/171Lanturn.png/250px-171Lanturn.png",
                      "#0172 Pichu\nhttp://cdn.bulbagarden.net/upload/thumb/b/b9/172Pichu.png/250px-172Pichu.png",
                      "#0173 Cleffa\nhttp://cdn.bulbagarden.net/upload/thumb/e/e4/173Cleffa.png/250px-173Cleffa.png",
                      "#0174 Igglybuff\nhttp://cdn.bulbagarden.net/upload/thumb/4/4d/174Igglybuff.png/250px-174Igglybuff.png",
                      "#0175 Togepi\nhttp://cdn.bulbagarden.net/upload/thumb/6/6b/175Togepi.png/250px-175Togepi.png",
                      "#0176 Togetic\nhttp://cdn.bulbagarden.net/upload/thumb/1/11/176Togetic.png/250px-176Togetic.png",
                      "#0177 Natu\nhttp://cdn.bulbagarden.net/upload/thumb/5/5b/177Natu.png/250px-177Natu.png",
                      "#0178 Xatu\nhttp://cdn.bulbagarden.net/upload/thumb/f/f4/178Xatu.png/250px-178Xatu.png",
                      "#0179 Mareep\nhttp://cdn.bulbagarden.net/upload/thumb/6/6b/179Mareep.png/250px-179Mareep.png",
                      "#0180 Flaaffy\nhttp://cdn.bulbagarden.net/upload/thumb/6/6f/180Flaaffy.png/250px-180Flaaffy.png",
                      "#0181 Ampharos\nhttp://cdn.bulbagarden.net/upload/thumb/4/47/181Ampharos.png/250px-181Ampharos.png",
                      "#0182 Bellossom\nhttp://cdn.bulbagarden.net/upload/thumb/c/cd/182Bellossom.png/250px-182Bellossom.png",
                      "#0183 Marill\nhttp://cdn.bulbagarden.net/upload/thumb/4/42/183Marill.png/250px-183Marill.png",
                      "#0184 Azumarill\nhttp://cdn.bulbagarden.net/upload/thumb/a/a5/184Azumarill.png/250px-184Azumarill.png",
                      "#0185 Sudowoodo\nhttp://cdn.bulbagarden.net/upload/thumb/1/1e/185Sudowoodo.png/250px-185Sudowoodo.png",
                      "#0186 Politoed\nhttp://cdn.bulbagarden.net/upload/thumb/a/a4/186Politoed.png/250px-186Politoed.png",
                      "#0187 Hoppip\nhttp://cdn.bulbagarden.net/upload/thumb/f/f8/187Hoppip.png/250px-187Hoppip.png",
                      "#0188 Skiploom\nhttp://cdn.bulbagarden.net/upload/thumb/4/4f/188Skiploom.png/250px-188Skiploom.png",
                      "#0189 Jumpluff\nhttp://cdn.bulbagarden.net/upload/thumb/5/5e/189Jumpluff.png/250px-189Jumpluff.png",
                      "#0190 Aipom\nhttp://cdn.bulbagarden.net/upload/thumb/4/42/190Aipom.png/250px-190Aipom.png",
                      "#0191 Sunkern\nhttp://cdn.bulbagarden.net/upload/thumb/9/95/191Sunkern.png/250px-191Sunkern.png",
                      "#0192 Sunflora\nhttp://cdn.bulbagarden.net/upload/thumb/9/98/192Sunflora.png/250px-192Sunflora.png",
                      "#0193 Yanma\nhttp://cdn.bulbagarden.net/upload/thumb/d/dd/193Yanma.png/250px-193Yanma.png",
                      "#0194 Wooper\nhttp://cdn.bulbagarden.net/upload/thumb/7/78/194Wooper.png/250px-194Wooper.png",
                      "#0195 Quagsire\nhttp://cdn.bulbagarden.net/upload/thumb/a/a4/195Quagsire.png/250px-195Quagsire.png",
                      "#0196 Espeon\nhttp://cdn.bulbagarden.net/upload/thumb/a/a7/196Espeon.png/250px-196Espeon.png",
                      "#0197 Umbreon\nhttp://cdn.bulbagarden.net/upload/thumb/3/3d/197Umbreon.png/250px-197Umbreon.png",
                      "#0198 Murkrow\nhttp://cdn.bulbagarden.net/upload/thumb/3/33/198Murkrow.png/250px-198Murkrow.png",
                      "#0199 Slowking\nhttp://cdn.bulbagarden.net/upload/thumb/e/e1/199Slowking.png/250px-199Slowking.png",
                      "#0200 Misdreavus\nhttp://cdn.bulbagarden.net/upload/thumb/b/be/200Misdreavus.png/250px-200Misdreavus.png",
                      "#0201 Unown\nhttp://cdn.bulbagarden.net/upload/thumb/7/77/201Unown.png/250px-201Unown.png",
                      "#0202 Wobbuffet\nhttp://cdn.bulbagarden.net/upload/thumb/1/17/202Wobbuffet.png/250px-202Wobbuffet.png",
                      "#0203 Girfarig\nhttp://cdn.bulbagarden.net/upload/thumb/1/11/203Girafarig.png/250px-203Girafarig.png",
                      "#0204 Pineco\nhttp://cdn.bulbagarden.net/upload/thumb/0/0b/204Pineco.png/250px-204Pineco.png",
                      "#0205 Forretress\nhttp://cdn.bulbagarden.net/upload/thumb/6/68/205Forretress.png/250px-205Forretress.png",
                      "#0206 Dunsparce\nhttp://cdn.bulbagarden.net/upload/thumb/2/20/206Dunsparce.png/250px-206Dunsparce.png",
                      "#0207 Gligar\nhttp://cdn.bulbagarden.net/upload/thumb/0/04/207Gligar.png/250px-207Gligar.png",
                      "#0208 Steelix\nhttp://cdn.bulbagarden.net/upload/thumb/b/ba/208Steelix.png/250px-208Steelix.png",
                      "#0209 Snubbull\nhttp://cdn.bulbagarden.net/upload/thumb/7/7f/209Snubbull.png/250px-209Snubbull.png",
                      "#0210 Granbull\nhttp://cdn.bulbagarden.net/upload/thumb/b/b1/210Granbull.png/250px-210Granbull.png",
                      "#0211 Qwilfish\nhttp://cdn.bulbagarden.net/upload/thumb/2/21/211Qwilfish.png/250px-211Qwilfish.png",
                      "#0212 Scizor\nhttp://cdn.bulbagarden.net/upload/thumb/5/55/212Scizor.png/250px-212Scizor.png",
                      "#0213 Shuckle\nhttp://cdn.bulbagarden.net/upload/thumb/c/c7/213Shuckle.png/250px-213Shuckle.png",
                      "#0214 Heracross\nhttp://cdn.bulbagarden.net/upload/thumb/4/47/214Heracross.png/250px-214Heracross.png",
                      "#0215 Sneasel\nhttp://cdn.bulbagarden.net/upload/thumb/7/71/215Sneasel.png/250px-215Sneasel.png",
                      "#0216 Teddiursa\nhttp://cdn.bulbagarden.net/upload/thumb/e/e9/216Teddiursa.png/250px-216Teddiursa.png",
                      "#0217 Ursaring\nhttp://cdn.bulbagarden.net/upload/thumb/e/e9/217Ursaring.png/250px-217Ursaring.png",
                      "#0218 Slugma\nhttp://cdn.bulbagarden.net/upload/thumb/6/68/218Slugma.png/250px-218Slugma.png",
                      "#0219 Magcarco\nhttp://cdn.bulbagarden.net/upload/thumb/6/65/219Magcargo.png/250px-219Magcargo.png",
                      "#0220 Swinub\nhttp://cdn.bulbagarden.net/upload/thumb/b/b5/220Swinub.png/250px-220Swinub.png",
                      "#0221 Piloswine\nhttp://cdn.bulbagarden.net/upload/thumb/4/49/221Piloswine.png/250px-221Piloswine.png",
                      "#0222 Corsola\nhttp://cdn.bulbagarden.net/upload/thumb/f/fc/222Corsola.png/250px-222Corsola.png",
                      "#0223 Remoraid\nhttp://cdn.bulbagarden.net/upload/thumb/9/95/223Remoraid.png/250px-223Remoraid.png",
                      "#0224 Octillery\nhttp://cdn.bulbagarden.net/upload/thumb/c/cb/224Octillery.png/250px-224Octillery.png",
                      "#0225 Delibird\nhttp://cdn.bulbagarden.net/upload/thumb/3/3f/225Delibird.png/250px-225Delibird.png",
                      "#0226 Mantine\nhttp://cdn.bulbagarden.net/upload/thumb/c/c5/226Mantine.png/250px-226Mantine.png",
                      "#0227 Skarmory\nhttp://cdn.bulbagarden.net/upload/thumb/3/35/227Skarmory.png/250px-227Skarmory.png",
                      "#0228 Houndour\nhttp://cdn.bulbagarden.net/upload/thumb/5/53/228Houndour.png/250px-228Houndour.png",
                      "#0229 Houndoom\nhttp://cdn.bulbagarden.net/upload/thumb/5/51/229Houndoom.png/250px-229Houndoom.png",
                      "#0230 Kingdra\nhttp://cdn.bulbagarden.net/upload/thumb/3/3c/230Kingdra.png/250px-230Kingdra.png",
                      "#0231 Phanpy\nhttp://cdn.bulbagarden.net/upload/thumb/d/d3/231Phanpy.png/250px-231Phanpy.png",
                      "#0232 Donphan\nhttp://cdn.bulbagarden.net/upload/thumb/5/53/232Donphan.png/250px-232Donphan.png",
                      "#0233 Porygon2\nhttp://cdn.bulbagarden.net/upload/thumb/9/99/233Porygon2.png/250px-233Porygon2.png",
                      "#0234 Stantler\nhttp://cdn.bulbagarden.net/upload/thumb/5/50/234Stantler.png/250px-234Stantler.png",
                      "#0235 Smeargle\nhttp://cdn.bulbagarden.net/upload/thumb/9/92/235Smeargle.png/250px-235Smeargle.png",
                      "#0236 Tyrogue\nhttp://cdn.bulbagarden.net/upload/thumb/c/c7/236Tyrogue.png/250px-236Tyrogue.png",
                      "#0237 Hitmontop\nhttp://cdn.bulbagarden.net/upload/thumb/9/94/237Hitmontop.png/250px-237Hitmontop.png",
                      "#0238 Smoochum\nhttp://cdn.bulbagarden.net/upload/thumb/0/0e/238Smoochum.png/250px-238Smoochum.png",
                      "#0239 Elekid\nhttp://cdn.bulbagarden.net/upload/thumb/5/5d/239Elekid.png/250px-239Elekid.png",
                      "#0240 Magby\nhttp://cdn.bulbagarden.net/upload/thumb/c/cb/240Magby.png/250px-240Magby.png",
                      "#0241 Miltank\nhttp://cdn.bulbagarden.net/upload/thumb/1/13/241Miltank.png/250px-241Miltank.png",
                      "#0242 Blissey\nhttp://cdn.bulbagarden.net/upload/thumb/5/56/242Blissey.png/250px-242Blissey.png",
                      "#0243 Raikou\nhttp://cdn.bulbagarden.net/upload/thumb/c/c1/243Raikou.png/250px-243Raikou.png",
                      "#0244 Entei\nhttp://cdn.bulbagarden.net/upload/thumb/f/f9/244Entei.png/250px-244Entei.png",
                      "#0245 Suicune\nhttp://cdn.bulbagarden.net/upload/thumb/d/da/245Suicune.png/250px-245Suicune.png",
                      "#0246 Larvitar\nhttp://cdn.bulbagarden.net/upload/thumb/7/70/246Larvitar.png/250px-246Larvitar.png",
                      "#0247 Pupitar\nhttp://cdn.bulbagarden.net/upload/thumb/a/a1/247Pupitar.png/250px-247Pupitar.png",
                      "#0248 Tyranitar\nhttp://cdn.bulbagarden.net/upload/thumb/8/82/248Tyranitar.png/250px-248Tyranitar.png",
                      "#0249 Lugia\nhttp://cdn.bulbagarden.net/upload/thumb/4/44/249Lugia.png/250px-249Lugia.png",
                      "#0250 Ho-Oh\nhttp://cdn.bulbagarden.net/upload/thumb/6/67/250Ho-Oh.png/250px-250Ho-Oh.png",
                      "#0251 Celebi\nhttp://cdn.bulbagarden.net/upload/thumb/e/e7/251Celebi.png/250px-251Celebi.png",
                      "#0252 Treecko\nhttp://cdn.bulbagarden.net/upload/thumb/2/2c/252Treecko.png/250px-252Treecko.png",
                      "#0253 Grovyle\nhttp://cdn.bulbagarden.net/upload/thumb/e/ea/253Grovyle.png/250px-253Grovyle.png",
                      "#0254 Sceptile\nhttp://cdn.bulbagarden.net/upload/thumb/3/3e/254Sceptile.png/250px-254Sceptile.png",
                      "#0255 Torchic\nhttp://cdn.bulbagarden.net/upload/thumb/9/91/255Torchic.png/250px-255Torchic.png",
                      "#0256 Combusken\nhttp://cdn.bulbagarden.net/upload/thumb/2/29/256Combusken.png/250px-256Combusken.png",
                      "#0257 Blaziken\nhttp://cdn.bulbagarden.net/upload/thumb/9/90/257Blaziken.png/250px-257Blaziken.png",
                      "#0258 Mudkip\nhttp://cdn.bulbagarden.net/upload/thumb/6/60/258Mudkip.png/250px-258Mudkip.png",
                      "#0259 Marshtomp\nhttp://cdn.bulbagarden.net/upload/thumb/2/27/259Marshtomp.png/250px-259Marshtomp.png",
                      "#0260 Swampert\nhttp://cdn.bulbagarden.net/upload/thumb/b/b6/260Swampert.png/250px-260Swampert.png",
                      "#0261 Poochyena\nhttp://cdn.bulbagarden.net/upload/thumb/f/fc/261Poochyena.png/250px-261Poochyena.png",
                      "#0262 Mightyena\nhttp://cdn.bulbagarden.net/upload/thumb/f/f1/262Mightyena.png/250px-262Mightyena.png",
                      "#0263 Zigzagon\nhttp://cdn.bulbagarden.net/upload/thumb/4/47/263Zigzagoon.png/250px-263Zigzagoon.png",
                      "#0264 Linoone\nhttp://cdn.bulbagarden.net/upload/thumb/f/f7/264Linoone.png/250px-264Linoone.png",
                      "#0265 Wumple\nhttp://cdn.bulbagarden.net/upload/thumb/7/76/265Wurmple.png/250px-265Wurmple.png",
                      "#0266 Silcoon\nhttp://cdn.bulbagarden.net/upload/thumb/e/ef/266Silcoon.png/250px-266Silcoon.png",
                      "#0267 Beautifly\nhttp://cdn.bulbagarden.net/upload/thumb/4/4c/267Beautifly.png/250px-267Beautifly.png",
                      "#0268 Cascoon\nhttp://cdn.bulbagarden.net/upload/thumb/a/a3/268Cascoon.png/250px-268Cascoon.png",
                      "#0269 Dustox\nhttp://cdn.bulbagarden.net/upload/thumb/3/34/269Dustox.png/250px-269Dustox.png",
                      "#0270 Lotad\nhttp://cdn.bulbagarden.net/upload/thumb/e/ee/270Lotad.png/250px-270Lotad.png",
                      "#0271 Lombre\nhttp://cdn.bulbagarden.net/upload/thumb/8/8b/271Lombre.png/250px-271Lombre.png",
                      "#0272 Ludicolo\nhttp://cdn.bulbagarden.net/upload/thumb/f/ff/272Ludicolo.png/250px-272Ludicolo.png",
                      "#0273 Seedot\nhttp://cdn.bulbagarden.net/upload/thumb/8/84/273Seedot.png/250px-273Seedot.png",
                      "#0274 Nuzleaf\nhttp://cdn.bulbagarden.net/upload/thumb/0/07/274Nuzleaf.png/250px-274Nuzleaf.png",
                      "#0275 Shiftry\nhttp://cdn.bulbagarden.net/upload/thumb/f/f7/275Shiftry.png/250px-275Shiftry.png",
                      "#0276 Taillow\nhttp://cdn.bulbagarden.net/upload/thumb/e/e4/276Taillow.png/250px-276Taillow.png",
                      "#0277 Swellow\nhttp://cdn.bulbagarden.net/upload/thumb/4/45/277Swellow.png/250px-277Swellow.png",
                      "#0278 Wingull\nhttp://cdn.bulbagarden.net/upload/thumb/3/39/278Wingull.png/250px-278Wingull.png",
                      "#0279 Pelipper\nhttp://cdn.bulbagarden.net/upload/thumb/f/f2/279Pelipper.png/250px-279Pelipper.png",
                      "#0280 Ralts\nhttp://cdn.bulbagarden.net/upload/thumb/e/e1/280Ralts.png/250px-280Ralts.png",
                      "#0281 Kirlia\nhttp://cdn.bulbagarden.net/upload/thumb/0/00/281Kirlia.png/250px-281Kirlia.png",
                      "#0282 Gardevoir\nhttp://cdn.bulbagarden.net/upload/thumb/9/99/282Gardevoir.png/250px-282Gardevoir.png",
                      "#0283 Surskit\nhttp://cdn.bulbagarden.net/upload/thumb/f/f6/283Surskit.png/250px-283Surskit.png",
                      "#0284 Masquerain\nhttp://cdn.bulbagarden.net/upload/thumb/0/0a/284Masquerain.png/250px-284Masquerain.png",
                      "#0285 Shroomish\nhttp://cdn.bulbagarden.net/upload/thumb/d/d8/285Shroomish.png/250px-285Shroomish.png",
                      "#0286 Breloom\nhttp://cdn.bulbagarden.net/upload/thumb/d/de/286Breloom.png/250px-286Breloom.png",
                      "#0287 Slakoth\nhttp://cdn.bulbagarden.net/upload/thumb/d/d2/287Slakoth.png/250px-287Slakoth.png",
                      "#0288 Vigoroth\nhttp://cdn.bulbagarden.net/upload/thumb/6/61/288Vigoroth.png/250px-288Vigoroth.png",
                      "#0289 Slaking\nhttp://cdn.bulbagarden.net/upload/thumb/7/71/289Slaking.png/250px-289Slaking.png",
                      "#0290 Nincada\nhttp://cdn.bulbagarden.net/upload/thumb/9/90/290Nincada.png/250px-290Nincada.png",
                      "#0291 Ninjask\nhttp://cdn.bulbagarden.net/upload/thumb/7/76/291Ninjask.png/250px-291Ninjask.png",
                      "#0292 Shedinja\nhttp://cdn.bulbagarden.net/upload/thumb/5/59/292Shedinja.png/250px-292Shedinja.png",
                      "#0293 Whismur\nhttp://cdn.bulbagarden.net/upload/thumb/6/6c/293Whismur.png/250px-293Whismur.png",
                      "#0294 Loudred\nhttp://cdn.bulbagarden.net/upload/thumb/1/12/294Loudred.png/250px-294Loudred.png",
                      "#0295 Exploud\nhttp://cdn.bulbagarden.net/upload/thumb/1/12/295Exploud.png/250px-295Exploud.png",
                      "#0296 Makuhita\nhttp://cdn.bulbagarden.net/upload/thumb/b/b6/296Makuhita.png/250px-296Makuhita.png",
                      "#0297 Hariyama\nhttp://cdn.bulbagarden.net/upload/thumb/6/6f/297Hariyama.png/250px-297Hariyama.png",
                      "#0298 Azurill\nhttp://cdn.bulbagarden.net/upload/thumb/a/ac/298Azurill.png/250px-298Azurill.png",
                      "#0299 Nosepass\nhttp://cdn.bulbagarden.net/upload/thumb/8/89/299Nosepass.png/250px-299Nosepass.png",
                      "#0300 Skitty\nhttp://cdn.bulbagarden.net/upload/thumb/8/8a/300Skitty.png/250px-300Skitty.png"
                      ]
        return await self.bot.say(randchoice(pokemonran))
    
def setup(bot):
    bot.add_cog(pokemon(bot))
