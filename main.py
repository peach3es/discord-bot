import discord 
import os
from dotenv import load_dotenv
from discord.ext import commands

from bot_command import reg_commmands #imports bot commands from bot_command.py

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
bot.add_cog(reg_commmands(bot)) #calls bot commands from another file


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