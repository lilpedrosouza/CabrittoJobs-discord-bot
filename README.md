# CabrittoJobs - Discord Bot

CabrittoJobs é um bot para Discord que ajuda você a encontrar vagas na área de tecnologia através de comandos simples. O bot foca principalmente em oportunidades de estágios e empregos de nível júnior, facilitando a busca por novas oportunidades no mercado de trabalho.

## Recursos
- Busca de vagas de emprego na área de tecnologia.
- Filtragem por estágios e cargos de nível júnior.
- Integração direta com APIs de busca de emprego.
- Retorno dinâmico das vagas diretamente no chat do Discord.

## Configuração do Bot
Siga os passos abaixo para configurar e rodar o CabrittoJobs no seu servidor do Discord:

### 1. Clonando o Repositório
```bash
 git clone https://github.com/seu-usuario/cabrittojobs.git
 cd cabrittojobs
```

### 2. Criando e Configurando o Arquivo `.env`
Copie o arquivo de exemplo e preencha os valores conforme as instruções:
```bash
cp .env_example .env
```
Edite o arquivo `.env` e adicione as seguintes credenciais:

- **API_KEY**: Obtenha sua chave de API no [RapidAPI](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch/)
- **DISCORD_BOT_TOKEN**: Crie um bot no [Discord Developer Portal](https://discord.com/developers/applications) e copie seu token

### 3. Criando e Configurando o Bot no Discord
1. Acesse [Discord Developer Portal](https://discord.com/developers/applications) e crie uma nova aplicação.
2. No menu "Bot", clique em "Adicionar Bot".
3. Clique em "Redefinir Token" e copie o valor gerado para o arquivo `.env`.
4. Desative a opção **Bot Público** (a menos que queira torná-lo acessível a todos).
5. Habilite **Message Content Intent** na seção "Privileged Gateway Intents".
6. No menu "OAuth2 > URL Generator", selecione os escopos `bot` e `applications.commands`.
7. Copie a URL gerada, cole no seu navegador e adicione o bot ao seu servidor.

### 4. Instalando Dependências
```bash
pip install discord.py pyshorteners httpx
```

### 5. Executando o Bot
```bash
python bot.py
```
Se tudo estiver configurado corretamente, o bot estará ativo e pronto para ser utilizado!

## Comandos Disponíveis
Com o bot configurado, você pode usar os seguintes comandos no chat do Discord:

| Comando | Descrição |
|---------|-------------|
| `/jobs [vaga]` | Busca por vagas de emprego na área informada |
| `/estagio [vaga]` | Busca por estágios na área informada |

**Exemplo de uso:**
```bash
/jobs desenvolvedor python
```

O bot retornará um conjunto de vagas de acordo com o termo pesquisado.

## Futuras Atualizações
O bot ainda está na sua primeira versão e novas funcionalidades serão adicionadas em breve, incluindo:
- Melhor filtragem de vagas.
- Integração com outras APIs de emprego.
- Opção para salvar vagas favoritas.

## Licença
Este projeto é distribuído sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário.

---
