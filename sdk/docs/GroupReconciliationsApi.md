# lusid.GroupReconciliationsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comparison_ruleset**](GroupReconciliationsApi.md#create_comparison_ruleset) | **POST** /api/reconciliations/comparisonrulesets | [EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset
[**get_comparison_ruleset**](GroupReconciliationsApi.md#get_comparison_ruleset) | **GET** /api/reconciliations/comparisonrulesets/{scope}/{code} | [EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code


# **create_comparison_ruleset**
> GroupReconciliationComparisonRuleset create_comparison_ruleset(create_group_reconciliation_comparison_ruleset_request=create_group_reconciliation_comparison_ruleset_request)

[EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset

Creates a set of core and aggregate rules to be run for a group reconciliation

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
    api_instance = lusid.GroupReconciliationsApi(api_client)
    create_group_reconciliation_comparison_ruleset_request = {"id":{"scope":"MySourceScope","code":"MySourcePortfolioCode"},"displayName":"Compare by instrument and strategy","reconciliationType":"Holding","coreAttributeRules":[{"left":{"key":"path to instrument property","operation":"Value"},"right":{"key":"path to LUID property","operation":"Value"},"allowableStringMappings":[{"leftValue":"Microsoft","rightValue":"MSFT","direction":"UniDirectional"}],"isComparisonCaseSensitive":false},{"left":{"key":"path to strategy property","operation":"Value"},"right":{"key":"path to investment strategy property","operation":"Value"},"allowableStringMappings":[{"leftValue":"HighRisk","rightValue":"HR","direction":"BiDirectional"}],"isComparisonCaseSensitive":true}],"aggregateAttributeRules":[{"left":{"key":"path to units property","operation":"Sum"},"right":{"key":"path to count property","operation":"Sum"},"tolerance":{"type":"Absolute","value":10}},{"left":{"key":"path to price property","operation":"Sum"},"right":{"key":"path to price property","operation":"Sum"},"tolerance":{"type":"Relative","value":2}}]} # CreateGroupReconciliationComparisonRulesetRequest | The request containing the details of the ruleset (optional)

    try:
        # [EXPERIMENTAL] CreateComparisonRuleset: Create a Group Reconciliation Comparison Ruleset
        api_response = api_instance.create_comparison_ruleset(create_group_reconciliation_comparison_ruleset_request=create_group_reconciliation_comparison_ruleset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupReconciliationsApi->create_comparison_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_reconciliation_comparison_ruleset_request** | [**CreateGroupReconciliationComparisonRulesetRequest**](CreateGroupReconciliationComparisonRulesetRequest.md)| The request containing the details of the ruleset | [optional] 

### Return type

[**GroupReconciliationComparisonRuleset**](GroupReconciliationComparisonRuleset.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created comparison ruleset |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comparison_ruleset**
> GroupReconciliationComparisonRuleset get_comparison_ruleset(scope, code, as_at=as_at)

[EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code

Retrieves one Group Reconciliation Comparison Ruleset by scope and code

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
    api_instance = lusid.GroupReconciliationsApi(api_client)
    scope = 'scope_example' # str | The scope of the specified comparison ruleset.
code = 'code_example' # str | The code of the specified comparison ruleset. Together with the domain and scope this uniquely              identifies the reconciliation comparison ruleset.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the comparison ruleset definition. Defaults to return              the latest version of the definition if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetComparisonRuleset: Get a single Group Reconciliation Comparison Ruleset by scope and code
        api_response = api_instance.get_comparison_ruleset(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GroupReconciliationsApi->get_comparison_ruleset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the specified comparison ruleset. | 
 **code** | **str**| The code of the specified comparison ruleset. Together with the domain and scope this uniquely              identifies the reconciliation comparison ruleset. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the comparison ruleset definition. Defaults to return              the latest version of the definition if not specified. | [optional] 

### Return type

[**GroupReconciliationComparisonRuleset**](GroupReconciliationComparisonRuleset.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested comparison ruleset |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

