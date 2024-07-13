from pydantic import BaseModel


class JmapConfig(BaseModel):
    provider_domain: str | None
    email_address: str | None
    auth_token: str | None


class Config(BaseModel):
    signature: str
    db_path: str
    editor: str | None = None
    jmap: JmapConfig | None = None
