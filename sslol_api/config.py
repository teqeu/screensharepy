import os

API_BASE_URL = "https://screenshare.lol/api"
DEFAULT_TIMEOUT = 10

def getapikey():
    """Get API key from environment variables."""
    return os.getenv("SSLOL_API_KEY")
