from discord.ext import commands
import os
import sys
from logzero import logger

# Create the bot instance
bot = commands.Bot(command_prefix="!")


# Once the bot is ready
@bot.event
async def on_ready():
    # Print a message to the log with the bot username
    logger.info("Logged in as {}".format(bot.user))


# Check that the bot token is in an environment variable
if os.getenv("TOKEN") is None:
    logger.error("Please set the 'TOKEN' environment variable to the Discord" +
                 "token.")
    sys.exit(1)

count = 0

# For each of the files in the 'cogs' directory
for file in os.listdir("cogs"):
    # If it is a Python file
    if file.endswith(".py"):
        count += 1
        # Load the file into the bot instance
        bot.load_extension("cogs.{}".format(file[:-3]))

logger.info("Loaded {} cog(s)".format(count))

# Start running the bot with the bot token environment variable
bot.run(os.getenv("TOKEN"))
