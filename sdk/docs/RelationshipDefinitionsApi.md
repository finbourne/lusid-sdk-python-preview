# lusid.RelationshipDefinitionsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:55270*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relationship_definition**](RelationshipDefinitionsApi.md#create_relationship_definition) | **POST** /api/relationshipdefinitions | [EXPERIMENTAL] CreateRelationshipDefinition: Create Relationship Definition
[**get_relationship_definition**](RelationshipDefinitionsApi.md#get_relationship_definition) | **GET** /api/relationshipdefinitions/{scope}/{code} | [EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition
[**update_relationship_definition**](RelationshipDefinitionsApi.md#update_relationship_definition) | **PUT** /api/relationshipdefinitions/{scope}/{code} | [EXPERIMENTAL] UpdateRelationshipDefinition: Update Relationship Definition


# **create_relationship_definition**
> RelationshipDefinition create_relationship_definition(create_relationship_definition_request)

[EXPERIMENTAL] CreateRelationshipDefinition: Create Relationship Definition

Create a new relationship definition to be used for creating relationships between entities.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:55270
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:55270"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:55270"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.RelationshipDefinitionsApi(api_client)
    create_relationship_definition_request = {"scope":"PortfolioManagementTeam","code":"Traders","sourceEntityType":"Portfolio","targetEntityType":"Person","displayName":"Authorised traders to trade for specific portfolio ","outwardDescription":"can be traded by","inwardDescription":"can trade with portfolio","lifeTime":"TimeVariant","relationshipCardinality":"ManyToMany"} # CreateRelationshipDefinitionRequest | The definition of the new relationship.

    try:
        # [EXPERIMENTAL] CreateRelationshipDefinition: Create Relationship Definition
        api_response = api_instance.create_relationship_definition(create_relationship_definition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationshipDefinitionsApi->create_relationship_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_relationship_definition_request** | [**CreateRelationshipDefinitionRequest**](CreateRelationshipDefinitionRequest.md)| The definition of the new relationship. | 

### Return type

[**RelationshipDefinition**](RelationshipDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created relationship definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relationship_definition**
> RelationshipDefinition get_relationship_definition(scope, code, as_at=as_at)

[EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition

Retrieve the specified relationship definition

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:55270
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:55270"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:55270"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.RelationshipDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope of the specified relationship definition.
code = 'code_example' # str | The code of the specified relationship definition. Together with the domain and scope this uniquely              identifies the relationship definition.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the relationship definition. Defaults to return              the latest version of the definition if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetRelationshipDefinition: Get relationship definition
        api_response = api_instance.get_relationship_definition(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationshipDefinitionsApi->get_relationship_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified relationship definition. | 
 **code** | **str**| The code of the specified relationship definition. Together with the domain and scope this uniquely              identifies the relationship definition. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the relationship definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**RelationshipDefinition**](RelationshipDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested relationship definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_relationship_definition**
> RelationshipDefinition update_relationship_definition(scope, code, update_relationship_definition_request)

[EXPERIMENTAL] UpdateRelationshipDefinition: Update Relationship Definition

Update the definition of a specified existing relationship. Not all elements within a relationship definition  are modifiable due to the potential implications for values already stored against the relationship.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:55270
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:55270"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:55270"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.RelationshipDefinitionsApi(api_client)
    scope = 'scope_example' # str | The scope of the relationship definition being updated.
code = 'code_example' # str | The code of the relationship definition being updated. Together with the scope this uniquely              identifies the relationship definition.
update_relationship_definition_request = {"displayName":"Authorised traders to trade for specific portfolio ","outwardDescription":"can be traded by","inwardDescription":"can trade with portfolio"} # UpdateRelationshipDefinitionRequest | The details of relationship definition to update.

    try:
        # [EXPERIMENTAL] UpdateRelationshipDefinition: Update Relationship Definition
        api_response = api_instance.update_relationship_definition(scope, code, update_relationship_definition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationshipDefinitionsApi->update_relationship_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the relationship definition being updated. | 
 **code** | **str**| The code of the relationship definition being updated. Together with the scope this uniquely              identifies the relationship definition. | 
 **update_relationship_definition_request** | [**UpdateRelationshipDefinitionRequest**](UpdateRelationshipDefinitionRequest.md)| The details of relationship definition to update. | 

### Return type

[**RelationshipDefinition**](RelationshipDefinition.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated relationship definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

