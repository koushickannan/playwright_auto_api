import json
from typing import Tuple

from common.utils.logger_config import get_logger
from common.base.base_client import BaseClient
from playwright.sync_api import APIRequestContext
from common.endpoints.post_endpoint import PostEndpoint
from apis.reqres.testdata.token_test_data import create_tenant_admin_token, create_guest_token, \
    create_guest_token_by_gid


class TokenClient(BaseClient):

    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)
        self.logger = get_logger(module_name=__name__)

    def create_token(self, payload_provider, endpoint_key) -> (int, dict):
        endpoint = PostEndpoint(payload_provider=payload_provider, endpoint=endpoint_key)

        status_code, response = self.request_processor(endpoint)
        self.logger.info("\nCreate Token Response:\n{}".format(json.dumps(response, indent=4)))
        return status_code, response

    def create_tenant_admin_token(self, env: str) -> Tuple[int, dict]:
        token_request = create_tenant_admin_token(env)
        return self.create_token(token_request, "token_endpoint")

    def create_guest_token_by_gid(self, env: str) -> Tuple[int, dict]:
        token_request = create_guest_token_by_gid(env)
        return self.create_token(token_request, "guest_endpoint")

    def create_guest_token(self, env: str) -> Tuple[int, dict]:
        token_request = create_guest_token(env)
        return self.create_token(token_request, "token_endpoint")
