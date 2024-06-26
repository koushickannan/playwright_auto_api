import pytest
from allure import description, epic, story, step
from core.utils.logger_config import get_logger
from apis.reqres.clients.token_client import TokenClient
from assertpy.assertpy import assert_that
from http import HTTPStatus


@epic("Token Generation")
@story("Test token modules")
@description("Scenarios: Create token")
class TestTokenModules:
    logger = get_logger(module_name=__name__)

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

    @step("Create a guest token by GID using BFF")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_guest_token_by_gid(self, guest_token_bff):
        assert guest_token_bff is not None
