import discord
from discord.ext import commands
from bot_log import setup_discord_bot
from discord import Message
import hikari 

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = hikari.GatewayBot('MTIwNzgxNTExMDg2MTc4NzE5Ng.GVvJTe.SKw9lySHu_T8KCyQr4exmOvKa8Dh81eDlKZdEM')
client = discord.Client( intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'{message.author} é viado')

client.run('MTIwNzgxNTExMDg2MTc4NzE5Ng.GVvJTe.SKw9lySHu_T8KCyQr4exmOvKa8Dh81eDlKZdEM')

setup_discord_bot()
