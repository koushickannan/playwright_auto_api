from assertpy import assert_that

from apis.reqres.clients.login_client import LoginClient
from apis.reqres.testdata.login_test_data import login
from common.constants.http_status import HTTPStatus
from common.utils.assert_utils import Assertions
from common.utils.config_parser import get_config
from common.utils.logger_config import get_logger
import pytest
from allure import description, epic, story, step


@epic("Login")
@story("Test login modules")
@description("Scenarios: Verify Login use cases")
class TestLoginModules:
    logger = get_logger(module_name=__name__)

    @pytest.fixture(scope="class")
    def login_client(self, request_context, env):
        def create_login_client(base_url: str) -> LoginClient:
            context_generator = request_context(base_url)
            context = next(context_generator)
            return LoginClient(request_context=context)

        return create_login_client

    @step("Verify Learner login flow")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_learner_login(self, login_client, guest_token, env):
        base_url = get_config(env, None, "bff_url")
        client = login_client(base_url)
        request_payload = login(env)
        endpoint_key = "login_endpoint"  # This should match your endpoint configuration key
        status_code, response = client.login_v1(
            endpoint_key=endpoint_key,
            payload=request_payload,
            auth_token=guest_token
        )

        # Assertions to verify the response
        Assertions.assert_status_code(status_code, HTTPStatus.OK)
        Assertions.assert_response_contains(response['data'],"token")

    @step("Verify login with incorrect password")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_learner_login_incorrect_password(self, login_client, guest_token, env):
        base_url = get_config(env, None, "bff_url")
        client = login_client(base_url)
        request_payload = login(env, password="Test@123")
        endpoint_key = "login_endpoint"  # This should match your endpoint configuration key
        status_code, response = client.login_v1(
            endpoint_key=endpoint_key,
            payload=request_payload,
            auth_token=guest_token
        )

        # Assertions to verify the response
        Assertions.assert_status_code(status_code, HTTPStatus.BAD_REQUEST)
