import discord
import aiohttp
import random
from discord.ext import commands
import io
import os


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

    @commands.command()
    async def coffee(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://coffee.alexflipnote.dev/random.json") as r:
                res = await r.json()
                embed = discord.Embed(title="hehe coffee get it?", color=0xA52A2A)
                embed.set_image(url=res["file"])
                await ctx.send(embed=embed)
                
def setup(bot):
	bot.add_cog(bruh(bot))
