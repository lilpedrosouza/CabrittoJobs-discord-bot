import discord
from discord.ext import commands
from discord import app_commands
import random
import os
from dotenv import load_dotenv
from jobs_api import obter_vagas

# Carregar variáveis de ambiente
load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

# Configurar intenções do bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


# Inicializar o bot
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        self.tree.add_command(jobs)
        self.tree.add_command(estagio)
        await self.tree.sync()


bot = MyBot()


async def buscar_vagas(interaction: discord.Interaction, tipo_vaga: str, job: str) -> None:
    await interaction.response.defer()  # Defer a interação para indicar que estamos processando

    query = f'{tipo_vaga} {job} no Brasil'
    page = random.randint(1, 3)
    num_pages = random.randint(1, 3)
    date_posted = 'month'
    remote_only = 'True'
    employment_types = 'fulltime, parttime, intern, contractor'

    try:
        embeds = await obter_vagas(query, page, num_pages, date_posted, remote_only, employment_types)

        if embeds:
            for embed in embeds:
                await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send("Não foram encontradas vagas.")
    except Exception as e:
        await interaction.followup.send(f"Ocorreu um erro ao obter as vagas: {e}")


# Definir o comando de barra para vagas de desenvolvedor
@app_commands.command(name="jobs", description="Procura por vagas de desenvolvedor no Brasil.")
@app_commands.describe(job="Especifique o tipo de desenvolvedor (ex: Python, JavaScript)")
async def jobs(interaction: discord.Interaction, job: str) -> None:
    await buscar_vagas(interaction, 'Desenvolvedor', job)


# Definir o comando de barra para vagas de estágio
@app_commands.command(name="estagio", description="Procura por vagas de estagio no Brasil.")
@app_commands.describe(job="Especifique o tipo de estágio (ex: Python, JavaScript)")
async def estagio(interaction: discord.Interaction, job: str) -> None:
    await buscar_vagas(interaction, 'Estágio', job)


# Executar o bot
if __name__ == "__main__":
    bot.run(discord_token)
