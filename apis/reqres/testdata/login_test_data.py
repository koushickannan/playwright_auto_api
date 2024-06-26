from apis.reqres.models.requests.login_request import LoginRequest
from core.utils.config_parser import get_config


def login(env: str, user_name: str = None, password: str = None) -> dict:
    if not user_name:
        user_name = get_config(env, None, "userName")
    if not password:
        password = get_config(env, None, "password")

    login_request = LoginRequest(
        userName=user_name,
        password=password,
        remember=False
    ).dict()

    return login_request
