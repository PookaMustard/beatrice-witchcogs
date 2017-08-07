 
# beatrice-witchcogs
General-purpose cogs made for Red-DiscordBot, mostly search cogs, occasionally themed after Beatrice, the Golden Witch of Umineko no Naku Koro ni. They're all made to be used with Red-DiscordBot. It is assumed you know how to use Red-DiscordBot and how to install and download cogs.

## Cogs
### Appsearcher
Fetches search results from various application sites. Currently supports:
- `[p]humblebundle [gamename]` - Fetches a search link on Humble using your gamename
- `[p]itch [gamename]` - Fetches a search link on itch.io
- `[p]origin [gamename]` - Fetches a search link on Origin
- `[p]winstore [gamename]` - Fetches a search link on Windows Store
- `[p]gplay [appname]` - Fetches a search link on Google Play Store
- `[p]ios [appname]` - Fetches a search link on Apple iTunes Store
- `[p]xb [gamename]` - Fetches a search link on Xbox Store
- `[p]ps [gamename]` - Fetches a search link on PlayStation Store
- `[p]nintendo [gamename]` - Fetches a search link on Nintendo Store
- `[p]steamsearch [gamename]` - Fetches a search link on steam
- `[p]steamid [gameid]` - Makes a link out of the specified steam game id


### Command Request
If you're a bot owner who frequently adds new commands on the community's call and you have your private bot development server, Command Request takes command requests from your target community and sends them into one channel for easier bot development (which is saved via a command). Currently supports:
- `[p]commandrequest [command]` - Relays requested command to your current server. The `channelidstring` variable in the cog must be changed to reflect your current requests channel. The command request channel ID must be set through the next command.
- `[p]savechannelid [channelid]` - Saves the channel ID of the desired command request channel. Use Discord Developer Mode to copy the desired command request channel's ID.

### Echo
Makes the bot repeat what you say, while taking into account that only the bot owner can use Echo. Supports spaces but not newlines. Currently supports:
- `[p]echo [text]` - Repeats what you said after the command in the same channel.
- `[p]sonar [channelid] [text]` - Repeats what you said in a specific channel using the channel's ID.

### GOG
Fetches games or movies from GOG.com and displays information about them such as the prices and the platforms. Requires requests and BeautifulSoup4 to operate. Currently supports:
- `[p]gog [search query]` - Search and display information for the specified game or movie. Will ask the user which result they want if more than one result is detected. Used for up-to-date searches.
- `[p]gogcount` - Says how many products there are on GOG.com.

### Is It Down
Makes the bot check if a site is up and online or down and offline. May be prone to errors depending on the status of the site in question. It requires the dependencies asyncio and aiohttp Usage:
- `[p]isitdown [url]`

### Itch
Searches for products sold on the indie marketplace itch.io. Usage:
- `[p]itch [search]`

### Minecraft
Various Minecraft utilities. Usage:
- `[p]minecraft status` - Checks the various Minecraft.net API status affecting gameplay
- `[p]minecraft wiki [search]` - Searches the official Minecraft Wiki for articles
- `[p]minecraft player [player_name]` - Looks up a player's information such as skins, capes, or ID

### MyAnimeList Search
Makes the bot generate links for MAL search results. Currently supports:
- `[p]mal [searchname]` - Generates all-purpose search link for the specified string
- `[p]manga [manganame]` - Generates search link for the specified manga
- `[p]anime [animename]` - Generates search link for the specified anime
- `[p]malcharacter [charactername]` - Generates search link for the specified character
- `[p]mangalist [username]` - Generates mangalist link for the specified user
- `[p]animelist [username]` - Generates animelist link for the specified user

### Pokémon
Fetches the Pokédex entry, name and image of a Pokémon and embeds them into Discord. Usage:
- `[p]pokedex` - Sends the entirety of the Pokédex in a DM to the user.
- `[p]pokemon [optional: pokémonname OR pokedéx entry]` - Fetches a Pokémon. If there are no parameters provided, the bot will assume a random Pokémon. Otherwise, the bot will fetch the Pokémon listed under the specified Pokédex entry or EXACT Pokémon name.

### The Pirate Bay
Fetches up to eight possible matching torrents from The Pirate Bay using web crawling, and provides basic information on the torrents and the search URL if more than five results were found. Torrents may be NSFW. Usage:
- `[p]tpb [search query]` - To search for any torrent
- `[p]tpbcat [categories separated by commas with no spaces] [search query]` - To search for a torrent in a specified category

## Contact
The cogs should generally work fine, but sometimes there might be an unexpected error or bug that hinders the experience. In case you do find such an issue, either leave an issue on this repo, or contact me on Discord at Pooka#2892.
