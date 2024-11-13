from pydantic import BaseModel


class ConfigModel(BaseModel):
    url: str
    browser: str
    timeout: int
