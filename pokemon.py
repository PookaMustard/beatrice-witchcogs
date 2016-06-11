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
        pokemonran = ["http://cdn.bulbagarden.net/upload/thumb/0/0d/025Pikachu.png/250px-025Pikachu.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/3e/039Jigglypuff.png/250px-039Jigglypuff.png",
                      "http://cdn.bulbagarden.net/upload/thumb/b/b1/151Mew.png/250px-151Mew.png",
                      "http://cdn.bulbagarden.net/upload/thumb/2/21/001Bulbasaur.png/250px-001Bulbasaur.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/73/002Ivysaur.png/250px-002Ivysaur.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/ae/003Venusaur.png/250px-003Venusaur.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/73/004Charmander.png/250px-004Charmander.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/4a/005Charmeleon.png/250px-005Charmeleon.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/7e/006Charizard.png/250px-006Charizard.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/39/007Squirtle.png/250px-007Squirtle.png",
                      "http://cdn.bulbagarden.net/upload/thumb/0/0c/008Wartortle.png/250px-008Wartortle.png",
                      "http://cdn.bulbagarden.net/upload/thumb/0/02/009Blastoise.png/250px-009Blastoise.png",
                      "http://cdn.bulbagarden.net/upload/thumb/5/5d/010Caterpie.png/250px-010Caterpie.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/cd/011Metapod.png/250px-011Metapod.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/d1/012Butterfree.png/250px-012Butterfree.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/df/013Weedle.png/250px-013Weedle.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/f0/014Kakuna.png/250px-014Kakuna.png",
                      "http://cdn.bulbagarden.net/upload/thumb/6/61/015Beedrill.png/250px-015Beedrill.png",
                      "http://cdn.bulbagarden.net/upload/thumb/5/55/016Pidgey.png/250px-016Pidgey.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/7a/017Pidgeotto.png/250px-017Pidgeotto.png",
                      "http://cdn.bulbagarden.net/upload/thumb/5/57/018Pidgeot.png/250px-018Pidgeot.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/46/019Rattata.png/250px-019Rattata.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/f4/020Raticate.png/250px-020Raticate.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/8b/021Spearow.png/250px-021Spearow.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/a0/022Fearow.png/250px-022Fearow.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/fa/023Ekans.png/250px-023Ekans.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/cd/024Arbok.png/250px-024Arbok.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/88/026Raichu.png/250px-026Raichu.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/9e/027Sandshrew.png/250px-027Sandshrew.png",
                      "http://cdn.bulbagarden.net/upload/thumb/0/0b/028Sandslash.png/250px-028Sandslash.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/81/029Nidoran.png/250px-029Nidoran.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/cd/030Nidorina.png/250px-030Nidorina.png",
                      "http://cdn.bulbagarden.net/upload/thumb/b/bf/031Nidoqueen.png/250px-031Nidoqueen.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/4a/032Nidoran.png/250px-032Nidoran.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/9f/033Nidorino.png/250px-033Nidorino.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/c6/034Nidoking.png/250px-034Nidoking.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/f4/035Clefairy.png/250px-035Clefairy.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/a9/036Clefable.png/250px-036Clefable.png",
                      "http://cdn.bulbagarden.net/upload/thumb/6/60/037Vulpix.png/250px-037Vulpix.png",
                      "http://cdn.bulbagarden.net/upload/thumb/0/05/038Ninetales.png/250px-038Ninetales.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/92/040Wigglytuff.png/250px-040Wigglytuff.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/da/041Zubat.png/250px-041Zubat.png",
                      "http://cdn.bulbagarden.net/upload/thumb/0/0c/042Golbat.png/250px-042Golbat.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/43/043Oddish.png/250px-043Oddish.png",
                      "http://cdn.bulbagarden.net/upload/thumb/2/2a/044Gloom.png/250px-044Gloom.png",
                      "http://cdn.bulbagarden.net/upload/thumb/6/6a/045Vileplume.png/250px-045Vileplume.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/d4/046Paras.png/250px-046Paras.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/80/047Parasect.png/250px-047Parasect.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/ad/048Venonat.png/250px-048Venonat.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/d3/049Venomoth.png/250px-049Venomoth.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/31/050Diglett.png/250px-050Diglett.png",
                      "http://cdn.bulbagarden.net/upload/thumb/e/e5/051Dugtrio.png/250px-051Dugtrio.png",
                      "http://cdn.bulbagarden.net/upload/thumb/d/d6/052Meowth.png/250px-052Meowth.png",
                      "http://cdn.bulbagarden.net/upload/thumb/1/13/053Persian.png/250px-053Persian.png",
                      "http://cdn.bulbagarden.net/upload/thumb/5/53/054Psyduck.png/250px-054Psyduck.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/fe/055Golduck.png/250px-055Golduck.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/41/056Mankey.png/250px-056Mankey.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/9a/057Primeape.png/250px-057Primeape.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/3d/058Growlithe.png/250px-058Growlithe.png",
                      "http://cdn.bulbagarden.net/upload/thumb/b/b8/059Arcanine.png/250px-059Arcanine.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/49/060Poliwag.png/250px-060Poliwag.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/a9/061Poliwhirl.png/250px-061Poliwhirl.png",
                      "http://cdn.bulbagarden.net/upload/thumb/2/2d/062Poliwrath.png/250px-062Poliwrath.png",
                      "http://cdn.bulbagarden.net/upload/thumb/6/62/063Abra.png/250px-063Abra.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/97/064Kadabra.png/250px-064Kadabra.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/cc/065Alakazam.png/250px-065Alakazam.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/85/066Machop.png/250px-066Machop.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/8e/067Machoke.png/250px-067Machoke.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/8f/068Machamp.png/250px-068Machamp.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/a2/069Bellsprout.png/250px-069Bellsprout.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/9f/070Weepinbell.png/250px-070Weepinbell.png",
                      "http://cdn.bulbagarden.net/upload/thumb/b/be/071Victreebel.png/250px-071Victreebel.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/4e/072Tentacool.png/250px-072Tentacool.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/f6/073Tentacruel.png/250px-073Tentacruel.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/98/074Geodude.png/250px-074Geodude.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/75/075Graveler.png/250px-075Graveler.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/f2/076Golem.png/250px-076Golem.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/3b/077Ponyta.png/250px-077Ponyta.png",
                      "http://cdn.bulbagarden.net/upload/thumb/3/3f/078Rapidash.png/250px-078Rapidash.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/70/079Slowpoke.png/250px-079Slowpoke.png",
                      "http://cdn.bulbagarden.net/upload/thumb/8/80/080Slowbro.png/250px-080Slowbro.png",
                      "http://cdn.bulbagarden.net/upload/thumb/6/6c/081Magnemite.png/250px-081Magnemite.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/72/082Magneton.png/250px-082Magneton.png",
                      "http://cdn.bulbagarden.net/upload/thumb/f/f8/083Farfetch%27d.png/250px-083Farfetch%27d.png",
                      "http://cdn.bulbagarden.net/upload/thumb/5/54/084Doduo.png/250px-084Doduo.png",
                      "http://cdn.bulbagarden.net/upload/thumb/9/93/085Dodrio.png/250px-085Dodrio.png",
                      "http://cdn.bulbagarden.net/upload/thumb/1/1f/086Seel.png/250px-086Seel.png",
                      "http://cdn.bulbagarden.net/upload/thumb/c/c7/087Dewgong.png/250px-087Dewgong.png",
                      "http://cdn.bulbagarden.net/upload/thumb/a/a0/088Grimer.png/250px-088Grimer.png",
                      "http://cdn.bulbagarden.net/upload/thumb/7/7c/089Muk.png/250px-089Muk.png",
                      "http://cdn.bulbagarden.net/upload/thumb/4/40/090Shellder.png/250px-090Shellder.png",
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
                      "http://cdn.bulbagarden.net/upload/thumb/8/84/101Electrode.png/250px-101Electrode.png"
                      ]
        return await self.bot.say(randchoice(pokemonran))
    
def setup(bot):
    bot.add_cog(pokemon(bot))
