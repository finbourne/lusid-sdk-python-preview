# lusid.ScopesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_entity_scopes**](ScopesApi.md#list_entity_scopes) | **GET** /api/scopes/{entityType} | ListEntityScopes: List Entity Scopes
[**list_scopes**](ScopesApi.md#list_scopes) | **GET** /api/scopes | ListScopes: List Scopes


# **list_entity_scopes**
> ResourceListOfScopeDefinition list_entity_scopes(entity_type, as_at=as_at, page=page, limit=limit)

ListEntityScopes: List Entity Scopes

List all the scopes for a given entity type that contain data.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ScopesApi(api_client)
    entity_type = 'entity_type_example' # str | The entity type to list scopes for.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve scopes. Defaults to latest datetime if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing scopes from a previous call to list scopes.              This value is returned from the previous call. If a pagination token is provided, the limit and asAt fields              must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this number. Defaults to 100 if not specified. (optional)

    try:
        # ListEntityScopes: List Entity Scopes
        api_response = api_instance.list_entity_scopes(entity_type, as_at=as_at, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopesApi->list_entity_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The entity type to list scopes for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve scopes. Defaults to latest datetime if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing scopes from a previous call to list scopes.              This value is returned from the previous call. If a pagination token is provided, the limit and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this number. Defaults to 100 if not specified. | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of scopes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scopes**
> ResourceListOfScopeDefinition list_scopes(filter=filter)

ListScopes: List Scopes

List all the scopes that contain data.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ScopesApi(api_client)
    filter = 'filter_example' # str | Expression to filter the result set.              For example, to filter on the Scope, use \"scope eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # ListScopes: List Scopes
        api_response = api_instance.list_scopes(filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopesApi->list_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set.              For example, to filter on the Scope, use \&quot;scope eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfScopeDefinition**](ResourceListOfScopeDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of scopes |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

