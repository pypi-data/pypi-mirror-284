"""
    xpan

    xpanapi  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class MultimediafileApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.xpanfilelistall_endpoint = _Endpoint(
            settings={
                'response_type': (dict,),
                'auth': [],
                'endpoint_path': '/rest/2.0/xpan/multimedia?method=listall&openapi=xpansdk',
                'operation_id': 'xpanfilelistall',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://pan.baidu.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'access_token',
                    'path',
                    'recursion',
                    'web',
                    'start',
                    'limit',
                    'order',
                    'desc',
                ],
                'required': [
                    'access_token',
                    'path',
                    'recursion',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'access_token':
                        (str,),
                    'path':
                        (str,),
                    'recursion':
                        (int,),
                    'web':
                        (str,),
                    'start':
                        (int,),
                    'limit':
                        (int,),
                    'order':
                        (str,),
                    'desc':
                        (int,),
                },
                'attribute_map': {
                    'access_token': 'access_token',
                    'path': 'path',
                    'recursion': 'recursion',
                    'web': 'web',
                    'start': 'start',
                    'limit': 'limit',
                    'order': 'order',
                    'desc': 'desc',
                },
                'location_map': {
                    'access_token': 'query',
                    'path': 'query',
                    'recursion': 'query',
                    'web': 'query',
                    'start': 'query',
                    'limit': 'query',
                    'order': 'query',
                    'desc': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json; charset=UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.xpanmultimediafilemetas_endpoint = _Endpoint(
            settings={
                'response_type': (dict,),
                'auth': [],
                'endpoint_path': '/rest/2.0/xpan/multimedia?method=filemetas&openapi=xpansdk',
                'operation_id': 'xpanmultimediafilemetas',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://pan.baidu.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'access_token',
                    'fsids',
                    'thumb',
                    'extra',
                    'dlink',
                    'path',
                    'needmedia',
                ],
                'required': [
                    'access_token',
                    'fsids',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'access_token':
                        (str,),
                    'fsids':
                        (str,),
                    'thumb':
                        (str,),
                    'extra':
                        (str,),
                    'dlink':
                        (str,),
                    'path':
                        (str,),
                    'needmedia':
                        (int,),
                },
                'attribute_map': {
                    'access_token': 'access_token',
                    'fsids': 'fsids',
                    'thumb': 'thumb',
                    'extra': 'extra',
                    'dlink': 'dlink',
                    'path': 'path',
                    'needmedia': 'needmedia',
                },
                'location_map': {
                    'access_token': 'query',
                    'fsids': 'query',
                    'thumb': 'query',
                    'extra': 'query',
                    'dlink': 'query',
                    'path': 'query',
                    'needmedia': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json; UTF-8'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def xpanfilelistall(
        self,
        access_token,
        path,
        recursion,
        **kwargs
    ):
        """xpanfilelistall  # noqa: E501

        listall  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.xpanfilelistall(access_token, path, recursion, async_req=True)
        >>> result = thread.get()

        Args:
            access_token (str):
            path (str):
            recursion (int):

        Keyword Args:
            web (str): [optional]
            start (int): [optional]
            limit (int): [optional]
            order (str): [optional]
            desc (int): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['access_token'] = \
            access_token
        kwargs['path'] = \
            path
        kwargs['recursion'] = \
            recursion
        return self.xpanfilelistall_endpoint.call_with_http_info(**kwargs)

    def xpanmultimediafilemetas(
        self,
        access_token,
        fsids,
        **kwargs
    ):
        """xpanmultimediafilemetas  # noqa: E501

        multimedia filemetas  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.xpanmultimediafilemetas(access_token, fsids, async_req=True)
        >>> result = thread.get()

        Args:
            access_token (str):
            fsids (str):

        Keyword Args:
            thumb (str): [optional]
            extra (str): [optional]
            dlink (str): 下载地址。下载接口需要用到dlink。. [optional]
            path (str): 查询共享目录或专属空间内文件时需要。共享目录格式： /uk-fsid（其中uk为共享目录创建者id， fsid对应共享目录的fsid）。专属空间格式：/_pcs_.appdata/xpan/。. [optional]
            needmedia (int): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['access_token'] = \
            access_token
        kwargs['fsids'] = \
            fsids
        return self.xpanmultimediafilemetas_endpoint.call_with_http_info(**kwargs)

