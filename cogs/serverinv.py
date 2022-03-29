import discord
from discord.ext import commands

class Example(commands.Cog):

  def __init__(self, client):
     self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
     print("server cmd works")

  @commands.command(pass_context=True)
  async def serverinv(self, ctx, *cog):

    embed = discord.Embed(
      title = '/brixton inv',
      description = '*https://discord.gg/brixton*',
      colour = discord.Colour.default()
    )
    
    embed.set_image(url="https://images-ext-1.discordapp.net/external/T7sWSm4BiX5ebciMJyaQfOIjJHyLChEwu_P--g9aqRk/https/media.discordapp.net/attachments/859883140423614474/859883158493593600/dividerrr.gif")

    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Example(client))