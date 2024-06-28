import json

from playwright.async_api import APIRequestContext

from common.endpoints.post_endpoint import PostEndpoint
from common.base.base_client import BaseClient
from common.utils.logger_config import get_logger


class LoginClient(BaseClient):

    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)
        self.logger = get_logger(module_name=__name__)

    def login_v1(
            self,
            endpoint_key: str,
            payload: dict,
            auth_token: str = None
    ) -> (int, dict):
        endpoint = PostEndpoint(
            endpoint=endpoint_key,
            payload_provider=payload
        )
        status_code, response = self.request_processor(
            endpoint,
            auth_token=auth_token
        )
        self.logger.info("\nLogin Response :\n{}".format(json.dumps(response, indent=4)))
        return status_code, response
