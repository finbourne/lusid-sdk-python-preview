# lusid.BlocksApi

All URIs are relative to *http://local-unit-test-server.lusid.com:34515*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_block**](BlocksApi.md#delete_block) | **DELETE** /api/blocks/{scope}/{code} | [EXPERIMENTAL] Delete block
[**get_block**](BlocksApi.md#get_block) | **GET** /api/blocks/{scope}/{code} | [EXPERIMENTAL] Get Block
[**list_blocks**](BlocksApi.md#list_blocks) | **GET** /api/blocks | [EXPERIMENTAL] List Blocks
[**upsert_blocks**](BlocksApi.md#upsert_blocks) | **POST** /api/blocks | [EXPERIMENTAL] Upsert Block


# **delete_block**
> DeletedEntityResponse delete_block(scope, code)

[EXPERIMENTAL] Delete block

Delete an block. Deletion will be valid from the block's creation datetime.  This means that the block will no longer exist at any effective datetime from the asAt datetime of deletion.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:34515
configuration.host = "http://local-unit-test-server.lusid.com:34515"
# Create an instance of the API class
api_instance = lusid.BlocksApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The block scope.
code = 'code_example' # str | The block's code. This, together with the scope uniquely identifies the block to delete.

try:
    # [EXPERIMENTAL] Delete block
    api_response = api_instance.delete_block(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->delete_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The block scope. | 
 **code** | **str**| The block&#39;s code. This, together with the scope uniquely identifies the block to delete. | 

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
**200** | The response from deleting an block. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block**
> Block get_block(scope, code, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] Get Block

Fetch a Block that matches the specified identifier

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:34515
configuration.host = "http://local-unit-test-server.lusid.com:34515"
# Create an instance of the API class
api_instance = lusid.BlocksApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope to which the block belongs.
code = 'code_example' # str | The block's unique identifier.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the block. Defaults to return the latest version of the block if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Block\" domain to decorate onto the block.              These take the format {domain}/{scope}/{code} e.g. \"Block/system/Name\". (optional)

try:
    # [EXPERIMENTAL] Get Block
    api_response = api_instance.get_block(scope, code, as_at=as_at, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->get_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the block belongs. | 
 **code** | **str**| The block&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the block. Defaults to return the latest version of the block if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Block\&quot; domain to decorate onto the block.              These take the format {domain}/{scope}/{code} e.g. \&quot;Block/system/Name\&quot;. | [optional] 

### Return type

[**Block**](Block.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The block matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_blocks**
> PagedResourceListOfBlock list_blocks(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] List Blocks

Fetch the last pre-AsAt date version of each block in scope (does not fetch the entire history).

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:34515
configuration.host = "http://local-unit-test-server.lusid.com:34515"
# Create an instance of the API class
api_instance = lusid.BlocksApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the block. Defaults to return the latest version of the block if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing blocks from a previous call to list blocks.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = '' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional) (default to '')
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Block\" domain to decorate onto each block.                  These take the format {domain}/{scope}/{code} e.g. \"Block/system/Name\". (optional)

try:
    # [EXPERIMENTAL] List Blocks
    api_response = api_instance.list_blocks(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->list_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the block. Defaults to return the latest version of the block if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing blocks from a previous call to list blocks.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] [default to &#39;&#39;]
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Block\&quot; domain to decorate onto each block.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Block/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfBlock**](PagedResourceListOfBlock.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Blocks in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_blocks**
> ResourceListOfBlock upsert_blocks(body=body)

[EXPERIMENTAL] Upsert Block

Upsert; update existing blocks with given ids, or create new blocks otherwise.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:34515
configuration.host = "http://local-unit-test-server.lusid.com:34515"
# Create an instance of the API class
api_instance = lusid.BlocksApi(lusid.ApiClient(configuration))
body = {} # object | The collection of block requests. (optional)

try:
    # [EXPERIMENTAL] Upsert Block
    api_response = api_instance.upsert_blocks(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlocksApi->upsert_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| The collection of block requests. | [optional] 

### Return type

[**ResourceListOfBlock**](ResourceListOfBlock.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of blocks. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

