# lusid.PersonsApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_person**](PersonsApi.md#delete_person) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] Delete person
[**delete_person_access_metadata**](PersonsApi.md#delete_person_access_metadata) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EXPERIMENTAL] Delete a Person Access Metadata entry
[**delete_person_identifiers**](PersonsApi.md#delete_person_identifiers) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] Delete Person Identifiers
[**delete_person_properties**](PersonsApi.md#delete_person_properties) | **DELETE** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] Delete Person Properties
[**get_all_person_access_metadata**](PersonsApi.md#get_all_person_access_metadata) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata | [EXPERIMENTAL] Get Access Metadata rules for a Person
[**get_person**](PersonsApi.md#get_person) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code} | [EXPERIMENTAL] Get Person
[**get_person_access_metadata_by_key**](PersonsApi.md#get_person_access_metadata_by_key) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EXPERIMENTAL] Get an entry identified by a metadataKey in the Access Metadata of a Person
[**get_person_property_time_series**](PersonsApi.md#get_person_property_time_series) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties/time-series | [EXPERIMENTAL] Get Person Property Time Series
[**get_person_relations**](PersonsApi.md#get_person_relations) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relations | [EXPERIMENTAL] Get Relations for Person
[**get_person_relationships**](PersonsApi.md#get_person_relationships) | **GET** /api/persons/{idTypeScope}/{idTypeCode}/{code}/relationships | [EXPERIMENTAL] Get Relationships for Person
[**list_persons**](PersonsApi.md#list_persons) | **GET** /api/persons/{idTypeScope}/{idTypeCode} | [EXPERIMENTAL] List Persons
[**set_person_identifiers**](PersonsApi.md#set_person_identifiers) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/identifiers | [EXPERIMENTAL] Set Person Identifiers
[**set_person_properties**](PersonsApi.md#set_person_properties) | **POST** /api/persons/{idTypeScope}/{idTypeCode}/{code}/properties | [EXPERIMENTAL] Set Person Properties
[**upsert_person**](PersonsApi.md#upsert_person) | **POST** /api/persons | [EXPERIMENTAL] Upsert Person
[**upsert_person_access_metadata**](PersonsApi.md#upsert_person_access_metadata) | **PUT** /api/persons/{idTypeScope}/{idTypeCode}/{code}/metadata/{metadataKey} | [EXPERIMENTAL] Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.


# **delete_person**
> DeletedEntityResponse delete_person(id_type_scope, id_type_code, code)

[EXPERIMENTAL] Delete person

Delete a person. Deletion will be valid from the person's creation datetime.  This means that the person will no longer exist at any effective datetime from the asAt datetime of deletion.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | The scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | The code of the person identifier type.
code = 'code_example' # str | Code of the person under specified identifier type scope and code. This together with defined              identifier type uniquely identifies the person to delete.

try:
    # [EXPERIMENTAL] Delete person
    api_response = api_instance.delete_person(id_type_scope, id_type_code, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->delete_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| The scope of the person identifier type. | 
 **id_type_code** | **str**| The code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type scope and code. This together with defined              identifier type uniquely identifies the person to delete. | 

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
**200** | The response from deleting person. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person_access_metadata**
> DeletedEntityResponse delete_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at)

[EXPERIMENTAL] Delete a Person Access Metadata entry

Deletes the Person Access Metadata entry that exactly matches the provided identifier parts.    It is important to always check to verify success (or failure).

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
id_type_code = 'id_type_code_example' # str | Code of the person identifier.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
effective_at = 'effective_at_example' # str | The effective date to delete at, if this is not supplied, it will delete all data found (optional)

try:
    # [EXPERIMENTAL] Delete a Person Access Metadata entry
    api_response = api_instance.delete_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->delete_person_access_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **effective_at** | **str**| The effective date to delete at, if this is not supplied, it will delete all data found | [optional] 

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
**200** | The Access Metadata with the given metadataKey has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person_identifiers**
> DeletedEntityResponse delete_person_identifiers(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)

[EXPERIMENTAL] Delete Person Identifiers

Delete identifiers that belong to the given property keys of the person.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
property_keys = ['property_keys_example'] # list[str] | The property keys of the identifiers to delete. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". Each property must be from the \"Person\" domain. Identifiers or identifiers not specified in request will not be changed.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete the identifiers. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime of identifiers are perpetual. (optional)

try:
    # [EXPERIMENTAL] Delete Person Identifiers
    api_response = api_instance.delete_person_identifiers(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->delete_person_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **property_keys** | [**list[str]**](str.md)| The property keys of the identifiers to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. Each property must be from the \&quot;Person\&quot; domain. Identifiers or identifiers not specified in request will not be changed. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete the identifiers. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime of identifiers are perpetual. | [optional] 

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
**200** | The datetime that the identifiers were deleted from the specified person |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_person_properties**
> DeletedEntityResponse delete_person_properties(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)

[EXPERIMENTAL] Delete Person Properties

Delete all properties that belong to the given property keys of the person.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
property_keys = ['property_keys_example'] # list[str] | The property keys of the person's properties to delete. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". Each property must be from the \"Person\" domain. Properties or identifiers not specified in request will not be changed.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete the properties. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime of properties are perpetual. (optional)

try:
    # [EXPERIMENTAL] Delete Person Properties
    api_response = api_instance.delete_person_properties(id_type_scope, id_type_code, code, property_keys, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->delete_person_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **property_keys** | [**list[str]**](str.md)| The property keys of the person&#39;s properties to delete. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. Each property must be from the \&quot;Person\&quot; domain. Properties or identifiers not specified in request will not be changed. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete the properties. Defaults to the current LUSID system datetime if not specified.              Must not include an effective datetime of properties are perpetual. | [optional] 

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
**200** | The datetime that the properties were deleted from the specified person |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_person_access_metadata**
> dict(str, list[AccessMetadataValue]) get_all_person_access_metadata(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] Get Access Metadata rules for a Person

Pass the Scope and Code of the Person identifier along with the person code parameter to retrieve the associated Access Metadata

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
id_type_code = 'id_type_code_example' # str | Code of the person identifier.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

try:
    # [EXPERIMENTAL] Get Access Metadata rules for a Person
    api_response = api_instance.get_all_person_access_metadata(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_all_person_access_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Access Metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata | [optional] 

### Return type

**dict(str, list[AccessMetadataValue])**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The access metadata for the Person or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person**
> Person get_person(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] Get Person

Retrieve the definition of a person.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
code = 'code_example' # str | Code of the person under specified scope and code. This together with stated identifier type uniquely              identifies the person.
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Person\" domain to decorate onto each person.              These take the format {domain}/{scope}/{code} e.g. \"Person/ContactDetails/Address\". Defaults to include all properties if not specified. (optional)
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the person. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the person. Defaults to return the latest version of the person if not specified. (optional)

try:
    # [EXPERIMENTAL] Get Person
    api_response = api_instance.get_person(id_type_scope, id_type_code, code, property_keys=property_keys, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Person\&quot; domain to decorate onto each person.              These take the format {domain}/{scope}/{code} e.g. \&quot;Person/ContactDetails/Address\&quot;. Defaults to include all properties if not specified. | [optional] 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the person. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the person. Defaults to return the latest version of the person if not specified. | [optional] 

### Return type

[**Person**](Person.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested person definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_access_metadata_by_key**
> list[AccessMetadataValue] get_person_access_metadata_by_key(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] Get an entry identified by a metadataKey in the Access Metadata of a Person

Get a specific Person Access Metadata by specifying the corresponding identifier parts and Person code                No matching will be performed through this endpoint. To retrieve an entry, it is necessary to specify, exactly, the identifier of the entry

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
id_type_code = 'id_type_code_example' # str | Code of the person identifier.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the Access Metadata (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Access Metadata (optional)

try:
    # [EXPERIMENTAL] Get an entry identified by a metadataKey in the Access Metadata of a Person
    api_response = api_instance.get_person_access_metadata_by_key(id_type_scope, id_type_code, code, metadata_key, effective_at=effective_at, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_person_access_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the Access Metadata | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Access Metadata | [optional] 

### Return type

[**list[AccessMetadataValue]**](AccessMetadataValue.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved Person access metadata filtered by metadataKey or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_property_time_series**
> ResourceListOfPropertyInterval get_person_property_time_series(id_type_scope, id_type_code, code, property_key=property_key, as_at=as_at, filter=filter, page=page, limit=limit)

[EXPERIMENTAL] Get Person Property Time Series

List the complete time series of a person property.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely identifies the person.
property_key = 'property_key_example' # str | The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\".              Each property must be from the \"Person\" domain. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the person's property history. Defaults to return the current datetime if not supplied. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
page = 'page_example' # str | The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)

try:
    # [EXPERIMENTAL] Get Person Property Time Series
    api_response = api_instance.get_person_property_time_series(id_type_scope, id_type_code, code, property_key=property_key, as_at=as_at, filter=filter, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_person_property_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely identifies the person. | 
 **property_key** | **str**| The property key of the property that will have its history shown. These must be in the format {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;.              Each property must be from the \&quot;Person\&quot; domain. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the person&#39;s property history. Defaults to return the current datetime if not supplied. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties from a previous call to get property time series.              This value is returned from the previous call. If a pagination token is provided the filter and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 

### Return type

[**ResourceListOfPropertyInterval**](ResourceListOfPropertyInterval.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The time series of the property |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_relations**
> ResourceListOfRelation get_person_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EXPERIMENTAL] Get Relations for Person

Get relations for the specified person.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relations. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the person's relations. Defaults to return the latest LUSID AsAt time if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the relations. Users should provide null or empty string for this field until further notice. (optional)
identifier_types = ['identifier_types_example'] # list[str] | Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. (optional)

try:
    # [EXPERIMENTAL] Get Relations for Person
    api_response = api_instance.get_person_relations(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_person_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get relations. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the person&#39;s relations. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relations. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**list[str]**](str.md)| Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. They must be from the \&quot;Person\&quot; or \&quot;LegalEntity\&quot; domain.              Only identifier types stated will be used to look up relevant entities in relations. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelation**](ResourceListOfRelation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relations for the specified person. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_person_relationships**
> ResourceListOfRelationship get_person_relationships(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EXPERIMENTAL] Get Relationships for Person

Get relationships for the specified person.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person's identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person's identifier type.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. (optional)
filter = 'filter_example' # str | Expression to filter relationships. Users should provide null or empty string for this field until further notice. (optional)
identifier_types = ['identifier_types_example'] # list[str] | Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \"Person/CompanyDetails/Role\". They must be from the \"Person\" or \"LegalEntity\" domain.              Only identifier types stated will be used to look up relevant entities in relationships. If not applicable, provide an empty array. (optional)

try:
    # [EXPERIMENTAL] Get Relationships for Person
    api_response = api_instance.get_person_relationships(id_type_scope, id_type_code, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->get_person_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person&#39;s identifier type. | 
 **id_type_code** | **str**| Code of the person&#39;s identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **effective_at** | **str**| The effective datetime or cut label at which to get relationships. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to return the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter relationships. Users should provide null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**list[str]**](str.md)| Identifiers types (as property keys) used for referencing Persons or Legal Entities. These take the format              {domain}/{scope}/{code} e.g. \&quot;Person/CompanyDetails/Role\&quot;. They must be from the \&quot;Person\&quot; or \&quot;LegalEntity\&quot; domain.              Only identifier types stated will be used to look up relevant entities in relationships. If not applicable, provide an empty array. | [optional] 

### Return type

[**ResourceListOfRelationship**](ResourceListOfRelationship.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relationships for the specified person. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_persons**
> PagedResourceListOfPerson list_persons(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] List Persons

List persons which have identifiers of a specific identifier type's scope and code, and satisfies filter criteria.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing portfolios from a previous call to list portfolios. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. Defaults to 65,535 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the result set.               For example, to filter on the LUPID, use \"lusidPersonId eq 'string'\"              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Person\" domain to decorate onto each person.              These take the format {domain}/{scope}/{code} e.g. \"Person/ContactDetails/Address\". (optional)

try:
    # [EXPERIMENTAL] List Persons
    api_response = api_instance.list_persons(id_type_scope, id_type_code, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->list_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the people. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the people. Defaults to return the latest version              of each people if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolios from a previous call to list portfolios. This  value is returned from the previous call. If a pagination token is provided the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. Defaults to 65,535 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the result set.               For example, to filter on the LUPID, use \&quot;lusidPersonId eq &#39;string&#39;\&quot;              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Person\&quot; domain to decorate onto each person.              These take the format {domain}/{scope}/{code} e.g. \&quot;Person/ContactDetails/Address\&quot;. | [optional] 

### Return type

[**PagedResourceListOfPerson**](PagedResourceListOfPerson.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | People in specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_person_identifiers**
> Person set_person_identifiers(id_type_scope, id_type_code, code, set_person_identifiers_request)

[EXPERIMENTAL] Set Person Identifiers

Set identifiers of the person.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
set_person_identifiers_request = {"identifiers":{"person/PayrollSystem1/Id":{"key":"Person/PayrollSystem1/Id","value":{"labelValue":"HSI3453333"}}}} # SetPersonIdentifiersRequest | Request containing identifiers to set for the person. Identifiers not specified in request will not be changed.

try:
    # [EXPERIMENTAL] Set Person Identifiers
    api_response = api_instance.set_person_identifiers(id_type_scope, id_type_code, code, set_person_identifiers_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->set_person_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **set_person_identifiers_request** | [**SetPersonIdentifiersRequest**](SetPersonIdentifiersRequest.md)| Request containing identifiers to set for the person. Identifiers not specified in request will not be changed. | 

### Return type

[**Person**](Person.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Person with updated identifiers. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_person_properties**
> Person set_person_properties(id_type_scope, id_type_code, code, set_person_properties_request)

[EXPERIMENTAL] Set Person Properties

Set properties of the person.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier type.
id_type_code = 'id_type_code_example' # str | Code of the person identifier type.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code. This together with stated identifier type uniquely              identifies the person.
set_person_properties_request = {"properties":{"person/ContactDetails/Phone":[{"key":"Person/ContactDetails/Phone","value":{"labelValue":"01156786789"},"effectiveFrom":"2019-07-01T00:00:00.0000000+00:00"}]}} # SetPersonPropertiesRequest | Request containing properties to set for the person. Properties not specified in request will not be changed.

try:
    # [EXPERIMENTAL] Set Person Properties
    api_response = api_instance.set_person_properties(id_type_scope, id_type_code, code, set_person_properties_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->set_person_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier type. | 
 **id_type_code** | **str**| Code of the person identifier type. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. This together with stated identifier type uniquely              identifies the person. | 
 **set_person_properties_request** | [**SetPersonPropertiesRequest**](SetPersonPropertiesRequest.md)| Request containing properties to set for the person. Properties not specified in request will not be changed. | 

### Return type

[**Person**](Person.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Person with updated properties or identifiers. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_person**
> Person upsert_person(upsert_person_request)

[EXPERIMENTAL] Upsert Person

Create or update a new person under the specified scope.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
upsert_person_request = {"identifiers":{"person/HrSystem1/InternalId":{"key":"Person/HrSystem1/InternalId","value":{"labelValue":"XY10001111"}},"person/PayrollSystem1/Id":{"key":"Person/PayrollSystem1/Id","value":{"labelValue":"HSI3453456"}},"person/CompanyIntranet/LoginId":{"key":"Person/CompanyIntranet/LoginId","value":{"labelValue":"johnsmith001"}}},"properties":{"person/PersonalDetails/Name":[{"key":"Person/PersonalDetails/Name","value":{"labelValue":"John Smith"}}],"person/CompanyDetails/Role":[{"key":"Person/CompanyDetails/Role","value":{"labelValue":"SalesRepresentative"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},{"key":"Person/CompanyDetails/Role","value":{"labelValue":"CustomerServiceRepresentative"},"effectiveFrom":"2016-07-01T00:00:00.0000000+00:00"}]},"displayName":"Person1DisplayName","description":"Person1Description"} # UpsertPersonRequest | Request to create or update a person.

try:
    # [EXPERIMENTAL] Upsert Person
    api_response = api_instance.upsert_person(upsert_person_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->upsert_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_person_request** | [**UpsertPersonRequest**](UpsertPersonRequest.md)| Request to create or update a person. | 

### Return type

[**Person**](Person.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created or updated person |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_person_access_metadata**
> ResourceListOfAccessMetadataValueOf upsert_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, upsert_person_access_metadata_request, effective_at=effective_at)

[EXPERIMENTAL] Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Person Access Metadata entry in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Person Access Metadata rule or failure message if unsuccessful.                It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exist with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched.

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

# Defining host is optional and default to https://fbn-prd.lusid.com/api
configuration.host = "https://fbn-prd.lusid.com/api"
# Create an instance of the API class
api_instance = lusid.PersonsApi(lusid.ApiClient(configuration))
id_type_scope = 'id_type_scope_example' # str | Scope of the person identifier.
id_type_code = 'id_type_code_example' # str | Code of the person identifier.
code = 'code_example' # str | Code of the person under specified identifier type's scope and code.
metadata_key = 'metadata_key_example' # str | Key of the metadata entry to retrieve
upsert_person_access_metadata_request = {"metadata":[{"value":"SilverLicence","provider":"TestDataProvider"}]} # UpsertPersonAccessMetadataRequest | The Person Access Metadata entry to upsert
effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to upsert the Access Metadata (optional)

try:
    # [EXPERIMENTAL] Upsert a Person Access Metadata entry associated with a specific metadataKey. This creates or updates the data in LUSID.
    api_response = api_instance.upsert_person_access_metadata(id_type_scope, id_type_code, code, metadata_key, upsert_person_access_metadata_request, effective_at=effective_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonsApi->upsert_person_access_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_type_scope** | **str**| Scope of the person identifier. | 
 **id_type_code** | **str**| Code of the person identifier. | 
 **code** | **str**| Code of the person under specified identifier type&#39;s scope and code. | 
 **metadata_key** | **str**| Key of the metadata entry to retrieve | 
 **upsert_person_access_metadata_request** | [**UpsertPersonAccessMetadataRequest**](UpsertPersonAccessMetadataRequest.md)| The Person Access Metadata entry to upsert | 
 **effective_at** | **str**| The effectiveAt datetime at which to upsert the Access Metadata | [optional] 

### Return type

[**ResourceListOfAccessMetadataValueOf**](ResourceListOfAccessMetadataValueOf.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated or inserted item or any failure. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

