# lusid.OrderManagementApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_transactions**](OrderManagementApi.md#book_transactions) | **POST** /api/ordermanagement/booktransactions | [EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.
[**cancel_orders**](OrderManagementApi.md#cancel_orders) | **POST** /api/ordermanagement/cancelorders | [EARLY ACCESS] CancelOrders: Cancel existing orders
[**cancel_orders_and_move_remaining**](OrderManagementApi.md#cancel_orders_and_move_remaining) | **POST** /api/ordermanagement/cancelordersandmoveremaining | [EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks
[**cancel_placements**](OrderManagementApi.md#cancel_placements) | **POST** /api/ordermanagement/$cancelplacements | [EARLY ACCESS] CancelPlacements: Cancel existing placements
[**create_orders**](OrderManagementApi.md#create_orders) | **POST** /api/ordermanagement/createorders | [EARLY ACCESS] CreateOrders: Upsert a Block and associated orders
[**get_order_history**](OrderManagementApi.md#get_order_history) | **GET** /api/ordermanagement/order/{scope}/{code}/$history | [EXPERIMENTAL] GetOrderHistory: Get the history of an order and related entity changes
[**move_orders**](OrderManagementApi.md#move_orders) | **POST** /api/ordermanagement/moveorders | [EARLY ACCESS] MoveOrders: Move orders to new or existing block
[**place_blocks**](OrderManagementApi.md#place_blocks) | **POST** /api/ordermanagement/placeblocks | [EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.
[**run_allocation_service**](OrderManagementApi.md#run_allocation_service) | **POST** /api/ordermanagement/allocate | [EXPERIMENTAL] RunAllocationService: Runs the Allocation Service
[**update_orders**](OrderManagementApi.md#update_orders) | **POST** /api/ordermanagement/updateorders | [EARLY ACCESS] UpdateOrders: Update existing orders
[**update_placements**](OrderManagementApi.md#update_placements) | **POST** /api/ordermanagement/$updateplacements | [EARLY ACCESS] UpdatePlacements: Update existing placements


# **book_transactions**
> BookTransactionsResponse book_transactions(book_transactions_request, apply_fees_and_commission=apply_fees_and_commission)

[EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.

Takes a collection of allocation IDs, and maps fields from those allocations and related orders onto new transactions.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    book_transactions_request = {"allocationIds":[{"scope":"MyScope","code":"ALLOC00000123"},{"scope":"MyScope","code":"ALLOC00000456"}],"transactionProperties":{}} # BookTransactionsRequest | The allocations to create transactions for
apply_fees_and_commission = True # bool | Whether to apply fees and commissions to transactions (default: true) (optional) (default to True)

    try:
        # [EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.
        api_response = api_instance.book_transactions(book_transactions_request, apply_fees_and_commission=apply_fees_and_commission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->book_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **book_transactions_request** | [**BookTransactionsRequest**](BookTransactionsRequest.md)| The allocations to create transactions for | 
 **apply_fees_and_commission** | **bool**| Whether to apply fees and commissions to transactions (default: true) | [optional] [default to True]

### Return type

[**BookTransactionsResponse**](BookTransactionsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results from booking transactions from allocations |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_orders**
> CancelOrdersResponse cancel_orders(request_body)

[EARLY ACCESS] CancelOrders: Cancel existing orders

The response returns both the collection of successfully canceled orders, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    request_body = {"request1":{"scope":"MyScope","code":"Order00000123"},"request2":{"scope":"MyScope","code":"Order00000124"}} # dict(str, ResourceId) | The request containing the ids of the orders to be cancelled.

    try:
        # [EARLY ACCESS] CancelOrders: Cancel existing orders
        api_response = api_instance.cancel_orders(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, ResourceId)**](ResourceId.md)| The request containing the ids of the orders to be cancelled. | 

### Return type

[**CancelOrdersResponse**](CancelOrdersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled orders along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_orders_and_move_remaining**
> CancelOrdersAndMoveRemainingResponse cancel_orders_and_move_remaining(request_body)

[EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks

Cancels existing orders, reducing their quantities to those aleady placed. Any remaining quantities are moved  to new orders in new blocks. The placed quantities are distributed to the cancelled orders on a pro-rata basis.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    request_body = {"request1":{"cancelOrderId":{"scope":"MyScope","code":"Order1"},"moveRemainingToOrderId":{"scope":"MyScope","code":"Order1_Rollover"},"moveRemainingToBlockId":{"scope":"MyScope","code":"Block_Rollover"}},"request2":{"cancelOrderId":{"scope":"MyScope","code":"Order2"},"moveRemainingToOrderId":{"scope":"MyScope","code":"Order2_Rollover"},"moveRemainingToBlockId":{"scope":"MyScope","code":"Block_Rollover"}}} # dict(str, CancelOrdersAndMoveRemainingRequest) | The request containing the orders to be cancelled, and the destinations of remaining quantities.

    try:
        # [EARLY ACCESS] CancelOrdersAndMoveRemaining: Cancel existing orders and move any unplaced quantities to new orders in new blocks
        api_response = api_instance.cancel_orders_and_move_remaining(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->cancel_orders_and_move_remaining: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, CancelOrdersAndMoveRemainingRequest)**](CancelOrdersAndMoveRemainingRequest.md)| The request containing the orders to be cancelled, and the destinations of remaining quantities. | 

### Return type

[**CancelOrdersAndMoveRemainingResponse**](CancelOrdersAndMoveRemainingResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled and moved orders, along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_placements**
> CancelPlacementsResponse cancel_placements(request_body)

[EARLY ACCESS] CancelPlacements: Cancel existing placements

The response returns both the collection of successfully canceled placements, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    request_body = {"request1":{"scope":"MyScope","code":"PLAC00000123"},"request2":{"scope":"MyScope","code":"PLAC00000124"}} # dict(str, ResourceId) | The request containing the ids of the placements to be cancelled.

    try:
        # [EARLY ACCESS] CancelPlacements: Cancel existing placements
        api_response = api_instance.cancel_placements(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->cancel_placements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, ResourceId)**](ResourceId.md)| The request containing the ids of the placements to be cancelled. | 

### Return type

[**CancelPlacementsResponse**](CancelPlacementsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully cancelled placements along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_orders**
> ResourceListOfBlockAndOrders create_orders(block_and_orders_create_request)

[EARLY ACCESS] CreateOrders: Upsert a Block and associated orders

Upsert a Block and create associated orders.  This will fail if the block exists and already references orders with differing fields to the upsert request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    block_and_orders_create_request = {"requests":[{"blockId":{"scope":"MyScope","code":"BLOCK00000123"},"orders":[{"properties":{"Order/MyScope/SomeOrderProperty":{"key":"Order/MyScope/SomeOrderProperty","value":{"labelValue":"XYZ000034567"}}},"quantity":100,"id":{"scope":"MyScope","code":"ORDER00000123"},"state":"New","date":"0001-01-01T00:00:00.0000000+00:00"},{"properties":{"Order/MyScope/SomeOrderProperty":{"key":"Order/MyScope/SomeOrderProperty","value":{"labelValue":"XYZ000034567"}}},"quantity":150,"id":{"scope":"MyScope","code":"ORDER00000124"},"state":"New","date":"0001-01-01T00:00:00.0000000+00:00"}],"blockProperties":{"Block/MyScope/SomeOrderProperty":{"key":"Block/MyScope/SomeOrderProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"Instrument/default/Currency":"GBP"},"side":"Buy","type":"Limit","timeInForce":"GoodTilCancel","date":"1999-06-05T00:00:00.0000000+00:00","limitPrice":{"amount":534,"currency":"USD"}}]} # BlockAndOrdersCreateRequest | The collection of block and orders requests.

    try:
        # [EARLY ACCESS] CreateOrders: Upsert a Block and associated orders
        api_response = api_instance.create_orders(block_and_orders_create_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->create_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_and_orders_create_request** | [**BlockAndOrdersCreateRequest**](BlockAndOrdersCreateRequest.md)| The collection of block and orders requests. | 

### Return type

[**ResourceListOfBlockAndOrders**](ResourceListOfBlockAndOrders.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A collection of block and associated orders. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_history**
> ResourceListOfChangeIntervalWithOrderManagementDetail get_order_history(scope, code, as_at=as_at)

[EXPERIMENTAL] GetOrderHistory: Get the history of an order and related entity changes

Get the changes that have happened to an order and related entities.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    scope = 'scope_example' # str | The scope of the order.
code = 'code_example' # str | The code of the order.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the history of the order and related entities. Defaults              to return the latest version if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetOrderHistory: Get the history of an order and related entity changes
        api_response = api_instance.get_order_history(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->get_order_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the order. | 
 **code** | **str**| The code of the order. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the history of the order and related entities. Defaults              to return the latest version if not specified. | [optional] 

### Return type

[**ResourceListOfChangeIntervalWithOrderManagementDetail**](ResourceListOfChangeIntervalWithOrderManagementDetail.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The history of the specified order and related entities (changes that have been made to it). |  -  |
**400** | The details of the input related failure |  -  |
**404** | Order not found. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_orders**
> ResourceListOfMovedOrderToDifferentBlockResponse move_orders(move_orders_to_different_blocks_request)

[EARLY ACCESS] MoveOrders: Move orders to new or existing block

Move an order to a block, creating the block if it does not already exist.   This will fail if the block exists and already references orders with differing fields to the upsert request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    move_orders_to_different_blocks_request = {"requests":[{"destinationBlockId":{"scope":"MyScope","code":"BLOCK00000123"},"orderId":{"scope":"MyScope","code":"ORDER00000123"}}]} # MoveOrdersToDifferentBlocksRequest | The collection of order and destination block ids.

    try:
        # [EARLY ACCESS] MoveOrders: Move orders to new or existing block
        api_response = api_instance.move_orders(move_orders_to_different_blocks_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->move_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_orders_to_different_blocks_request** | [**MoveOrdersToDifferentBlocksRequest**](MoveOrdersToDifferentBlocksRequest.md)| The collection of order and destination block ids. | 

### Return type

[**ResourceListOfMovedOrderToDifferentBlockResponse**](ResourceListOfMovedOrderToDifferentBlockResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of block and order pairs for each order moved into a block, and the Id of the order&#39;s previous block (if any). |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_blocks**
> ResourceListOfPlacement place_blocks(place_blocks_request=place_blocks_request)

[EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.

The referenced block's existence will be verified.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    place_blocks_request = {"requests":[{"id":{"scope":"MyScope","code":"PLAC00000123"},"blockIds":[{"scope":"MyScope","code":"BLOCK00000123"}],"properties":{"Placement/MyScope/SomePlacementProperty":{"key":"Placement/MyScope/SomePlacementProperty","value":{"labelValue":"XYZ000034567"}}},"instrumentIdentifiers":{"Instrument/default/Currency":"GBP"},"quantity":100,"state":"New","side":"Buy","timeInForce":"GoodTilCancel","type":"Limit","createdDate":"2006-04-11T00:00:00.0000000+00:00","limitPrice":{"amount":12413.33,"currency":"USD"},"stopPrice":{"amount":124335.33,"currency":"USD"},"counterparty":"SomeCounterparty","entryType":"Manual"}]} # PlaceBlocksRequest | The request containing the blocks to the placed. (optional)

    try:
        # [EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.
        api_response = api_instance.place_blocks(place_blocks_request=place_blocks_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->place_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_blocks_request** | [**PlaceBlocksRequest**](PlaceBlocksRequest.md)| The request containing the blocks to the placed. | [optional] 

### Return type

[**ResourceListOfPlacement**](ResourceListOfPlacement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The block placements. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_allocation_service**
> AllocationServiceRunResponse run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm)

[EXPERIMENTAL] RunAllocationService: Runs the Allocation Service

This will allocate executions for a given list of placements back to their originating orders.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    resource_id = [{"scope":"MyScope","code":"PLAC00000123"},{"scope":"MyScope","code":"PLAC00000456"}] # list[ResourceId] | The List of Placement IDs for which you wish to allocate executions.
allocation_algorithm = 'allocation_algorithm_example' # str | A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \"PR-FIFO\".  This defaults to \"PR-FIFO\". (optional)

    try:
        # [EXPERIMENTAL] RunAllocationService: Runs the Allocation Service
        api_response = api_instance.run_allocation_service(resource_id, allocation_algorithm=allocation_algorithm)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->run_allocation_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**list[ResourceId]**](ResourceId.md)| The List of Placement IDs for which you wish to allocate executions. | 
 **allocation_algorithm** | **str**| A string representation of the allocation algorithm you would like to use to allocate shares from executions e.g. \&quot;PR-FIFO\&quot;.  This defaults to \&quot;PR-FIFO\&quot;. | [optional] 

### Return type

[**AllocationServiceRunResponse**](AllocationServiceRunResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The results from a run of the Allocation Service |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_orders**
> UpdateOrdersResponse update_orders(request_body)

[EARLY ACCESS] UpdateOrders: Update existing orders

The response returns both the collection of successfully updated orders, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    request_body = {"update1":{"id":{"scope":"MyScope","code":"Code1"},"quantity":101},"update2":{"id":{"scope":"MyScope","code":"Code2"},"quantity":100,"portfolioId":{"scope":"MyScope","code":"NewPortfolio"},"properties":{"Order/MyScope/OrderProperty":{"key":"Order/MyScope/OrderProperty","value":{"labelValue":"NewValue"}}}}} # dict(str, OrderUpdateRequest) | The request containing the orders to be updated.

    try:
        # [EARLY ACCESS] UpdateOrders: Update existing orders
        api_response = api_instance.update_orders(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->update_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, OrderUpdateRequest)**](OrderUpdateRequest.md)| The request containing the orders to be updated. | 

### Return type

[**UpdateOrdersResponse**](UpdateOrdersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated orders along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_placements**
> UpdatePlacementsResponse update_placements(request_body)

[EARLY ACCESS] UpdatePlacements: Update existing placements

The response returns both the collection of successfully updated placements, as well as those  that failed. For each failure, a reason is provided. It is important to check the failed set for  unsuccessful results.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://www.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://www.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.OrderManagementApi(api_client)
    request_body = {"request1":{"id":{"scope":"MyScope","code":"PLAC00000123"},"quantity":100,"properties":{"Placement/MyScope/SomePlacementProperty":{"key":"Placement/MyScope/SomePlacementProperty","value":{"labelValue":"XYZ000034567"}}},"counterparty":"SomeCounterparty","entryType":"Manual"}} # dict(str, PlacementUpdateRequest) | The request containing the placements to be updated.

    try:
        # [EARLY ACCESS] UpdatePlacements: Update existing placements
        api_response = api_instance.update_placements(request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->update_placements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, PlacementUpdateRequest)**](PlacementUpdateRequest.md)| The request containing the placements to be updated. | 

### Return type

[**UpdatePlacementsResponse**](UpdatePlacementsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully updated placements along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

