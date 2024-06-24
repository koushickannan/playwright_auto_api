from __future__ import annotations
from typing import Callable, Union, Optional, Dict
from core.base.base_endpoint import IEndpointTemplate
from core.utils.config_parser import get_endpoint
from core.constants.http_methods import HttpMethods


class PostEndpoint(IEndpointTemplate):
    def __init__(self, payload_provider: Union[Callable[[], dict], dict], endpoint: str):
        self.payload_provider = payload_provider
        self.endpoint = endpoint

    def url(self) -> str:
        return get_endpoint(self.endpoint)

    def http_method(self) -> str:
        return HttpMethods.POST.name

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
        if callable(self.payload_provider):
            return self.payload_provider().dict() if hasattr(self.payload_provider(),
                                                             'dict') else self.payload_provider()
        return self.payload_provider

    # def request_body1(self) -> dict | None:
    #     return create_guest_token().dict()
