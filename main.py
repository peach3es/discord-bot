import discord #discord package
from discord.ui import button
from discord.ext  import commands
client = discord.Client() #client

@client.event
async def on_ready():
#bot's content
  testing_channel = client.get_channel(980145563326644255)

  await testing_channel.send("You turned me on ;P")
#Run client on server
client.run('OTgwMTQ2NTEyODc5MzE3MDIy.GZfrmU.iI40W1SagHrEiO0T-aijZT_rF3Mgcn35vL0ZW0')


