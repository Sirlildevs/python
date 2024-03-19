words = ['arse','shithead','shit head','s h i t h e a d','f u c k','s h i t','b i t c h','arsehead', 'arsehole', 'ass', 'asshole', 'bastard', 'bitch', 'bloody', 'bollocks', 'brotherfucker', 'bugger', 'bullshit', 'child-fucker', 'Christ on a bike', 'Christ on a cracker', 'cock', 'cocksucker', 'crap', 'cunt', 'cyka blyat', 'damn', 'damn it', 'dick', 'dickhead', 'dyke', 'fatherfucker', 'frigger', 'fuck', 'goddamn', 'godsdamn', 'hell', 'holy shit', 'horseshit', 'in shit', 'Jesus Christ', 'Jesus fuck', 'Jesus H. Christ', 'Jesus Harold Christ', 'Jesus, Mary and Joseph', 'Jesus wept', 'kike', 'motherfucker', 'nigga', 'nigra', 'pigfucker', 'piss', 'prick', 'pussy', 'shit', 'shit ass', 'shite', 'sisterfucker', 'slut', 'son of a whore', 'son of a bitch', 'spastic', 'sweet Jesus', 'turd', 'twat', 'wanker']








from discord import Client, Intents
from discord.ext import commands
from discord.utils import get
import discord
import views


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


client = Client(intents=intents)
bot = commands.Bot(command_prefix=";", intents=intents)
gamedefult = discord.Game("Watching Fur and Foil Retreat")



@bot.event
async def on_ready():
    print("ready")
    await bot.tree.sync()
    await bot.change_presence(status=discord.Status.online, activity=gamedefult)
    

@bot.hybrid_command()
async def requestroles(ctx):
    view = views.rolesview()
    await ctx.channel.send(embed=views.rolesview.embed , view=view)



        
with open("key.txt", "r") as f:
    key = f.read()
    bot.run(token=key)


