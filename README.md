# ssLOL API Client – `screensharepy`

A universal Python client for the [screenshare.lol](https://screenshare.lol) API, designed to work seamlessly across Discord bots, web apps, scripts, and CLI tools. Supports both synchronous and asynchronous requests with typed Pydantic models and a modular, extensible architecture.

---

## 🚀 Features

- ✅ Sync + Async support  
- 🧩 Modular design with typed Pydantic models  
- 🔐 Flexible API key handling (env or direct)  
- 🛠️ CLI tool for quick lookups  
- 🤖 Discord bot & FastAPI integration examples  

---

## 📦 Installation

```bash
1. Clone the repository
git clone https://github.com/teqeu/screensharepy.git
cd screensharepy
```

```bash
2. Install dependencies

pip install -r requirements.txt

```
```bash
3. Install the package locally

If you want to use it anywhere in Python while working in the project:

pip install -e .
```

**Requirements:**
- Python 3.8+
- Dependencies: `requests`, `httpx`, `pydantic` (installed automatically)

---

## 🔑 Setup

### Option 1: Environment Variable

```bash
# Windows (PowerShell)
$env:SSLOL_API_KEY="YOUR_API_KEY"

# Linux/macOS
export SSLOL_API_KEY="YOUR_API_KEY"
```

### Option 2: Pass API Key Directly

```python
from sslol_api.client import SSLolClient
client = SSLolClient(api_key="YOUR_API_KEY")
```

---

## 🧪 Basic Usage

### Synchronous

```python
from sslol_api.client import SSLolClient
from sslol_api.models import SearchResponse

client = SSLolClient()
raw_data = client.get_user("707967805026467851")
response = SearchResponse(**raw_data)

print("Discord ID:", response.user.discord_id)
print("Total guild records:", response.summary.total_guild_records)
print("Flagged:", response.flagged) # returns null (TODO)
```

### Asynchronous

```python
import asyncio
from sslol_api.client import SSLolClient
from sslol_api.models import SearchResponse

client = SSLolClient()

async def main():
    raw_data = await client.get_user_async("707967805026467851")
    response = SearchResponse(**raw_data)
    print("Discord ID:", response.user.discord_id)
    print("Total guild records:", response.summary.total_guild_records)
    print("Flagged:", response.flagged)

asyncio.run(main())
```

---

## 🖥️ CLI Usage

```bash
python -m sslol_api.cli discord_id --async_mode
```

With API key:

```bash
python -m sslol_api.cli discord_id --async_mode
```

---

## 🤖 Discord Bot Integration (discord.py)

```python
import discord
from sslol_api.client import SSLolClient
from sslol_api.models import SearchResponse

client = SSLolClient()
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)

@bot.slash_command(description="Check ssLOL user data")
async def check_user(ctx, discord_id: str):
    raw_data = await client.get_user_async(discord_id)
    response = SearchResponse(**raw_data)
    await ctx.respond(
        f"Discord ID: {response.user.discord_id}\n"
        f"Total guild records: {response.summary.total_guild_records}\n"
        f"Flagged: {response.flagged}" # TODO (line no. 80)
    )

bot.run("discordtoken")
```

---


## ❗ Error Handling

```python
from sslol_api.client import SSLolClient
from sslol_api.exceptions import SSLolAPIError

client = SSLolClient()

try:
    raw_data = client.get_user("707967805026467851")
except SSLolAPIError as e:
    print("API Error:", e)
```

- `SSLolConnectionError` → Network issues  
- `SSLolResponseError` → Invalid JSON responses  

---

## 📚 License

MIT License © [teqeu](https://github.com/teqeu)

---

## 🌐 Links

- [screenshare.lol](https://screenshare.lol)  
- [GitHub Repo](https://github.com/teqeu/screensharepy)