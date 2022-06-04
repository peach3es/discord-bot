import discord
from discord import activity
from discord.ext import commands

class reg_commmands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity = discord.Game("I'm gay"))
        print("The bot is ready")

    # @commands.Cog.listener() <-- this part is broken
    # async def on_message(message, self):
    #   if message.author == self.user:
    #     return
    #   print("mails")
    #   await self.process_commands(message)

    @commands.command(
        help = "Shows the user the list of available games",
        name = "gamelist",
        aliases = ["game", "g", "Gamelist", "game list", "list", "play"]
        )
    async def gamelist(self, ctx):
        myembed = discord.Embed(
            title="Game List", 
            colour=discord.Colour(0xbc708f),
            description="**Select the game you would like to play:**")

        #myembed.set_author(name = "1V1")
        myembed.set_footer(text="🏆 1V1")
        myembed.add_field(name="Tic Tac Toe", value="A classic 1 vs 1 game where you need to place 3 of your marks" 
                                                    " in horizontal, vertical, or diagonal to win"
                                                    "\nTo play, type: ```#tictactoe @mention```", inline = False)
        myembed.add_field(name = "Connect 4", value = "A classic 1 vs 1 game where you need to connect 4 of your checkers in a row to win"
                                                    "\nTo play, type: ```#connect4 @mention```", inline = False)
        
        await ctx.channel.send(embed = myembed)

    @commands.group(
        name = "help",
        aliases = ["HELP", "Help"],
        invoke_without_command = True
        )
    async def help(self, ctx):
        helpembed = discord.Embed(
            title = "Help Commands",
            colour = discord.Colour(0xbc708f),
            description = "All available commands for this bot:"
            )
        
        #helpembed.set_author(name = "1V1")
        helpembed.set_footer(text = "🏆 1V1")
        helpembed.add_field(name="Game List", value="`#gamelist`", inline=True)
        helpembed.add_field(name="Help", value="`#help`", inline=True)
        helpembed.add_field(name="Leaderboard", value="`#leaderboard`", inline=True)

        await ctx.channel.send(embed = helpembed)

    @help.command(
        name = "help"
    )
    async def _help(self, ctx):
        hembed = discord.Embed(
            title = "#help",
            colour = discord.Colour(0xbc708f),
            description = "Shows the help menu"
        )
        hembed.set_footer(text = "🏆 1V1")
        await ctx.channel.send(embed = hembed)

    @commands.command(  
        name = "leaderboard",
        aliases = ["score"],
        help = "Show user the top 5 placement in the server"
        )
    async def leaderboard(self, ctx):
        Lembed = discord.Embed(
            title = "Leaderboard",
            colour = discord.Colour(0xbc708f) 
        )   

        #Lembed.set_author(name = "1V1")
        Lembed.set_footer(text = "🏆 1V1")
        Lembed.add_field(name = "First place 🥇 : ", value = "peaches", inline = False)
        Lembed.add_field(name = "Second place 🥈 : ", value = "bongesquab quarespants", inline = False)
        Lembed.add_field(name = "Third place 🥉 : ", value = "-", inline = False)
        Lembed.add_field(name = "Fourth place: ", value = "-", inline = False)
        Lembed.add_field(name = "Fifth place: ", value = "-", inline = False)

        await ctx.channel.send(embed = Lembed)
