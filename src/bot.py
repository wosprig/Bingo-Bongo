import os
import string

import discord
from discord.ext import commands
import asyncio
import numpy as np
import time


client = discord.Client()
bot = commands.Bot(command_prefix="w!", description="Just trying this out.")
bot.remove_command('help')
names = {
    'glenna',
    'wo',
    'fi',
    'sci',
    'dream',
    'anon',
    'mystic',
    'cheer'
}
help_text = "`w!fave` __name__ - Finds a random gif of one of `name`'s faves"


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def fave(ctx, name=""):
    if name.lower() in names:
        file = open(f"images/{name.lower()}.dat", 'r')
        images = file.read().split('\n')
    else:
        await ctx.send("Sorry, I don't recognise that name.")
        return

    np.random.seed(seed=round(time.time()))
    index = np.random.randint(low=0, high=len(images)-1)
    await ctx.send(images[index])


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="BingoBongo", description="Wo's trying bots.", color=0x21c6bb)

    # give info about you here
    embed.add_field(name="Author", value="Wosprig")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)


@bot.command()
async def help(ctx, cmd=""):
    if cmd == "":
        await ctx.send("Command prefix: `w!`\n"
                       "You can use `w!help <command_name>` for more detailed help.\n"
                       "__**BingoBongo help**__"
                       )
        embed = discord.Embed(title="__List of commands:__", description=help_text, color=0x21c6bb)
        await ctx.send(embed=embed)
    elif cmd == 'fave':
        await ctx.send("fave `name`")
        embed = discord.Embed(description="Sends random image of `name`'s favourite DCMK character.", color=0xeabd1c)
        await ctx.send(embed=embed)
        embed = discord.Embed(color=0x21c6bb)
        embed.add_field(name="__Possible names__", value="Anon\nCheer\nDream\nFi\nGlenna\nMystic\nSci\nWo", inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def when_mentioned(ctx, cmd: string):
    if cmd == "help":
        help(ctx)


bot.run(os.environ["BOT_TOKEN"])
