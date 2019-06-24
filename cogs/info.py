from discord.ext import commands
import discord
import time


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Pong!"""
        before = time.monotonic()
        message = await ctx.send("Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content="Pong -> **{}ms**".format(round(ping, 2)))

    @commands.command(aliases=["join"])
    async def invite(self, ctx):
        """Send bot invite link"""
        await ctx.send("🌐 Invite me to your Discord server using this URL:\n" +
                       "<{}>".format(
                           discord.utils.oauth_url(self.bot.user.id)))

    @commands.command(aliases=["info"])
    async def about(self, ctx):
        """About the bot"""
        embed = discord.Embed(title="About Chase Discord Bot")
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="Servers", value=len(ctx.bot.guilds), inline=True)
        embed.add_field(name="Commands Loaded", value=len(
            [x.name for x in self.bot.commands]), inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
