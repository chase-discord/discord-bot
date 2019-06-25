from discord.ext import commands
import discord


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def roles(self, ctx):
        """List all of the available roles in the server"""
        print()
        await ctx.send("Here are available roles to join: {}\n\n_Use the `{}` command to join one of these roles._".format(", ".join(["`{}`".format(r.name) for r in ctx.guild.roles]), ctx.bot.command_prefix + "join"))

    @commands.command()
    @commands.guild_only()
    async def join(self, ctx, arg_role):
        """Join a role in the server"""
        if arg_role not in [r.name for r in ctx.guild.roles]:
            await ctx.send("❌ Sorry, that role wasn't found!")
            return

        role = next((r for r in ctx.guild.roles if r.name == arg_role), None)

        await ctx.author.add_roles(role, reason="Automated Role")
        await ctx.send("✔️ Your roles have been updated!")
    
    @commands.command()
    @commands.guild_only()
    async def leave(self, ctx, arg_role):
        """Leave a role in the server"""
        if arg_role not in [r.name for r in ctx.guild.roles]:
            await ctx.send("❌ Sorry, that role wasn't found!")
            return
        
        role = next((r for r in ctx.guild.roles if r.name == arg_role), None)

        await ctx.author.remove_roles(role, reason="Automated Role")
        await ctx.send("✔️ Your roles have been updated!")


def setup(bot):
    bot.add_cog(Roles(bot))
