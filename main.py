import discord
import os
import deezlib

client = discord.Client()

TOKEN = os.environ['TOKEN']
prefix = 'dd'


deezlib = [["deez", "deez nuts!"], ["bofa", "bofa deez nuts!"], ["cd", "c deez nuts!"], ["dragon", "dragon deez nuts on your face!"], ["ligma", "ligma balls!"], ["sugon", "sugon deez nuts!"], ["goblin", "goblin deez nuts!"], ["kenya", "kenya fit deez nuts in your mouth?"], ["sea of thieves", "sea of thieves nuts fit in your mouth"], ["candice", "candice dick fit in your mouth?"], ["slaw bunnies", "slob on deez nuts!"], ["kombucha", "kombucha mouth on deez nuts"], ["tulips", "Put tulips on deez nuts"], ["papapear", "Papapear of deez nuts in your mouth"], ["china", "China fit deez nuts in your mouth"], ["doomah", "Doomah nuts fit in your mouth"], ["Ken", "Ken deez nuts fit in your mouth"], ["luca", "Luca deez nuts"], ["sugma", "sugma nuts"], ["sugoma", "sugonma nuts!"], ["ken", "ken deez nuts fit in your mouth"], ["joe", "joemama"], ["parodies", "pair of deez nuts"]]




@client.event
async def on_message(message):
  
  if message.author == client.user:
    return

  if message.content.lower().startswith(prefix+"LoL online"):

    await message.channel.send("idk")

  for j in deezlib:
    if message.content.lower().__contains__(j[0]):
      await message.channel.send(j[1])


  



@client.event
async def on_connect():
  print('Dr. Deez has arrived. Prepare yourself.')

  


client.run(TOKEN)
