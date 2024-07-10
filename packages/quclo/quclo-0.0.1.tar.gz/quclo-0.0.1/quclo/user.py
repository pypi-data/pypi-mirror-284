"""User module for Quclo."""

import datetime
import requests
from quclo.utils import save_api_key, load_api_key


class User:
    """User class for interacting with the Quclo API."""

    def __init__(self, email: str = None, password: str = None):
        """Initialize the User object."""
        self.email = email
        self.password = password
        self.access_token = (
            self._get_access_token(self.email, self.password)
            if self.email and self.password
            else load_api_key()
        )

    def _get_access_token(self, email: str, password: str) -> str:
        """Get the access token for the user."""
        response = requests.post(
            "https://quclo.com/api/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "password",
                "username": email,
                "password": password,
            },
        )
        return response.json().get("access_token")

    def create(self, email: str, password: str) -> dict:
        """Create a new user."""
        response = requests.post(
            "https://quclo.com/api/users/",
            json={"email": email, "password": password},
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def get_api_key(
        self,
        expires_at: datetime.datetime | None = None,
    ) -> str:
        """Get the API key for the user."""
        access_token = self._get_access_token(self.email, self.password)
        expires_at_str = expires_at.isoformat() + "Z" if expires_at else None
        api_key_response = requests.post(
            "https://quclo.com/api/api_keys/",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            },
            json={"expires_at": expires_at_str if expires_at else None},
        )
        return api_key_response.json().get("api_key")
