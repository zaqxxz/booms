import discord
from discord.ext import commands

class Moderation(commands.Cog):

  def __init__(self, client):
     self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
     print("mod cmds work")

  @commands.command(aliases=['mod'], pass_context=True)
  async def moderation(self, ctx, *cog):

      embed = discord.Embed(
        colour = discord.Colour.default()
      )
    
      embed.set_author(name='mod cmds')
      embed.add_field(name='mute', value='mutes mentioned user.', inline=True)
      embed.add_field(name='unmute', value='unmutes mentioned user.', inline=True)
      embed.add_field(name='ban', value='bans mentioned user.', inline=True)
      embed.add_field(name='unban', value='unbans mentioned user.', inline=True)
      embed.add_field(name='kick', value='kicks mentioned user.', inline=True)
      embed.set_image(url="https://images-ext-1.discordapp.net/external/T7sWSm4BiX5ebciMJyaQfOIjJHyLChEwu_P--g9aqRk/https/media.discordapp.net/attachments/859883140423614474/859883158493593600/dividerrr.gif")

      await ctx.send(embed=embed)







def setup(client):
    client.add_cog(Moderation(client))