# lusid.OrderManagementApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_transactions**](OrderManagementApi.md#book_transactions) | **POST** /api/ordermanagement/booktransactions | [EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.
[**create_orders**](OrderManagementApi.md#create_orders) | **POST** /api/ordermanagement/createorders | [EARLY ACCESS] CreateOrders: Upsert a Block and associated orders
[**move_orders**](OrderManagementApi.md#move_orders) | **POST** /api/ordermanagement/moveorders | [EARLY ACCESS] MoveOrders: Move orders to new or existing block
[**place_blocks**](OrderManagementApi.md#place_blocks) | **POST** /api/ordermanagement/placeblocks | [EARLY ACCESS] PlaceBlocks: Places blocks for a given list of placement requests.
[**run_allocation_service**](OrderManagementApi.md#run_allocation_service) | **POST** /api/ordermanagement/allocate | [EXPERIMENTAL] RunAllocationService: Runs the Allocation Service


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

