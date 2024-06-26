from pydantic import BaseModel


class LoginRequest(BaseModel):
    userName: str
    password: str
    remember: bool
