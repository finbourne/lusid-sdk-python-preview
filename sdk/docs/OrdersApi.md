# lusid.OrdersApi

All URIs are relative to *http://local-unit-test-server.lusid.com:39510*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_order**](OrdersApi.md#delete_order) | **DELETE** /api/orders/{scope}/{code} | [EXPERIMENTAL] Delete order
[**get_order**](OrdersApi.md#get_order) | **GET** /api/orders/{scope}/{code} | [EXPERIMENTAL] Get Order
[**list_orders**](OrdersApi.md#list_orders) | **GET** /api/orders | [EXPERIMENTAL] List Orders
[**upsert_order_properties**](OrdersApi.md#upsert_order_properties) | **POST** /api/orders/{scope}/properties | [EXPERIMENTAL] Upsert Order Properties
[**upsert_orders**](OrdersApi.md#upsert_orders) | **POST** /api/orders | [EXPERIMENTAL] Upsert Order


# **delete_order**
> DeletedEntityResponse delete_order(scope, code)

[EXPERIMENTAL] Delete order

Delete an order. Deletion will be valid from the order's creation datetime.  This means that the order will no longer exist at any effective datetime from the asAt datetime of deletion.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:39510
configuration.host = "http://local-unit-test-server.lusid.com:39510"
# Create an instance of the API class
api_instance = lusid.OrdersApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The order scope.
code = 'code_example' # str | The order's code. This, together with the scope uniquely identifies the order to delete.

try:
    # [EXPERIMENTAL] Delete order
    api_response = api_instance.delete_order(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->delete_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The order scope. | 
 **code** | **str**| The order&#39;s code. This, together with the scope uniquely identifies the order to delete. | 

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
**200** | The response from deleting an order. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(scope, code, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] Get Order

Fetch an Order that matches the specified identifier

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:39510
configuration.host = "http://local-unit-test-server.lusid.com:39510"
# Create an instance of the API class
api_instance = lusid.OrdersApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope to which the order belongs.
code = 'code_example' # str | The order's unique identifier.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Orders\" domain to decorate onto the order.              These take the format {domain}/{scope}/{code} e.g. \"Orders/system/Name\". (optional)

try:
    # [EXPERIMENTAL] Get Order
    api_response = api_instance.get_order(scope, code, as_at=as_at, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the order belongs. | 
 **code** | **str**| The order&#39;s unique identifier. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto the order.              These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;. | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The order matching the given identifier. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> PagedResourceListOfOrder list_orders(as_at=as_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] List Orders

Fetch the last pre-AsAt date version of each order in scope (does not fetch the entire history).

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:39510
configuration.host = "http://local-unit-test-server.lusid.com:39510"
# Create an instance of the API class
api_instance = lusid.OrdersApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing orders from a previous call to list orders.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = '' # str | Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. (optional) (default to '')
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the \"Orders\" domain to decorate onto each order.                  These take the format {domain}/{scope}/{code} e.g. \"Orders/system/Name\". (optional)

try:
    # [EXPERIMENTAL] List Orders
    api_response = api_instance.list_orders(as_at=as_at, page=page, sort_by=sort_by, start=start, limit=limit, filter=filter, property_keys=property_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to retrieve the order. Defaults to return the latest version of the order if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing orders from a previous call to list orders.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, effectiveAt, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid. | [optional] [default to &#39;&#39;]
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the \&quot;Orders\&quot; domain to decorate onto each order.                  These take the format {domain}/{scope}/{code} e.g. \&quot;Orders/system/Name\&quot;. | [optional] 

### Return type

[**PagedResourceListOfOrder**](PagedResourceListOfOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Orders in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_order_properties**
> UpsertOrderPropertiesResponse upsert_order_properties(scope, upsert_order_properties_request=upsert_order_properties_request)

[EXPERIMENTAL] Upsert Order Properties

Update or insert one or more order properties for existing orders with given ids. Each order property will be updated  if it already exists and inserted if it does not. If any properties fail to be updated or inserted, none will be updated or inserted and  the reason for the failure will be returned.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:39510
configuration.host = "http://local-unit-test-server.lusid.com:39510"
# Create an instance of the API class
api_instance = lusid.OrdersApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope to which the orders belong.
upsert_order_properties_request = [{"properties":[{"key":"Order/MyScope/SomeOrderProperty","value":{"labelValue":"XYZ000034567"}},{"key":"Order/MyScope/AnotherOrderProperty","value":{"labelValue":"XYZ000056748"},"effectiveFrom":"2018-05-10T12:00:00.0000000+00:00","effectiveUntil":"2019-07-12T12:00:00.0000000+00:00"},{"key":"Order/MyScope/AdditionalOrderProperty","value":{"labelValue":"XYZ000099134"},"effectiveFrom":"2020-03-05T00:00:00.0000000+00:00"}],"id":"ORD00000123"}] # list[UpsertOrderPropertiesRequest] | A collection of order property upsert requests. (optional)

try:
    # [EXPERIMENTAL] Upsert Order Properties
    api_response = api_instance.upsert_order_properties(scope, upsert_order_properties_request=upsert_order_properties_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->upsert_order_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to which the orders belong. | 
 **upsert_order_properties_request** | [**list[UpsertOrderPropertiesRequest]**](UpsertOrderPropertiesRequest.md)| A collection of order property upsert requests. | [optional] 

### Return type

[**UpsertOrderPropertiesResponse**](UpsertOrderPropertiesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | An upsert order properties response. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_orders**
> ResourceListOfOrder upsert_orders(order_set_request=order_set_request)

[EXPERIMENTAL] Upsert Order

Upsert; update existing orders with given ids, or create new orders otherwise.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:39510
configuration.host = "http://local-unit-test-server.lusid.com:39510"
# Create an instance of the API class
api_instance = lusid.OrdersApi(lusid.ApiClient(configuration))
order_set_request = {"orderRequests":[{"properties":{"order/MyScope/SomeOrderProperty":{"key":"Order/MyScope/SomeOrderProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"instrument/default/Currency":"GBP"},"quantity":100,"side":"Buy","orderBookId":{"scope":"MyScope","code":"UKEQ Orders"},"portfolioId":{"scope":"MyScope","code":"UK Equity"},"id":{"scope":"MyScope","code":"ORD00000123"}}]} # OrderSetRequest | The collection of order requests. (optional)

try:
    # [EXPERIMENTAL] Upsert Order
    api_response = api_instance.upsert_orders(order_set_request=order_set_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->upsert_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_set_request** | [**OrderSetRequest**](OrderSetRequest.md)| The collection of order requests. | [optional] 

### Return type

[**ResourceListOfOrder**](ResourceListOfOrder.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

