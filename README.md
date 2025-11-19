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
pip install sslol-api
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
print("Flagged:", response.flagged)
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
python -m sslol_api.cli 707967805026467851 --async_mode
```

With API key:

```bash
python -m sslol_api.cli 707967805026467851 --async_mode --api_key YOUR_API_KEY
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
        f"Flagged: {response.flagged}"
    )

bot.run("YOUR_DISCORD_BOT_TOKEN")
```

---

## 🌐 FastAPI Integration

```python
from fastapi import FastAPI
from sslol_api.client import SSLolClient
from sslol_api.models import SearchResponse

app = FastAPI()
client = SSLolClient()

@app.get("/user/{discord_id}")
async def get_user(discord_id: str):
    raw_data = await client.get_user_async(discord_id)
    response = SearchResponse(**raw_data)
    return response.dict()
```

---

## 📊 Pydantic Models

- `SearchResponse` — Full response object  
- `UserInfo` — Discord user info  
- `GuildJoinLeave` — Guild join/leave records  
- `Summary` — Ticket and guild record summary  

All fields are typed and validated.

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