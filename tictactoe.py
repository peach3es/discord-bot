from tkinter import Place
import discord 
from discord.ext import commands
from discord import activity
import random

class tictactoe (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    player1 = ""
    player2 = ""
    turn = ""
    gameOver = True

    board = []

    winning_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]    

    @commands.command(
        name = "tictactoe"
        aliases = ["ttt"]
    )
    async def tictactoe(self, ctx, p1 : discord.Member, p2 : discord.Member):
        global player1
        global player2
        global turn
        global gameOver
        global count
 
        if gameOver:
            global board
            board = ["⬜", "⬜", "⬜",
                     "⬜", "⬜", "⬜",
                     "⬜", "⬜", "⬜"]
            turn = ""
            gameOver = False
            count = 0

            player1 = p1
            player2 = p2

            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]
            
            num = random.randint(1, 2)

            if num == 1:
                turn = player1
                await ctx.send("<@"str(player1.id) + "> starts! You're Xs.")
            elif num == 2:
                turn = player2
                await ctx.send("<@"str(player2.id) + "> starts! You're Xs.")
        else:
            await ctx.send("A game is already started ya goof. Finish that one first please :)")
    
    @commands.command(
        name = "place"
        aliases = ["put"]
    )
    async def place(self, ctx, pos_: int):
        global player1
        global player2
        global turn
        global count
        global board

        if not gameOver:
            mark = ""
            