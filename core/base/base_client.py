"""
This module is used for basic CRUD operations using Playwright -> APIRequestContext
"""
from playwright.sync_api import APIRequestContext
from core.base.base_endpoint import IEndpointTemplate
from core.constants.http_methods import HttpMethods


class BaseClient:

    def __init__(self, request_context: APIRequestContext):
        self.request_context = request_context

    def request_processor(self, endpoint: IEndpointTemplate.__class__, **kwargs) -> (int, dict):
        """
        This function processes the http request based on http methods
        :param endpoint: it takes endpoint specifications which can be
        provided by extending the "IEndpointTemplate" interface
        :param kwargs: it takes keyword arguments required in special cases,
        these are optional arguments
        :return: it returns http status code and response
        """
        url = endpoint.url()
        http_method = endpoint.http_method()
        query_params = endpoint.query_parameters()
        auth_token = kwargs.get('auth_token')
        path_params = endpoint.path_parameters()
        headers = endpoint.headers(auth_token=auth_token)
        request_body = endpoint.request_body()

        # if path_params:
        #     url = url.format(**path_params)

        if path_params:
            for key, value in path_params.items():
                #url = url.format(**path_params)
                url = url.replace(f'{{{key}}}', str(value))

        # if query_params:
        #     url += '?'
        #     url += '&'.join([f'{key}={value}' for key, value in query_params.items()])

        if query_params:
            # Construct the query string with the specified format
            query_string = '&'.join([f'{key}={value}' for key, value in query_params.items()])
            url += f'?{query_string}'

        response = None

        # match http_method:
        #     case HttpMethods.GET.name:
        #         response = self.request_context.get(url=url, headers=headers)
        #     case HttpMethods.POST.name:
        #         response = self.request_context.post(url=url, headers=headers, data=request_body)

        if http_method == HttpMethods.GET.name:
            response = self.request_context.get(url=url, headers=headers)
        elif http_method == HttpMethods.POST.name:
            response = self.request_context.post(url=url, headers=headers, data=request_body)
        elif http_method == HttpMethods.PATCH.name:
            response = self.request_context.post(url=url, headers=headers, data=request_body)
        elif http_method == HttpMethods.PUT.name:
            response = self.request_context.post(url=url, headers=headers, data=request_body)
        elif http_method == HttpMethods.DELETE.name:
            response = self.request_context.post(url=url, headers=headers, data=request_body)
        else:
            raise ValueError(f"Unsupported HTTP method: {http_method}")

        return response.status, response.json()
