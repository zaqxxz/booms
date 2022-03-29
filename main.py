import os
import json
import discord
import sqlite3
import asyncio
import random
import hashlib
import requests
import traceback
import time
import sys
import aiohttp
import subprocess
import json
from discord.ext import commands


intents = discord.Intents.default()
client = commands.Bot(command_prefix = ',', intents = intents, help_command=None)

def info(bot):
  bot.remove_command('help')
  
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Streaming(name=';-;', url='https://www.twitch.tv/zaqxxz'))
  print("==================")
  print("Logged in as")
  print('{}'.format(client.user.name))
  print("{}".format(client.user.id))
  print("==================")
  print('Servers connected to:')
  for guild in client.guilds:
    members = len(guild.members)
    print(f'{guild.name} ({members}) Owner: {guild.owner}')
    print("==================")
    


# Load Cog
@client.command()
@commands.has_role(955175055652954122)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded.')
    print(f'{extension} loaded by {ctx.author}')

# Unload Cog
@client.command()
@commands.has_role(955175055652954122)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} unloaded.')
    print(f'{extension} unloaded by {ctx.author}')

# Reload Cog
@client.command()
@commands.has_role(955175055652954122)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    
    embed = discord.Embed(
      description = f'curse reloaded {extension} cmd.',
      colour = discord.Colour.default()
  )

    await ctx.send(embed=embed)
    print(f'{extension} reloaded by {ctx.author}')

# Restart Bot
import sys
def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command()
@commands.has_role(955175055652954122)
async def restart(ctx):
    
    embed = discord.Embed(
      description = 'brb, curse is restarting bot...',
      colour = discord.Colour.default()\
    )
    await ctx.send(embed=embed)
    restart_bot()

############ UNMUTE ############
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have been unmuted from: - {ctx.guild.name}")
   embed = discord.Embed(description=f" unmuted ~ {member.mention}",colour=discord.Colour.default())
   await ctx.send(embed=embed)

############ MUTE ############
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="muted")

   await member.add_roles(mutedRole)
   await member.send(f" you have been muted from: - {ctx.guild.name}")
   
   embed = discord.Embed(description=f" muted ~ {member.mention}",colour=discord.Colour.default())
   await ctx.send(embed=embed)

############ BAN ############
@client.command()
@commands.has_permissions(ban_members=True)   
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    
    embed = discord.Embed(title="banned", description=f" member ~ {member.mention}",colour=discord.Colour.default())
    await ctx.send(embed=embed)

############ KICK ############
@client.command()
@commands.has_permissions(kick_members=True)   
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    
    embed = discord.Embed(title="kicked", description=f" member ~ {member.mention}",colour=discord.Colour.default())
    await ctx.send(embed=embed)

############ UNBAN ############
@client.command()
@commands.has_permissions(ban_members=True)   
async def unban(ctx, member, id : int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    
    embed = discord.Embed(title="unbanned", description=f" member ~ {member.mention}",colour=discord.Colour.default())
    await ctx.send(embed=embed)


########### AVATAR ###########
@client.command(aliases=['avatar'])
async def av(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    embed=discord.Embed(title=f'{avamember}\'s avatar', inline=False)
    embed.set_image(url=userAvatarUrl)
    await ctx.send(embed=embed)

########### MEMBER COUNT ############
@client.command(aliases=["mc"])
async def membercount(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"members",description=a,color=discord.Color((0)))
    await ctx.send(embed=b)

########## SAY ############
@client.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)

########## PURGE ###########
@client.command(aliases=['p'])
@commands.has_permissions(manage_messages=True)
async def purge(context, amount=5):
    await context.channel.purge(limit=amount+1)

########### PING #############
@client.command()
async def ping(ctx):

    embed = discord.Embed(
      colour = discord.Colour.default()
    )

    embed.add_field(name=f'pong', value=f'``latensy is {round(client.latency * 1000)}ms``')
    await ctx.send(embed=embed)

######### Roles ############
@client.command()
async def xbox(ctx, member: discord.Member):
   xboxRole = discord.utils.get(ctx.guild.roles, name="Xbox")

   await member.add_roles(xboxRole)
   await member.send(f" you have been given Xbox role in: - {ctx.guild.name}")
   embed = discord.Embed(description=f" {member.mention} was given **Xbox** role.",colour=discord.Colour.default())
   await ctx.send(embed=embed)

########## TWERK #############
twerk_gifs = ['https://i.kym-cdn.com/entries/icons/original/000/012/061/tumblr_m8718gBJWN1qgpx0l.gif', 'https://media0.giphy.com/media/gnE9JR4OxfLig/200w.gif?cid=82a1493bjhw4nhbslk1y1zka6vkbex17uqomsumxkxgpbmya&rid=200w.gif&ct=g', 'https://static.wikia.nocookie.net/degrassi/images/7/77/A09je5d_460sa.gif/revision/latest/scale-to-width-down/245?cb=20140615230310', 'https://c.tenor.com/PZFkE6MFC3sAAAAM/twerk-princejoy.gif', 'https://i.pinimg.com/originals/70/da/a1/70daa116465172ba48b1c3803ec8ab78.gif', 'https://c.tenor.com/YEdq5ZDPXH8AAAAd/twerk-twerking.gif', 'https://c.tenor.com/ibcN1Kvh1ucAAAAd/twerk-twerking.gif', 'https://c.tenor.com/3NTa3Xj7N4cAAAAM/twerking-twerk.gif', 'https://c.tenor.com/oZ-5pHxZcpAAAAAM/twerking-dance.gif', 'https://c.tenor.com/6vmDDkUAkxQAAAAd/twerk-twerking.gif', 'https://c.tenor.com/7H3f1ft63KkAAAAC/dog-twerk.gif' ]

@client.command()
async def twerk(ctx, *cog):
  
  embed = discord.Embed(
        colour = discord.Colour.default()
      )

  embed.set_image(url=(random.choice(twerk_gifs)))

  await ctx.send(embed=embed)

########## MEME ############
memes_1 = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWr44lDchlTJcyCU95a8M4jSVX9qIyuznoLQ&usqp=CAU', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPrmwE_GcI7HDcN9ik5OUR88XYoLReQMJNXw&usqp=CAU', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXTzlWhNlS67tIYsv2iBwEwLlzrmaVTS4UOw&usqp=CAU', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF1yQD-CHs5hRfeDtaf5QLCABvAXLlhuYmIw&usqp=CAU', 'https://i.inews.co.uk/content/uploads/2018/05/CaTFfjhrxRFV1NpMcQvYFPxVl7lVFBAmt9tkPkfqanE.jpg', 'https://filmdaily.co/wp-content/uploads/2020/06/darkmeme-01.jpg']
@client.command()
async def meme(ctx, *cog):
  
  embed = discord.Embed(
        colour = discord.Colour.default()
      )

  embed.set_image(url=(random.choice(memes_1)))

  await ctx.send(embed=embed)
########## SNIPE ############
snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command(aliases=['s'])
async def snipe(ctx):
    channel = ctx.channel
    try: 
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await sleep(60)
        await ctx.send(embed = em)
    except KeyError: 
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")

        


########### RATE ##########
@client.command()
async def rate(ctx):
      
    embed = discord.Embed(
        colour = discord.Colour.default()
      )

    embed=discord.Embed(description=f'You are {random.randrange(101)}% cool.')
    
    await ctx.send(embed=embed)





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('OTU1NjEwNzUzOTgzOTkxODQ4.YjkL3g.8iveYy9I3Sict0sThccEY1Zmglo')