import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

bot = commands.Bot(command_prefix=commands.when_mentioned_or("n!", "N!"), description="DAMN BRO NO WAY IT's THE HELP SECTION!!!!!! BRUH!HH!H!H!H!!H", case_insensitive=True)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="with my nuts tbh")) #tbh
    print("YUH COFFEE TIME BRUHHHHH COFFEEE MOMENT>>>>>>")
    
extensions = [
	'cogs.bruh',
    'cogs.owner'
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)

keep_alive()
token = os.getenv("BOT_TOKEN")
bot.run(token)
