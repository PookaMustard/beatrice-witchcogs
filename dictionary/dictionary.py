from discord.ext import commands
try:
    from PyDictionary import PyDictionary as dictionary
    PyDictionaryAvailable = True
except:
    PyDictionaryAvailable = False


class Dictionary:
    """Search the online dictionary for a given word."""

    def __init__(self, bot):
        self.bot = bot

    def meaningtextformat(self, function, result):
        try:
            count = len(result[function]) - 1
            if count > 4:
                count = 4
            counter = 0
            text = "\n**__" + function + ":__**"
            while counter <= count:
                text = text + "\n• " + str(result[function][counter])
                counter = counter + 1
            return text
        except KeyError:
            text = ""
            return text

    def nymtextformat(self, function, result, word):
        count = len(result) - 1
        counter = 0
        text = "Found the following " + function + " for **" + word + "**:"
        while counter <= count:
            text = text + "\n• " + str(result[counter])
            counter = counter + 1
        return text

    @commands.command()
    async def dictionary(self, word):
        """Checks the dictionary for the meanings of a given word."""

        word = word.lower()
        try:
            result = dictionary.meaning(word)
            nountext = self.meaningtextformat("Noun", result)
            verbtext = self.meaningtextformat("Verb", result)
            adjtext = self.meaningtextformat("Adjective", result)
            advtext = self.meaningtextformat("Adverb", result)
        except TypeError:
            return await self.bot.say("No results found. Are you " +
                                      "searching for a valid word?")
        text = "\n" + nountext + "\n" + verbtext + "\n" + adjtext + "\n" + \
               advtext
        definition = "Found the following definitions for **" + word + "**:" \
                     + text
        return await self.bot.say(definition)

    @commands.command()
    async def synonym(self, word):
        """Checks the dictionary for the synonyms for a given word."""

        word = word.lower()
        result = dictionary.synonym(word)
        try:
            text = self.nymtextformat("synonyms", result, word)
            return await self.bot.say(text)
        except TypeError:
            return await self.bot.say("No results found. Are you " +
                                      "searching for a valid word?")

    @commands.command()
    async def antonym(self, word):
        """Checks the dictionary for the antonyms for a given word."""

        word = word.lower()
        result = dictionary.antonym(word)
        try:
            text = self.nymtextformat("antonyms", result, word)
            return await self.bot.say(text)
        except TypeError:
            return await self.bot.say("No results found. Are you " +
                                      "searching for a valid word?")


def setup(bot):
    if PyDictionaryAvailable:
        bot.add_cog(Dictionary(bot))
    else:
        raise RuntimeError("You need to run 'pip3 install PyDictionary', " +
                           "as it is needed for this cog to run.")
