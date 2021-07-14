import discord
from discord_components import *
from discord.ext import commands
from random import choice
from asyncio import TimeoutError

ch1 = ["Rock", "Scissors", "Paper"]


class rps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rps(self, ctx):

        comp = choice(ch1)

        yet = discord.Embed(title=f"{ctx.author.display_name}'s Rock Paper Scissors Game!", description=">Status: You haven't click on any button yet!", color=0xFFEA00)

        win = discord.Embed(title=f"{ctx.author.display_name}, You Won!", description=f">Status: **You have won!** Bot had chosen {comp}", color=0x00FF00)

        out = discord.Embed(title=f"{ctx.author.display_name}, You didn't click on time", description=">Status: **Timed Out!**", color=discord.Color.red())

        lost = discord.Embed(title=f"{ctx.author.display_name}, You Lost!", description=f">Status: **You have lost!** Bot had chosen {comp}", color=0x00FF00)

        tie = discord.Embed(title=f"{ctx.author.display_name}, It was a Tie!", description=f">Status: **Tie!** Bot has chosen {comp}", color=0x00FF00)

        m = await ctx.send(
            embed=yet,
            components=[[Button(style=1, label="Rock"), Button(
                style=3, label="Paper"), Button(style=4, label="Scissors")]]
        )

        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel

        try:
            res = await self.bot.wait_for("button_click", check=check, timeout=15)
            player = res.component.label

            if player == comp:
                await m.edit(embed=tie, components=[])

            if player == "Rock" and comp == "Paper":
                await m.edit(embed=lost, components=[])

            if player != "Rock" and comp == "Scissors":
                await m.edit(embed=win, components=[])

            if player == "Paper" and comp == "Rock":
                await m.edit(embed=win, components=[])

            if player == "Paper" and comp == "Scissors":
                await m.edit(embed=lost, components=[])

            if player == "Scissors" and comp != "Rock":
                await m.edit(embed=lost, components=[])

            if player == "Scissors" and comp == "Paper":
                await m.edit(embed=win, components=[])

        except TimeoutError:
            await m.edit(
                embed=out,
                components=[],
            )


def setup(bot):
    bot.add_cog(rps(bot))
