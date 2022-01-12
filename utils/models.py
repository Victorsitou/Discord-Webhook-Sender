from pydantic import BaseModel


class Config(BaseModel):
    webhook: str
    console_color: str
    username: str
    avatar_url: str
