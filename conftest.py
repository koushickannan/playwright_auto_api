import pytest
from typing import Generator, Callable

from playwright.sync_api import Playwright, APIRequestContext
from core.utils.config_parser import get_config
from apis.reqres.clients.token_client import TokenClient


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="QA", help="Environment to run tests against")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def token_storage():
    return {}


@pytest.fixture(scope="session")
def request_context(playwright: Playwright, env) -> Callable[[str], Generator[APIRequestContext, None, None]]:
    """
        Fixture to create request context with a given base URL.
        """

    def create_context(base_url: str) -> Generator[APIRequestContext, None, None]:
        r_context = playwright.request.new_context(base_url=base_url)
        yield r_context
        r_context.dispose()

    return create_context


# ##Working request_context --> commenting to check dynamic base_url
# @pytest.fixture(scope="session")
# def request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
#     """
#     Fixture to create request context with a given base URL.
#     """
#     base_url = get_config("BaseConfig", "base_url")
#     r_context = playwright.request.new_context(base_url=base_url)
#     yield r_context
#     r_context.dispose()


@pytest.fixture(scope="session")
# def token_client(request_context: APIRequestContext) -> Callable[[str], TokenClient]:
def token_client(request_context, env) -> Callable[[str], TokenClient]:
    def create_client(base_url: str) -> TokenClient:
        # context = request_context  # Use the already provided request context
        # client = TokenClient(request_context=context)
        # return client
        context_generator = request_context(base_url)
        context = next(context_generator)  # Get the APIRequestContext
        client = TokenClient(request_context=context)
        return client

    return create_client


@pytest.fixture(scope="session")
def tenant_admin_token(token_client, token_storage, env):
    client = token_client(get_config(env, None, "base_url"))
    status_code, response = client.create_tenant_admin_token(env)
    assert status_code == 200  # or whatever the expected status code is
    token_storage['tenant_admin_token'] = response['data']['token']
    print("Tenant Admin Token : ", response['data']['token'])
    return response['data']['token']


@pytest.fixture(scope="session")
def guest_token(token_client, token_storage, env):
    client = token_client(get_config(env, None, "base_url"))
    status_code, response = client.create_guest_token(env)
    assert status_code == 200  # or whatever the expected status code is
    token_storage['guest_token'] = response['data']['token']
    print("Guest Token : ", response['data']['token'])
    return response['data']['token']


@pytest.fixture(scope="session")
def guest_token_bff(token_client, token_storage, env):
    client = token_client(get_config(env, None, "bff_url"))
    status_code, response = client.create_guest_token_by_gid(env)
    assert status_code == 200  # or whatever the expected status code is
    token_storage['guest_token_by_gid'] = response['data']['token']
    print("Guest Token by GID: ", response['data']['token'])
    return response['data']['token']


@pytest.fixture(scope="session")
def request_headers():
    return {'Accept': 'application/json', 'Content-Type': 'application/json'}
