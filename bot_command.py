import discord
from discord import activity
from discord.ext import commands

class reg_commmands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = "your bs"))
        print("The bot is ready")

    # @commands.Cog.listener() <-- this part is broken
    # async def on_message(message, self):
    #   if message.author == self.user:
    #     return
    #   print("mails")
    #   await self.process_commands(message)

    @commands.command(
        help = "Shows the user the bot's list of games",
        name = "gamelist",
        aliases = ["game", "g", "Gamelist", "game list", "list", "play"]
        )
    async def gamelist(self, ctx):
        myembed = discord.Embed(
            title="Game List", 
            colour=discord.Colour(0xbc708f),
            description="**Select the game you would like to play:**")

        #myembed.set_author(name = "1V1")
        myembed.set_footer(text="1V1")
        myembed.add_field(name="Tic Tac Toe", value="A classic game of tic tac toe to play with your friends (1 vs 1) \nTo play, type: ```#tictactoe @mention```")
        
        await ctx.channel.send(embed = myembed)

    @commands.command(
        name = "help",
        aliases = ["HELP", "Help"]
        )
    async def help(self, ctx):
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

    @commands.command(  
        name = "leaderboard",
        aliases = ["score"],
        help = "Show user placement in the server"
        )
    async def leaderboard(self, ctx):
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
