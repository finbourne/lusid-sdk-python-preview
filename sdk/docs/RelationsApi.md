# lusid.RelationsApi

All URIs are relative to *http://localhost:42259*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation**](RelationsApi.md#create_relation) | **POST** /api/relations/{scope}/{code} | [EXPERIMENTAL] Create Relation


# **create_relation**
> Relation create_relation(scope, code, create_relation_request, effective_at=effective_at)

[EXPERIMENTAL] Create Relation

Create a relation between two entity objects by their identifiers

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

# Defining host is optional and default to http://localhost:42259
configuration.host = "http://localhost:42259"
# Create an instance of the API class
api_instance = lusid.RelationsApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | Scope of the relation to create.
code = 'code_example' # str | Code of the relation to create.
create_relation_request = {"sourceEntityId":{"scope":"UkPortfolio","code":"PortfolioId-148176"},"targetEntityId":{"idTypeScope":"HrSystem1","idTypeCode":"InternalId","code":"XY10001111"}} # CreateRelationRequest | The details of the relation to create.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified. (optional)

try:
    # [EXPERIMENTAL] Create Relation
    api_response = api_instance.create_relation(scope, code, create_relation_request, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->create_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the relation to create. | 
 **code** | **str**| Code of the relation to create. | 
 **create_relation_request** | [**CreateRelationRequest**](CreateRelationRequest.md)| The details of the relation to create. | 
 **effective_at** | **str**| The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**Relation**](Relation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly created relation. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

