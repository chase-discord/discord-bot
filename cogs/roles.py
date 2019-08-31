from discord.ext import commands
import discord
from discord.ext.commands import MissingRequiredArgument


def get_allowed_roles(ctx, bot):
    available_roles = ctx.guild.roles
    bot_roles = ctx.guild.get_member(bot.user.id).roles
    output = []

    available_roles.pop(0)
    bot_roles.pop(0)

    for role in available_roles:
        if role in bot_roles:
            break
        output.append(role)

    return output


def get_role_by_name(role_name, ctx, bot):
    role_list = get_allowed_roles(ctx, bot)
    role_name = role_name.lower().trim()

    if role_name not in [r.name for r in role_list]:
        await ctx.send("❌ Sorry, that role wasn't found!")
        return

    return next((r for r in role_list if r.name == role_name), None)


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def roles(self, ctx):
        """List all of the available roles in the server"""
        role_list = get_allowed_roles(ctx, self.bot)

        await ctx.send("Here are available roles to join: {}\n\n_Use the `{}` command to join one of these roles._".format(", ".join(["`{}`".format(r.name.lower()) for r in role_list]), ctx.bot.command_prefix + "join"))

    @commands.command()
    @commands.guild_only()
    async def join(self, ctx, arg_role):
        """Join a role in the server"""
        role = get_role_by_name(arg_role, ctx, self.bot)

        try:
            await ctx.author.add_roles(role, reason="Automated Role")
        except discord.errors.Forbidden:
            await ctx.send("❌ Whoops! There was a problem giving that role!")
            return

        await ctx.send("✔️ Your roles have been updated!")

    @commands.command()
    @commands.guild_only()
    async def leave(self, ctx, arg_role):
        """Leave a role in the server"""
        role = get_role_by_name(arg_role, ctx, self.bot)

        await ctx.author.remove_roles(role, reason="Automated Role")
        await ctx.send("✔️ Your roles have been updated!")

    @join.error
    @leave.error
    async def role_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("⚠️ Make sure you add a role after the command (e.g `!join maths`)")


def setup(bot):
    bot.add_cog(Roles(bot))
