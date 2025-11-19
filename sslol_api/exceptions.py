class SSLolAPIError(Exception):
    """Base exception for ssLOL API errors."""

class SSLolConnectionError(SSLolAPIError):
    """Raised for network or connection issues."""

class SSLolResponseError(SSLolAPIError):
    """Raised for invalid responses from the API."""
