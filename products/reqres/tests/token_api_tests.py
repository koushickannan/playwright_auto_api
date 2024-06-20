import pytest
from allure import description, epic, story, step
from core.utils.logger_config import get_logger
from products.reqres.clients.token_client import TokenClient
from assertpy.assertpy import assert_that
from http import HTTPStatus


@epic("Token Generation")
@story("Test token modules")
@description("Scenarios: Create token")
class TestTokenModules:
    logger = get_logger(module_name=__name__)
    #
    # @pytest.fixture
    # def token_client(self, request_context):
    #     user_client_context = TokenClient(request_context=request_context)
    #     yield user_client_context

    @step("Create a tenant admin token")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_create_tenant_admin_token(self, tenant_admin_token):
        assert tenant_admin_token is not None

    @step("Create a guest token")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_guest_token(self, guest_token):
        assert guest_token is not None

    @step("Get Users")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_get_users_by_gid(self, tenant_admin_token):
        assert tenant_admin_token is not None
        

