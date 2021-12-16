import discord
import os
import deezlib

client = discord.Client()

TOKEN = os.environ.get(TOKEN)
prefix = 'dd'





@client.event
async def on_message(message):
  
  if message.author == client.user:
    return

  if message.content.lower().startswith(prefix+"LoL online"):

    await message.channel.send("idk")

  for j in deezlib.replies:
    if message.content.lower().__contains__(j[0]):
      await message.channel.send(j[1])


  



@client.event
async def on_connect():
  print('Dr. Deez has arrived. Prepare yourself.')

  


client.run(TOKEN)
