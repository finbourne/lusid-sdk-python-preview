# lusid.OrderManagementApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_transactions**](OrderManagementApi.md#book_transactions) | **POST** /api/ordermanagement/booktransactions | [EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.
[**run_allocation_service**](OrderManagementApi.md#run_allocation_service) | **POST** /api/ordermanagement/allocate | [EXPERIMENTAL] RunAllocationService: Runs the Allocation Service


# **book_transactions**
> BookTransactionsResponse book_transactions(resource_id)

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
    resource_id = [{"scope":"MyScope","code":"ALLOC00000123"},{"scope":"MyScope","code":"ALLOC00000456"}] # list[ResourceId] | The allocations to create transactions for

    try:
        # [EXPERIMENTAL] BookTransactions: Books transactions using specific allocations as a source.
        api_response = api_instance.book_transactions(resource_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderManagementApi->book_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**list[ResourceId]**](ResourceId.md)| The allocations to create transactions for | 

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

