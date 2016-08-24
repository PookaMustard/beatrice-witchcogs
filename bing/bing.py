from .utils.dataIO import fileIO
from .utils import checks
import json
import os
import discord
from discord.ext import commands
from random import randint
try:
	from py_bing_search import PyBingImageSearch, PyBingWebSearch, PyBingVideoSearch, PyBingNewsSearch
	bingavailable = True
except:
	bingavailable = False

DATADIR = "data/bing"
SETTINGS = DATADIR + "/settings.json"

class Bing:
	"""Fetches search results from Bing.
	Uses the Python module py_bing_search as a frontend for Red"""
	
	def __init__(self, bot):
		self.bot = bot
		
	def getfrombing(self, apikey, text, limit, operation):
		if operation == 'moderateimagesearch':
			bing_obj = PyBingImageSearch(apikey, text, custom_params="&Adult='Moderate'")
		elif operation == 'strictimagesearch':
			bing_obj = PyBingImageSearch(apikey, text, custom_params="&Adult='Strict'")
		elif operation == 'adultimagesearch':
			bing_obj = PyBingImageSearch(apikey, text, custom_params="&Adult='Off'")
		elif operation == 'websearch':
			bing_obj = PyBingWebSearch(apikey, text, web_only=False)
		elif operation == 'videosearch':
			bing_obj = PyBingVideoSearch(apikey, text)
		elif operation == 'newssearch':
			bing_obj = PyBingNewsSearch(apikey, text)
		result = bing_obj.search(limit=limit, format='json')
		return result
		
	def obtainresult(self, result, operation):
		maxnum = len(result)
		if operation == 'moderateimagesearch' or operation == 'videosearch' or \
			operation == 'strictimagesearch' or operation == 'adultimagesearch':
			try:
				return result[randint(1, maxnum) - 1].media_url
			except ValueError:
				return "Search failed."
		elif operation == 'websearch':
			try:
				return result[randint(1, maxnum) - 1].url
			except ValueError:
				return "Search failed."
		elif operation == 'newssearch':
			num = randint(1, maxnum) - 1
			try:
				time = result[num].date
			except ValueError:
				return "Search failed."
			time = "Date: " + time
			time = time.replace('T', '\nTime: ').replace('Z', '')
			bottext = result[num].title + "\n" + result[num].url + "\n" + time + "\n" + \
				result[num].description
			return bottext
			
	def limitget(self, text):
		if text.split(' ', 1)[0].lower() == 'random':
			text = text.replace('random ', '', 1)
			limit = 100
		else:
			limit = 1
		return text, limit
		
	def setadultchannel(self, channel, status):
		settings = loadauth()
		settings['adult']['channels'][channel.id] = status
		saveauth(settings)
		return settings
		
	def setadultserver(self, server, status):
		settings = loadauth()
		settings['adult']['servers'][server.id] = status
		saveauth(settings)
		return settings
		
	def checkadult(self, server, channel, settings):
		if channel.id not in settings['adult']['channels']:
			adultchannel = 'Unknown'
		else:
			adultchannel = settings['adult']['channels'][channel.id]
		if server.id not in settings['adult']['servers']:
			adultserver = 'False'
		else:
			adultserver = settings['adult']['servers'][server.id]
		if adultchannel == 'False':
			return False
		elif (adultchannel == 'True' or adultchannel == 'Unknown') and adultserver == 'True':
			return True
		elif adultchannel == 'True' and adultserver == 'False':
			return True
		elif adultchannel == 'Unknown' and adultserver == 'False':
			return False
			
	@commands.command(pass_context=True)
	@checks.is_owner()
	async def apikey_bing(self, ctx, key):
		"""Set the Bing API key."""
		settings = loadauth()
		settings['apikey'] = key
		saveauth(settings)
		return await self.bot.say("Bing API key saved.")
		
	@commands.command(pass_context=True)
	@checks.is_owner()
	async def bing_clearsettings(self, ctx):
		"""Clears all Bing settings, including API key and %bingadult access"""
		message = ctx.message
		await self.bot.say("Are you sure you want to delete all of the Bing cog's settings?\n(y/n)")
		response = await self.bot.wait_for_message(author=message.author)
		if response.content.lower().strip() == "y":
			clearauth()
			return await self.bot.say("Settings successfully cleared. You need to reset the API key before " +
				"using the Bing cog again.")
		else:
			return await self.bot.say("Cancelled clear operation.")
		
	@commands.command(pass_context=True)
	@checks.admin_or_permissions(manage_server=True)
	async def bingsetadult(self, ctx, setting):
		"""Sets %bingadult status.
		[setting] can either be server or channel."""
		
		channel = ctx.message.channel
		server = ctx.message.server
		message = ctx.message
		if setting == 'channel':
			await self.bot.say("Do you want to enable %bingadult for this channel? This will enable this  " +
				"channel to use the %bingadult command, which image searches Bing with Safe Search " +
				"turned off. Do note that this setting will override the global server setting and " +
				"thus will allow %bingadult in this channel even if the global server setting is off. " +
				"\n**ARE YOU SURE YOU WANT TO TOGGLE %bingadult?**\n(y/n)")
		elif setting == 'server':
			await self.bot.say("Do you want to enable %bingadult for this server? This will enable your " +
				"server to use the %bingadult command, which image searches Bing with Safe Search " +
				"turned off. Do note that this setting will be overriden per channel if a channel " +
				"is set to accept usage of %bingadult. **ARE YOU SURE YOU WANT TO TOGGLE %bingadult?**\n" +
				"(y/n)")
		else:
			return await self.bot.say("```This command accepts either server or channel. Please use it again.```")
		response = await self.bot.wait_for_message(author=message.author)
		if response.content.lower().strip() == "y":
			if setting == 'channel':
				settings = self.setadultchannel(channel, 'True')
				return await self.bot.say("Enabled %bingadult settings for this channel.")
			elif setting == 'server':
				settings = self.setadultserver(server, 'True')
				return await self.bot.say("Enabled %bingadult settings for this server.")
		else:
			if setting  == 'channel':
				settings = self.setadultchannel(channel, 'False')
				return await self.bot.say("Disabled %bingadult settings for this channel.")
			elif setting == 'server':
				settings = self.setadultserver(server, 'False')
				return await self.bot.say("Disabled %bingadult settings for this server.")
		
	@commands.command()
	async def bing(self, *, text):
		"""Searches Bing for images."""
		settings = loadauth()
		operation = 'moderateimagesearch'
		if settings['apikey'] == '' or settings['apikey'] == 'blank':
			return await self.bot.say("Missing or incorrect API key. Please contact the owner to add an API key.")
		apikey = settings['apikey']
		text, limit = self.limitget(text)
		result = self.getfrombing(apikey, text, limit, operation)
		bottext = self.obtainresult(result, operation)
		return await self.bot.say(bottext)
		
	@commands.command()
	async def bingstrict(self, *, text):
		"""Searches Bing for images with a strict Safe Search."""
		settings = loadauth()
		operation = 'strictimagesearch'
		if settings['apikey'] == '' or settings['apikey'] == 'blank':
			return await self.bot.say("Missing or incorrect API key. Please contact the owner to add an API key.")
		apikey = settings['apikey']
		text, limit = self.limitget(text)
		result = self.getfrombing(apikey, text, limit, operation)
		bottext = self.obtainresult(result, operation)
		return await self.bot.say(bottext)
		
	@commands.command(pass_context=True)
	async def bingadult(self, ctx,  *, text):
		"""Searches Bing for images with Safe Search off."""
		settings = loadauth()
		channel = ctx.message.channel
		server = ctx.message.server
		operation = 'adultimagesearch'
		check = self.checkadult(server, channel, settings)
		if check == False:
			return await self.bot.say("Usage of %bingadult is disabled in this server and/or channel.")
		if settings['apikey'] == '' or settings['apikey'] == 'blank':
			return await self.bot.say("Missing or incorrect API key. Please contact the owner to add an API key.")
		apikey = settings['apikey']
		text, limit = self.limitget(text)
		result = self.getfrombing(apikey, text, limit, operation)
		bottext = self.obtainresult(result, operation)
		return await self.bot.say(bottext)
		
	@commands.command()
	async def bingsearch(self, *, text):
		"""Searches Bing for web results."""
		settings = loadauth()
		operation = 'websearch'
		if settings['apikey'] == '' or settings['apikey'] == 'blank':
			return await self.bot.say("Missing or incorrect API key. Please contact the owner to add an API key.")
		apikey = settings['apikey']
		text, limit = self.limitget(text)
		result = self.getfrombing(apikey, text, limit, operation)
		bottext = self.obtainresult(result, operation)
		return await self.bot.say(bottext)
		
	@commands.command()
	async def bingvideo(self, *, text):
		"""Searches Bing for video results."""
		settings = loadauth()
		operation = 'videosearch'
		if settings['apikey'] == '' or settings['apikey'] == 'blank':
			return await self.bot.say("Missing or incorrect API key. Please contact the owner to add an API key.")
		apikey = settings['apikey']
		text, limit = self.limitget(text)
		result = self.getfrombing(apikey, text, limit, operation)
		bottext = self.obtainresult(result, operation)
		return await self.bot.say(bottext)
		
	@commands.command()
	async def bingnews(self, *, text):
		"""Searches Bing for video results."""
		settings = loadauth()
		operation = 'newssearch'
		if settings['apikey'] == '' or settings['apikey'] == 'blank':
			return await self.bot.say("Missing or incorrect API key. Please contact the owner to add an API key.")
		apikey = settings['apikey']
		text, limit = self.limitget(text)
		result = self.getfrombing(apikey, text, limit, operation)
		bottext = self.obtainresult(result, operation)
		return await self.bot.say(bottext)

def saveauth(settings):
	settings = settings
	with open(SETTINGS, 'w') as f:
		json.dump(settings, f)
	return

def loadauth():
	settings = {}
	with open(SETTINGS, 'r') as f:
		settings = json.load(f)
	return settings
	
def clearauth():
	settings = { 'apikey': 'blank', 'adult' : {'servers': {}, 'channels': {}}}
	fileIO(SETTINGS, "save", settings)
	return

def check_folders():
	if not os.path.exists(DATADIR):
		print("Creating data directory for Command Request cog")
		os.mkdir(DATADIR)
			
def check_files():
	if not fileIO(SETTINGS, "check"):
		settings = { 'apikey': 'blank', 'adult' : {'servers': {}, 'channels': {}}}
		print("Creating blank data file for Command Request cog")
		fileIO(SETTINGS, "save", settings)

def setup(bot):
	if bingavailable:
		check_folders()
		check_files()
		bot.add_cog(Bing(bot))
	else:
		raise RuntimeError("You need to run 'pip3 install py-bing-search', as it is needed for this cog to run.")
