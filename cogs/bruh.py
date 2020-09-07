import discord
from discord.ext import commands


class bruh(commands.Cog):
    """
    bruh
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pekis(self, ctx):
        """pekis"""
        await ctx.send("https://cdn.discordapp.com/attachments/711686111205785711/752227168112607293/Screen_Shot_2020-09-07_at_1.52.05_AM.png")
        
def setup(bot):
	bot.add_cog(bruh(bot))