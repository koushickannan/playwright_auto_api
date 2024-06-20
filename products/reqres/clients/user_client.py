import json
from typing import Optional, Dict

from core.utils.logger_config import get_logger
from core.base.base_client import BaseClient
from products.reqres.endpoints.get_endpoint import GetEndpoint
from playwright.sync_api import APIRequestContext


class UserClient(BaseClient):

    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)
        self.logger = get_logger(module_name=__name__)

    def get_user(self, endpoint_key: str, query_params: dict, auth_token: str = None) -> (int, dict):
        endpoint = GetEndpoint(endpoint=endpoint_key, query_params=query_params)
        status_code, response = self.request_processor(endpoint, auth_token=auth_token)
        self.logger.info("\nGet User Response:\n{}".format(json.dumps(response, indent=4)))
        return status_code, response
