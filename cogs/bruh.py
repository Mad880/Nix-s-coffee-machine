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
        # holy shit didudueuu omGG SO YOOFOD AD TBEING NGOOD!
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
     #bRUHR RALMOA AOM Oenkey EMOENKEEY EMOENEKEY laMRAOMMOOMMAOOAMAOMMOAOMAMOA

    @commands.command()
    async def koffeemachien(self, ctx):
      embed = discord.Embed(title="Koffee machien dispens koffee", color=0x555a74)
      embed.set_image(url="https://cdn.discordapp.com/attachments/711686111205785711/770292166059622410/Screen_Shot_2020-09-07_at_2.20.00_AM.png")
      embed.set_footer(text="koffee tastse e suo youg")
      await ctx.send(embed=embed)
#bruh i am fucking high when i make this bullshit i swear

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        channel = self.bot.get_channel(770319873804730409)
        agree = self.bot.get_emoji(758404116367540275)
        disagree = self.bot.get_emoji(758404182561914900)
        embed = discord.Embed(title=f"some idiot ({ctx.author.display_name}) suggested something probably stupid", description="wow bro thanks for trying to make the bot worse i love you too", color=0x555a74) 
        embed.add_field(name="Suggestion:", value=suggestion)
        embed.set_footer(text="please don't be n!childporn") # bruh
        sent = await channel.send(embed=embed)
        await sent.add_reaction(emoji=agree)
        await sent.add_reaction(emoji=disagree)
        await ctx.send(f"ok cool let's see his suggestion in {channel.mention}")

    @commands.command()
    async def yourmom(self, ctx):
     embed = discord.Embed(title="ur mom lmaooo")
     embed.set_image(url="https://cdn.discordapp.com/attachments/670975058734350346/770572797230710795/Screen_Shot_2020-10-27_at_8.15.20_AM.png")
     embed.set_footer(text="nuts")
     await ctx.send(embed=embed)

    @commands.command()
    async def heil(self, ctx):
      embed = discord.Embed(title="Guys what the hell!?!?!?!?! it's literally hitler rn!!!!!!", color=0x555a74)
      embed.set_image(url="https://cdn.discordapp.com/attachments/670975058734350346/770572790733602836/balls.jpg")
      embed.set_footer(text="OMG NO WAY HITLER I'M YOUR BIGGEST FAN!!!!!!")
      await ctx.send(embed=embed)

    @commands.command()
    async def phil(self, ctx):
      embed = discord.Embed(title="got nutz!!!!",
      color=0x555a74)
      embed.set_image(url="https://cdn.discordapp.com/attachments/670975058734350346/770577878190522378/Screen_Shot_2020-10-27_at_8.25.45_AM.png")
      embed.set_footer(text="holy shit it's literally nutshack phil")
      await ctx.send(embed=embed)

    @commands.command()
    async def domesticviolence(self, ctx):
      embed = discord.Embed(title="WE GOIn INTERNATIONAL!!!",
      color=0x555a74)
      embed.set_image(url="https://cdn.discordapp.com/attachments/670975058734350346/770572847742976000/lol.jpeg")
      embed.set_footer(text="lmamo")
      await ctx.send(embed=embed)
    
    @commands.command()
    async def dickhead(self, ctx):
      await ctx.send("https://cdn.discordapp.com/attachments/670975058734350346/770637879080386580/yes.png")

    @commands.command()
    async def tyler(self, ctx):
      await ctx.send("[Tyler] Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler Tyler [retard]")

    @commands.command()
    async def balls(self, ctx):
      await ctx.send ("AR-EE-TEE-AY-AR-EE-TEE-DEE")

    @commands.command()
    async def grapes(self, ctx):
     embed = discord.Embed(title="grapes", color=0x555a74)
     embed.set_image(url="https://cdn.discordapp.com/attachments/766966300014149642/770669743665315921/download-8.jpg")
     embed.set_footer(text="grapes")
     await ctx.send(embed=embed)

    @commands.command()
    async def nuggets(self, ctx):
      await ctx.send ("badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets badggets")

    @commands.command()
    async def bruh(self, ctx):
      await ctx.send("BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!! BRUH!!!")

    @commands.command()
    async def shitshitshit(self, ctx):
      await ctx.send("SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT SHIT")


    @commands.command()
    async def gaystride(self, ctx):
      await ctx.send("fuck you")

    @commands.command()
    async def imgay(self, ctx):
      await ctx.send("Aye, he’s in love with who I am!\nBack in high school I used to jerk him with my hands…\nnow I hit that orgy sex with condoms in my hand\nI did half a xan\nnow I’m pounding on my mans\nhad me out like a light ayyy yuh like a light ayyy yuh like a light aye\nslept through the pipe aye \nnot for tonight\nseven sixty-seven man that shit got double wedgies man I still got dick to settle man\nI smashed on the block\nmade her ripe\ncut the lice\nrape me twice\nniggas think im straight\nit’s on sight\nnothing nice\nbooty looking ripe\njesus christ\nDICKS OVER RICE\nTHAT’S WHAT I LIKE\nTHAT’S WHAT WE LIKE\nLOST MY RESPECT \n**WHEN I SUCK THE COCK I GET WETTY WITH MY NECK**\nSEE THE COCK THAT I TOOK\nTHAT HAD ME SHOOK\nJERK ON HIS JIMMY\nI BEEN ON THAT COCK MILLY ROCK TILL IM DIZZY\n(AYE YUH) LIKE WITH IZZY\n(FUCK YUH) NOONE’S SEEN HIM\n(AYE YEAH) I TRIED TO SKEET HIM\nHE’S IN LOVE WITH WHO I AM\nBACK IN HIGH SCHOOL I USED TO JERK HIM WITH MY HANDS\nNOW I HIT THAT ORGY SEX WITH CONDOMS IN MY HAND\nI DID HALF A XAN NOW IM POUNDING ON MY MANS\nHAD ME OUT LIKE A LIGHT (LIKE A LIGHT)\nLIKE A LIGHT (LIKE A LIGHT) LIKE A LIGHT (LIKE A LIGHT) YEAAAAAH\nPASSING COCKS ON STEADY LICKING DICKS AINT GETTING WISE\nYEAH HE SAID I GOT THAT BOOTY LIKE I KNOW MY BOOTY TIGHT YEAHHHH\nIT’S ABSOLUTE\nMY BOOTY LOOSE\nLADDER PENIS\nWE EAT IT TOO YEAH\nWE BACK ON THAT DICK WE RIDE THAT COCK UNTIL WE POOP YEAAAH \nSHAWTY IN THE BACK HE SAID HIS BOOTY LIKE A NEWT YEAH\nAYE WHAT IT LOOK\nMY BOOTY SHOOK\nDONE WITH NECK\nTHE BOOTY CROOK\nPASS ME TO HIS HOMIE YEAH THAT PENIS GOT ME HOOKED\nBABY DADDY AT MY HOUSE MAKE THIS BABY MOTHER SHOOK YEAAAAAAAAAAAH")


def setup(bot):
    bot.add_cog(bruh(bot))
