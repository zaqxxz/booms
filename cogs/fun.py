import discord
import aiohttp
import random
from discord.ext import commands

class Fun(commands.Cog):

  def __init__(self, client):
     self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
        print("fun cmds work")
      
  @commands.command(pass_context=True)
  async def fun(self, ctx, *cog):

      embed = discord.Embed(
        colour = discord.Colour.default()
      )
    
      embed.set_author(name='fun cmds')
      embed.add_field(name='say', value='i mock what you say.', inline=True)
      embed.add_field(name='twerk', value='sends twerk gif.', inline=True)
      embed.add_field(name='meme', value='sends a random meme.', inline=True)
      embed.add_field(name='rate', value='rates how cool you are.' )
      embed.set_image(url="https://images-ext-1.discordapp.net/external/T7sWSm4BiX5ebciMJyaQfOIjJHyLChEwu_P--g9aqRk/https/media.discordapp.net/attachments/859883140423614474/859883158493593600/dividerrr.gif")

      await ctx.send(embed=embed)
  




def setup(client):
    client.add_cog(Fun(client))