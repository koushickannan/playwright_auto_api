from typing import Dict, Any

from products.reqres.models.requests.token_request import TokenRequest, Scope, GuestTokenRequest
from faker import Faker

data_generator = Faker()


def create_tenant_admin_token() -> dict:
    token_request = TokenRequest(
        tenantId="1",
        tenantSecret="651c0b1373527e43a46d26300dd94f022f297578223f89f69ded529289d8dafe",
        grantType="oauth2.0",
        scope=Scope(
            role="tenant_admin",
            userId="739",
            storeCode="710",
            langCode="en",
            externalUserId="6889",
            region="US"
        )
    ).dict()
    return token_request


def create_guest_token() -> dict:
    token_request = GuestTokenRequest(
        globalId="8BL-0006"
    ).dict()
    return token_request
