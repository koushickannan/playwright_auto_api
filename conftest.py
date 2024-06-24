import pytest
from typing import Generator, Callable
from playwright.sync_api import Playwright, APIRequestContext
from core.utils.config_parser import get_config
from apis.reqres.clients.token_client import TokenClient


@pytest.fixture(scope="session")
def token_storage():
    return {}


#
# @pytest.fixture(scope="session", params=["base_url1", "base_url2"])
# def base_url(request) -> str:
#     """
#     This fixture provides different base URLs for testing.
#     :param request: pytest fixture for accessing parameterization
#     :return: base URL
#     """
#     return get_config("BaseConfig", request.param)
#
#
# @pytest.fixture(scope="session")
# def request_context(playwright: Playwright, base_url: str) -> \
#         Generator[APIRequestContext, None, None]:
#     """
#     This is request context fixture to be reused for request processing.
#     :param base_url:
#     :param playwright: instance for Playwright library
#     :return:it returns the request context
#     """
#     r_context = playwright.request.new_context(
#         #base_url=get_config("BaseConfig", "base_url")
#         base_url=base_url
#     )
#     yield r_context
#     r_context.dispose()
#
# @pytest.fixture(scope="session")
# def request_context(playwright: Playwright) -> Callable[[str], Generator[APIRequestContext, None, None]]:
#     """
#         Fixture to create request context with a given base URL.
#         """
#
#     def create_context(base_url: str) -> Generator[APIRequestContext, None, None]:
#         r_context = playwright.request.new_context(base_url=base_url)
#         yield r_context
#         r_context.dispose()
#
#     return create_context

@pytest.fixture(scope="session")
def request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    """
    Fixture to create request context with a given base URL.
    """
    base_url = get_config("BaseConfig", "base_url")
    r_context = playwright.request.new_context(base_url=base_url)
    yield r_context
    r_context.dispose()


#
# @pytest.fixture(scope="session")
# # def token_client(request_context) -> TokenClient:
# #     return TokenClient(request_context=request_context)
# def token_client(request_context) -> Callable[[str], TokenClient]:
#     def create_client(base_url: str) -> TokenClient:
#         context_generator = request_context(base_url)
#         context = next(context_generator)  # Get the APIRequestContext
#         client = TokenClient(request_context=context)
#         return client
#
#     return create_client
@pytest.fixture(scope="session")
def token_client(request_context: APIRequestContext) -> Callable[[str], TokenClient]:
    def create_client(base_url: str) -> TokenClient:
        context = request_context  # Use the already provided request context
        client = TokenClient(request_context=context)
        return client

    return create_client


@pytest.fixture(scope="session")
def tenant_admin_token(token_client, token_storage):
    client = token_client(get_config("BaseConfig", "base_url"))
    status_code, response = client.create_tenant_admin_token()
    #status_code, response = token_client.create_tenant_admin_token(base_url=get_config("BaseConfig", "base_url"))
    assert status_code == 200  # or whatever the expected status code is
    token_storage['tenant_admin_token'] = response['data']['token']
    print("Tenant Admin Token : ", response['data']['token'])
    return response['data']['token']


@pytest.fixture(scope="session")
def guest_token(token_client, token_storage):
    #status_code, response = token_client.create_guest_token(base_url=get_config("BaseConfig", "bff_url"))
    client = token_client(get_config("BaseConfig", "bff_url"))
    status_code, response = client.create_guest_token()
    assert status_code == 200  # or whatever the expected status code is
    token_storage['guest_token'] = response['data']['token']
    print("Guest Token : ", response['data']['token'])
    return response['data']['token']


@pytest.fixture(scope="session")
def base_url():
    return get_config("BaseConfig", "base_url")


@pytest.fixture(scope="session")
def request_headers():
    return {'Accept': 'application/json', 'Content-Type': 'application/json'}
