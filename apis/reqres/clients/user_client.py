import json

from common.utils.logger_config import get_logger
from common.base.base_client import BaseClient
from common.endpoints.get_endpoint import GetEndpoint
from playwright.sync_api import APIRequestContext

from common.endpoints.post_endpoint import PostEndpoint


class UserClient(BaseClient):

    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)
        self.logger = get_logger(module_name=__name__)

    def get_user(
            self,
            endpoint_key: str,
            query_params: dict = None,
            auth_token: str = None,
            path_params: dict = None
    ) -> (int, dict):
        endpoint = GetEndpoint(
            endpoint=endpoint_key,
            query_params=query_params,
            path_params=path_params
        )
        status_code, response = self.request_processor(
            endpoint,
            auth_token=auth_token
        )
        self.logger.info(
            "\nGet User Response:\n{}".format(json.dumps(response, indent=4))
        )
        return status_code, response

    def create_user(
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
        self.logger.info("\nCreate User Response:\n{}".format(json.dumps(response, indent=4)))
        return status_code, response
