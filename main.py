import discord
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=commands.when_mentioned_or("n!", "N!"), description="Beep boop I'm Nix's coffee machine", case_insensitive=True)

@bot.event
async def on_ready():
    print("I am ready")

extensions = [
	'cogs.bruh',
    'cogs.owner'
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)

keep_alive()
bot.run("no u")
