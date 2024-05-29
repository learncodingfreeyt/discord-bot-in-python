import discord
from discord.ext import commands

# Setting up the intents which specify what events the bot will listen to.
intents = discord.Intents.default()
intents.message_content = True  # Enabling the intent to read message content.

# Creating an instance of the Bot with a command prefix "!" and the specified intents.
bot = commands.Bot("!", intents=intents)

# Event that runs when the bot is ready and connected to Discord.
@bot.event
async def on_ready():
	print(f"Bot Ready: {bot.user}")  # Prints a message to the console indicating the bot is ready.

# Slash command definition for the bot.
@bot.slash_command(name="ping", description="ping command")
async def _ping(ctx):
	await ctx.respond("pong")  # Responds with "pong" when the /ping command is used.
	return

# Prefix command definition for the bot.
@bot.command()
async def test(ctx):
	await ctx.reply("test 22")  # Replies with "test 22" when the !test command is used.
	return

# Running the bot with the provided token.
bot.run("TOKEN")
