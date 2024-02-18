import discord
import logging
import logging.handlers
import os

def setup_discord_bot():
    log_directory = 'log'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    log_file_path = os.path.join(log_directory, 'discord.log')

    handler = logging.handlers.RotatingFileHandler(
        filename=log_file_path,
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Assume client refers to a discord.Client subclass...
    # Suppress the default configuration since we have our own
    client.run('MTIwNzgxNTExMDg2MTc4NzE5Ng.GVvJTe.SKw9lySHu_T8KCyQr4exmOvKa8Dh81eDlKZdEM', log_handler=None)

