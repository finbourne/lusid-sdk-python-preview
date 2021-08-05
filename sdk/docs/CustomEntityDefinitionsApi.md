# lusid.CustomEntityDefinitionsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:37031*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_entity_definition**](CustomEntityDefinitionsApi.md#create_custom_entity_definition) | **POST** /api/customentitydefinitions | [EXPERIMENTAL] Create a new CustomEntityDefinition
[**get_definition**](CustomEntityDefinitionsApi.md#get_definition) | **GET** /api/customentitydefinitions/{customEntityId} | [EXPERIMENTAL] Get CustomEntityDefinition


# **create_custom_entity_definition**
> CustomEntityDefinition create_custom_entity_definition(custom_entity_definition_request=custom_entity_definition_request)

[EXPERIMENTAL] Create a new CustomEntityDefinition

Create a custom entity definition that does not already exist. Will return a Bad Request if the CustomEntityDefinition already exists

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:37031
configuration.host = "http://local-unit-test-server.lusid.com:37031"
# Create an instance of the API class
api_instance = lusid.CustomEntityDefinitionsApi(lusid.ApiClient(configuration))
custom_entity_definition_request = {"customEntityId":"issue","displayName":"Issue","description":"Represents an issue in the system","fieldSchema":[{"name":"Assigned","temporality":"Bitemporal","type":"bool","required":true},{"name":"Status","temporality":"Bitemporal","type":"string","required":true},{"name":"Effort In Days","temporality":"Monotemporal","type":"number","required":false},{"name":"DateCreated","temporality":"Monotemporal","type":"datetime","required":true}]} # CustomEntityDefinitionRequest | The CustomEntityDefinitionRequest (optional)

try:
    # [EXPERIMENTAL] Create a new CustomEntityDefinition
    api_response = api_instance.create_custom_entity_definition(custom_entity_definition_request=custom_entity_definition_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomEntityDefinitionsApi->create_custom_entity_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_entity_definition_request** | [**CustomEntityDefinitionRequest**](CustomEntityDefinitionRequest.md)| The CustomEntityDefinitionRequest | [optional] 

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
**200** | The created custom entity definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_definition**
> CustomEntityDefinition get_definition(custom_entity_id, as_at=as_at)

[EXPERIMENTAL] Get CustomEntityDefinition

Retrieve a CustomEntityDefinition by a specific Id at a point in AsAt time

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:37031
configuration.host = "http://local-unit-test-server.lusid.com:37031"
# Create an instance of the API class
api_instance = lusid.CustomEntityDefinitionsApi(lusid.ApiClient(configuration))
custom_entity_id = 'custom_entity_id_example' # str | Id of the CustomEntityDefinition
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt at which to retrieve the CustomEntityDefinition (optional)

try:
    # [EXPERIMENTAL] Get CustomEntityDefinition
    api_response = api_instance.get_definition(custom_entity_id, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomEntityDefinitionsApi->get_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_entity_id** | **str**| Id of the CustomEntityDefinition | 
 **as_at** | **datetime**| The AsAt at which to retrieve the CustomEntityDefinition | [optional] 

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
**200** | The requested custom entity definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

