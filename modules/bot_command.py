import discord
from discord.ext import commands

class Bot_Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("The bot is ready")

    @commands.command()
    async def gamelist(self, ctx):
        myembed = discord.Embed(
            title="Game List", 
            colour=discord.Colour(0xbc708f),
            description="**Select the game you would like to play:**")

        #myembed.set_author(name = "1V1")
        myembed.set_footer(text="1V1")
        myembed.add_field(name="Tic Tac Toe", value="A classic game of tic tac toe to play with your friends (1 vs 1) \nTo play, type: ```#tictactoe @mention```")
        
        await ctx.channel.send(embed = myembed)
def setup(bot):
    bot.add_cog(Bot_Command(bot))