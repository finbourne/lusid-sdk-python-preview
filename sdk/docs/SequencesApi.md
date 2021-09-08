# lusid.SequencesApi

All URIs are relative to *http://local-unit-test-server.lusid.com:62389*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sequence**](SequencesApi.md#create_sequence) | **POST** /api/sequences/{scope} | [EXPERIMENTAL] Create a new sequence
[**get_sequence_definition**](SequencesApi.md#get_sequence_definition) | **GET** /api/sequences/{scope}/{code} | [EXPERIMENTAL] Return the definition of a sequence
[**next**](SequencesApi.md#next) | **GET** /api/sequences/{scope}/{code}/next | [EXPERIMENTAL] Get the next set of values from the sequence


# **create_sequence**
> SequenceDefinition create_sequence(scope, create_sequence_request=create_sequence_request)

[EXPERIMENTAL] Create a new sequence

Create a new sequence

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:62389
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:62389"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:62389"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SequencesApi(api_client)
    scope = 'scope_example' # str | Scope of the sequence definition.
create_sequence_request = {"code":"TestCode","increment":1,"minValue":0,"maxValue":10,"start":0,"cycle":false} # CreateSequenceRequest | Request to create sequence definition. (optional)

    try:
        # [EXPERIMENTAL] Create a new sequence
        api_response = api_instance.create_sequence(scope, create_sequence_request=create_sequence_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencesApi->create_sequence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence definition. | 
 **create_sequence_request** | [**CreateSequenceRequest**](CreateSequenceRequest.md)| Request to create sequence definition. | [optional] 

### Return type

[**SequenceDefinition**](SequenceDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful creation of the sequence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sequence_definition**
> SequenceDefinition get_sequence_definition(scope, code)

[EXPERIMENTAL] Return the definition of a sequence

Return the detailed definition of a sequence

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:62389
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:62389"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:62389"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SequencesApi(api_client)
    scope = 'scope_example' # str | Scope of the sequence definition.
code = 'code_example' # str | Code of the sequence definition. This together with stated scope uniquely              identifies the sequence definition.

    try:
        # [EXPERIMENTAL] Return the definition of a sequence
        api_response = api_instance.get_sequence_definition(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencesApi->get_sequence_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence definition. | 
 **code** | **str**| Code of the sequence definition. This together with stated scope uniquely              identifies the sequence definition. | 

### Return type

[**SequenceDefinition**](SequenceDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested sequence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **next**
> NextValueInSequenceResponse next(scope, code, batch=batch)

[EXPERIMENTAL] Get the next set of values from the sequence

Get the next set of values from the sequence

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:62389
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:62389"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:62389"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.SequencesApi(api_client)
    scope = 'scope_example' # str | Scope of the sequence definition.
code = 'code_example' # str | Code of the sequence definition. This together with stated scope uniquely              identifies the sequence definition.
batch = 1 # int | Number of sequences items to return for the specified sequence definition. (optional) (default to 1)

    try:
        # [EXPERIMENTAL] Get the next set of values from the sequence
        api_response = api_instance.next(scope, code, batch=batch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SequencesApi->next: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the sequence definition. | 
 **code** | **str**| Code of the sequence definition. This together with stated scope uniquely              identifies the sequence definition. | 
 **batch** | **int**| Number of sequences items to return for the specified sequence definition. | [optional] [default to 1]

### Return type

[**NextValueInSequenceResponse**](NextValueInSequenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gets the next set of values for the sequence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

