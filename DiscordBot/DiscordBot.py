import discord
import random
import time
import asyncio

TOKEN = "OTUzNzU5NDM2MDIxODM3ODU2.YjJPsQ.X6oAFSlB-OkLUIu4gGO0fkszJ9k"

client = discord.Client()

responses = [
    "No",
    "Yes",
    "My sources say no",
    "It seems likely"
]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(".ping"):
        await message.channel.send("pong")

    if message.content.startswith(".say"):
        mes = message.content.split()
        output = ""
        for word in mes[1:]:
            output += word
            output += " "
        await message.channel.send(output)
        await message.delete()

    if message.content.startswith(".8ball"):
        await message.channel.send(random.choice(responses))

@client.event
async def on_ready():
    print("RUNNING")

client.run(TOKEN)
print(client.user.name)

