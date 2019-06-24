import discord
import aiohttp

#================
from commands import subjects

#================

f = open("token.txt", "r")
token = f.read()
print(token)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_split = message.split()
    if message_split[0] == "!c":
        if message_split[1] == "subjects":
            subjects.handle(client, message, message_split)
        else
            print("return message saying invalid command")
    

client.run(token)
