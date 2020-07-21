# lusid.ConventionsApi

All URIs are relative to *http://localhost:56044*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_conventions**](ConventionsApi.md#delete_conventions) | **DELETE** /api/conventions/{scope}/{code} | [EXPERIMENTAL] Delete the conventions of given scope and code, assuming that it is present.
[**get_flow_conventions**](ConventionsApi.md#get_flow_conventions) | **GET** /api/conventions/{scope}/{code} | [EXPERIMENTAL] Get Flow Conventions
[**list_conventions**](ConventionsApi.md#list_conventions) | **GET** /api/conventions | [EXPERIMENTAL] List the set of conventions


# **delete_conventions**
> AnnulSingleStructuredDataResponse delete_conventions(scope, code)

[EXPERIMENTAL] Delete the conventions of given scope and code, assuming that it is present.

Delete the specified conventions from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.  It is important to always check for any unsuccessful response.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:56044
configuration.host = "http://localhost:56044"
# Create an instance of the API class
api_instance = lusid.ConventionsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the conventions to delete.
code = 'code_example' # str | The conventions to delete.

try:
    # [EXPERIMENTAL] Delete the conventions of given scope and code, assuming that it is present.
    api_response = api_instance.delete_conventions(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConventionsApi->delete_conventions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the conventions to delete. | 
 **code** | **str**| The conventions to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flow_conventions**
> GetConventionsResponse get_flow_conventions(scope, code, as_at=as_at)

[EXPERIMENTAL] Get Flow Conventions

Get a Flow Conventions from a single scope.  The response will return either the conventions that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:56044
configuration.host = "http://localhost:56044"
# Create an instance of the API class
api_instance = lusid.ConventionsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the Flow Conventions to retrieve.
code = 'code_example' # str | The name of the Flow Conventions to retrieve the data for.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Flow Conventions. Defaults to return the latest version if not specified. (optional)

try:
    # [EXPERIMENTAL] Get Flow Conventions
    api_response = api_instance.get_flow_conventions(scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConventionsApi->get_flow_conventions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Flow Conventions to retrieve. | 
 **code** | **str**| The name of the Flow Conventions to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Flow Conventions. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetConventionsResponse**](GetConventionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Flow Conventions or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conventions**
> ResourceListOfGetConventionsResponse list_conventions(as_at=as_at)

[EXPERIMENTAL] List the set of conventions

List the set of conventions at the specified date/time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:56044
configuration.host = "http://localhost:56044"
# Create an instance of the API class
api_instance = lusid.ConventionsApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the conventions. Defaults to latest if not specified. (optional)

try:
    # [EXPERIMENTAL] List the set of conventions
    api_response = api_instance.list_conventions(as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConventionsApi->list_conventions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the conventions. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetConventionsResponse**](ResourceListOfGetConventionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested conventions |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

