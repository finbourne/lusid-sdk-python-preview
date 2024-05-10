# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.140
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
from lusid.models.lusid_problem_details import LusidProblemDetails
from lusid.models.lusid_validation_problem_details import LusidValidationProblemDetails
from lusid.models.portfolio_entity import PortfolioEntity
from lusid.models.resource_list_of_change import ResourceListOfChange


class EntitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_portfolio_by_entity_unique_id(self, entity_unique_id, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetPortfolioByEntityUniqueId: Get portfolio by EntityUniqueId  # noqa: E501

        Retrieve the definition of a particular portfolio.  If the portfolio is deleted, this will return the state of the portfolio immediately prior to deletion.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_portfolio_by_entity_unique_id(entity_unique_id, async_req=True)
        >>> result = thread.get()

        :param entity_unique_id: The universally unique identifier of the portfolio definition. (required)
        :type entity_unique_id: str
        :param effective_at: The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified.
        :type effective_at: str
        :param as_at: The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified.
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
        :rtype: PortfolioEntity
        """
        kwargs['_return_http_data_only'] = True
        return self.get_portfolio_by_entity_unique_id_with_http_info(entity_unique_id, **kwargs)  # noqa: E501

    def get_portfolio_by_entity_unique_id_with_http_info(self, entity_unique_id, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetPortfolioByEntityUniqueId: Get portfolio by EntityUniqueId  # noqa: E501

        Retrieve the definition of a particular portfolio.  If the portfolio is deleted, this will return the state of the portfolio immediately prior to deletion.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_portfolio_by_entity_unique_id_with_http_info(entity_unique_id, async_req=True)
        >>> result = thread.get()

        :param entity_unique_id: The universally unique identifier of the portfolio definition. (required)
        :type entity_unique_id: str
        :param effective_at: The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified.
        :type effective_at: str
        :param as_at: The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified.
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
        :rtype: (PortfolioEntity, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'entity_unique_id',
            'effective_at',
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
                    " to method get_portfolio_by_entity_unique_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'entity_unique_id' is set
        if self.api_client.client_side_validation and ('entity_unique_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['entity_unique_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `entity_unique_id` when calling `get_portfolio_by_entity_unique_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('entity_unique_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_unique_id']) > 40):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_unique_id` when calling `get_portfolio_by_entity_unique_id`, length must be less than or equal to `40`")  # noqa: E501
        if self.api_client.client_side_validation and ('entity_unique_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['entity_unique_id']) < 30):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_unique_id` when calling `get_portfolio_by_entity_unique_id`, length must be greater than or equal to `30`")  # noqa: E501
        if self.api_client.client_side_validation and 'entity_unique_id' in local_var_params and not re.search(r'^[a-zA-Z0-9\-]+$', local_var_params['entity_unique_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `entity_unique_id` when calling `get_portfolio_by_entity_unique_id`, must conform to the pattern `/^[a-zA-Z0-9\-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'entity_unique_id' in local_var_params:
            path_params['entityUniqueId'] = local_var_params['entity_unique_id']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params and local_var_params['effective_at'] is not None:  # noqa: E501
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
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
        header_params['X-LUSID-SDK-Version'] = '1.1.140'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "PortfolioEntity",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/entities/portfolios/{entityUniqueId}', 'GET',
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

    def get_portfolio_changes(self, scope, effective_at, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.  # noqa: E501

        Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subscriptions (e.g corporate actions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_portfolio_changes(scope, effective_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope (required)
        :type scope: str
        :param effective_at: The effective date of the origin. (required)
        :type effective_at: str
        :param as_at: The as-at date of the origin.
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
        :rtype: ResourceListOfChange
        """
        kwargs['_return_http_data_only'] = True
        return self.get_portfolio_changes_with_http_info(scope, effective_at, **kwargs)  # noqa: E501

    def get_portfolio_changes_with_http_info(self, scope, effective_at, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetPortfolioChanges: Get the next change to each portfolio in a scope.  # noqa: E501

        Gets the time of the next (earliest effective at) modification (correction and/or amendment) to each portfolio in a scope relative to a point in bitemporal time.  Includes changes from parent portfolios in different scopes.  Excludes changes from subscriptions (e.g corporate actions).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_portfolio_changes_with_http_info(scope, effective_at, async_req=True)
        >>> result = thread.get()

        :param scope: The scope (required)
        :type scope: str
        :param effective_at: The effective date of the origin. (required)
        :type effective_at: str
        :param as_at: The as-at date of the origin.
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
        :rtype: (ResourceListOfChange, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'scope',
            'effective_at',
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
                    " to method get_portfolio_changes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if self.api_client.client_side_validation and ('scope' not in local_var_params or  # noqa: E501
                                                        local_var_params['scope'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scope` when calling `get_portfolio_changes`")  # noqa: E501
        # verify the required parameter 'effective_at' is set
        if self.api_client.client_side_validation and ('effective_at' not in local_var_params or  # noqa: E501
                                                        local_var_params['effective_at'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `effective_at` when calling `get_portfolio_changes`")  # noqa: E501

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_portfolio_changes`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('effective_at' in local_var_params and  # noqa: E501
                                                        len(local_var_params['effective_at']) > 256):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, length must be less than or equal to `256`")  # noqa: E501
        if self.api_client.client_side_validation and ('effective_at' in local_var_params and  # noqa: E501
                                                        len(local_var_params['effective_at']) < 0):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, length must be greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'effective_at' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_\+:\.]+$', local_var_params['effective_at']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `effective_at` when calling `get_portfolio_changes`, must conform to the pattern `/^[a-zA-Z0-9\-_\+:\.]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'scope' in local_var_params and local_var_params['scope'] is not None:  # noqa: E501
            query_params.append(('scope', local_var_params['scope']))  # noqa: E501
        if 'effective_at' in local_var_params and local_var_params['effective_at'] is not None:  # noqa: E501
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
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
        header_params['X-LUSID-SDK-Version'] = '1.1.140'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            400: "LusidValidationProblemDetails",
            200: "ResourceListOfChange",
        }

        return self.api_client.call_api(
            '/api/entities/changes/portfolios', 'GET',
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
