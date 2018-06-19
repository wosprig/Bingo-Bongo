import numpy as np
import os

import discord
from discord.ext import commands

import constants
import data
import utils

client = discord.Client()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('w!'), description=constants.DESCRIPTION)
bot.remove_command('help')
values = data.Data()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(aliases=["alias"])
async def aliases(ctx, *args):
    if len(args) == 0:
        await ctx.send("Correct usage is `w!aliases` __name__")
        return

    arg = " ".join(args)

    if arg.lower() in values.names.keys() or arg.lower() in values.ships.keys():
        desc = values.getaliases(arg)
        arg = arg.capitalize()
        embed = discord.Embed(title=f"Aliases for {arg}", description=desc, color=0x21c6bb)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Sorry, I don't recognise that name.")


@bot.command(aliases=["faves"])
async def fave(ctx, *args):
    if len(args) == 0:
        await ctx.send("Correct usage is `w!fave` __name__")
        return

    arg = " ".join(args)
    if arg.lower() in values.names.keys():
        name = values.names.get(arg.lower())
        filename = name.lower()
    else:
        filename = "mystic"
        # await ctx.send("Sorry, I don't recognise that name.")

    image = utils.random_from_file(f"images/people/{filename}.dat")
    await ctx.send(image)


@bot.command()
async def ship(ctx, *args):
    if len(args) == 0:
        await ctx.send("Correct usage is `w!ship` __name__")
        return

    arg = " ".join(args)

    if arg.lower() in values.ships:
        name = values.ships.get(arg.lower())
        image = utils.random_from_file(f"images/ships/{name.lower()}.dat")
        await ctx.send(image)
    else:
        await ctx.send("Sorry, I don't recognise that ship.")


@bot.command()
async def random(ctx):
    all_names = values.ship_aliases.keys() + values.all_aliases.keys()
    rand = np.random.randint(0, len(all_names))
    filename = all_names[rand]
    if filename in values.ship_aliases.keys():
        image = utils.random_from_file(f"images/ships/{filename.lower()}.dat")
    else:
        image = utils.random_from_file(f"images/people/{filename.lower()}.dat")
    await ctx.send(image)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="BingoBongo", description=constants.DESCRIPTION, color=constants.MAIN_COLOUR)

    # give info about you here
    embed.add_field(name="Author", value="Wosprig")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f'{len(bot.guilds)}')

    # give users a link to invite this bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)


@bot.command()
async def help(ctx, cmd=""):
    if cmd == "":
        await ctx.send(constants.HELP_PREFIX)
        embed = discord.Embed(title="__List of commands:__", description=constants.COMMAND_LIST, color=constants.MAIN_COLOUR)
        await ctx.send(embed=embed)
    elif cmd == 'fave':
        await ctx.send("fave `name`")
        embed = discord.Embed(description=constants.FAVE_HELP, color=constants.SUB_COLOUR)
        await ctx.send(embed=embed)
        embed = discord.Embed(color=constants.MAIN_COLOUR)
        embed.add_field(name="__Possible names__", value=values.name_list, inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'ship':
        await ctx.send("ship `shipName`")
        embed = discord.Embed(description=constants.SHIP_HELP, color=constants.SUB_COLOUR)
        await ctx.send(embed=embed)
        embed = discord.Embed(color=constants.MAIN_COLOUR)
        embed.add_field(name="__Possible ships__", value=values.ship_list, inline=False)
        await ctx.send(embed=embed)
    elif cmd == 'aliases':
        await ctx.send("aliases `name`")
        embed = discord.Embed(description=constants.ALIASES_HELP, color=constants.SUB_COLOUR)
        await ctx.send(embed=embed)


bot.run(os.environ["BOT_TOKEN"])
