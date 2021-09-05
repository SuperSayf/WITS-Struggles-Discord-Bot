import discord
import os
from discord.ext import commands
from discord_components import *
from prsaw import RandomStuffV2
import pyrebase
import time
from random import randint

###########################################################################################

activity = discord.Activity(type=discord.ActivityType.watching, name="|help")

intents = discord.Intents.default() 
intents.members = True

bot = commands.Bot(command_prefix="|", intents=intents, activity=activity,
                   status=discord.Status.online)

bot.remove_command('help')

###########################################################################################

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'singapore'
    }
]

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
bot.load_extension('dismusic')

###########################################################################################

rs = RandomStuffV2() 

no_Talk_Chanels = [819927672477450283,820009033703882792,820687219568017459,821088628431257600]
Talk_Chanels = [857618527825559563]

#Initialize Firebase
firebaseConfig={
  "apiKey": "***REMOVED***",
  "authDomain": "***REMOVED***",
  "databaseURL": "***REMOVED***",
  "projectId": "***REMOVED***",
  "storageBucket": "***REMOVED***.appspot.com",
  "messagingSenderId": "***REMOVED***",
  "appId": "1:***REMOVED***:web:4613b01fc6286a9d71c6ea",
  "measurementId": "***REMOVED***"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

@bot.event
async def on_message(message):
    if bot.user == message.author:
        return
    if message.webhook_id:
        return
    if message.channel.id in no_Talk_Chanels:
        return
    if bot.user.mentioned_in(message):
        response = await rs.get_ai_response(message.content)
        await message.reply(response)
    else:
        if message.channel.id in Talk_Chanels:
            data = {"UserMessage":message.content,"Username":message.author.name + " (Discord)"}
            db.child("Messages").child(str(round(time.time()))+"-"+str(randint(10, 9999999))).set(data)
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
