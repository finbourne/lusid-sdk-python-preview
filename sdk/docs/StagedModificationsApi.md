# lusid.StagedModificationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_decision**](StagedModificationsApi.md#add_decision) | **POST** /api/stagedmodifications/{id}/decision | [EXPERIMENTAL] AddDecision: AddDecision
[**get_staged_modification**](StagedModificationsApi.md#get_staged_modification) | **GET** /api/stagedmodifications/{id} | [EXPERIMENTAL] GetStagedModification: GetStagedModification
[**list_requested_changes**](StagedModificationsApi.md#list_requested_changes) | **GET** /api/stagedmodifications/{id}/requestedChanges | [EXPERIMENTAL] ListRequestedChanges: ListRequestedChanges
[**list_staged_modifications**](StagedModificationsApi.md#list_staged_modifications) | **GET** /api/stagedmodifications | [EXPERIMENTAL] ListStagedModifications: ListStagedModifications


# **add_decision**
> StagedModification add_decision(id, staged_modification_decision_request)

[EXPERIMENTAL] AddDecision: AddDecision

Add decision to staged modification, Approve or Reject.

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
    api_instance = lusid.StagedModificationsApi(api_client)
    id = 'id_example' # str | Unique Id for a staged modification..
staged_modification_decision_request = {"decision":"Approve","comment":"Looks Good"} # StagedModificationDecisionRequest | The decision on the requested staged modification, \"Approve\" or \"Reject\".

    try:
        # [EXPERIMENTAL] AddDecision: AddDecision
        api_response = api_instance.add_decision(id, staged_modification_decision_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StagedModificationsApi->add_decision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Id for a staged modification.. | 
 **staged_modification_decision_request** | [**StagedModificationDecisionRequest**](StagedModificationDecisionRequest.md)| The decision on the requested staged modification, \&quot;Approve\&quot; or \&quot;Reject\&quot;. | 

### Return type

[**StagedModification**](StagedModification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staged_modification**
> StagedModification get_staged_modification(id, as_at=as_at)

[EXPERIMENTAL] GetStagedModification: GetStagedModification

Retrieve the details of a staged modification.

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
    api_instance = lusid.StagedModificationsApi(api_client)
    id = 'id_example' # str | The unique identifier for a staged modification.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the staged modification. Defaults to latest if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetStagedModification: GetStagedModification
        api_response = api_instance.get_staged_modification(id, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StagedModificationsApi->get_staged_modification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for a staged modification. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the staged modification. Defaults to latest if not specified. | [optional] 

### Return type

[**StagedModification**](StagedModification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_requested_changes**
> PagedResourceListOfStagedModificationsRequestedChangeInterval list_requested_changes(id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListRequestedChanges: ListRequestedChanges

List the requested changes for a staged modification.

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
    api_instance = lusid.StagedModificationsApi(api_client)
    id = 'id_example' # str | Unique Id for a staged modification..
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list changes. Defaults to return the latest version              of each staged change if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing requested staged modification changes from a previous call to list requested              staged modifications. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
sort_by = ['sort_by_example'] # list[str] | A list of field names suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # [EXPERIMENTAL] ListRequestedChanges: ListRequestedChanges
        api_response = api_instance.list_requested_changes(id, as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StagedModificationsApi->list_requested_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique Id for a staged modification.. | 
 **as_at** | **datetime**| The asAt datetime at which to list changes. Defaults to return the latest version              of each staged change if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing requested staged modification changes from a previous call to list requested              staged modifications. This value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**list[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfStagedModificationsRequestedChangeInterval**](PagedResourceListOfStagedModificationsRequestedChangeInterval.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested changes in staged modification. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_staged_modifications**
> PagedResourceListOfStagedModification list_staged_modifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListStagedModifications: ListStagedModifications

List summaries of the staged modifications.

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
    api_instance = lusid.StagedModificationsApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list staged modifications. Defaults to return the latest version              of each staged modification if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing staged modifications from a previous call to list staged modifications. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
sort_by = ['sort_by_example'] # list[str] | A list of field names suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # [EXPERIMENTAL] ListStagedModifications: ListStagedModifications
        api_response = api_instance.list_staged_modifications(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StagedModificationsApi->list_staged_modifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list staged modifications. Defaults to return the latest version              of each staged modification if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing staged modifications from a previous call to list staged modifications. This              value is returned from the previous call. If a pagination token is provided the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **sort_by** | [**list[str]**](str.md)| A list of field names suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfStagedModification**](PagedResourceListOfStagedModification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List summary of staged modifications. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

