# lusid.LegalEntitiesApi

All URIs are relative to *http://localhost:46318*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_legal_entity**](LegalEntitiesApi.md#delete_legal_entity) | **DELETE** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] Delete legal entity
[**get_legal_entity**](LegalEntitiesApi.md#get_legal_entity) | **GET** /api/legalentities/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] Get Legal Entity
[**upsert_legal_entity**](LegalEntitiesApi.md#upsert_legal_entity) | **POST** /api/legalentities | [EXPERIMENTAL] Upsert Legal Entity


# **delete_legal_entity**
> DeletedEntityResponse delete_legal_entity(id_type_scope, id_type_code, code)

[EXPERIMENTAL] Delete legal entity

Delete a legal entity. Deletion will be valid from the legal entity's creation datetime.  This means that the legal entity will no longer exist at any effective datetime from the asAt datetime of deletion.

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

# Defining host is optional and default to http://localhost:46318
configuration.host = "http://localhost:46318"
# Create an instance of the API class
api_instance = lusid.LegalEntitiesApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | The scope of the legal entity identifier type.
id_type_code = 'id_type_code_example' # str | The code of the legal entity identifier type.
code = 'code_example' # str | Code of the legal entity under specified identifier type scope and code. This together with defined              identifier type uniquely identifies the legal entity to delete.

try:
    # [EXPERIMENTAL] Delete legal entity
    api_response = api_instance.delete_legal_entity(id_type_scope, id_type_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalEntitiesApi->delete_legal_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| The scope of the legal entity identifier type. | 
 **id_type_code** | **str**| The code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified identifier type scope and code. This together with defined              identifier type uniquely identifies the legal entity to delete. | 

### Return type

[**DeletedEntityResponse**](DeletedEntityResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response from deleting legal entity. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_entity**
> LegalEntity get_legal_entity(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] Get Legal Entity

Retrieve the definition of a legal entity.

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

# Defining host is optional and default to http://localhost:46318
configuration.host = "http://localhost:46318"
# Create an instance of the API class
api_instance = lusid.LegalEntitiesApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the legal entity identifier type.
id_type_code = 'id_type_code_example' # str | Code of the legal entity identifier type.
code = 'code_example' # str | Code of the legal entity under specified scope and code. This together with stated identifier type uniquely              identifies the legal entity.
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"LegalEntity\" domain to decorate onto each legal entity.              These take the format {domain}/{scope}/{code} e.g. \"LegalEntity/ContactDetails/Address\". Defaults to include all properties if not specified. (optional)
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the legal entity. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the legal entity. Defaults to return the latest version of the legal entity if not specified. (optional)

try:
    # [EXPERIMENTAL] Get Legal Entity
    api_response = api_instance.get_legal_entity(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalEntitiesApi->get_legal_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the legal entity identifier type. | 
 **id_type_code** | **str**| Code of the legal entity identifier type. | 
 **code** | **str**| Code of the legal entity under specified scope and code. This together with stated identifier type uniquely              identifies the legal entity. | 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;LegalEntity\&quot; domain to decorate onto each legal entity.              These take the format {domain}/{scope}/{code} e.g. \&quot;LegalEntity/ContactDetails/Address\&quot;. Defaults to include all properties if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the legal entity. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the legal entity. Defaults to return the latest version of the legal entity if not specified. | [optional] 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested legal entity definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_legal_entity**
> LegalEntity upsert_legal_entity(upsert_legal_entity_request)

[EXPERIMENTAL] Upsert Legal Entity

Create or update new legal entity under specified scope

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

# Defining host is optional and default to http://localhost:46318
configuration.host = "http://localhost:46318"
# Create an instance of the API class
api_instance = lusid.LegalEntitiesApi(lusid.ApiClient(configuration))
upsert_legal_entity_request = {"identifiers":{"legalEntity/ExternalIdentifier/LEI":{"key":"LegalEntity/ExternalIdentifier/LEI","value":{"labelValue":"LEI_12345678"}},"legalEntity/InternalIdentifier/InternalLeiId":{"key":"LegalEntity/InternalIdentifier/InternalLeiId","value":{"labelValue":"Internal_XHSP2038"}}},"properties":{"legalEntity/Details/Name":{"key":"LegalEntity/Details/Name","value":{"labelValue":"Legal Entity Inc."}},"legalEntity/Details/Country":{"key":"LegalEntity/Details/Country","value":{"labelValue":"United Kingdom"},"effectiveFrom":"2016-01-01T00:00:00+00:00"},"legalEntity/Status/Active":{"key":"LegalEntity/Status/Active","value":{"labelValue":"Active"},"effectiveFrom":"2016-07-01T00:00:00+00:00"}}} # UpsertLegalEntityRequest | Request to create or update a legal entity.

try:
    # [EXPERIMENTAL] Upsert Legal Entity
    api_response = api_instance.upsert_legal_entity(upsert_legal_entity_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegalEntitiesApi->upsert_legal_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_legal_entity_request** | [**UpsertLegalEntityRequest**](UpsertLegalEntityRequest.md)| Request to create or update a legal entity. | 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created or updated legal entity |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

