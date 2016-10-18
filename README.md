
# beatrice-witchcogs
General-purpose cogs made for Red-DiscordBot, mostly search cogs, occasionally themed after Beatrice, the Golden Witch of Umineko no Naku Koro ni. They're all made to be used with Red-DiscordBot. It is assumed you know how to use Red-DiscordBot and how to install and download cogs.

##Cogs
###Appsearcher
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

###Bing
Fetches search results from Bing and embeds them into Discord. It is a Red-DiscordBot frontend for py-bing-search (a required dependency), which requires an API key which you can set via `[p]apikey_bing`. It requires the Python module py-bing-search to work. Supports fetching the first result and a random operation from at max 100 results. Currently supports:
- `[p]bing [optional:random] [imagesearch]` - Looks up Bing for an image and embeds it into Discord in full resolution, with Safe Search set to Moderate.
- `[p]bingstrict [optional:random] [imagesearch]` - Looks up Bing for an image and embeds it into Discord in full resolution, with Safe Search set to Strict. 
- `[p]bingadult [optional:random] [imagesearch]` - Looks up Bing for an image and embeds it into Discord in full resolution, with Safe Search set to Off. Must be enabled by admins on a server and/or channel basis using `[p]bingset adult [channel/server]` for either servers or channels, with the channel settings prioritized before the server settings.
- `[p]bingsearch [optional:random] [websearch]` - Looks up Bing for a web URL and embeds it into Discord.
- `[p]bingvideo [optional:random] [videosearch]` - Looks up Bing for a video URL and embeds it into Discord
- `[p]bingnews [optional:random] [newsearch]` - Looks Bing for a news URL and embeds it into Discord along with a short headline, date and time and a summary of the headline.
- `[p]bing_clearsettings` - Clears saved adult channels and servers as well as the Bing API key.

###Command Request
If you're a bot owner who frequently adds new commands on the community's call and you have your private bot development server, Command Request takes command requests from your target community and sends them into one channel for easier bot development (which is saved via a command). Currently supports:
- `[p]commandrequest [command]` - Relays requested command to your current server. The `channelidstring` variable in the cog must be changed to reflect your current requests channel. The command request channel ID must be set through the next command.
- `[p]savechannelid [channelid]` - Saves the channel ID of the desired command request channel. Use Discord Developer Mode to copy the desired command request channel's ID.

###Echo
Makes the bot repeat what you say, while taking into account that only the bot owner can use Echo. Supports spaces but not newlines. Currently supports:
- `[p]echo [text]` - Repeats what you said after the command in the same channel.
- `[p]sonar [channelid] [text]` - Repeats what you said in a specific channel using the channel's ID.

###GOG
Fetches games or movies from GOG.com and displays information about them such as the prices and the platforms. Requires requests and BeautifulSoup4 to operate. Currently supports:
- `[p]gog [searchname]` - Search and display information for the specified game or movie. Will ask the user which result they want if more than one result is detected.
- `[p]gog [randomgame]` - Will display any random game from GOG.com.
- `[p]gog [gamecount]` - Will display the amount of DRM-free games on GOG.com

###Is It Down
Makes the bot check if a site is up and online or down and offline. May be prone to errors depending on the status of the site in question. It requires the dependencies asyncio and aiohttp Usage:
- `[p]isitdown [url]`
 
###MyAnimeList Search
Makes the bot generate links for MAL search results. Currently supports:
- `[p]mal [searchname]` - Generates all-purpose search link for the specified string
- `[p]manga [manganame]` - Generates search link for the specified manga
- `[p]anime [animename]` - Generates search link for the specified anime
- `[p]malcharacter [charactername]` - Generates search link for the specified character
- `[p]mangalist [username]` - Generates mangalist link for the specified user
- `[p]animelist [username]` - Generates animelist link for the specified user

###Pokémon
Fetches the Pokédex entry, name and image of a Pokémon and embeds them into Discord. Usage:
- `[p]pokedex` - Sends the entirety of the Pokédex in a DM to the user.
- `[p]pokemon [optional: pokémonname OR pokedéx entry]` - Fetches a Pokémon. If there are no parameters provided, the bot will assume a random Pokémon. Otherwise, the bot will fetch the Pokémon listed under the specified Pokédex entry or EXACT Pokémon name.

###The Pirate Bay
Makes the bot generate links for TPB search results. Selected search entry may or may not be NSFW. Usage:
- `[p]tpb [searchname]`

##Contact
The cogs should generally work fine, but sometimes there might be an unexpected error or bug that hinders the experience. In case you do find such an issue, either leave an issue on this repo, or contact me on Discord at Pooka#2892.
