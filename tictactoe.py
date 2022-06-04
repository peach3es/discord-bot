import discord 
from discord.ext import commands
from discord import activity

class tictactoe (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(
        name = "tictactoe"
        aliases = ["ttt"]
    )
    async def tictactoe(self, ctx):
