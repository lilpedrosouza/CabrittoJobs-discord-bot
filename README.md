# CabrittoJobs - DiscrodBOT
Um bot do Discord que envia vagas na área de tecnologia através de comandos. O CabrittoJobs o ajudará a encontrar oportunidades nesse mercado, concentrando-se principalmente em estágios e empregos de nível júnior.

# Configurando o seu bot
1. Copie .env_example para a sua .env comece a preencher os valores conforme detalhado abaixo
2. Acesse https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch/, crie uma nova chave de API e preencha API_KEY na pasta .env
3. Crie seu próprio aplicativo Discord em https://discord.com/developers/applications
4. Vá para a guia Bot e clique em "Adicionar Bot"
   - Clique em "Redefinir Token" e preencha DISCORD_BOT_TOKEN na pasta .env
   - Desative o "Bot Público", a menos que queira que seu bot fique visível para todos
   - Habilite "Message Content Intent" em "Privileged Gateway Intents"
5. Instale dependências e execute o bot
   ```
   pip install discord.py
   pip install pyshorteners
   pip install httpx
   pip install lightbulb
   pip install hikari
   ```
# Comandos
Com o bot configurado basta digitar ```!jobs (o nome da vaga que deseja)``` no chat do discord sem os parenteses, que ira aparecer um conjunto de vagas.
> [!NOTE]
> O bot ainda esta na sua primeira versão, novas features ainda serão adcionadas em breve para otimização e novas funcionalidades.
