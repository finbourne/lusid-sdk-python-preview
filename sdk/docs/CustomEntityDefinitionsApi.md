# lusid.CustomEntityDefinitionsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:42566*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_entity_definition**](CustomEntityDefinitionsApi.md#create_custom_entity_definition) | **POST** /api/customentities/entitytypes | [EXPERIMENTAL] CreateCustomEntityDefinition: Define a new custom entityType.
[**get_definition**](CustomEntityDefinitionsApi.md#get_definition) | **GET** /api/customentities/entitytypes/{entityType} | [EXPERIMENTAL] GetDefinition: Get a custom entityType definition.


# **create_custom_entity_definition**
> CustomEntityDefinition create_custom_entity_definition(custom_entity_definition_request)

[EXPERIMENTAL] CreateCustomEntityDefinition: Define a new custom entityType.

The API will return a Bad Request if the custom entityType already exists.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:42566
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42566"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42566"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CustomEntityDefinitionsApi(api_client)
    custom_entity_definition_request = {"entityTypeName":"SupportTicket","displayName":"Support Ticket","description":"Support Ticket","fieldSchema":[{"name":"clientId","lifetime":"Perpetual","type":"String","required":true},{"name":"issueDescription","lifetime":"TimeVariant","type":"String","required":true},{"name":"internalNotes","lifetime":"TimeVariant","type":"String","required":false},{"name":"isResolved","lifetime":"TimeVariant","type":"Boolean","required":false}]} # CustomEntityDefinitionRequest | The payload containing the description of the custom entityType.

    try:
        # [EXPERIMENTAL] CreateCustomEntityDefinition: Define a new custom entityType.
        api_response = api_instance.create_custom_entity_definition(custom_entity_definition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntityDefinitionsApi->create_custom_entity_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_entity_definition_request** | [**CustomEntityDefinitionRequest**](CustomEntityDefinitionRequest.md)| The payload containing the description of the custom entityType. | 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created custom entityType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_definition**
> CustomEntityDefinition get_definition(entity_type, as_at=as_at)

[EXPERIMENTAL] GetDefinition: Get a custom entityType definition.

Retrieve a CustomEntityDefinition by a specific EntityType at a point in AsAt time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:42566
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42566"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:42566"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CustomEntityDefinitionsApi(api_client)
    entity_type = 'entity_type_example' # str | The identifier for the custom entity type, derived from the \"entityTypeName\" provided on creation.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt datetime at which to retrieve the definition. (optional)

    try:
        # [EXPERIMENTAL] GetDefinition: Get a custom entityType definition.
        api_response = api_instance.get_definition(entity_type, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntityDefinitionsApi->get_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The identifier for the custom entity type, derived from the \&quot;entityTypeName\&quot; provided on creation. | 
 **as_at** | **datetime**| The AsAt datetime at which to retrieve the definition. | [optional] 

### Return type

[**CustomEntityDefinition**](CustomEntityDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested custom entity definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

