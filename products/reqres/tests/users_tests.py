import pytest
import self
from allure import description, epic, story, step
import requests

from core.utils.config_parser import get_config
from core.utils.logger_config import get_logger
from products.reqres.clients.user_client import UserClient
from products.reqres.endpoints.get_endpoint import GetEndpoint


@epic("Users")
@story("Verify user modules")
@description("Scenarios: Get Users")
class TestUserModules:
    logger = get_logger(module_name=__name__)

    @pytest.fixture(scope="class")
    def user_client(self, request_context):
        user_client_context = UserClient(request_context=request_context)
        yield user_client_context

    @step("Get Users by global ID")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_get_user_by_gid(self, user_client, tenant_admin_token):
        query_params = {"nrpId": "8BL-0006"}
        endpoint_key = "get_user_endpoint"  # This should match your endpoint configuration key
        status_code, response = user_client.get_user(endpoint_key=endpoint_key, query_params=query_params,
                                                     auth_token=tenant_admin_token)

        # Assertions to verify the response
        assert status_code == 200
        #Fetch user ID from the response
        user_id = response['data']['users'][0]['id']
        self.logger.info("User ID: %s", user_id)
