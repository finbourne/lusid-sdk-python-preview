# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.622
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid.models.create_custom_entity_type_request import CreateCustomEntityTypeRequest
from lusid.models.custom_entity_type import CustomEntityType
from lusid.models.lusid_problem_details import LusidProblemDetails
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid.models.paged_resource_list_of_custom_entity_type import PagedResourceListOfCustomEntityType
from lusid.models.update_custom_entity_type_request import UpdateCustomEntityTypeRequest


class CustomEntityTypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_custom_entity_type(self, create_custom_entity_type_request, **kwargs):  # noqa: E501
        """[EARLY ACCESS] CreateCustomEntityType: Define a new Custom Entity Type.  # noqa: E501

        The API will return a Bad Request if the Custom Entity Type already exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_custom_entity_type(create_custom_entity_type_request, async_req=True)
        >>> result = thread.get()

        :param create_custom_entity_type_request: The payload containing the description of the Custom Entity Type. (required)
        :type create_custom_entity_type_request: CreateCustomEntityTypeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CustomEntityType
        """
        kwargs['_return_http_data_only'] = True
        return self.create_custom_entity_type_with_http_info(create_custom_entity_type_request, **kwargs)  # noqa: E501

    def create_custom_entity_type_with_http_info(self, create_custom_entity_type_request, **kwargs):  # noqa: E501
        """[EARLY ACCESS] CreateCustomEntityType: Define a new Custom Entity Type.  # noqa: E501

        The API will return a Bad Request if the Custom Entity Type already exists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_custom_entity_type_with_http_info(create_custom_entity_type_request, async_req=True)
        >>> result = thread.get()

        :param create_custom_entity_type_request: The payload containing the description of the Custom Entity Type. (required)
        :type create_custom_entity_type_request: CreateCustomEntityTypeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (CustomEntityType, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'create_custom_entity_type_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_custom_entity_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_custom_entity_type_request' is set
        if self.api_client.client_side_validation and ('create_custom_entity_type_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['create_custom_entity_type_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `create_custom_entity_type_request` when calling `create_custom_entity_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_custom_entity_type_request' in local_var_params:
            body_params = local_var_params['create_custom_entity_type_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.0.622'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "CustomEntityType",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentitytypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_custom_entity_type(self, entity_type, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetCustomEntityType: Get a Custom Entity Type.  # noqa: E501

        Retrieve a specific Custom Entity Type at a point in AsAt time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_custom_entity_type(entity_type, async_req=True)
        >>> result = thread.get()

        :param entity_type: The identifier for the Custom Entity Type, derived from the \"entityTypeName\" provided on creation. (required)
        :type entity_type: str
        :param as_at: The AsAt datetime at which to retrieve the definition.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CustomEntityType
        """
        kwargs['_return_http_data_only'] = True
        return self.get_custom_entity_type_with_http_info(entity_type, **kwargs)  # noqa: E501

    def get_custom_entity_type_with_http_info(self, entity_type, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetCustomEntityType: Get a Custom Entity Type.  # noqa: E501

        Retrieve a specific Custom Entity Type at a point in AsAt time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_custom_entity_type_with_http_info(entity_type, async_req=True)
        >>> result = thread.get()

        :param entity_type: The identifier for the Custom Entity Type, derived from the \"entityTypeName\" provided on creation. (required)
        :type entity_type: str
        :param as_at: The AsAt datetime at which to retrieve the definition.
        :type as_at: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (CustomEntityType, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'entity_type',
            'as_at'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_entity_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'entity_type' is set
        if self.api_client.client_side_validation and ('entity_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['entity_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `entity_type` when calling `get_custom_entity_type`")  # noqa: E501

        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) > 65):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `get_custom_entity_type`, length must be less than or equal to `65`")  # noqa: E501
        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `get_custom_entity_type`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'entity_type' in local_var_params:
            path_params['entityType'] = local_var_params['entity_type']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.0.622'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "CustomEntityType",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentitytypes/{entityType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_custom_entity_types(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] ListCustomEntityTypes: List Custom Entity Types.  # noqa: E501

        List all Custom Entity Types matching particular criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_custom_entity_types(async_req=True)
        >>> result = thread.get()

        :param as_at: The asAt datetime at which to list the entities. Defaults to returning the latest version              of each Custom Entity Type if not specified.
        :type as_at: datetime
        :param limit: When paginating, limit the results to this number. Defaults to 100 if not specified.
        :type limit: int
        :param filter: Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914.
        :type filter: str
        :param sort_by: A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\"
        :type sort_by: list[str]
        :param page: The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit, sortBy,              and asAt fields must not have changed since the original request.
        :type page: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PagedResourceListOfCustomEntityType
        """
        kwargs['_return_http_data_only'] = True
        return self.list_custom_entity_types_with_http_info(**kwargs)  # noqa: E501

    def list_custom_entity_types_with_http_info(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] ListCustomEntityTypes: List Custom Entity Types.  # noqa: E501

        List all Custom Entity Types matching particular criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_custom_entity_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param as_at: The asAt datetime at which to list the entities. Defaults to returning the latest version              of each Custom Entity Type if not specified.
        :type as_at: datetime
        :param limit: When paginating, limit the results to this number. Defaults to 100 if not specified.
        :type limit: int
        :param filter: Expression to filter the results. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914.
        :type filter: str
        :param sort_by: A list of field names to sort by, each suffixed by \" ASC\" or \" DESC\"
        :type sort_by: list[str]
        :param page: The pagination token to use to continue listing entities; this              value is returned from the previous call. If a pagination token is provided, the filter, limit, sortBy,              and asAt fields must not have changed since the original request.
        :type page: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (PagedResourceListOfCustomEntityType, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'as_at',
            'limit',
            'filter',
            'sort_by',
            'page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_custom_entity_types" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 5000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_custom_entity_types`, must be a value less than or equal to `5000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_custom_entity_types`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('filter' in local_var_params and  # noqa: E501
                                                        len(local_var_params['filter']) > 16384):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_custom_entity_types`, length must be less than or equal to `16384`")  # noqa: E501
        if self.api_client.client_side_validation and ('filter' in local_var_params and  # noqa: E501
                                                        len(local_var_params['filter']) < 0):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_custom_entity_types`, length must be greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'filter' in local_var_params and not re.search(r'^[\s\S]*$', local_var_params['filter']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_custom_entity_types`, must conform to the pattern `/^[\s\S]*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in local_var_params and  # noqa: E501
                                                        len(local_var_params['page']) > 500):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_custom_entity_types`, length must be less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in local_var_params and  # noqa: E501
                                                        len(local_var_params['page']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_custom_entity_types`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and not re.search(r'^[a-zA-Z0-9\+\/]*={0,3}$', local_var_params['page']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_custom_entity_types`, must conform to the pattern `/^[a-zA-Z0-9\+\/]*={0,3}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'as_at' in local_var_params and local_var_params['as_at'] is not None:  # noqa: E501
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sortBy'] = 'multi'  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.0.622'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "PagedResourceListOfCustomEntityType",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentitytypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def update_custom_entity_type(self, entity_type, update_custom_entity_type_request, **kwargs):  # noqa: E501
        """[EARLY ACCESS] UpdateCustomEntityType: Modify an existing Custom Entity Type.  # noqa: E501

        The API will return a Bad Request if the Custom Entity Type does not exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_custom_entity_type(entity_type, update_custom_entity_type_request, async_req=True)
        >>> result = thread.get()

        :param entity_type: The identifier for the Custom Entity Type, derived from the \"entityTypeName\" provided on creation. (required)
        :type entity_type: str
        :param update_custom_entity_type_request: The payload containing the description of the Custom Entity Type. (required)
        :type update_custom_entity_type_request: UpdateCustomEntityTypeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CustomEntityType
        """
        kwargs['_return_http_data_only'] = True
        return self.update_custom_entity_type_with_http_info(entity_type, update_custom_entity_type_request, **kwargs)  # noqa: E501

    def update_custom_entity_type_with_http_info(self, entity_type, update_custom_entity_type_request, **kwargs):  # noqa: E501
        """[EARLY ACCESS] UpdateCustomEntityType: Modify an existing Custom Entity Type.  # noqa: E501

        The API will return a Bad Request if the Custom Entity Type does not exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_custom_entity_type_with_http_info(entity_type, update_custom_entity_type_request, async_req=True)
        >>> result = thread.get()

        :param entity_type: The identifier for the Custom Entity Type, derived from the \"entityTypeName\" provided on creation. (required)
        :type entity_type: str
        :param update_custom_entity_type_request: The payload containing the description of the Custom Entity Type. (required)
        :type update_custom_entity_type_request: UpdateCustomEntityTypeRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (CustomEntityType, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'entity_type',
            'update_custom_entity_type_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_custom_entity_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'entity_type' is set
        if self.api_client.client_side_validation and ('entity_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['entity_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `entity_type` when calling `update_custom_entity_type`")  # noqa: E501
        # verify the required parameter 'update_custom_entity_type_request' is set
        if self.api_client.client_side_validation and ('update_custom_entity_type_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['update_custom_entity_type_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `update_custom_entity_type_request` when calling `update_custom_entity_type`")  # noqa: E501

        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) > 65):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `update_custom_entity_type`, length must be less than or equal to `65`")  # noqa: E501
        if self.api_client.client_side_validation and ('entity_type' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_type']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_type` when calling `update_custom_entity_type`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'entity_type' in local_var_params:
            path_params['entityType'] = local_var_params['entity_type']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_custom_entity_type_request' in local_var_params:
            body_params = local_var_params['update_custom_entity_type_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.0.622'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "CustomEntityType",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/customentitytypes/{entityType}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
