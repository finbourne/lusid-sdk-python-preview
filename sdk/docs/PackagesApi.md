# lusid.PackagesApi

All URIs are relative to *http://local-unit-test-server.lusid.com:54759*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_package**](PackagesApi.md#delete_package) | **DELETE** /api/packages/{scope}/{code} | [EXPERIMENTAL] DeletePackage: Delete package
[**get_package**](PackagesApi.md#get_package) | **GET** /api/packages/{scope}/{code} | [EXPERIMENTAL] GetPackage: Get Package
[**list_packages**](PackagesApi.md#list_packages) | **GET** /api/packages | [EXPERIMENTAL] ListPackages: List Packages
[**upsert_packages**](PackagesApi.md#upsert_packages) | **POST** /api/packages | [EXPERIMENTAL] UpsertPackages: Upsert Package


# **delete_package**
> DeletedEntityResponse delete_package(scope, code)

[EXPERIMENTAL] DeletePackage: Delete package

Delete an package. Deletion will be valid from the package's creation datetime.  This means that the package will no longer exist at any effective datetime from the asAt datetime of deletion.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:54759
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:54759"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:54759"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PackagesApi(api_client)
    scope = 'scope_example' # str | The package scope.
code = 'code_example' # str | The package's code. This, together with the scope uniquely identifies the package to delete.

    try:
        # [EXPERIMENTAL] DeletePackage: Delete package
        api_response = api_instance.delete_package(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->delete_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The package scope. | 
 **code** | **str**| The package&#39;s code. This, together with the scope uniquely identifies the package to delete. | 

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
**200** | The response from deleting an package. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package**
> Package get_package(scope, code, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetPackage: Get Package

Fetch a Package that matches the specified identifier

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:54759
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:54759"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:54759"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PackagesApi(api_client)
    scope = 'scope_example' # str | The scope to which the package belongs.
code = 'code_example' # str | The package's unique identifier.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the package. Defaults to return the latest version of the package if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Package\" domain to decorate onto the package.              These take the format {domain}/{scope}/{code} e.g. \"Package/system/Name\". (optional)

    try:
        # [EXPERIMENTAL] GetPackage: Get Package
        api_response = api_instance.get_package(scope, code, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->get_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the package belongs. | 
 **code** | **str**| The package&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the package. Defaults to return the latest version of the package if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Package\&quot; domain to decorate onto the package.              These take the format {domain}/{scope}/{code} e.g. \&quot;Package/system/Name\&quot;. | [optional] 

### Return type

[**Package**](Package.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The package matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packages**
> PagedResourceListOfPackage list_packages(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListPackages: List Packages

Fetch the last pre-AsAt date version of each package in scope (does not fetch the entire history).

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:54759
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:54759"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:54759"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PackagesApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the package. Defaults to return the latest version of the package if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing packages from a previous call to list packages.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = '' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional) (default to '')
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Package\" domain to decorate onto each package.                  These take the format {domain}/{scope}/{code} e.g. \"Package/system/Name\". (optional)

    try:
        # [EXPERIMENTAL] ListPackages: List Packages
        api_response = api_instance.list_packages(as_at=as_at, page=page, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->list_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the package. Defaults to return the latest version of the package if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing packages from a previous call to list packages.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] [default to &#39;&#39;]
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Package\&quot; domain to decorate onto each package.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Package/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfPackage**](PagedResourceListOfPackage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Packages in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_packages**
> ResourceListOfPackage upsert_packages(package_set_request=package_set_request)

[EXPERIMENTAL] UpsertPackages: Upsert Package

Upsert; update existing packages with given ids, or create new packages otherwise.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:54759
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:54759"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:54759"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PackagesApi(api_client)
    package_set_request = {"requests":[{"id":{"scope":"MyScope","code":"PACK00000123"},"orderIds":[{"scope":"MyScope","code":"ORDER00000123"}],"orderInstructionIds":[{"scope":"MyScope","code":"INSTR00000123"}],"properties":{"package/MyScope/SomePackageProperty":{"key":"Package/MyScope/SomePackageProperty","value":{"labelValue":"XYZ000034567"}}}}]} # PackageSetRequest | The collection of package requests. (optional)

    try:
        # [EXPERIMENTAL] UpsertPackages: Upsert Package
        api_response = api_instance.upsert_packages(package_set_request=package_set_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PackagesApi->upsert_packages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_set_request** | [**PackageSetRequest**](PackageSetRequest.md)| The collection of package requests. | [optional] 

### Return type

[**ResourceListOfPackage**](ResourceListOfPackage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of packages. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

