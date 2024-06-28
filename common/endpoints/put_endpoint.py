from __future__ import annotations
from typing import Callable, Union, Optional, Dict
from common.base.base_endpoint import IEndpointTemplate
from common.utils.config_parser import get_endpoint
from common.constants.http_methods import HttpMethods


class PutEndpoint(IEndpointTemplate):
    def __init__(self, endpoint: str, payload_provider: Union[Callable[[], dict], dict] = None):
        self.payload_provider = payload_provider
        self.endpoint = endpoint

    def url(self) -> str:
        return get_endpoint(self.endpoint)

    def http_method(self) -> str:
        return HttpMethods.PUT.name

    def query_parameters(self) -> dict | None:
        return None

    def path_parameters(self, path_id=None) -> Optional[Dict[str, str]]:
        return {"path_id": path_id} if path_id else None

    def headers(self, auth_token: str = None) -> dict:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        if auth_token:
            headers['Authorization'] = f'Bearer {auth_token}'
        return headers

    def request_body(self) -> dict | None:
        if self.payload_provider is None:
            return None
        if callable(self.payload_provider):
            payload = self.payload_provider()
            return payload.dict() if hasattr(payload, 'dict') else payload
        return self.payload_provider
