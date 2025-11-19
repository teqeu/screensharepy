# ssLOL API Client
A **universal Python client** for the [screenshare.lol (ssLOL) API](https://screenshare.lol), designed to work in **Discord bots, web apps, scripts, CLI tools, and other Python applications**. Supports **synchronous and asynchronous requests** with **typed responses** using Pydantic.  
## **Installation**
### Using `pip`
```bash
pip install sslol-api
Requirements
Python 3.8+

Dependencies installed automatically: requests, httpx, pydantic

Setup
1. API Key
Set your ssLOL API key in an environment variable:
Windows (PowerShell):

powershell
Copy code
$env:SSLOL_API_KEY="YOUR_API_KEY"
Linux/macOS (bash/zsh):

bash
Copy code
export SSLOL_API_KEY="YOUR_API_KEY"
You can also pass the API key directly to the client:

python
Copy code
from sslol_api.client import SSLolClient
client = SSLolClient(api_key="YOUR_API_KEY")
Basic Usage
Synchronous
python
Copy code
from sslol_api.client import SSLolClient
from sslol_api.models import SearchResponse
client = SSLolClient()
raw_data = client.get_user("707967805026467851")
response = SearchResponse(**raw_data)
print("Discord ID:", response.user.discord_id)
print("Total guild records:", response.summary.total_guild_records)
print("Flagged:", response.flagged)
Asynchronous
python
Copy code
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
CLI Usage
bash
Copy code
python -m sslol_api.cli 707967805026467851 --async_mode
Optional: pass API key directly

bash
Copy code
python -m sslol_api.cli 707967805026467851 --async_mode --api_key YOUR_API_KEY
Integration Examples
Discord Bot (discord.py)
python
Copy code
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
    await ctx.respond(f"Discord ID: {response.user.discord_id}\nTotal guild records: {response.summary.total_guild_records}\nFlagged: {response.flagged}")
bot.run("YOUR_DISCORD_BOT_TOKEN")
FastAPI Web Application
python
Copy code
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
Python Script / Analytics
python
Copy code
from sslol_api.client import SSLolClient
from sslol_api.models import SearchResponse
client = SSLolClient()
discord_ids = ["707967805026467851", "123456789012345678"]
for user_id in discord_ids:
    raw_data = client.get_user(user_id)
    user = SearchResponse(**raw_data)
    print(f"{user.user.discord_id} joined {len(user.guild_join_leave)} guilds")
Pydantic Models
SearchResponse — Full response object

UserInfo — Discord user info

GuildJoinLeave — Guild join/leave records

Summary — Tickets and guild record summary
All fields are typed and validated. Example:

python
Copy code
print(response.user.discord_id)
print(response.summary.total_guild_records)
print(response.flagged)
Error Handling
All exceptions inherit from SSLolAPIError:

python
Copy code
from sslol_api.client import SSLolClient
from sslol_api.exceptions import SSLolAPIError
client = SSLolClient()
try:
    raw_data = client.get_user("707967805026467851")
except SSLolAPIError as e:
    print("API Error:", e)
SSLolConnectionError → network issues

SSLolResponseError → invalid JSON responses

Advanced Features
Sync + Async support — works in bots, web apps, scripts

CLI tool — can fetch user data from terminal

Flexible API key — environment variable or direct argument

Validator-friendly — all fields are typed, including flagged (True/False/None)