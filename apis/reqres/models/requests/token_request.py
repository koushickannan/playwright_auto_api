from pydantic import BaseModel


class Scope(BaseModel):
    role: str
    userId: str
    storeCode: str
    langCode: str
    externalUserId: str
    region: str


class TokenRequest(BaseModel):
    tenantId: str
    tenantSecret: str
    grantType: str
    scope: Scope


class GuestTokenRequest(BaseModel):
    globalId: str
