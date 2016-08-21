# beatrice-witchcogs
General-purpose cogs made for Red-DiscordBot, mostly search cogs.
They're all made to be used with Red-DiscordBot. It is assumed you know how to use Red-DiscordBot.

##Cogs
###Appsearcher
Fetches search results from various application sites. Currently supports:
- `[p]gog [[gamename]/gamecount/random]` - Fetches a list of games on GOG. Allows you to choose from the available first 10 results and lists contextual info about the game such as pricing and platforms. Currently the most advanced command in Appsearcher.
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
- `[p]stemaid [gameid]` - Makes a link out of the specified steam game id

###Bing
Fetches search results from Bing and embeds them into Discord. It is a Red-DiscordBot frontend for py-bing-search. Supports fetching the first result and a random operation from at max 100 results. Currently supports:
- `[p]bing [optional:random] [imagesearch]` - Looks up Bing for an image and embeds it into Discord in full resolution, with Safe Search set to Moderate.
- `[p]bingstrict [optional:random] [imagesearch]` - Looks up Bing for an image and embeds it into Discord in full resolution, with Safe Search set to Strict. 
- `[p]bingadult [optional:random] [imagesearch]` - Looks up Bing for an image and embeds it into Discord in full resolution, with Safe Search set to Off. Must be enabled by admins on a server and/or channel basis using `[p]bingadultsets` for servers and `[p]bingadultsetc` for channels.
- `[p]bingsearch [optional:random] [websearch]` - Looks up Bing for a web URL and embeds it into Discord.
- `[p]bingvideo [optional:random] [videosearch]` - Looks up Bing for a video URL and embeds it into Discord
- `[p]bingnews [optional:random] [newsearch]` - Looks Bing for a news URL and embeds it into Discord along with a short headline, date and time and a summary of the headline.
