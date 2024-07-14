"""User module for Quclo."""

import requests
from quclo.models import User as UserModel
from quclo.utils import QUCLO_API_URL
from quclo.utils import duration_to_expires_at


class User:
    """User class for interacting with the Quclo API."""

    def __init__(
        self,
        email: str | None = None,
        password: str | None = None,
        token: str | None = None,
    ):
        """Initialize the User object."""
        assert UserModel(username=email, password=password, token=token)
        self.email = email
        self.password = password
        self.token = token

    def create(self) -> dict:
        """Create a new user."""
        response = requests.post(
            f"{QUCLO_API_URL}users/",
            json={"email": self.email, "password": self.password},
            headers={"Content-Type": "application/json"},
        )
        return response.json()

    def get_api_key(
        self,
        duration: int | None = None,
    ) -> str:
        """Get the API key for the user."""
        access_token = self._get_access_token(self.email, self.password)
        expires_at = duration_to_expires_at(duration)
        api_key_response = requests.post(
            f"{QUCLO_API_URL}api_keys/",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            },
            json={"expires_at": expires_at},
        )
        return api_key_response.json().get("api_key")

    def _get_access_token(self, email: str, password: str) -> str:
        """Get the access token for the user."""
        response = requests.post(
            f"{QUCLO_API_URL}token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "password",
                "username": email,
                "password": password,
            },
        )
        return response.json().get("access_token")
