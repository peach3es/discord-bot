import discord 
#from discord.ui import button
from discord.ext  import commands
# client = discord.Client() #client

TOKEN = "OTgwMTQ2NTEyODc5MzE3MDIy.GZfrmU.iI40W1SagHrEiO0T-aijZT_rF3Mgcn35vL0ZW0"

bot = commands.Bot(command_prefix = '_')

@bot.event
async def on_ready():
  testing_channel = bot.get_channel(980145563326644255)
  await testing_channel.send("I'm turned on ;P")

@bot.command(pass_context = True)
async def play(ctx):
#bot's content
  myembed = discord.Embed(
    title="Game List", 
    colour=discord.Colour(0xbc708f),
    description="Select the game you would like to play:")

  myembed.set_author(name="#play", url="https://discordapp.com")
  myembed.set_footer(text="#play")
  myembed.add_field(name="Tic Tac Toe", value="A classic game of tic tac toe to play with your friends (1 vs 1) ```#play tictactoe @mention```")

  await ctx.send(embed=myembed)
#Run client on server
bot.run(TOKEN)


