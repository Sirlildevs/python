from discord import Client, Intents
from discord.ext import commands
from discord.utils import get
import discord
import views


intents = discord.Intents.all()
Intents.message_content = True
client = Client(intents=intents)
bot = commands.Bot(command_prefix=";", intents=intents)
gamedefult = discord.Game("-----")


            


@bot.event
async def on_ready():
    print("ready")
    await bot.change_presence(status=discord.Status.online, activity=gamedefult)
   

@bot.command()
async def ping(ctx):
   view = views.pingview()
   await ctx.channel.send(view=view)

@bot.command()
async def requestrole(ctx):
    view = views.rolesview()
    await ctx.channel.send(embed=views.rolesview.embed , view=view)

@bot.command()
async def status(ctx, activity:str):
    game = discord.Game(activity)
    await bot.change_presence(status=discord.Status.online, activity=game)

with open("key.txt", "r") as f:
    key = f.read()
    bot.run(token=key)


