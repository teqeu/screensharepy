import requests
import httpx
from .config import API_BASE_URL, DEFAULT_TIMEOUT
from .exceptions import SSLolConnectionError, SSLolResponseError

def fetch_user_sync(user_id: str, api_key: str, timeout: int = DEFAULT_TIMEOUT):
    try:
        resp = requests.get(
            f"{API_BASE_URL}/search",
            params={"token": api_key, "user_id": user_id},
            timeout=timeout
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        raise SSLolConnectionError(f"Network error: {e}")
    except ValueError:
        raise SSLolResponseError("Invalid JSON response")

async def fetch_user_async(user_id: str, api_key: str, timeout: int = DEFAULT_TIMEOUT):
    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            resp = await client.get(f"{API_BASE_URL}/search", params={"token": api_key, "user_id": user_id})
            resp.raise_for_status()
            return resp.json()
        except httpx.RequestError as e:
            raise SSLolConnectionError(f"Network error: {e}")
        except ValueError:
            raise SSLolResponseError("Invalid JSON response")
