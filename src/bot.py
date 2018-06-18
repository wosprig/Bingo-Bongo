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
names = {}
all_aliases = {}
ships = {}
name_list = ""
ship_list = ""

help_text = "`w!fave` __name__ - Finds a random gif of one of `name`'s faves\n" \
            "`w!ship` __shipName__ - Finds a random gif of one of `shipName`\n" \
            "`w!aliases` __name__ - Finds all aliases for `name`."


def init():
    file = open("names.dat", 'r')
    temp = file.read().split('\n')
    global name_list
    for person in temp:
        components = person.split(" ")
        name = components[0]
        alias_list = [name]
        if len(components) > 1:
            alias_list.extend(components[1][1:len(components[1])-1].split(","))
            for alias in alias_list:
                names[alias] = name
        all_aliases[name] = alias_list
        name_list += name.capitalize() + "\n"

    file = open("ships.dat", 'r')
    global ships
    ships = file.read().split('\n')
    global ship_list
    for relationship in ships:
        ship_list += relationship.capitalize() + "\n"


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    init()


@bot.command()
async def aliases(ctx, arg=""):
    if arg.lower() in names.keys():
        name = names.get(arg.lower())
        desc = ""
        for alias in all_aliases.get(name):
            desc += alias.capitalize() + "\n"

        embed = discord.Embed(title=f"Aliases for {arg}", description=desc, color=0x21c6bb)
        await ctx.send(embed=embed)
    elif arg == "":
        await ctx.send("Correct usage is `w!aliases` __name__")
    else:
        await ctx.send("Sorry, I don't recognise that name.")


@bot.command()
async def fave(ctx, arg=""):
    print(names.keys())
    if arg.lower() in names.keys():
        name = names.get(arg.lower())
        file = open(f"images/people/{name}.dat", 'r')
        images = file.read().split('\n')
        np.random.seed(seed=round(time.time()))
        index = np.random.randint(low=0, high=len(images) - 1)
        await ctx.send(images[index])
    elif arg == "":
        await ctx.send("Correct usage is `w!fave` __name__")
    else:
        await ctx.send("Sorry, I don't recognise that name.")


@bot.command()
async def ship(ctx, name=""):
    if name.lower() in ships:
        file = open(f"images/ships/{name.lower()}.dat", 'r')
        images = file.read().split('\n')
        index = np.random.randint(low=0, high=len(images))
        await ctx.send(images[index])
    elif name == "":
        await ctx.send("Correct usage is `w!ship` __name__")
    else:
        await ctx.send("Sorry, I don't recognise that ship.")


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
        embed.add_field(name="__Possible names__", value=name_list, inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'ship':
        await ctx.send("ship `shipName`")
        embed = discord.Embed(description="Sends random image of `shipName`.", color=0xeabd1c)
        await ctx.send(embed=embed)
        embed = discord.Embed(color=0x21c6bb)
        embed.add_field(name="__Possible ships__", value=ship_list, inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def when_mentioned(ctx, cmd: string):
    if cmd == "help":
        help(ctx)


bot.run(os.environ["BOT_TOKEN"])
