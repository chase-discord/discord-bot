import discord
from commands import subjects
import os
import sys
from logzero import logger

client = discord.Client()


@client.event
async def on_ready():
    logger.info("Logged in as {}".format(client.user))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_split = message.split()
    if message_split[0] == "!c":
        if message_split[1] == "subjects":
            subjects.handle(client, message, message_split)
        else:
            print("return message saying invalid command")


if os.getenv("TOKEN") is None:
    logger.error("Please set the 'TOKEN' environment variable to the Discord token.")
    sys.exit(1)

client.run(os.getenv("TOKEN"))
