from tkinter import Label
import discord
from discord import activity
from discord.ui import Button, View
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
            description = "Use `#help <command>` for more info"
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
        hembed.add_field(name = "Aliases", value = "`#HELP`, `#Help`")
        await ctx.channel.send(embed = hembed)
        
    @help.command(
            name = "gamelist"
        )
    async def _gamelist(self, ctx):
        gembed = discord.Embed(
            title = "#gamelist",
            colour = discord.Colour(0xbc708f),
            description = "Shows the list of available games menu"
        )
        gembed.set_footer(text = "🏆 1V1")
        gembed.add_field(name = "Aliases", value = "`#g`, `#game`, `list`")
        await ctx.channel.send(embed = gembed)

    @help.command(
            name = "leaderboard"
        )
    async def _leaderboard(self, ctx):
        lembed = discord.Embed(
            title = "#leaderboard",
            colour = discord.Colour(0xbc708f),
            description = "Shows the top 5 placement in the server"
        )
        lembed.set_footer(text = "🏆 1V1")
        lembed.add_field(name = "Aliases", value = "`#rank`, `#placement`")
        await ctx.channel.send(embed = lembed)        

    @commands.command(  
        name = "leaderboard",
        aliases = ["score", "rank", "placement"]
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
    
    @commands.command(
        name = "duel",
        aliases = ["fight"]
    )
    async def duel(self, ctx):
        buttonAccept = Button(label = "Accept", style = discord.ButtonStyle.green, emoji = "⚔️")
        buttonDecline = Button(label = "Decline", style = discord.ButtonStyle.danger, emoji = "🛡️")

        view = View()
        view.add_items(buttonAccept)
        view.add_items(buttonDecline)
        await ctx.channel.send("Would you like the accept the challenge?", view = view)
