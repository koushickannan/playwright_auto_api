from __future__ import annotations

from typing import Union, Callable, Optional, Dict

from core.base.base_endpoint import IEndpointTemplate
from core.utils.config_parser import get_endpoint
from core.constants.http_methods import HttpMethods


class GetEndpoint(IEndpointTemplate):
    def __init__(self, endpoint: str, query_params: Optional[Dict[str, str]] = None):
        self.endpoint = endpoint
        self.query_params = query_params or {}
        self.auth_token = None

    def url(self) -> str:
        return get_endpoint(self.endpoint)

    def http_method(self) -> str:
        return HttpMethods.GET.name

    # def query_parameters(self) -> Dict[str, str]:
    #     return self.query_params

    def query_parameters(self) -> Optional[Dict[str, str]]:
        # Format the query parameters as a single key-value pair
        if self.query_params:
            query_string = ','.join([f'{key}=={value}' for key, value in self.query_params.items()])
            return {'query': f'({query_string})'}
        return None

    def path_parameters(self, user_id=None) -> dict | None:
        # If no path parameters are needed, return None
        return {"user_id": user_id} if user_id else None

    def headers(self, auth_token: str = None) -> dict:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        if auth_token:
            headers['Authorization'] = f'Bearer {auth_token}'
        return headers

    def request_body(self) -> None:
        return None

