# lusid.CustomEntitiesApi

All URIs are relative to *http://local-unit-test-server.lusid.com:38291*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_entity**](CustomEntitiesApi.md#get_custom_entity) | **GET** /api/customentities/{entityType}/{identifierType}/{identifierValue} | [EXPERIMENTAL] Get CustomEntity
[**upsert_custom_entity**](CustomEntitiesApi.md#upsert_custom_entity) | **POST** /api/customentities/{entityType} | [EXPERIMENTAL] Upsert a new CustomEntity


# **get_custom_entity**
> CustomEntityResponse get_custom_entity(entity_type, identifier_type, identifier_value, identifier_scope, as_at=as_at)

[EXPERIMENTAL] Get CustomEntity

Retrieve a CustomEntity by a specific Id at a point in AsAt time

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:38291
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:38291"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:38291"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CustomEntitiesApi(api_client)
    entity_type = 'entity_type_example' # str | The type of entity to retrieve. This is included in the response from M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.CreateCustomEntityDefinition(Finbourne.WebApi.Interface.Dto.CustomEntityDefinitions.CustomEntityDefinitionRequest).
identifier_type = 'identifier_type_example' # str | An identifier type attached to the CustomEntity
identifier_value = 'identifier_value_example' # str | The identifier value
identifier_scope = 'identifier_scope_example' # str | The identifier scope
as_at = '2013-10-20T19:20:30+01:00' # datetime | The AsAt at which to retrieve the CustomEntity (optional)

    try:
        # [EXPERIMENTAL] Get CustomEntity
        api_response = api_instance.get_custom_entity(entity_type, identifier_type, identifier_value, identifier_scope, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntitiesApi->get_custom_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of entity to retrieve. This is included in the response from M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.CreateCustomEntityDefinition(Finbourne.WebApi.Interface.Dto.CustomEntityDefinitions.CustomEntityDefinitionRequest). | 
 **identifier_type** | **str**| An identifier type attached to the CustomEntity | 
 **identifier_value** | **str**| The identifier value | 
 **identifier_scope** | **str**| The identifier scope | 
 **as_at** | **datetime**| The AsAt at which to retrieve the CustomEntity | [optional] 

### Return type

[**CustomEntityResponse**](CustomEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Custom Entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_custom_entity**
> CustomEntityResponse upsert_custom_entity(entity_type, custom_entity_request)

[EXPERIMENTAL] Upsert a new CustomEntity

Insert the custom entity if it does not exist or update the custom entity with the supplied state if it does exist.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:38291
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:38291"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:38291"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.CustomEntitiesApi(api_client)
    entity_type = 'entity_type_example' # str | The type of the CustomEntity to be created. An entityType can be created using the M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.GetDefinition(System.String,System.Nullable{System.DateTimeOffset}) endpoint.
custom_entity_request = {"displayName":"Issue","description":"Issue with loading data","effectiveAt":"2021-07-23T12:00:00.0000000+00:00","identifiers":[{"identifierScope":"DataLoadingIssues","identifierType":"InternalId","identifierValue":"92099a2006074deb8c6398b3acbe7687"},{"identifierScope":"DataLoadingIssues","identifierType":"JiraID","identifierValue":"PLAT-250"}],"fields":[{"name":"IssueName","value":"InstrumentNotFound"},{"name":"Status","value":"InProgress"},{"name":"StoryPointEstimate","value":1},{"name":"Assigned","value":true},{"name":"DateCreated","value":"2021-07-13T12:00:00.0000000+00:00"}]} # CustomEntityRequest | The CustomEntity to be created

    try:
        # [EXPERIMENTAL] Upsert a new CustomEntity
        api_response = api_instance.upsert_custom_entity(entity_type, custom_entity_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomEntitiesApi->upsert_custom_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| The type of the CustomEntity to be created. An entityType can be created using the M:Finbourne.WebApi.Controllers.CustomEntityDefinitionController.GetDefinition(System.String,System.Nullable{System.DateTimeOffset}) endpoint. | 
 **custom_entity_request** | [**CustomEntityRequest**](CustomEntityRequest.md)| The CustomEntity to be created | 

### Return type

[**CustomEntityResponse**](CustomEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The upserted Custom Entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

