import discord
import numpy as np
import os
from discord.ext import commands
from PIL import Image, ImageDraw
from io import BytesIO


class rip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rip(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        rip = Image.open(os.getcwd()+'\\cogs\\rip\\rip.png')

        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data).convert("RGB")
        npImage = np.array(pfp)
        h, w = pfp.size

        alpha = Image.new('L', pfp.size, 0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0, 0, h, w], 0, 360, fill=255)
        npAlpha = np.array(alpha)
        npImage = np.dstack((npImage, npAlpha))
        pfp = Image.fromarray(npImage)

        pfp = pfp.resize((130, 130))

        rip.paste(pfp, (221, 210), pfp)

        rip.save(os.getcwd()+'\\cogs\\rip\\prip.png')

        await ctx.send(file=discord.File(os.getcwd()+'\\cogs\\rip\\prip.png'), content=member.mention)


def setup(bot):
    bot.add_cog(rip(bot))
