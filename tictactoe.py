import discord 
from discord.ext import commands
from discord import activity
import random

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

def checkWinner(winning_conditions, mark):
    for condition in winning_conditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            return True     #gameOver is True if any winning combo is found
    return False            #If not found, gameOver is false (game is still being played)

class tictactoe (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name = "tictactoe",
        aliases = ["ttt"]
    )
    async def tictactoe(self, ctx, p2 : discord.Member):
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

            player1 = ctx.author
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
                await ctx.send("<@" + str(player1.id) + "> starts!")
            elif num == 2:
                turn = player2
                await ctx.send("<@" + str(player2.id) + "> starts!")
        else:
            await ctx.send("A game is already started ya goof. Finish that one first please 😃")
    
    @commands.command(
        name = "place",
        aliases = ["put"]
    )
    async def place(self, ctx, pos : int):
        global player1
        global player2
        global turn
        global count
        global board
        global gameOver
        global winning_conditions

        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:" 
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == "⬜":
                    board[pos - 1] = mark
                    count += 1

                    #print the board after the move is made
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]
                    
                    #function to check if someone won
                    gameOver = checkWinner(winning_conditions, mark)

                    #declare winner or tie
                    if gameOver:
                        if turn == player1:
                            await ctx.send("<@" + str(player1.id) + "> wins! 🎉") 
                        elif turn == player2:
                            await ctx.send("<@" + str(player2.id) + "> wins! 🎉")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("It's a tie, ggwp 🤝")

                    #change turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                    


                else:
                    await ctx.send("Please use a position from 1-9 designating an empty spot.")
            else:
                await ctx.send("Dude, wait your turn 😡")    
        else:
            await ctx.send("Start a game to place a piece, silly. Use ```#tictactoe @player2```")

# IMPLEMENT ERROR HANDLING!!!!!
# @tictactoe.error()