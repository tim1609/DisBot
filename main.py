import discord
from discord.ext import commands
import random


with open("TokenDisbot.txt", "r") as tf:
    TOKEN = tf.readline()

Bot = commands.Bot(command_prefix="!!")

@Bot.event
async def on_ready():
    print(f'{Bot.user} подключен к Discord!')
    for guild in Bot.guilds:
        print(
            f'{Bot.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id})'
        )

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    await message.channel.send(f"{message.author} : {message.content}")

@Bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Привет мой аналоговый друг!")

@Bot.command(name="randint")
async def my_randint(ctx, min_int, max_int):
    num = random.randint(int(min_int), int(max_int))
    await ctx.send(num)

Bot.run(TOKEN)


#client = discord.Client()
# @client.event
# async def on_ready():
#     print(f'{client.user} подключен к Discord!')
#     for guild in client.guilds:
#         print(
#             f'{client.user} подключились к чату:\n'
#             f'{guild.name}(id: {guild.id})'
#         )
# client.run(TOKEN)