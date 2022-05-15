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

hello = [
    "hello",
    "Hi",
    "sup"
]

heads = [
    "heads",
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

    if message.content.startswith(".help"):
        embed = discord.Embed(title="__Commands__", color=0x00ff00)
        embed.add_field(name=".help", value="Shows this message")
        embed.add_field(name=".ping", value="replies with pong")
        embed.add_field(name=".say", value="make the bot say something")
        await message.channel.send(content=None, embed=embed)

    if message.content.startswith("hello"):
        channel = message.channel
        await channel.send("hey \n"
                            "do you want to play heads or tails? \n")

        def check(m):
            return m.content in ("yes", "sure", "Yes", "Sure",)

        msg = await client.wait_for('message', check=check)
        await channel.send("Ok \n"
                           "i pick \n")
        await channel.send(random.choice(heads))
        await channel.send("the winner is...")
        await channel.send(random.choice(heads))

@client.event
async def on_ready():
    print("RUNNING")

client.run(TOKEN)
print(client.user.name)
