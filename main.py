import discord 
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
discord_token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
  command_prefix = '#',
  help_command = None,
  # help_command = commands.DefaultHelpCommand(no_category="#play commands"),
  intents = intents
)

# @bot.event
# async def on_ready():
#   print("The bot is ready")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  print("mails")
  await bot.process_commands(message)

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'modules.{extension}')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'modules.{extension}')

for filename in os.listdir('./modules'):
  if filename.endswith('.py'):
    bot.load_extension(f'modules.{filename[:-3]}')

# @bot.command(
#   help = "Shows the user the bot's list of games",
#   name = "gamelist",
#   aliases = ["game", "g", "Gamelist", "game list", "list", "play"]
# )
# async def gamelist(ctx):
#   myembed = discord.Embed(
#     title="Game List", 
#     colour=discord.Colour(0xbc708f),
#     description="**Select the game you would like to play:**")

#   #myembed.set_author(name = "1V1")
#   myembed.set_footer(text="1V1")
#   myembed.add_field(name="Tic Tac Toe", value="A classic game of tic tac toe to play with your friends (1 vs 1) \nTo play, type: ```#tictactoe @mention```")
  
#   await ctx.channel.send(embed = myembed)
  
@bot.command(
  name = "help",
  aliases = ["HELP", "Help"]
)
async def help(ctx):
  helpembed = discord.Embed(
    title = "Help Commands",
    colour = discord.Colour(0xbc708f),
    description = "All available commands for this bot:")
  
  #helpembed.set_author(name = "1V1")
  helpembed.set_footer(text = "1V1")
  helpembed.add_field(name="Game List", value="`#gamelist\n\naliases:\n - #g\n - #game\n - #play`", inline=True)
  helpembed.add_field(name="Help", value="`#help`", inline=True)
  helpembed.add_field(name="Leaderboard", value="`#leaderboard`\n\n aliases:\n - #score", inline=True)

  await ctx.channel.send(embed = helpembed)

@bot.command(  
  name = "leaderboard",
  aliases = ["score"],
  help = "Show user placement in the server"
)
async def leaderboard(ctx):
  Lembed = discord.Embed(
    title = "Leaderboard",
    colour = discord.Colour(0xbc708f) 
  )   

  #Lembed.set_author(name = "1V1")
  Lembed.set_footer(text = "1V1")
  Lembed.add_field(name = "First place 🥇 : ", value = "peaches", inline = False)
  Lembed.add_field(name = "Second place 🥈 : ", value = "bongesquab quarespants", inline = False)
  Lembed.add_field(name = "Third place 🥉 : ", value = "-", inline = False)
  Lembed.add_field(name = "Fourth place: ", value = "-", inline = False)
  Lembed.add_field(name = "Fifth place: ", value = "-", inline = False)

  await ctx.channel.send(embed = Lembed)


# @bot.command(
#   name = "tictactoe",

# duel system here

#tictactoe code here
# )

@bot.command(
  name = "connect4",
  aliases = ["con4", "c4"],
  help = "This command allows user to play a game of connect 4"
)
async def connect(ctx):
  Cembed = discord.Embed(
    title = "Connect 4",
    colour = discord.Colour(0xbc708f)
  )

  await ctx.channel.send (embed = Cembed)
  
bot.run(discord_token)