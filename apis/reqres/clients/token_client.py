import json, pytest
from typing import Tuple

from core.utils.logger_config import get_logger
from core.base.base_client import BaseClient
from playwright.sync_api import APIRequestContext
from apis.reqres.endpoints.post_endpoint import PostEndpoint
from apis.reqres.testdata.token_test_data import create_tenant_admin_token, create_guest_token


class TokenClient(BaseClient):

    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)
        self.logger = get_logger(module_name=__name__)
        #self.create_token_endpoint = CreateTokenEndpoint()

    def create_token(self, payload_provider, endpoint_key) -> (int, dict):
        endpoint = PostEndpoint(payload_provider=payload_provider, endpoint=endpoint_key)
        # Set the base URL dynamically
        #self.request_context.set_base_url(base_url)
        status_code, response = self.request_processor(endpoint)
        self.logger.info("\nCreate Token Response:\n{}".format(json.dumps(response, indent=4)))
        return status_code, response

    def create_tenant_admin_token(self, env: str) -> Tuple[int, dict]:
        token_request = create_tenant_admin_token(env)
        return self.create_token(token_request, "token_endpoint")

    def create_guest_token(self, env: str) -> Tuple[int, dict]:
        token_request = create_guest_token(env)
        return self.create_token(token_request, "guest_endpoint")


"""
    def create_tenant_admin_token(self) -> (int, dict):
        status_code, response = self.request_processor(self.create_token_endpoint)
        self.logger.info("\nCreate Token Response:\n{}".format(json.dumps(response, indent=4)))
        return status_code, response

    def create_guest_token(self) -> (int, dict):
        status_code, response = self.request_processor(self.create_token_endpoint)
        self.logger.info("\nCreate Token Response:\n{}".format(json.dumps(response, indent=4)))
        return status_code, response

"""
