# lusid.OrderGraphApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_order_graph_blocks**](OrderGraphApi.md#list_order_graph_blocks) | **GET** /api/ordergraph/blocks | ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
[**list_order_graph_placement_children**](OrderGraphApi.md#list_order_graph_placement_children) | **GET** /api/ordergraph/placementchildren/{scope}/{code} | [EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.
[**list_order_graph_placements**](OrderGraphApi.md#list_order_graph_placements) | **GET** /api/ordergraph/placements | ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.


# **list_order_graph_blocks**
> PagedResourceListOfOrderGraphBlock list_order_graph_blocks(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, use_compliance_v2=use_compliance_v2)

ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.

Lists all blocks of orders, subject to the filter, along with the IDs of orders, placements, allocations and  executions in the block, the total quantities of each, and a simple text field describing the overall state.

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
    api_instance = lusid.OrderGraphApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | See https://support.lusid.com/knowledgebase/article/KA-01832/ (optional)
pagination_token = 'pagination_token_example' # str | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
sort_by = ['sort_by_example'] # list[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
limit = 56 # int | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
filter = '' # str | See https://support.lusid.com/knowledgebase/article/KA-01914/ (optional) (default to '')
property_keys = ['property_keys_example'] # list[str] | Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ (optional)
use_compliance_v2 = False # bool | Whether to use the V2 compliance engine when deriving compliance statuses for orders. (default: false) (optional) (default to False)

    try:
        # ListOrderGraphBlocks: Lists blocks that pass the filter provided, and builds a summary picture of the state of their associated order entities.
        api_response = api_instance.list_order_graph_blocks(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys, use_compliance_v2=use_compliance_v2)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderGraphApi->list_order_graph_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**list[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **filter** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01914/ | [optional] [default to &#39;&#39;]
 **property_keys** | [**list[str]**](str.md)| Must be block-level properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 
 **use_compliance_v2** | **bool**| Whether to use the V2 compliance engine when deriving compliance statuses for orders. (default: false) | [optional] [default to False]

### Return type

[**PagedResourceListOfOrderGraphBlock**](PagedResourceListOfOrderGraphBlock.md)

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

# **list_order_graph_placement_children**
> PagedResourceListOfOrderGraphPlacement list_order_graph_placement_children(scope, code, as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, property_keys=property_keys)

[EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.

Lists all child order placements, for the specified parent placement, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.

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
    api_instance = lusid.OrderGraphApi(api_client)
    scope = 'scope_example' # str | The parent placement's scope
code = 'code_example' # str | The parent placement's code
as_at = '2013-10-20T19:20:30+01:00' # datetime | See https://support.lusid.com/knowledgebase/article/KA-01832/ (optional)
pagination_token = 'pagination_token_example' # str | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
sort_by = ['sort_by_example'] # list[str] | Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName. (optional)
limit = 56 # int | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
property_keys = ['property_keys_example'] # list[str] | Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ (optional)

    try:
        # [EARLY ACCESS] ListOrderGraphPlacementChildren: Lists all placements for the parent placement specified by the scope and code, and builds a summary picture of the state of their associated order entities.
        api_response = api_instance.list_order_graph_placement_children(scope, code, as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderGraphApi->list_order_graph_placement_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The parent placement&#39;s scope | 
 **code** | **str**| The parent placement&#39;s code | 
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**list[str]**](str.md)| Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **property_keys** | [**list[str]**](str.md)| Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 

### Return type

[**PagedResourceListOfOrderGraphPlacement**](PagedResourceListOfOrderGraphPlacement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all child Placements for the specified Placement. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_graph_placements**
> PagedResourceListOfOrderGraphPlacement list_order_graph_placements(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)

ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.

Lists all order placements, subject to the filter, along with the IDs of the block and order that the  placement is for, each placement's quantity, the IDs of all allocations and executions in the placement  and the total quantities of those, and a simple text field describing the overall state of the placement.

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
    api_instance = lusid.OrderGraphApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | See https://support.lusid.com/knowledgebase/article/KA-01832/ (optional)
pagination_token = 'pagination_token_example' # str | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
sort_by = ['sort_by_example'] # list[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\". (optional)
limit = 56 # int | See https://support.lusid.com/knowledgebase/article/KA-01915/ (optional)
filter = '' # str | See https://support.lusid.com/knowledgebase/article/KA-01914/ (optional) (default to '')
property_keys = ['property_keys_example'] # list[str] | Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ (optional)

    try:
        # ListOrderGraphPlacements: Lists placements that pass the filter provided, and builds a summary picture of the state of their associated order entities.
        api_response = api_instance.list_order_graph_placements(as_at=as_at, pagination_token=pagination_token, sort_by=sort_by, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderGraphApi->list_order_graph_placements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| See https://support.lusid.com/knowledgebase/article/KA-01832/ | [optional] 
 **pagination_token** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **sort_by** | [**list[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot;. | [optional] 
 **limit** | **int**| See https://support.lusid.com/knowledgebase/article/KA-01915/ | [optional] 
 **filter** | **str**| See https://support.lusid.com/knowledgebase/article/KA-01914/ | [optional] [default to &#39;&#39;]
 **property_keys** | [**list[str]**](str.md)| Must be placement properties. See https://support.lusid.com/knowledgebase/article/KA-01855/ | [optional] 

### Return type

[**PagedResourceListOfOrderGraphPlacement**](PagedResourceListOfOrderGraphPlacement.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Placements in scope. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

