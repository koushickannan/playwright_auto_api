import pytest
from allure import description, epic, story, step
from assertpy import assert_that

from common.constants.http_status import HTTPStatus
from common.utils.assert_utils import Assertions
from common.utils.config_parser import get_config
from common.utils.logger_config import get_logger
from apis.reqres.clients.user_client import UserClient
from apis.reqres.testdata.user_test_data import create_user_request_payload


@epic("Users")
@story("Verify user modules")
@description("Scenarios: Users")
class TestUserModules:
    logger = get_logger(module_name=__name__)
    user_id = None

    @pytest.fixture(scope="class")
    def user_client(self, request_context, env):
        def create_user_client(base_url: str) -> UserClient:
            context_generator = request_context(base_url)
            context = next(context_generator)
            return UserClient(request_context=context)

        return create_user_client

    @step("Create retail user")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_create_retail_user(self, user_client, guest_token, env):
        base_url = get_config(env, None, "base_url")
        client = user_client(base_url)
        request_payload = create_user_request_payload()
        endpoint_key = "get_user_endpoint"  # This should match your endpoint configuration key
        status_code, response = client.create_user(
            endpoint_key=endpoint_key,
            payload=request_payload,
            auth_token=guest_token
        )

        # Assertions to verify the response
        Assertions.assert_status_code(status_code, HTTPStatus.OK)

        # Fetch user ID from the response
        self.__class__.user_id = response['data']['id']
        self.logger.info("User ID from create retail user API: %s", self.__class__.user_id)

    @step("Get Users by global ID")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_get_user_by_gid(self, user_client, tenant_admin_token, env):
        base_url = get_config(env, None, "base_url")
        client = user_client(base_url)
        nrp_id = get_config(env, None, "nrp_id")
        query_params = {"nrpId": nrp_id}
        endpoint_key = "get_user_endpoint"  # This should match your endpoint configuration key
        status_code, response = client.get_user(
            endpoint_key=endpoint_key,
            query_params=query_params,
            auth_token=tenant_admin_token
        )

        # Assertions to verify the response
        Assertions.assert_status_code(status_code, HTTPStatus.OK)

    @step("Get Users by User ID")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_get_user_by_id(self, user_client, tenant_admin_token, env):
        base_url = get_config(env, None, "base_url")
        client = user_client(base_url)
        user_id = self.__class__.user_id
        endpoint_key = "get_user_id_endpoint"  # This should match your endpoint configuration key
        status_code, response = client.get_user(
            endpoint_key=endpoint_key,
            auth_token=tenant_admin_token,
            path_params={"user_id": user_id}
        )

        # Assertions to verify the response
        Assertions.assert_status_code(status_code, HTTPStatus.OK)
