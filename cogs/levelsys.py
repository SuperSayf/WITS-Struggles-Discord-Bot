import discord
from discord.ext import commands
from pymongo import MongoClient

bot_channel = 857618527825559563
talk_chanels = [819930408824471582, 819934375327039538, 819934432369705012, 847826201233457203, 819932068741644330, 857235624981561364, 857618527825559563, 819945562949681181, 819945683926384650, 819945780294320218, 819945849991200799,
    819933361299783762, 819932645055266856, 819932827088191488, 819933060887609354, 819933085084418078, 819933576153530378, 819933623729520650, 821441897058271232, 821004414357733387, 855098224875798540, 855099352451514428, 857635656515846145]

level = ["lvl 10", "lvl 20", "lvl 30", "lvl 40", "lvl 50", "Legend (max lvl)"]
levelnum = [10, 20, 30, 40, 50, 100]

cluster = MongoClient(
    "***REMOVED***")

levelling = cluster["discord"]["levelling"]


class levelsys(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_chanels:
            stats = levelling.find_one({"id": message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id": message.author.id, "xp": 100}
                    levelling.insert_one(newuser)
                else:
                    if len(message.clean_content) > 100:
                        xp = stats["xp"] + 35
                    elif len(message.clean_content) > 80:
                        xp = stats["xp"] + 30
                    elif len(message.clean_content) > 60:
                        xp = stats["xp"] + 25
                    elif len(message.clean_content) > 40:
                        xp = stats["xp"] + 20
                    elif len(message.clean_content) > 20:
                        xp = stats["xp"] + 15
                    elif len(message.clean_content) > 10:
                        xp = stats["xp"] + 10
                    else:
                        xp = stats["xp"] + 5
                    levelling.update_one({"id" : message.author.id}, {"$set" : {"xp" : xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.channel.send(f"well done {message.author.mention}! You leveled up to **level: {lvl}**!")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(description=f"{message.author.mention} you have gotten role **{level[i]}***!!!")
                                embed.set_thumbnail(url=message.author.avatar_url)
                                await message.channel.send(embed=embed)

    @commands.command()
    async def rank(self, ctx):
        if ctx.channel.id == bot_channel:
            stats = levelling.find_one({"id" : ctx.author.id})
            if stats is None:
                embed = discord.Embed(description="You haven't sent any messages, no rank!!!")
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                boxes = int((xp/(200*((1/2) * lvl)))*20)
                rankings = levelling.find().sort("xp",-1)
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                embed = discord.Embed(title="{}'s level stats".format(ctx.author.name))
                embed.add_field(name="Name", value=ctx.author.mention, inline=True)
                embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
                embed.add_field(name=f"Progress Bar [lvl {lvl}]", value=boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline=False)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)

    @commands.command()
    async def leaderboard(self, ctx):
        if (ctx.channel.id == bot_channel):
            rankings = levelling.find().sort("xp", -1)
            i = 1
            embed = discord.Embed(title="Rankings")
            for x in rankings:
                # Use try if server has less than 10 members
                temp = ctx.guild.get_member(x["id"])
                tempxp = x["xp"]
                embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempxp}", inline=False)
                i += 1
                if i == 11:
                    break
            await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(levelsys(bot))
