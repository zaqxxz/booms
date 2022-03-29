import discord
from discord.ext import commands

class Example(commands.Cog):

  def __init__(self, client):
     self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
     print("support cmd works")

  @commands.command(pass_context=True)
  async def support(self, ctx, *cog):

    embed = discord.Embed(
      colour = discord.Colour.default()
    )
    
    embed.set_author(name='bot support')
    embed.add_field(name='Curse', value='*curse#6666*', inline=True)
    embed.set_image(url="https://cdn.discordapp.com/attachments/940294860269821962/940366922212605972/IMG_4404.gif")

    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Example(client))