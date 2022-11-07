# lusid.TransactionTaxRulesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_rule_set**](TransactionTaxRulesApi.md#create_tax_rule_set) | **POST** /api/transactions/taxrules | [EXPERIMENTAL] CreateTaxRuleSet: Create a tax rule set.
[**delete_tax_rule_set**](TransactionTaxRulesApi.md#delete_tax_rule_set) | **DELETE** /api/transactions/taxrules/{scope}/{code} | [EXPERIMENTAL] DeleteTaxRuleSet: Deletes a tax rule.
[**get_tax_rule_set**](TransactionTaxRulesApi.md#get_tax_rule_set) | **GET** /api/transactions/taxrules/{scope}/{code} | [EXPERIMENTAL] GetTaxRuleSet: Retrieve the definition of single tax rule set.
[**list_tax_rule_sets**](TransactionTaxRulesApi.md#list_tax_rule_sets) | **GET** /api/transactions/taxrules | [EXPERIMENTAL] ListTaxRuleSets: List tax rules.
[**update_tax_rule_set**](TransactionTaxRulesApi.md#update_tax_rule_set) | **PUT** /api/transactions/taxrules/{scope}/{code} | [EXPERIMENTAL] UpdateTaxRuleSet: Update a tax rule set.


# **create_tax_rule_set**
> TaxRuleSet create_tax_rule_set(create_tax_rule_set_request, effective_at=effective_at)

[EXPERIMENTAL] CreateTaxRuleSet: Create a tax rule set.

Creates a tax rule set definition at the given effective time.  The user must be entitled to read any properties specified in each rule.

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
    api_instance = lusid.TransactionTaxRulesApi(api_client)
    create_tax_rule_set_request = {"id":{"scope":"myScope","code":"RuleSetName"},"displayName":"Rule set display name","description":"Rule set description","outputPropertyKey":"Transaction/default/TaxRate","rules":[{"name":"UKTaxRule","description":"Rule for the UK tax rate","rate":30,"criteria":[{"key":"Instrument/myScope/market","value":"GB","op":"Equals"},{"key":"Portfolio/myScope/taxDomicile","value":"GB","op":"Equals"}]}]} # CreateTaxRuleSetRequest | The contents of the rule set.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the rule set will take effect.  Defaults to the current LUSID system datetime if not specified. (optional)

    try:
        # [EXPERIMENTAL] CreateTaxRuleSet: Create a tax rule set.
        api_response = api_instance.create_tax_rule_set(create_tax_rule_set_request, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionTaxRulesApi->create_tax_rule_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tax_rule_set_request** | [**CreateTaxRuleSetRequest**](CreateTaxRuleSetRequest.md)| The contents of the rule set. | 
 **effective_at** | **str**| The effective datetime or cut label at which the rule set will take effect.  Defaults to the current LUSID system datetime if not specified. | [optional] 

### Return type

[**TaxRuleSet**](TaxRuleSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create a rule set for tax calculations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_rule_set**
> DeletedEntityResponse delete_tax_rule_set(scope, code)

[EXPERIMENTAL] DeleteTaxRuleSet: Deletes a tax rule.

<br>              Deletes the rule for all effective time.                <br>              The rule will remain viewable at previous as at times, but it will no longer be considered applicable.                <br>              This cannot be undone.              

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
    api_instance = lusid.TransactionTaxRulesApi(api_client)
    scope = 'scope_example' # str | The rule set scope.
code = 'code_example' # str | The rule set code.

    try:
        # [EXPERIMENTAL] DeleteTaxRuleSet: Deletes a tax rule.
        api_response = api_instance.delete_tax_rule_set(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionTaxRulesApi->delete_tax_rule_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | 
 **code** | **str**| The rule set code. | 

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
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_rule_set**
> TaxRuleSet get_tax_rule_set(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetTaxRuleSet: Retrieve the definition of single tax rule set.

Retrieves the tax rule set definition at the given effective and as at times.

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
    api_instance = lusid.TransactionTaxRulesApi(api_client)
    scope = 'scope_example' # str | The rule set scope.
code = 'code_example' # str | The rule set code.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID  system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. (optional)

    try:
        # [EXPERIMENTAL] GetTaxRuleSet: Retrieve the definition of single tax rule set.
        api_response = api_instance.get_tax_rule_set(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionTaxRulesApi->get_tax_rule_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | 
 **code** | **str**| The rule set code. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. | [optional] 

### Return type

[**TaxRuleSet**](TaxRuleSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of one rule set. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tax_rule_sets**
> ResourceListOfTaxRuleSet list_tax_rule_sets(effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] ListTaxRuleSets: List tax rules.

Retrieves all tax rule set definitions at the given effective and as at times

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
    api_instance = lusid.TransactionTaxRulesApi(api_client)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID  system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. (optional)

    try:
        # [EXPERIMENTAL] ListTaxRuleSets: List tax rules.
        api_response = api_instance.list_tax_rule_sets(effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionTaxRulesApi->list_tax_rule_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. | [optional] 

### Return type

[**ResourceListOfTaxRuleSet**](ResourceListOfTaxRuleSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rule sets available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_rule_set**
> TaxRuleSet update_tax_rule_set(scope, code, update_tax_rule_set_request, effective_at=effective_at)

[EXPERIMENTAL] UpdateTaxRuleSet: Update a tax rule set.

Updates the tax rule set definition at the given effective time.  The user must be entitled to read any properties specified in each rule.

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
    api_instance = lusid.TransactionTaxRulesApi(api_client)
    scope = 'scope_example' # str | The rule set scope.
code = 'code_example' # str | The rule set code.
update_tax_rule_set_request = {"displayName":"Rule set display name","description":"Rule set description","outputPropertyKey":"Transaction/default/TaxRate","rules":[{"name":"UKTaxRule","description":"Rule for the UK tax rate","rate":30,"criteria":[{"key":"Instrument/myScope/market","value":"GB","op":"Equals"},{"key":"Portfolio/myScope/taxDomicile","value":"GB","op":"Equals"}]},{"name":"EUReclaimRate","description":"Rule for applying the reclaim rate to instruments in the European market","rate":-10,"criteria":[{"key":"Instrument/myScope/Market","value":["FR","NL","DE"],"op":"In"}]}]} # UpdateTaxRuleSetRequest | The contents of the rule set.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the rule set will take effect.  Defaults to the current LUSID system datetime if not specified.  The changes will take place from this effective time until the next effective time that the rule has been updated at.  For example, consider a rule that has been created or updated effective at the first day of the coming month.  An upsert effective from the current day will only change the definition until that day.  An additional upsert at the same time (first day of the month) is required if the newly-updated definition is to supersede the future definition. (optional)

    try:
        # [EXPERIMENTAL] UpdateTaxRuleSet: Update a tax rule set.
        api_response = api_instance.update_tax_rule_set(scope, code, update_tax_rule_set_request, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionTaxRulesApi->update_tax_rule_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The rule set scope. | 
 **code** | **str**| The rule set code. | 
 **update_tax_rule_set_request** | [**UpdateTaxRuleSetRequest**](UpdateTaxRuleSetRequest.md)| The contents of the rule set. | 
 **effective_at** | **str**| The effective datetime or cut label at which the rule set will take effect.  Defaults to the current LUSID system datetime if not specified.  The changes will take place from this effective time until the next effective time that the rule has been updated at.  For example, consider a rule that has been created or updated effective at the first day of the coming month.  An upsert effective from the current day will only change the definition until that day.  An additional upsert at the same time (first day of the month) is required if the newly-updated definition is to supersede the future definition. | [optional] 

### Return type

[**TaxRuleSet**](TaxRuleSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update rules for tax calculations. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

