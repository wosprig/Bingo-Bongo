import discord
from discord.ext import commands
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix="w!", description="Just trying this out.")
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def fave(ctx, name):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    # TODO


@bot.command(pass_context=True)
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
async def help(ctx):
    embed = discord.Embed(title="BingoBongo", description="Wo's trying bots. List of commands are:", color=0x21c6bb)

    embed.add_field(name="w!fave <name>", value="Finds a random gif of one of <name>'s faves", inline=False)

    await ctx.send(embed=embed)


bot.run($BOT_TOKEN)
