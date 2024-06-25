from typing import Dict, Any

from apis.reqres.models.requests.token_request import TokenRequest, Scope, GuestTokenRequest
from faker import Faker

from core.utils.config_parser import get_config

data_generator = Faker()


def create_tenant_admin_token(env: str) -> dict:
    tenant_id = get_config(env, None, "tenantId")
    tenant_secret = get_config(env, None, "tenantSecret")
    user_id = get_config(env, None, "userId")
    store_code = get_config(env, None, "storeCode")
    lang_code = get_config(env, None, "langCode")
    external_user_id = get_config(env, None, "externalUserId")
    region = get_config(env, None, "region")

    token_request = TokenRequest(
        tenantId=tenant_id,
        tenantSecret=tenant_secret,
        grantType="oauth2.0",
        scope=Scope(
            role="tenant_admin",
            userId=user_id,
            storeCode=store_code,
            langCode=lang_code,
            externalUserId=external_user_id,
            region=region
        )
    ).dict()
    return token_request


def create_guest_token(env: str) -> dict:
    global_id = get_config(env, None, "nrp_id")
    token_request = GuestTokenRequest(
        globalId=global_id
    ).dict()
    return token_request
