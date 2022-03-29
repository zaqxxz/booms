import discord
from discord.ext import commands

class roles(commands.Cog):

  def __init__(self, client):
     self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
     print("role cmds work")

######### XBOX #########
  @commands.command()
  async def x(ctx, member: discord.Member):
   xboxRole = discord.utils.get(ctx.guild.roles, name="Xbox")

   await member.add_roles(xboxRole)
   await member.send(f" you have been given Xbox role in: - {ctx.guild.name}")
   embed = discord.Embed(description=f" {member.mention} was given **Xbox** role.",colour=discord.Colour.blue())
   await ctx.send(embed=embed)












def setup(client):
    client.add_cog(roles(client))