# lusid.AggregationApi

All URIs are relative to *http://localhost:62080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_configuration_recipe**](AggregationApi.md#generate_configuration_recipe) | **POST** /api/aggregation/{scope}/{code}/$generateconfigurationrecipe | [EXPERIMENTAL] Generates a recipe sufficient to perform valuations for the given portfolio.
[**get_aggregation**](AggregationApi.md#get_aggregation) | **POST** /api/aggregation/{scope}/{code}/$aggregate | [EXPERIMENTAL] Aggregate data in a portfolio or portfolio group
[**get_aggregation_by_group**](AggregationApi.md#get_aggregation_by_group) | **POST** /api/portfoliogroups/{scope}/{code}/$aggregate | [EXPERIMENTAL] Aggregate data in a portfolio group
[**get_aggregation_by_portfolio**](AggregationApi.md#get_aggregation_by_portfolio) | **POST** /api/portfolios/{scope}/{code}/$aggregate | [EXPERIMENTAL] Aggregate data in a portfolio
[**get_aggregation_by_result_set**](AggregationApi.md#get_aggregation_by_result_set) | **POST** /api/results/{scope}/{resultsKey}/$aggregate | [EXPERIMENTAL] Aggregate using result data
[**get_aggregation_of_weighted_instruments**](AggregationApi.md#get_aggregation_of_weighted_instruments) | **POST** /api/portfolios/{scope}/$aggregateinlined | [EXPERIMENTAL] Aggregate data in an inlined portfolio
[**get_nested_aggregation**](AggregationApi.md#get_nested_aggregation) | **POST** /api/aggregation/{scope}/{code}/$aggregatenested | [EXPERIMENTAL] Aggregate data in a portfolio or portfolio group, as nested
[**get_nested_aggregation_by_group**](AggregationApi.md#get_nested_aggregation_by_group) | **POST** /api/portfoliogroups/{scope}/{code}/$aggregatenested | [EXPERIMENTAL] Aggregate data in a portfolio group, as nested
[**get_nested_aggregation_by_portfolio**](AggregationApi.md#get_nested_aggregation_by_portfolio) | **POST** /api/portfolios/{scope}/{code}/$aggregatenested | [EXPERIMENTAL] 
[**get_queryable_keys**](AggregationApi.md#get_queryable_keys) | **GET** /api/results/queryable/keys | [EXPERIMENTAL] Query the set of supported \&quot;addresses\&quot; that can be queried from the aggregation endpoint.


# **generate_configuration_recipe**
> ConfigurationRecipe generate_configuration_recipe(scope, code, create_recipe_request=create_recipe_request)

[EXPERIMENTAL] Generates a recipe sufficient to perform valuations for the given portfolio.

Given a set of scopes, a portfolio Id and a basic recipe, this endpoint generates a configuration recipe with relevant rules that can value the instruments in the portfolio.

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
create_recipe_request = {"recipeCreationMarketDataScopes":["MyScope"],"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00"} # CreateRecipeRequest | The request specifying the parameters to generating the recipe (optional)

try:
    # [EXPERIMENTAL] Generates a recipe sufficient to perform valuations for the given portfolio.
    api_response = api_instance.generate_configuration_recipe(scope, code, create_recipe_request=create_recipe_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->generate_configuration_recipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **create_recipe_request** | [**CreateRecipeRequest**](CreateRecipeRequest.md)| The request specifying the parameters to generating the recipe | [optional] 

### Return type

[**ConfigurationRecipe**](ConfigurationRecipe.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation**
> ListAggregationResponse get_aggregation(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)

[EXPERIMENTAL] Aggregate data in a portfolio or portfolio group

Aggregate data sourced from the specified portfolio or portfolio group

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio or portfolio group
code = 'code_example' # str | The code of the portfolio or portfolio group
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
aggregation_request = {"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00","metrics":[{"key":"Holding/default/PV","op":"Proportion"},{"key":"Holding/default/PV","op":"Sum"}],"groupBy":["Instrument/default/Name"],"portfolioIdentifierCode":"SinglePortfolio"} # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # [EXPERIMENTAL] Aggregate data in a portfolio or portfolio group
    api_response = api_instance.get_aggregation(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio or portfolio group | 
 **code** | **str**| The code of the portfolio or portfolio group | 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_by_group**
> ListAggregationResponse get_aggregation_by_group(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)

[EXPERIMENTAL] Aggregate data in a portfolio group

Aggregate data sourced from the specified portfolio group

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
aggregation_request = {"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00","metrics":[{"key":"Holding/default/PV","op":"Proportion"},{"key":"Holding/default/PV","op":"Sum"}],"groupBy":["Instrument/default/Name"],"portfolioIdentifierCode":"SinglePortfolio"} # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # [EXPERIMENTAL] Aggregate data in a portfolio group
    api_response = api_instance.get_aggregation_by_group(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_by_portfolio**
> ListAggregationResponse get_aggregation_by_portfolio(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)

[EXPERIMENTAL] Aggregate data in a portfolio

Aggregate data sourced from the specified portfolio

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
aggregation_request = {"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00","metrics":[{"key":"Holding/default/PV","op":"Proportion"},{"key":"Holding/default/PV","op":"Sum"}],"groupBy":["Instrument/default/Name"],"portfolioIdentifierCode":"SinglePortfolio"} # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # [EXPERIMENTAL] Aggregate data in a portfolio
    api_response = api_instance.get_aggregation_by_portfolio(scope, code, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation_by_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_by_result_set**
> ListAggregationResponse get_aggregation_by_result_set(scope, results_key, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)

[EXPERIMENTAL] Aggregate using result data

Aggregate data from a previously-run Result data set into a flat row of results

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the Result data set
results_key = 'results_key_example' # str | The key of the Result data set
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
aggregation_request = {"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00","metrics":[{"key":"Holding/default/PV","op":"Proportion"},{"key":"Holding/default/PV","op":"Sum"}],"groupBy":["Instrument/default/Name"],"portfolioIdentifierCode":"SinglePortfolio"} # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # [EXPERIMENTAL] Aggregate using result data
    api_response = api_instance.get_aggregation_by_result_set(scope, results_key, sort_by=sort_by, start=start, limit=limit, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation_by_result_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Result data set | 
 **results_key** | **str**| The key of the Result data set | 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_of_weighted_instruments**
> ListAggregationResponse get_aggregation_of_weighted_instruments(scope, sort_by=sort_by, start=start, limit=limit, inline_aggregation_request=inline_aggregation_request)

[EXPERIMENTAL] Aggregate data in an inlined portfolio

Aggregate data sourced from the portfolio that is defined by the weighted set of instruments passed to the request.

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the instruments should that be required
sort_by = ['sort_by_example'] # list[str] | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
start = 56 # int | Optional. When paginating, skip this number of results (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
inline_aggregation_request = {"request":{"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00","metrics":[{"key":"Holding/default/PV","op":"Proportion"},{"key":"Holding/default/PV","op":"Sum"}],"groupBy":["Instrument/default/Name"],"portfolioIdentifierCode":"SinglePortfolio"},"instruments":[{"quantity":10000,"holdingIdentifier":"my-holding-on-some-date","instrument":{"domAmount":100,"fgnAmount":-150,"isNdf":false,"fixingDate":"0001-01-01T00:00:00+00:00","fgnCcy":"GBP","refSpotRate":1.5,"startDate":"2018-03-05T00:00:00+00:00","maturityDate":"2018-04-04T00:00:00+00:00","domCcy":"USD","instrumentType":"FxForward"}}]} # InlineAggregationRequest | The request specifying the parameters of the aggregation and the inlined set of instruments to aggregate over. (optional)

try:
    # [EXPERIMENTAL] Aggregate data in an inlined portfolio
    api_response = api_instance.get_aggregation_of_weighted_instruments(scope, sort_by=sort_by, start=start, limit=limit, inline_aggregation_request=inline_aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_aggregation_of_weighted_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the instruments should that be required | 
 **sort_by** | [**list[str]**](str.md)| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **start** | **int**| Optional. When paginating, skip this number of results | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **inline_aggregation_request** | [**InlineAggregationRequest**](InlineAggregationRequest.md)| The request specifying the parameters of the aggregation and the inlined set of instruments to aggregate over. | [optional] 

### Return type

[**ListAggregationResponse**](ListAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nested_aggregation**
> NestedAggregationResponse get_nested_aggregation(scope, code, aggregation_request=aggregation_request)

[EXPERIMENTAL] Aggregate data in a portfolio or portfolio group, as nested

Aggregate data sourced from the specified portfolio or portfolio group into a nested structure. Data is nested following the group-by specifications.

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio or portfolio group
code = 'code_example' # str | The code of the portfolio or portfolio group
aggregation_request = {"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00","metrics":[{"key":"Holding/default/PV","op":"Proportion"},{"key":"Holding/default/PV","op":"Sum"}],"groupBy":["Instrument/default/Name"],"portfolioIdentifierCode":"SinglePortfolio"} # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # [EXPERIMENTAL] Aggregate data in a portfolio or portfolio group, as nested
    api_response = api_instance.get_nested_aggregation(scope, code, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_nested_aggregation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio or portfolio group | 
 **code** | **str**| The code of the portfolio or portfolio group | 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**NestedAggregationResponse**](NestedAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nested_aggregation_by_group**
> NestedAggregationResponse get_nested_aggregation_by_group(scope, code, aggregation_request=aggregation_request)

[EXPERIMENTAL] Aggregate data in a portfolio group, as nested

Obsolete - Aggregate data sourced from the specified portfolio group into a nested structure. Data is nested following the group-by specifications.

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio group
code = 'code_example' # str | The code of the portfolio group
aggregation_request = {"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00","metrics":[{"key":"Holding/default/PV","op":"Proportion"},{"key":"Holding/default/PV","op":"Sum"}],"groupBy":["Instrument/default/Name"],"portfolioIdentifierCode":"SinglePortfolio"} # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # [EXPERIMENTAL] Aggregate data in a portfolio group, as nested
    api_response = api_instance.get_nested_aggregation_by_group(scope, code, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_nested_aggregation_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio group | 
 **code** | **str**| The code of the portfolio group | 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**NestedAggregationResponse**](NestedAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nested_aggregation_by_portfolio**
> NestedAggregationResponse get_nested_aggregation_by_portfolio(scope, code, aggregation_request=aggregation_request)

[EXPERIMENTAL] 

Aggregate data in a portfolio, as nested

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the portfolio
code = 'code_example' # str | The code of the portfolio
aggregation_request = {"recipeId":{"scope":"MyScope","code":"default"},"asAt":"2018-03-05T00:00:00+00:00","effectiveAt":"2018-03-05T00:00:00+00:00","metrics":[{"key":"Holding/default/PV","op":"Proportion"},{"key":"Holding/default/PV","op":"Sum"}],"groupBy":["Instrument/default/Name"],"portfolioIdentifierCode":"SinglePortfolio"} # AggregationRequest | The request specifying the parameters of the aggregation (optional)

try:
    # [EXPERIMENTAL] 
    api_response = api_instance.get_nested_aggregation_by_portfolio(scope, code, aggregation_request=aggregation_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_nested_aggregation_by_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the portfolio | 
 **code** | **str**| The code of the portfolio | 
 **aggregation_request** | [**AggregationRequest**](AggregationRequest.md)| The request specifying the parameters of the aggregation | [optional] 

### Return type

[**NestedAggregationResponse**](NestedAggregationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queryable_keys**
> ResourceListOfAggregationQuery get_queryable_keys(page=page, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] Query the set of supported \"addresses\" that can be queried from the aggregation endpoint.

When a request is made for aggregation, the user needs to know what keys can be passed to it for queryable data. This endpoint allows to queries to provide the set of keys,  what they are and what they return.

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

# Defining host is optional and default to http://localhost:62080
configuration.host = "http://localhost:62080"
# Create an instance of the API class
api_instance = lusid.AggregationApi(lusid.ApiClient(configuration))
page = 'page_example' # str | The pagination token to use to continue listing queryable keys from a previous call to list queryable keys.              This value is returned from the previous call. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

try:
    # [EXPERIMENTAL] Query the set of supported \"addresses\" that can be queried from the aggregation endpoint.
    api_response = api_instance.get_queryable_keys(page=page, start=start, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AggregationApi->get_queryable_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing queryable keys from a previous call to list queryable keys.              This value is returned from the previous call. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set.              Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**ResourceListOfAggregationQuery**](ResourceListOfAggregationQuery.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

