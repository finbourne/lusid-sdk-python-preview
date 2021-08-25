# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3427
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (
    ApiTypeError,
    ApiValueError
)


class CustomEntityDefinitionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_custom_entity_definition(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Create a new CustomEntityDefinition  # noqa: E501

        Create a custom entity definition that does not already exist. Will return a Bad Request if the CustomEntityDefinition already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_entity_definition(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CustomEntityDefinitionRequest custom_entity_definition_request: The CustomEntityDefinitionRequest
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CustomEntityDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_custom_entity_definition_with_http_info(**kwargs)  # noqa: E501

    def create_custom_entity_definition_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Create a new CustomEntityDefinition  # noqa: E501

        Create a custom entity definition that does not already exist. Will return a Bad Request if the CustomEntityDefinition already exists  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_custom_entity_definition_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CustomEntityDefinitionRequest custom_entity_definition_request: The CustomEntityDefinitionRequest
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CustomEntityDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['custom_entity_definition_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_custom_entity_definition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'custom_entity_definition_request' in local_var_params:
            body_params = local_var_params['custom_entity_definition_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3427'

        return self.api_client.call_api(
            '/api/customentitydefinitions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomEntityDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_definition(self, custom_entity_id, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Get CustomEntityDefinition  # noqa: E501

        Retrieve a CustomEntityDefinition by a specific Id at a point in AsAt time  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_definition(custom_entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str custom_entity_id: Id of the CustomEntityDefinition (required)
        :param datetime as_at: The AsAt at which to retrieve the CustomEntityDefinition
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CustomEntityDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_definition_with_http_info(custom_entity_id, **kwargs)  # noqa: E501

    def get_definition_with_http_info(self, custom_entity_id, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Get CustomEntityDefinition  # noqa: E501

        Retrieve a CustomEntityDefinition by a specific Id at a point in AsAt time  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_definition_with_http_info(custom_entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str custom_entity_id: Id of the CustomEntityDefinition (required)
        :param datetime as_at: The AsAt at which to retrieve the CustomEntityDefinition
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CustomEntityDefinition, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['custom_entity_id', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_definition" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'custom_entity_id' is set
        if ('custom_entity_id' not in local_var_params or
                local_var_params['custom_entity_id'] is None):
            raise ApiValueError("Missing the required parameter `custom_entity_id` when calling `get_definition`")  # noqa: E501

        if ('custom_entity_id' in local_var_params and
                len(local_var_params['custom_entity_id']) > 64):
            raise ApiValueError("Invalid value for parameter `custom_entity_id` when calling `get_definition`, length must be less than or equal to `64`")  # noqa: E501
        if ('custom_entity_id' in local_var_params and
                len(local_var_params['custom_entity_id']) < 1):
            raise ApiValueError("Invalid value for parameter `custom_entity_id` when calling `get_definition`, length must be greater than or equal to `1`")  # noqa: E501
        if 'custom_entity_id' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['custom_entity_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `custom_entity_id` when calling `get_definition`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'custom_entity_id' in local_var_params:
            path_params['customEntityId'] = local_var_params['custom_entity_id']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3427'

        return self.api_client.call_api(
            '/api/customentitydefinitions/{customEntityId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CustomEntityDefinition',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
