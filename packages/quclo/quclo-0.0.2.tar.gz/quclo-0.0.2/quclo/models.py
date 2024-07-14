"""Data models for QuClo."""

from pydantic import BaseModel, EmailStr
from typing_extensions import Annotated
from annotated_types import Predicate
from openqasm3 import parser

OpenQASM3 = Annotated[str, Predicate(parser.parse)]


class User(BaseModel):
    username: EmailStr | None = None
    password: str | None = None
    token: str | None = None  # access token or api key

    def __init__(self, **data):
        super().__init__(**data)
        if not (self.username and self.password) and not self.token:
            raise ValueError("Email and password or API key is required.")


class Circuit(BaseModel):
    qasm: OpenQASM3
    backend: str | None = None
    priority: str | None = None

    def __init__(self, **data):
        super().__init__(**data)
        if not self.qasm:
            raise ValueError("QASM is required.")
        if self.backend and self.priority:
            raise ValueError("Cannot specify both backend and priority.")
        if not (self.backend or self.priority):
            raise ValueError("Either backend or priority is required.")


class Backend(BaseModel):
    pass
