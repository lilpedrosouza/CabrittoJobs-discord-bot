import hikari
import pyshorteners
from dotenv import load_dotenv
import os
import httpx
import random
from datetime import datetime

load_dotenv()

api_key = os.getenv("API_KEY")

def encurtar_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

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
        response = await client.get(api_url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()

            embeds = []

            for job in data['data']:
                title = job.get('job_title', '')
                company = job.get('employer_name', '')
                location = f"{job.get('job_city', '')}, {job.get('job_state', '')}, {job.get('job_country', '')}"
                date_posted = job.get('job_posted_at_datetime_utc', '')
                job_providers = job.get('job_apply_link', '')

                shortened_url = encurtar_url(job_providers)

                default_image = 'https://tse2.mm.bing.net/th/id/OIG1.w4HtNwd2AlWUDd5AbOaV?pid=ImgGn'
                date_posted = datetime.strptime(date_posted, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y")

                logo_url = job.get('employer_logo')
                if not logo_url:
                    logo_url = default_image

                embed = hikari.Embed(title=title, color=random.randint(0, 0xffffff))
                embed.set_thumbnail(logo_url)
                embed.add_field("Local:", value=location, inline=True)
                embed.add_field("Empresa:", value=company, inline=False)
                embed.add_field("Link da vaga:", value=f"[Clique aqui para se candidatar!]({shortened_url})", inline=True)
                embed.add_field("Data da publicação:", value=date_posted, inline=True)
                embed.set_footer(text=f"Job Provider: {job.get('job_publisher', '')}")
                embeds.append(embed)

            return embeds
        else:
            print("Response Status Code:", response.status_code)
            print("Response Content:", response.text)

        return None