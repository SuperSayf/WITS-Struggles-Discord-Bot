import discord
import os
from discord.ext import commands
from discord_components import *
from prsaw import RandomStuffV2

###########################################################################################

activity = discord.Activity(type=discord.ActivityType.watching, name="|help")

intents = discord.Intents.default() 
intents.members = True

bot = commands.Bot(command_prefix="|", intents=intents, activity=activity,
                   status=discord.Status.online)

bot.remove_command('help')

###########################################################################################

cogs = ["cogs.ping","cogs.rip.rip","cogs.levelsys","cogs.rps"]


@bot.event
async def on_ready():
    DiscordComponents(bot)
    print('WITS 2.0 Bot is online')
    print("Loading cogs . . .")
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(cog + " was loaded.")
        except Exception as e:
            print(e)

###########################################################################################

rs = RandomStuffV2(async_mode = True)

no_Talk_Chanels = [819927672477450283,820009033703882792,820687219568017459,821088628431257600]

@bot.event
async def on_message(message):
    if bot.user == message.author:
        return
    if message.channel.id in no_Talk_Chanels:
        return
    if bot.user.mentioned_in(message):
        response = await rs.get_ai_response(message.content)
        await message.reply(response)
    await bot.process_commands(message)

###########################################################################################

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name='Help')
    embed.add_field(name='|ping', value='Returns Pong!', inline=False)
    embed.add_field(
        name='|rip', value='Returns a gravestone image embedded with your pfp', inline=False)
    embed.add_field(name='|rip @user',
                    value='Returns a gravestone image embedded with the mentioned pfp', inline=False)
    embed.add_field(name='|rank', value='Returns your current rank in the server', inline=False)
    embed.add_field(name='|leaderboard', value='Returns a list of the top ranking people in the server', inline=False)
    embed.add_field(name='|rps', value='Play Rock, Paper and Scissors with the bot using buttons', inline=False)
    embed.add_field(name="**@WITS 2.0** example", value='The bot will respond to anything you say/ask', inline=False)

    await author.send(embed=embed)
    await ctx.send(f"{author.mention} check your DMs!")

###########################################################################################

bot.run("***REMOVED***")
