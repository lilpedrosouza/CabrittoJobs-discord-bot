import pyshorteners
from dotenv import load_dotenv
import discord
import os
import httpx
import random
from datetime import datetime

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("API_KEY")


def encurtar_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)


async def criar_embed(job):
    title = job.get('job_title', 'Título não disponível')
    company = job.get('employer_name', 'Empresa não disponível')
    location = f"{job.get('job_city', 'Cidade não disponível')}, {job.get('job_state', 'Estado não disponível')}, {job.get('job_country', 'País não disponível')}"
    date_posted = job.get('job_posted_at_datetime_utc', '')
    job_providers = job.get('job_apply_link', '')

    shortened_url = encurtar_url(job_providers)

    default_image = 'https://i.pinimg.com/564x/d0/a7/40/d0a7400d5f41a8e06554fb7515851def.jpg'
    if date_posted:
        date_posted = datetime.strptime(date_posted, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y")
    else:
        date_posted = 'Data não disponível'

    logo_url = job.get('employer_logo')

    embed = discord.Embed(title=title, color=random.randint(0, 0xffffff))
    embed.set_thumbnail(url=logo_url or default_image)
    embed.add_field(name="Local:", value=location, inline=True)
    embed.add_field(name="Empresa:", value=company, inline=False)
    embed.add_field(name="Link da vaga:", value=f"[Clique aqui para se candidatar!]({shortened_url})", inline=True)
    embed.add_field(name="Data da publicação:", value=date_posted, inline=True)
    embed.set_footer(text=f"Job Provider: {job.get('job_publisher', 'Não disponível')}")

    return embed


async def obter_vagas(query, page, num_pages, date_posted, remote_only, employment_types):
    api_url = "https://jsearch.p.rapidapi.com/search"
    params = {
        "query": query,
        "page": page,
        "num_pages": num_pages,
        "date_posted": date_posted,
        "remote_jobs_only": remote_only,
        "employment_types": employment_types
    }
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url, headers=headers, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"Erro na requisição: {e.response.status_code} - {e.response.text}")
            return None
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            return None

    data = response.json()
    embeds = [await criar_embed(job) for job in data.get('data', [])]

    return embeds
