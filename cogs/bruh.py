import discord
import aiohttp
import random
from discord.ext import commands
import io
import random
import os


class bruh(commands.Cog):
    """
    bruh
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pekis(self, ctx):
        embed = discord.Embed(title="harder than the pekis in d!p ek in", color=0x433b74)
        embed.set_image(url="https://cdn.discordapp.com/attachments/711686111205785711/752227168112607293/Screen_Shot_2020-09-07_at_1.52.05_AM.png")
        embed.set_footer(text="dude pekis is fucking funny ngl")
        await ctx.send(embed=embed)
        #holy fucking shit i did it by myself i am so fucking good dude i am literally better than roie holy shit!!!

    @commands.command()
    async def duck(self, ctx):
        """it's literally n!duck what do you want"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://random-d.uk/api/v1/random") as r:
                res = await r.json()
                embed = discord.Embed(title="oh wow a duck didnt expect that one so crazy!!!", color=0xFFFF00)
                embed.set_image(url=res['url'])
                embed.set_footer(text=f"Ducky requested by {ctx.author.display_name}")
                await ctx.send(embed=embed)
                #fuck off bro who the fuck needs help with this shit!!!! it's literally n!duck who fucking cares????

    @commands.command()
    async def coffee(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://coffee.alexflipnote.dev/random.json") as r:
                res = await r.json()
                embed = discord.Embed(title="its my job to dispense this so you better fucking enjoy it asshole", color=0xA52A2A)
                embed.set_image(url=res["file"])
                await ctx.send(embed=embed)

    @commands.command()
    async def ksi(self, ctx):
        embed = discord.Embed(title="KSI MOMENT", color=0x555a74)
        embed.set_image(url="https://cdn.discordapp.com/attachments/711686111205785711/769980174258536458/Screen_Shot_2020-10-22_at_12.39.32_PM.png")
        embed.set_footer(text="ksi")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def prankt(self, ctx):
  
        embed = discord.Embed(title="GOT PRANKED!!!!! LOL IMAGINE GETTING PRANKED BRO",
         color=0x555a74)
        embed.set_image(url="https://cdn.discordapp.com/attachments/711686111205785711/769981182951030794/prankt.png")
        embed.set_footer(text="lol prankt")
        await ctx.send(embed=embed)


    @commands.command()
    async def penis(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        penis_size = random.randint(1, 69)
        penis = '8' + '='*penis_size + 'D' 
        await ctx.send(f"{user.display_name}'s pp\n{penis}\nLength: {penis_size} meters long")


    
    @commands.command()
    async def trollface(self, ctx):
        embed = discord.Embed(title="lmao trolled gg",
        color=0x555a74)
        embed.set_image(url="https://cdn.discordapp.com/attachments/711686111205785711/769999310695694366/trollface.png")
        embed.set_footer(text="rip fucking career bro you got trolled")
        await ctx.send(embed=embed)


    @commands.command()
    async def cumbox(self, ctx):
        embed = discord.Embed(title="CUM BOX!!!",
        color=0x555a74)
        embed.set_image(url="https://cdn.discordapp.com/attachments/711686111205785711/770002976752140298/v573h44rle251.png")
        embed.set_footer(text="why does the cum look like that bro")
        await ctx.send(embed=embed)


    @commands.command()
    async def bullshit(self, ctx):
        embed = discord.Embed(title="PFFFFT BULLSHIT HE'S GAY!!!!!!!!!",
        color=0x555a74)
        embed.set_image(url="https://cdn.discordapp.com/attachments/711686111205785711/770017982692458506/Screen_Shot_2020-10-26_at_4.11.39_AM.png")
        embed.set_footer(text="i think he might be gay bro")
        await ctx.send(embed=embed)



    
    @commands.command()
    async def agree(self, ctx):
     await ctx.send("https://cdn.discordapp.com/attachments/711686111205785711/770018830181072896/DO_YOU_AGREE_WITH_HIM.mp4")
     


def setup(bot):
	bot.add_cog(bruh(bot)) 
