# lusid.PortfoliosApi

All URIs are relative to *https://fbn-prd.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_key_from_portfolio_access_metadata**](PortfoliosApi.md#delete_key_from_portfolio_access_metadata) | **DELETE** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EXPERIMENTAL] Delete a Portfolio Access Metadata Rule
[**delete_portfolio**](PortfoliosApi.md#delete_portfolio) | **DELETE** /api/portfolios/{scope}/{code} | Delete portfolio
[**delete_portfolio_properties**](PortfoliosApi.md#delete_portfolio_properties) | **DELETE** /api/portfolios/{scope}/{code}/properties | Delete portfolio properties
[**delete_portfolio_returns**](PortfoliosApi.md#delete_portfolio_returns) | **DELETE** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$delete | [EXPERIMENTAL] Delete Returns
[**get_portfolio**](PortfoliosApi.md#get_portfolio) | **GET** /api/portfolios/{scope}/{code} | Get portfolio
[**get_portfolio_aggregate_returns**](PortfoliosApi.md#get_portfolio_aggregate_returns) | **GET** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/aggregated | [EXPERIMENTAL] Aggregate Returns (This is a deprecated endpoint).
[**get_portfolio_aggregated_returns**](PortfoliosApi.md#get_portfolio_aggregated_returns) | **POST** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode}/$aggregated | [EXPERIMENTAL] Aggregated Returns
[**get_portfolio_commands**](PortfoliosApi.md#get_portfolio_commands) | **GET** /api/portfolios/{scope}/{code}/commands | [EARLY ACCESS] Get portfolio commands
[**get_portfolio_metadata**](PortfoliosApi.md#get_portfolio_metadata) | **GET** /api/portfolios/{scope}/{code}/metadata | [EXPERIMENTAL] Get access metadata rules for a portfolio
[**get_portfolio_properties**](PortfoliosApi.md#get_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties | Get portfolio properties
[**get_portfolio_property_time_series**](PortfoliosApi.md#get_portfolio_property_time_series) | **GET** /api/portfolios/{scope}/{code}/properties/time-series | [EXPERIMENTAL] Get portfolio property time series
[**get_portfolio_relations**](PortfoliosApi.md#get_portfolio_relations) | **GET** /api/portfolios/{scope}/{code}/relations | [EXPERIMENTAL] Get portfolio relations
[**get_portfolio_relationships**](PortfoliosApi.md#get_portfolio_relationships) | **GET** /api/portfolios/{scope}/{code}/relationships | [EXPERIMENTAL] Get portfolio relationships
[**get_portfolio_returns**](PortfoliosApi.md#get_portfolio_returns) | **GET** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | [EARLY ACCESS] Get Returns
[**get_portfolios_access_metadata_by_key**](PortfoliosApi.md#get_portfolios_access_metadata_by_key) | **GET** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EXPERIMENTAL] Get an entry identified by a metadataKey in the access metadata object
[**list_portfolio_properties**](PortfoliosApi.md#list_portfolio_properties) | **GET** /api/portfolios/{scope}/{code}/properties/list | [EXPERIMENTAL] Get portfolio properties
[**list_portfolios**](PortfoliosApi.md#list_portfolios) | **GET** /api/portfolios | List portfolios
[**list_portfolios_for_scope**](PortfoliosApi.md#list_portfolios_for_scope) | **GET** /api/portfolios/{scope} | List portfolios for scope
[**update_portfolio**](PortfoliosApi.md#update_portfolio) | **PUT** /api/portfolios/{scope}/{code} | Update portfolio
[**upsert_portfolio_access_metadata**](PortfoliosApi.md#upsert_portfolio_access_metadata) | **PUT** /api/portfolios/{scope}/{code}/metadata/{metadataKey} | [EXPERIMENTAL] Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.
[**upsert_portfolio_properties**](PortfoliosApi.md#upsert_portfolio_properties) | **POST** /api/portfolios/{scope}/{code}/properties | Upsert portfolio properties
[**upsert_portfolio_returns**](PortfoliosApi.md#upsert_portfolio_returns) | **POST** /api/portfolios/{scope}/{code}/returns/{returnScope}/{returnCode} | [EARLY ACCESS] Upsert Returns


# **delete_key_from_portfolio_access_metadata**
> DeletedEntityResponse delete_key_from_portfolio_access_metadata(scope, code, metadata_key, effective_at=effective_at)

[EXPERIMENTAL] Delete a Portfolio Access Metadata Rule

Delete the Portfolio Access Metadata Rule that exactly matches the provided identifier parts

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the Quote Access Metadata Rule to retrieve.
code = 'code_example' # str | Portfolio code
metadata_key = 'metadata_key_example' # str | The metadataKey identifying the access metadata entry to delete
effective_at = 'effective_at_example' # str | The effective date to delete at, if this is not supplied, it will delete all data found (optional)

    try:
        # [EXPERIMENTAL] Delete a Portfolio Access Metadata Rule
        api_response = api_instance.delete_key_from_portfolio_access_metadata(scope, code, metadata_key, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->delete_key_from_portfolio_access_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Quote Access Metadata Rule to retrieve. | 
 **code** | **str**| Portfolio code | 
 **metadata_key** | **str**| The metadataKey identifying the access metadata entry to delete | 
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
**200** | The rule that has been deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio**
> DeletedEntityResponse delete_portfolio(scope, code)

Delete portfolio

Delete a particular portfolio.                The deletion will take effect from the portfolio's creation datetime. This means that the portfolio will no longer exist at any effective datetime, as per the asAt datetime of deletion.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.

    try:
        # Delete portfolio
        api_response = api_instance.delete_portfolio(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->delete_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 

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
**200** | The datetime that the portfolio was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_properties**
> DeletedEntityResponse delete_portfolio_properties(scope, code, property_keys, effective_at=effective_at)

Delete portfolio properties

Delete one or more properties from a particular portfolio. If the properties are time-variant then an effective datetime from which  to delete properties must be specified. If the properties are perpetual then it is invalid to specify an effective datetime for deletion.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
property_keys = ['property_keys_example'] # list[str] | The property keys of the properties to delete. These must take the format              {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. Each property must be from the 'Portfolio' domain.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified 'effectiveAt' datetime. If the 'effectiveAt' is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. (optional)

    try:
        # Delete portfolio properties
        api_response = api_instance.delete_portfolio_properties(scope, code, property_keys, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->delete_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **property_keys** | [**list[str]**](str.md)| The property keys of the properties to delete. These must take the format              {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. Each property must be from the &#39;Portfolio&#39; domain. | 
 **effective_at** | **str**| The effective datetime or cut label at which to delete time-variant properties from.              The property must exist at the specified &#39;effectiveAt&#39; datetime. If the &#39;effectiveAt&#39; is not provided or is              before the time-variant property exists then a failure is returned. Do not specify this parameter if any of              the properties to delete are perpetual. | [optional] 

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
**200** | The datetime that the properties were deleted from the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio_returns**
> DeletedEntityResponse delete_portfolio_returns(scope, code, return_scope, return_code, from_effective_at, to_effective_at, period=period)

[EXPERIMENTAL] Delete Returns

Cancel one or more Returns which exist into the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio.
code = 'code_example' # str | The code of the  Portfolio.
return_scope = 'return_scope_example' # str | The scope of the Returns.
return_code = 'return_code_example' # str | The code of the Returns.
from_effective_at = 'from_effective_at_example' # str | The start date from which to delete the Returns.
to_effective_at = 'to_effective_at_example' # str | The end date from which to delete the Returns.
period = 'period_example' # str | The Period (Daily or Monthly) of the Returns to be deleted. (optional)

    try:
        # [EXPERIMENTAL] Delete Returns
        api_response = api_instance.delete_portfolio_returns(scope, code, return_scope, return_code, from_effective_at, to_effective_at, period=period)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->delete_portfolio_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **from_effective_at** | **str**| The start date from which to delete the Returns. | 
 **to_effective_at** | **str**| The end date from which to delete the Returns. | 
 **period** | **str**| The Period (Daily or Monthly) of the Returns to be deleted. | [optional] 

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
**200** | The successfully deleted Returns data along with any failures |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio**
> Portfolio get_portfolio(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

Get portfolio

Retrieve the definition of a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Portfolio' domain to decorate onto the portfolio.              These must take the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)

    try:
        # Get portfolio
        api_response = api_instance.get_portfolio(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the portfolio definition. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio definition. Defaults to returning the latest version of the portfolio definition if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto the portfolio.              These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolio definition |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_aggregate_returns**
> ResourceListOfAggregatedReturn get_portfolio_aggregate_returns(scope, code, return_scope, return_code, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, composite_method=composite_method, period=period, output_frequency=output_frequency, metrics=metrics, as_at=as_at, alternative_inc_date=alternative_inc_date)

[EXPERIMENTAL] Aggregate Returns (This is a deprecated endpoint).

Aggregate Returns which are on the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio.
code = 'code_example' # str | The code of the  Portfolio.
return_scope = 'return_scope_example' # str | The scope of the Returns.
return_code = 'return_code_example' # str | The code of the Returns.
recipe_id_scope = 'recipe_id_scope_example' # str | The Recipe Scope for getting the fx rates (optional)
recipe_id_code = 'recipe_id_code_example' # str | The Recipe Code for getting the fx rates (optional)
from_effective_at = 'from_effective_at_example' # str | The start date from which to calculate the Returns. (optional)
to_effective_at = 'to_effective_at_example' # str | The end date for which to calculate the Returns. (optional)
composite_method = 'composite_method_example' # str | The method used to calculate the Portfolio performance:              Equal/Asset. (optional)
period = 'period_example' # str | The type of the returns used to calculate the aggregation result: Daily/Monthly. (optional)
output_frequency = 'output_frequency_example' # str | The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. (optional)
metrics = ['metrics_example'] # list[str] | Determines what type of returns should be calculated, see https://support.lusid.com/knowledgebase/article/KA-01675/en-us for a list of available metrics. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)
alternative_inc_date = 'alternative_inc_date_example' # str | The date from which to consider the Returns on the Portfolio, if this is different from the date when Returns begin. Can be a date string or Portfolio property. (optional)

    try:
        # [EXPERIMENTAL] Aggregate Returns (This is a deprecated endpoint).
        api_response = api_instance.get_portfolio_aggregate_returns(scope, code, return_scope, return_code, recipe_id_scope=recipe_id_scope, recipe_id_code=recipe_id_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, composite_method=composite_method, period=period, output_frequency=output_frequency, metrics=metrics, as_at=as_at, alternative_inc_date=alternative_inc_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_aggregate_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **recipe_id_scope** | **str**| The Recipe Scope for getting the fx rates | [optional] 
 **recipe_id_code** | **str**| The Recipe Code for getting the fx rates | [optional] 
 **from_effective_at** | **str**| The start date from which to calculate the Returns. | [optional] 
 **to_effective_at** | **str**| The end date for which to calculate the Returns. | [optional] 
 **composite_method** | **str**| The method used to calculate the Portfolio performance:              Equal/Asset. | [optional] 
 **period** | **str**| The type of the returns used to calculate the aggregation result: Daily/Monthly. | [optional] 
 **output_frequency** | **str**| The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly. | [optional] 
 **metrics** | [**list[str]**](str.md)| Determines what type of returns should be calculated, see https://support.lusid.com/knowledgebase/article/KA-01675/en-us for a list of available metrics. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 
 **alternative_inc_date** | **str**| The date from which to consider the Returns on the Portfolio, if this is different from the date when Returns begin. Can be a date string or Portfolio property. | [optional] 

### Return type

[**ResourceListOfAggregatedReturn**](ResourceListOfAggregatedReturn.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_aggregated_returns**
> ResourceListOfAggregatedReturn get_portfolio_aggregated_returns(scope, code, return_scope, return_code, aggregated_returns_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, alternative_inc_date=alternative_inc_date)

[EXPERIMENTAL] Aggregated Returns

Aggregate Returns which are on the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio.
code = 'code_example' # str | The code of the  Portfolio.
return_scope = 'return_scope_example' # str | The scope of the Returns.
return_code = 'return_code_example' # str | The code of the Returns.
aggregated_returns_request = {"metrics":[{"window":"1Y","allowPartial":false,"annualised":false,"withFee":true,"alias":"1M"}],"recipeId":{"scope":"TestScope","code":"default"},"compositeMethod":"Asset","period":"Daily","outputFrequency":"Daily"} # AggregatedReturnsRequest | The request used in the AggregatedReturns.
from_effective_at = 'from_effective_at_example' # str | The start date from which to calculate the Returns. (optional)
to_effective_at = 'to_effective_at_example' # str | The end date for which to calculate the Returns. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)
alternative_inc_date = 'alternative_inc_date_example' # str | The date from which to consider the Returns on the Portfolio, if this is different from the date when Returns begin. Can be a date string or Portfolio property. (optional)

    try:
        # [EXPERIMENTAL] Aggregated Returns
        api_response = api_instance.get_portfolio_aggregated_returns(scope, code, return_scope, return_code, aggregated_returns_request, from_effective_at=from_effective_at, to_effective_at=to_effective_at, as_at=as_at, alternative_inc_date=alternative_inc_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_aggregated_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **aggregated_returns_request** | [**AggregatedReturnsRequest**](AggregatedReturnsRequest.md)| The request used in the AggregatedReturns. | 
 **from_effective_at** | **str**| The start date from which to calculate the Returns. | [optional] 
 **to_effective_at** | **str**| The end date for which to calculate the Returns. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 
 **alternative_inc_date** | **str**| The date from which to consider the Returns on the Portfolio, if this is different from the date when Returns begin. Can be a date string or Portfolio property. | [optional] 

### Return type

[**ResourceListOfAggregatedReturn**](ResourceListOfAggregatedReturn.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The aggregated returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_commands**
> ResourceListOfProcessedCommand get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter, page=page, limit=limit)

[EARLY ACCESS] Get portfolio commands

Get all the commands that modified a particular portfolio, including any input transactions.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
from_as_at = '2013-10-20T19:20:30+01:00' # datetime | The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. (optional)
to_as_at = '2013-10-20T19:20:30+01:00' # datetime | The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the User ID, specify \"userId.id eq 'string'\".              For more information about filtering, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
page = 'page_example' # str | The pagination token to use to continue listing commands; this value is returned from the previous call. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 500 if not specified. (optional)

    try:
        # [EARLY ACCESS] Get portfolio commands
        api_response = api_instance.get_portfolio_commands(scope, code, from_as_at=from_as_at, to_as_at=to_as_at, filter=filter, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **from_as_at** | **datetime**| The lower bound asAt datetime (inclusive) from which to retrieve commands. There is no lower bound if this is not specified. | [optional] 
 **to_as_at** | **datetime**| The upper bound asAt datetime (inclusive) from which to retrieve commands. There is no upper bound if this is not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the User ID, specify \&quot;userId.id eq &#39;string&#39;\&quot;.              For more information about filtering, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing commands; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 500 if not specified. | [optional] 

### Return type

[**ResourceListOfProcessedCommand**](ResourceListOfProcessedCommand.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The commands that modified the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_metadata**
> dict(str, list[AccessMetadataValue]) get_portfolio_metadata(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] Get access metadata rules for a portfolio

Pass the scope and portfolio code parameters to retrieve the AccessMetadata associated with a portfolio

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio Access Metadata Rule to retrieve.
code = 'code_example' # str | Portfolio code
effective_at = 'effective_at_example' # str | The effectiveAt datetime at which to retrieve the access metadata rule. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio access metadata. (optional)

    try:
        # [EXPERIMENTAL] Get access metadata rules for a portfolio
        api_response = api_instance.get_portfolio_metadata(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Access Metadata Rule to retrieve. | 
 **code** | **str**| Portfolio code | 
 **effective_at** | **str**| The effectiveAt datetime at which to retrieve the access metadata rule. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio access metadata. | [optional] 

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
**200** | The filtered list of results |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_properties**
> PortfolioProperties get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at)

Get portfolio properties

List all the properties of a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolio's properties. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolio's properties. Defaults to returning the latest version of each property if not specified. (optional)

    try:
        # Get portfolio properties
        api_response = api_instance.get_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolio&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio&#39;s properties. Defaults to returning the latest version of each property if not specified. | [optional] 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_property_time_series**
> ResourceListOfPropertyInterval get_portfolio_property_time_series(scope, code, property_key, portfolio_effective_at=portfolio_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)

[EXPERIMENTAL] Get portfolio property time series

Show the complete time series (history) for a particular portfolio property.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
property_key = 'property_key_example' # str | The property key of the property whose history to show.              This must be from the 'Portfolio' domain and in the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'.
portfolio_effective_at = 'portfolio_effective_at_example' # str | The effective datetime used to resolve the portfolio. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to show the history. Defaults to returning the current datetime if not supplied. (optional)
filter = 'filter_example' # str | Expression to filter the results. For more information about filtering,              see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
page = 'page_example' # str | The pagination token to use to continue listing properties; this value is returned from              the previous call. If a pagination token is provided, the filter, portfolioEffectiveAt, and asAt fields              must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the results to this number. (optional)

    try:
        # [EXPERIMENTAL] Get portfolio property time series
        api_response = api_instance.get_portfolio_property_time_series(scope, code, property_key, portfolio_effective_at=portfolio_effective_at, as_at=as_at, filter=filter, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_property_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **property_key** | **str**| The property key of the property whose history to show.              This must be from the &#39;Portfolio&#39; domain and in the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | 
 **portfolio_effective_at** | **str**| The effective datetime used to resolve the portfolio. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to show the history. Defaults to returning the current datetime if not supplied. | [optional] 
 **filter** | **str**| Expression to filter the results. For more information about filtering,              see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **page** | **str**| The pagination token to use to continue listing properties; this value is returned from              the previous call. If a pagination token is provided, the filter, portfolioEffectiveAt, and asAt fields              must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. | [optional] 

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

# **get_portfolio_relations**
> ResourceListOfRelation get_portfolio_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EXPERIMENTAL] Get portfolio relations

Get relations for a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve relations. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relations. Defaults to returning the latest LUSID AsAt time if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the relations. Provide a null or empty string for this field until further notice. (optional)
identifier_types = ['identifier_types_example'] # list[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.              These must be from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example              'Person/CompanyDetails/Role'. Only identifier types provided will be used to look up relevant entities in relations. If not applicable, provide an empty array. (optional)

    try:
        # [EXPERIMENTAL] Get portfolio relations
        api_response = api_instance.get_portfolio_relations(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relations. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relations. Defaults to returning the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relations. Provide a null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**list[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These must be from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. Only identifier types provided will be used to look up relevant entities in relations. If not applicable, provide an empty array. | [optional] 

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
**200** | The relations for the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_relationships**
> ResourceListOfRelationship get_portfolio_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)

[EXPERIMENTAL] Get portfolio relationships

Get relationships for a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve relationships. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve relationships. Defaults to returning the latest LUSID AsAt time if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the relationships. Provide a null or empty string for this field until further notice. (optional)
identifier_types = ['identifier_types_example'] # list[str] | Identifier types (as property keys) used for referencing Persons or Legal Entities.              These must be from the 'Person' or 'LegalEntity' domains and have the format {domain}/{scope}/{code}, for example              'Person/CompanyDetails/Role'. Only identifier types provided will be used to look up relevant entities in relationships. If not applicable, provide an empty array. (optional)

    try:
        # [EXPERIMENTAL] Get portfolio relationships
        api_response = api_instance.get_portfolio_relationships(scope, code, effective_at=effective_at, as_at=as_at, filter=filter, identifier_types=identifier_types)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve relationships. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve relationships. Defaults to returning the latest LUSID AsAt time if not specified. | [optional] 
 **filter** | **str**| Expression to filter the relationships. Provide a null or empty string for this field until further notice. | [optional] 
 **identifier_types** | [**list[str]**](str.md)| Identifier types (as property keys) used for referencing Persons or Legal Entities.              These must be from the &#39;Person&#39; or &#39;LegalEntity&#39; domains and have the format {domain}/{scope}/{code}, for example              &#39;Person/CompanyDetails/Role&#39;. Only identifier types provided will be used to look up relevant entities in relationships. If not applicable, provide an empty array. | [optional] 

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
**200** | The relationships for the specified portfolio. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_returns**
> ResourceListOfPerformanceReturn get_portfolio_returns(scope, code, return_scope, return_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)

[EARLY ACCESS] Get Returns

Get Returns which are on the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio.
code = 'code_example' # str | The code of the  Portfolio.
return_scope = 'return_scope_example' # str | The scope of the Returns.
return_code = 'return_code_example' # str | The code of the Returns.
from_effective_at = 'from_effective_at_example' # str | The start date from which to get the Returns. (optional)
to_effective_at = 'to_effective_at_example' # str | The end date from which to get the Returns. (optional)
period = 'period_example' # str | Show the Returns on a Daily or Monthly period. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Returns. Defaults to the latest. (optional)

    try:
        # [EARLY ACCESS] Get Returns
        api_response = api_instance.get_portfolio_returns(scope, code, return_scope, return_code, from_effective_at=from_effective_at, to_effective_at=to_effective_at, period=period, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolio_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **from_effective_at** | **str**| The start date from which to get the Returns. | [optional] 
 **to_effective_at** | **str**| The end date from which to get the Returns. | [optional] 
 **period** | **str**| Show the Returns on a Daily or Monthly period. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Returns. Defaults to the latest. | [optional] 

### Return type

[**ResourceListOfPerformanceReturn**](ResourceListOfPerformanceReturn.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Returns on the given time period. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolios_access_metadata_by_key**
> list[AccessMetadataValue] get_portfolios_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] Get an entry identified by a metadataKey in the access metadata object

Get a specific portfolio access metadata rule by specifying the corresponding identifier parts                No matching will be performed through this endpoint. To retrieve a rule, it is necessary to specify, exactly, the identifier of the rule

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio Access Metadata Rule to retrieve.
code = 'code_example' # str | The code of the portfolio
metadata_key = 'metadata_key_example' # str | Key of the metadata to retrieve
effective_at = 'effective_at_example' # str | The effective date of the rule (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the portfolio access metadata. (optional)

    try:
        # [EXPERIMENTAL] Get an entry identified by a metadataKey in the access metadata object
        api_response = api_instance.get_portfolios_access_metadata_by_key(scope, code, metadata_key, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->get_portfolios_access_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio Access Metadata Rule to retrieve. | 
 **code** | **str**| The code of the portfolio | 
 **metadata_key** | **str**| Key of the metadata to retrieve | 
 **effective_at** | **str**| The effective date of the rule | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the portfolio access metadata. | [optional] 

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
**200** | The successfully retrieved Portfolio Access Metadata Rule or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolio_properties**
> ResourceListOfProperty list_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit)

[EXPERIMENTAL] Get portfolio properties

List all the properties of a particular portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolio's properties. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolio's properties. Defaults to returning the latest version of each property if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing commands; this value is returned from the previous call. (optional)
limit = 56 # int | When paginating, limit the results per page to this number. (optional)

    try:
        # [EXPERIMENTAL] Get portfolio properties
        api_response = api_instance.list_portfolio_properties(scope, code, effective_at=effective_at, as_at=as_at, page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->list_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolio&#39;s properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolio&#39;s properties. Defaults to returning the latest version of each property if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing commands; this value is returned from the previous call. | [optional] 
 **limit** | **int**| When paginating, limit the results per page to this number. | [optional] 

### Return type

[**ResourceListOfProperty**](ResourceListOfProperty.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The properties of the specified portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolios**
> ResourceListOfPortfolio list_portfolios(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, query=query, property_keys=property_keys)

List portfolios

List all the portfolios matching particular criteria.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing portfolios; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 65,535 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the transaction type, specify \"type eq 'Transaction'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
query = 'query_example' # str | Expression specifying the criteria that the returned portfolios must meet. For example, to see which              portfolios have holdings in instruments with a LusidInstrumentId (LUID) of 'LUID_PPA8HI6M' or a Figi of 'BBG000BLNNH6',              specify \"instrument.identifiers in (('LusidInstrumentId', 'LUID_PPA8HI6M'), ('Figi', 'BBG000BLNNH6'))\". (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Portfolio' domain to decorate onto each portfolio.              These must take the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)

    try:
        # List portfolios
        api_response = api_instance.list_portfolios(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, query=query, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->list_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolios; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 65,535 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the transaction type, specify \&quot;type eq &#39;Transaction&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **query** | **str**| Expression specifying the criteria that the returned portfolios must meet. For example, to see which              portfolios have holdings in instruments with a LusidInstrumentId (LUID) of &#39;LUID_PPA8HI6M&#39; or a Figi of &#39;BBG000BLNNH6&#39;,              specify \&quot;instrument.identifiers in ((&#39;LusidInstrumentId&#39;, &#39;LUID_PPA8HI6M&#39;), (&#39;Figi&#39;, &#39;BBG000BLNNH6&#39;))\&quot;. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto each portfolio.              These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested portfolios |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolios_for_scope**
> ResourceListOfPortfolio list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)

List portfolios for scope

List all the portfolios in a particular scope.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope whose portfolios to list.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing portfolios. This  value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 65,535 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to return only transactions with a transaction type of 'Buy', specify \"type eq 'Buy'\".              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Portfolio' domain to decorate onto each portfolio.              These must take the format {domain}/{scope}/{code}, for example 'Portfolio/Manager/Id'. (optional)

    try:
        # List portfolios for scope
        api_response = api_instance.list_portfolios_for_scope(scope, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->list_portfolios_for_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope whose portfolios to list. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the portfolios. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the portfolios. Defaults to returning the latest version              of each portfolio if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing portfolios. This  value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt  and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 65,535 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to return only transactions with a transaction type of &#39;Buy&#39;, specify \&quot;type eq &#39;Buy&#39;\&quot;.              For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Portfolio&#39; domain to decorate onto each portfolio.              These must take the format {domain}/{scope}/{code}, for example &#39;Portfolio/Manager/Id&#39;. | [optional] 

### Return type

[**ResourceListOfPortfolio**](ResourceListOfPortfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portfolios in the specified scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portfolio**
> Portfolio update_portfolio(scope, code, update_portfolio_request, effective_at=effective_at)

Update portfolio

Update the definition of a particular portfolio.                Note that not all elements of a portfolio definition are  modifiable due to the potential implications for data already stored.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
update_portfolio_request = {"displayName":"MyPortfolioName","description":"Long form description of portfolio"} # UpdatePortfolioRequest | The updated portfolio definition.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to update the definition. Defaults to the current               LUSID system datetime if not specified. (optional)

    try:
        # Update portfolio
        api_response = api_instance.update_portfolio(scope, code, update_portfolio_request, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->update_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **update_portfolio_request** | [**UpdatePortfolioRequest**](UpdatePortfolioRequest.md)| The updated portfolio definition. | 
 **effective_at** | **str**| The effective datetime or cut label at which to update the definition. Defaults to the current               LUSID system datetime if not specified. | [optional] 

### Return type

[**Portfolio**](Portfolio.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated definition of the portfolio |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_access_metadata**
> ResourceListOfAccessMetadataValueOf upsert_portfolio_access_metadata(scope, code, metadata_key, upsert_portfolio_access_metadata_request, effective_at=effective_at)

[EXPERIMENTAL] Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.

Update or insert one Portfolio Access Metadata Rule in a single scope. An item will be updated if it already exists  and inserted if it does not.    The response will return the successfully updated or inserted Portfolio Access Metadata Rule or failure message if unsuccessful    It is important to always check to verify success (or failure).                Multiple rules for a metadataKey can exists with different effective at dates, when resources are accessed the rule that is active for the current time will be fetched

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope to use when updating or inserting the Portfolio Access Metadata Rule.
code = 'code_example' # str | Portfolio code
metadata_key = 'metadata_key_example' # str | Key of the access metadata to upsert
upsert_portfolio_access_metadata_request = {"metadata":[{"value":"SilverLicence","provider":"TestDataProvider"}]} # UpsertPortfolioAccessMetadataRequest | The Portfolio Access Metadata Rule to update or insert
effective_at = 'effective_at_example' # str | The date this rule will effective from (optional)

    try:
        # [EXPERIMENTAL] Upsert a Portfolio Access Metadata Rule associated with specific metadataKey. This creates or updates the data in LUSID.
        api_response = api_instance.upsert_portfolio_access_metadata(scope, code, metadata_key, upsert_portfolio_access_metadata_request, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->upsert_portfolio_access_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope to use when updating or inserting the Portfolio Access Metadata Rule. | 
 **code** | **str**| Portfolio code | 
 **metadata_key** | **str**| Key of the access metadata to upsert | 
 **upsert_portfolio_access_metadata_request** | [**UpsertPortfolioAccessMetadataRequest**](UpsertPortfolioAccessMetadataRequest.md)| The Portfolio Access Metadata Rule to update or insert | 
 **effective_at** | **str**| The date this rule will effective from | [optional] 

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
**200** | The successfully updated or inserted item or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_properties**
> PortfolioProperties upsert_portfolio_properties(scope, code, request_body)

Upsert portfolio properties

Create or update one or more properties for a particular portfolio. A property is updated if it  already exists and created if it does not. All properties must be from the 'Portfolio' domain.                Properties have an <i>effectiveFrom</i> datetime from which the property is valid, and an <i>effectiveUntil</i>  datetime until which it is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the portfolio.
code = 'code_example' # str | The code of the portfolio. Together with the scope this uniquely identifies the portfolio.
request_body = {"portfolio/MyScope/FundManagerName":{"key":"Portfolio/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"portfolio/MyScope/SomeProperty":{"key":"Portfolio/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"portfolio/MyScope/AnotherProperty":{"key":"Portfolio/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"portfolio/MyScope/ReBalanceInterval":{"key":"Portfolio/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # dict(str, ModelProperty) | The properties to be created or updated. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code}, for example               'Portfolio/Manager/Id'.

    try:
        # Upsert portfolio properties
        api_response = api_instance.upsert_portfolio_properties(scope, code, request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->upsert_portfolio_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio. | 
 **code** | **str**| The code of the portfolio. Together with the scope this uniquely identifies the portfolio. | 
 **request_body** | [**dict(str, ModelProperty)**](ModelProperty.md)| The properties to be created or updated. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code}, for example               &#39;Portfolio/Manager/Id&#39;. | 

### Return type

[**PortfolioProperties**](PortfolioProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_portfolio_returns**
> UpsertReturnsResponse upsert_portfolio_returns(scope, code, return_scope, return_code, performance_return)

[EARLY ACCESS] Upsert Returns

Update or insert returns into the specified portfolio.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-prd.lusid.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "https://fbn-prd.lusid.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.PortfoliosApi(api_client)
    scope = 'scope_example' # str | The scope of the Portfolio.
code = 'code_example' # str | The code of the  Portfolio.
return_scope = 'return_scope_example' # str | The scope of the Returns.
return_code = 'return_code_example' # str | The code of the Returns.
performance_return = [{"effectiveAt":"2019-11-28T00:00:00.0000000+00:00","rateOfReturn":0.1,"openingMarketValue":500,"closingMarketValue":550,"period":"Daily"},{"effectiveAt":"2019-11-29T00:00:00.0000000+00:00","rateOfReturn":-0.2,"openingMarketValue":550,"closingMarketValue":440,"period":"Daily"}] # list[PerformanceReturn] | This contains the Returns which need to be upsert.

    try:
        # [EARLY ACCESS] Upsert Returns
        api_response = api_instance.upsert_portfolio_returns(scope, code, return_scope, return_code, performance_return)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PortfoliosApi->upsert_portfolio_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Portfolio. | 
 **code** | **str**| The code of the  Portfolio. | 
 **return_scope** | **str**| The scope of the Returns. | 
 **return_code** | **str**| The code of the Returns. | 
 **performance_return** | [**list[PerformanceReturn]**](PerformanceReturn.md)| This contains the Returns which need to be upsert. | 

### Return type

[**UpsertReturnsResponse**](UpsertReturnsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The version of the portfolio that contains the newly updated or inserted Returns. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

