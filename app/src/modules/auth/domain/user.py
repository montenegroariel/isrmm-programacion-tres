from dataclasses import dataclass

@dataclass
class User:
    id: str | None
    email: str
    hashed_password: str