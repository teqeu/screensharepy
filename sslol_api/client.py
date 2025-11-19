from .api import fetch_user_sync, fetch_user_async
from .config import getapikey
from .exceptions import SSLolAPIError

class SSLolClient:
    def __init__(self, api_key: str = None, timeout: int = 10):
        self.api_key = api_key or getapikey()
        if not self.api_key:
            raise ValueError("API key is required")
        self.timeout = timeout

    def get_user(self, user_id: str):
        try:
            return fetch_user_sync(user_id, self.api_key, self.timeout)
        except SSLolAPIError as e:
            raise e

    async def get_user_async(self, user_id: str):
        try:
            return await fetch_user_async(user_id, self.api_key, self.timeout)
        except SSLolAPIError as e:
            raise e
