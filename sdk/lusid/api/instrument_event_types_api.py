# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.76
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
from lusid.models.transaction_template import TransactionTemplate
from lusid.models.transaction_template_request import TransactionTemplateRequest
from lusid.models.transaction_template_specification import TransactionTemplateSpecification


class InstrumentEventTypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_transaction_template(self, instrument_event_type, instrument_type, scope, transaction_template_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] CreateTransactionTemplate: Create Transaction Template  # noqa: E501

        Create a transaction template for a particular instrument event type in a scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_transaction_template(instrument_event_type, instrument_type, scope, transaction_template_request, async_req=True)
        >>> result = thread.get()

        :param instrument_event_type: The type of instrument events that the template is applied to. (required)
        :type instrument_event_type: str
        :param instrument_type: The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template (required)
        :type instrument_type: str
        :param scope: The scope in which the template lies. (required)
        :type scope: str
        :param transaction_template_request: A request defining a new transaction template to be created. (required)
        :type transaction_template_request: TransactionTemplateRequest
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
        :rtype: TransactionTemplate
        """
        kwargs['_return_http_data_only'] = True
        return self.create_transaction_template_with_http_info(instrument_event_type, instrument_type, scope, transaction_template_request, **kwargs)  # noqa: E501

    def create_transaction_template_with_http_info(self, instrument_event_type, instrument_type, scope, transaction_template_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] CreateTransactionTemplate: Create Transaction Template  # noqa: E501

        Create a transaction template for a particular instrument event type in a scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_transaction_template_with_http_info(instrument_event_type, instrument_type, scope, transaction_template_request, async_req=True)
        >>> result = thread.get()

        :param instrument_event_type: The type of instrument events that the template is applied to. (required)
        :type instrument_event_type: str
        :param instrument_type: The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template (required)
        :type instrument_type: str
        :param scope: The scope in which the template lies. (required)
        :type scope: str
        :param transaction_template_request: A request defining a new transaction template to be created. (required)
        :type transaction_template_request: TransactionTemplateRequest
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
        :rtype: (TransactionTemplate, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'instrument_event_type',
            'instrument_type',
            'scope',
            'transaction_template_request'
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
                    " to method create_transaction_template" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_event_type' is set
        if self.api_client.client_side_validation and ('instrument_event_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrument_event_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_event_type` when calling `create_transaction_template`")  # noqa: E501
        # verify the required parameter 'instrument_type' is set
        if self.api_client.client_side_validation and ('instrument_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrument_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_type` when calling `create_transaction_template`")  # noqa: E501
        # verify the required parameter 'scope' is set
        if self.api_client.client_side_validation and ('scope' not in local_var_params or  # noqa: E501
                                                        local_var_params['scope'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scope` when calling `create_transaction_template`")  # noqa: E501
        # verify the required parameter 'transaction_template_request' is set
        if self.api_client.client_side_validation and ('transaction_template_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_template_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_template_request` when calling `create_transaction_template`")  # noqa: E501

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_transaction_template`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_transaction_template`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_transaction_template`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'instrument_event_type' in local_var_params:
            path_params['instrumentEventType'] = local_var_params['instrument_event_type']  # noqa: E501
        if 'instrument_type' in local_var_params:
            path_params['instrumentType'] = local_var_params['instrument_type']  # noqa: E501
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_template_request' in local_var_params:
            body_params = local_var_params['transaction_template_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '1.1.76'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            201: "TransactionTemplate",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope}', 'POST',
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

    def get_transaction_template(self, instrument_event_type, instrument_type, scope, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetTransactionTemplate: Get Transaction Template  # noqa: E501

        Gets the Transaction Template that for the instrument event type within the scope specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_template(instrument_event_type, instrument_type, scope, async_req=True)
        >>> result = thread.get()

        :param instrument_event_type: The instrument event type of the transaction template (required)
        :type instrument_event_type: str
        :param instrument_type: The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template (required)
        :type instrument_type: str
        :param scope: The scope in which the template lies. When not supplied the scope is 'default'. (required)
        :type scope: str
        :param as_at: The AsAt time of the requested Transaction Template
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
        :rtype: TransactionTemplate
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transaction_template_with_http_info(instrument_event_type, instrument_type, scope, **kwargs)  # noqa: E501

    def get_transaction_template_with_http_info(self, instrument_event_type, instrument_type, scope, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetTransactionTemplate: Get Transaction Template  # noqa: E501

        Gets the Transaction Template that for the instrument event type within the scope specified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_template_with_http_info(instrument_event_type, instrument_type, scope, async_req=True)
        >>> result = thread.get()

        :param instrument_event_type: The instrument event type of the transaction template (required)
        :type instrument_event_type: str
        :param instrument_type: The instrument type of the transaction template. The combination of the instrument              event type, instrument type and scope uniquely identifies a transaction template (required)
        :type instrument_type: str
        :param scope: The scope in which the template lies. When not supplied the scope is 'default'. (required)
        :type scope: str
        :param as_at: The AsAt time of the requested Transaction Template
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
        :rtype: (TransactionTemplate, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'instrument_event_type',
            'instrument_type',
            'scope',
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
                    " to method get_transaction_template" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_event_type' is set
        if self.api_client.client_side_validation and ('instrument_event_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrument_event_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_event_type` when calling `get_transaction_template`")  # noqa: E501
        # verify the required parameter 'instrument_type' is set
        if self.api_client.client_side_validation and ('instrument_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrument_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_type` when calling `get_transaction_template`")  # noqa: E501
        # verify the required parameter 'scope' is set
        if self.api_client.client_side_validation and ('scope' not in local_var_params or  # noqa: E501
                                                        local_var_params['scope'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `scope` when calling `get_transaction_template`")  # noqa: E501

        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_transaction_template`, length must be less than or equal to `64`")  # noqa: E501
        if self.api_client.client_side_validation and ('scope' in local_var_params and  # noqa: E501
                                                        len(local_var_params['scope']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_transaction_template`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_transaction_template`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'instrument_event_type' in local_var_params:
            path_params['instrumentEventType'] = local_var_params['instrument_event_type']  # noqa: E501
        if 'instrument_type' in local_var_params:
            path_params['instrumentType'] = local_var_params['instrument_type']  # noqa: E501
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501

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
        header_params['X-LUSID-SDK-Version'] = '1.1.76'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "TransactionTemplate",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/instrumenteventtypes/{instrumentEventType}/transactiontemplates/{instrumentType}/{scope}', 'GET',
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

    def get_transaction_template_specification(self, instrument_event_type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetTransactionTemplateSpecification: Get Transaction Template Specification.  # noqa: E501

        Retrieve the transaction template specification for a particular event type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_template_specification(instrument_event_type, async_req=True)
        >>> result = thread.get()

        :param instrument_event_type: The requested instrument event type. (required)
        :type instrument_event_type: str
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
        :rtype: TransactionTemplateSpecification
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transaction_template_specification_with_http_info(instrument_event_type, **kwargs)  # noqa: E501

    def get_transaction_template_specification_with_http_info(self, instrument_event_type, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetTransactionTemplateSpecification: Get Transaction Template Specification.  # noqa: E501

        Retrieve the transaction template specification for a particular event type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_transaction_template_specification_with_http_info(instrument_event_type, async_req=True)
        >>> result = thread.get()

        :param instrument_event_type: The requested instrument event type. (required)
        :type instrument_event_type: str
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
        :rtype: (TransactionTemplateSpecification, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'instrument_event_type'
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
                    " to method get_transaction_template_specification" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'instrument_event_type' is set
        if self.api_client.client_side_validation and ('instrument_event_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['instrument_event_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `instrument_event_type` when calling `get_transaction_template_specification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instrument_event_type' in local_var_params:
            path_params['instrumentEventType'] = local_var_params['instrument_event_type']  # noqa: E501

        query_params = []

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
        header_params['X-LUSID-SDK-Version'] = '1.1.76'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "TransactionTemplateSpecification",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/instrumenteventtypes/{instrumentEventType}/transactiontemplatespecification', 'GET',
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
