from discord.ext import commands
import os
import sys
from logzero import logger

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    logger.info("Logged in as {}".format(bot.user))


if os.getenv("TOKEN") is None:
    logger.error("Please set the 'TOKEN' environment variable to the Discord" +
                 "token.")
    sys.exit(1)

count = 0

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        count += 1
        bot.load_extension("cogs.{}".format(file[:-3]))

logger.info("Loaded {} cog(s)".format(count))

bot.run(os.getenv("TOKEN"))
