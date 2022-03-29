import discord
from discord.ext import commands

class Utility(commands.Cog):

  def __init__(self, client):
     self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
     print("utility cmds work")

  @commands.command(aliases=['util'], pass_context=True)
  async def utility(self, ctx, *cog):

      embed = discord.Embed(
        colour = discord.Colour.default()
      )
    
      embed.set_author(name='util cmds')
      embed.add_field(name='serverinv', value='sends our current invite to our server.', inline=True)
      embed.add_field(name='avatar', value='sends a mentioned users profile picture.', inline=True)
      embed.add_field(name='membercount', value='sends our server member count.', inline=True)
      embed.add_field(name='purge', value='deletes selected amount of messages from a channel.', inline=True)
      embed.add_field(name='ping', value='sends the bot latency.', inline=True)
      embed.add_field(name='snipe', value='shows most recent deleted message.', inline=True)
      embed.set_image(url="https://images-ext-1.discordapp.net/external/T7sWSm4BiX5ebciMJyaQfOIjJHyLChEwu_P--g9aqRk/https/media.discordapp.net/attachments/859883140423614474/859883158493593600/dividerrr.gif")

      await ctx.send(embed=embed)







def setup(client):
    client.add_cog(Utility(client))