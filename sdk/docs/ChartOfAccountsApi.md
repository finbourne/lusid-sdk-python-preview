# lusid.ChartOfAccountsApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chart_of_accounts**](ChartOfAccountsApi.md#create_chart_of_accounts) | **POST** /api/chartofaccounts/{scope} | [EXPERIMENTAL] CreateChartOfAccounts: Create a Chart of Accounts
[**create_posting_module**](ChartOfAccountsApi.md#create_posting_module) | **POST** /api/chartofaccounts/{scope}/{code}/postingmodules | [EXPERIMENTAL] CreatePostingModule: Create a Posting Module
[**delete_accounts**](ChartOfAccountsApi.md#delete_accounts) | **POST** /api/chartofaccounts/{scope}/{code}/accounts/$delete | [EXPERIMENTAL] DeleteAccounts: Soft or hard delete multiple accounts
[**delete_chart_of_accounts**](ChartOfAccountsApi.md#delete_chart_of_accounts) | **DELETE** /api/chartofaccounts/{scope}/{code} | [EXPERIMENTAL] DeleteChartOfAccounts: Delete a Chart of Accounts
[**delete_posting_module**](ChartOfAccountsApi.md#delete_posting_module) | **DELETE** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] DeletePostingModule: Delete a Posting Module.
[**get_account**](ChartOfAccountsApi.md#get_account) | **GET** /api/chartofaccounts/{scope}/{code}/accounts/{accountCode} | [EXPERIMENTAL] GetAccount: Get Account
[**get_chart_of_accounts**](ChartOfAccountsApi.md#get_chart_of_accounts) | **GET** /api/chartofaccounts/{scope}/{code} | [EXPERIMENTAL] GetChartOfAccounts: Get ChartOfAccounts
[**get_posting_module**](ChartOfAccountsApi.md#get_posting_module) | **GET** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] GetPostingModule: Get a Posting Module
[**list_accounts**](ChartOfAccountsApi.md#list_accounts) | **GET** /api/chartofaccounts/{scope}/{code}/accounts | [EXPERIMENTAL] ListAccounts: List Accounts
[**list_charts_of_accounts**](ChartOfAccountsApi.md#list_charts_of_accounts) | **GET** /api/chartofaccounts | [EXPERIMENTAL] ListChartsOfAccounts: List Charts of Accounts
[**list_posting_module_rules**](ChartOfAccountsApi.md#list_posting_module_rules) | **GET** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode}/postingrules | [EXPERIMENTAL] ListPostingModuleRules: List Posting Module Rules
[**list_posting_modules**](ChartOfAccountsApi.md#list_posting_modules) | **GET** /api/chartofaccounts/{scope}/{code}/postingmodules | [EXPERIMENTAL] ListPostingModules: List Posting Modules
[**set_posting_module_details**](ChartOfAccountsApi.md#set_posting_module_details) | **PUT** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode} | [EXPERIMENTAL] SetPostingModuleDetails: Set the details of a Posting Module
[**set_posting_module_rules**](ChartOfAccountsApi.md#set_posting_module_rules) | **PUT** /api/chartofaccounts/{scope}/{code}/postingmodules/{postingModuleCode}/postingrules | [EXPERIMENTAL] SetPostingModuleRules: Set the rules of a Posting Module
[**upsert_account_properties**](ChartOfAccountsApi.md#upsert_account_properties) | **POST** /api/chartofaccounts/{scope}/{code}/accounts/{accountCode}/properties/$upsert | [EXPERIMENTAL] UpsertAccountProperties: Upsert account properties
[**upsert_accounts**](ChartOfAccountsApi.md#upsert_accounts) | **POST** /api/chartofaccounts/{scope}/{code}/accounts | [EXPERIMENTAL] UpsertAccounts: Upsert Accounts
[**upsert_chart_of_accounts_properties**](ChartOfAccountsApi.md#upsert_chart_of_accounts_properties) | **POST** /api/chartofaccounts/{scope}/{code}/properties/$upsert | [EXPERIMENTAL] UpsertChartOfAccountsProperties: Upsert Chart of Accounts properties


# **create_chart_of_accounts**
> ChartOfAccounts create_chart_of_accounts(scope, chart_of_accounts_request)

[EXPERIMENTAL] CreateChartOfAccounts: Create a Chart of Accounts

Create the given Chart of Accounts.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
chart_of_accounts_request = {"code":"ChartOfAccounts","displayName":"ChartOfAccountsName","description":"Standard COA","properties":{"ChartOfAccounts/MyScope/FundManagerName":{"key":"ChartOfAccounts/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"}}} # ChartOfAccountsRequest | The definition of the Chart of Accounts.

    try:
        # [EXPERIMENTAL] CreateChartOfAccounts: Create a Chart of Accounts
        api_response = api_instance.create_chart_of_accounts(scope, chart_of_accounts_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->create_chart_of_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **chart_of_accounts_request** | [**ChartOfAccountsRequest**](ChartOfAccountsRequest.md)| The definition of the Chart of Accounts. | 

### Return type

[**ChartOfAccounts**](ChartOfAccounts.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Chart of Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_posting_module**
> PostingModuleResponse create_posting_module(scope, code, posting_module_request)

[EXPERIMENTAL] CreatePostingModule: Create a Posting Module

Create the given Posting Module.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
posting_module_request = {"code":"PostingModuleCode","displayName":"PostingModuleName","description":"PostingModuleDescription","rules":[{"ruleId":"rule1Id","account":"account1","ruleFilter":"Transaction.TransactionId eq 'Transaction_1'"}]} # PostingModuleRequest | The definition of the Posting Module.

    try:
        # [EXPERIMENTAL] CreatePostingModule: Create a Posting Module
        api_response = api_instance.create_posting_module(scope, code, posting_module_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->create_posting_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **posting_module_request** | [**PostingModuleRequest**](PostingModuleRequest.md)| The definition of the Posting Module. | 

### Return type

[**PostingModuleResponse**](PostingModuleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_accounts**
> DeleteAccountsResponse delete_accounts(scope, code, request_body, delete_mode=delete_mode)

[EXPERIMENTAL] DeleteAccounts: Soft or hard delete multiple accounts

Delete one or more account from the Chart of Accounts. Soft deletion marks the account as inactive  While the Hard deletion is deleting the account.  The maximum number of accounts that this method can delete per request is 2,000.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts.
request_body = ["AccountCode1","AccountCode2"] # list[str] | The codes of the accounts to delete.
delete_mode = 'delete_mode_example' # str | The delete mode to use (defaults to 'Soft'). (optional)

    try:
        # [EXPERIMENTAL] DeleteAccounts: Soft or hard delete multiple accounts
        api_response = api_instance.delete_accounts(scope, code, request_body, delete_mode=delete_mode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->delete_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts. | 
 **request_body** | [**list[str]**](str.md)| The codes of the accounts to delete. | 
 **delete_mode** | **str**| The delete mode to use (defaults to &#39;Soft&#39;). | [optional] 

### Return type

[**DeleteAccountsResponse**](DeleteAccountsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The datetime that the Accounts were deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chart_of_accounts**
> DeletedEntityResponse delete_chart_of_accounts(scope, code)

[EXPERIMENTAL] DeleteChartOfAccounts: Delete a Chart of Accounts

Delete the given Chart of Accounts.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts to be deleted.
code = 'code_example' # str | The code of the Chart of Accounts to be deleted. Together with the scope this uniquely identifies the Chart of Accounts.

    try:
        # [EXPERIMENTAL] DeleteChartOfAccounts: Delete a Chart of Accounts
        api_response = api_instance.delete_chart_of_accounts(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->delete_chart_of_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts to be deleted. | 
 **code** | **str**| The code of the Chart of Accounts to be deleted. Together with the scope this uniquely identifies the Chart of Accounts. | 

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
**200** | The datetime that the Chart of Accounts was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_posting_module**
> DeletedEntityResponse delete_posting_module(scope, code, posting_module_code)

[EXPERIMENTAL] DeletePostingModule: Delete a Posting Module.

Delete the given Posting Module.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
posting_module_code = 'posting_module_code_example' # str | The code of the Posting Module to be deleted.

    try:
        # [EXPERIMENTAL] DeletePostingModule: Delete a Posting Module.
        api_response = api_instance.delete_posting_module(scope, code, posting_module_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->delete_posting_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **posting_module_code** | **str**| The code of the Posting Module to be deleted. | 

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
**200** | The datetime that the Posting Module was deleted. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account(scope, code, account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetAccount: Get Account

Retrieve the definition of a particular Account which is part of a Chart of Accounts.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
account_code = 'account_code_example' # str | The code of the Account.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Account properties. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Account definition. Defaults to returning the latest version of the Account definition if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Account' domain to decorate onto the Account.              These must take the format {domain}/{scope}/{code}, for example 'Account/Manager/Id'. If not provided will return all the entitled properties for that Account. (optional)

    try:
        # [EXPERIMENTAL] GetAccount: Get Account
        api_response = api_instance.get_account(scope, code, account_code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **account_code** | **str**| The code of the Account. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Account properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Account definition. Defaults to returning the latest version of the Account definition if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Account&#39; domain to decorate onto the Account.              These must take the format {domain}/{scope}/{code}, for example &#39;Account/Manager/Id&#39;. If not provided will return all the entitled properties for that Account. | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Account definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chart_of_accounts**
> ChartOfAccounts get_chart_of_accounts(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)

[EXPERIMENTAL] GetChartOfAccounts: Get ChartOfAccounts

Retrieve the definition of a particular Chart of Accounts.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the Chart of Accounts properties. Defaults to the current LUSID system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Chart of Accounts definition. Defaults to returning the latest version of the Chart of Accounts definition if not specified. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'ChartOfAccounts' domain to decorate onto the Chart of Accounts.              These must take the format {domain}/{scope}/{code}, for example 'ChartOfAccounts/Manager/Id'. If not provided will return all the entitled properties for that Chart of Accounts. (optional)

    try:
        # [EXPERIMENTAL] GetChartOfAccounts: Get ChartOfAccounts
        api_response = api_instance.get_chart_of_accounts(scope, code, effective_at=effective_at, as_at=as_at, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->get_chart_of_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the Chart of Accounts properties. Defaults to the current LUSID system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Chart of Accounts definition. Defaults to returning the latest version of the Chart of Accounts definition if not specified. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;ChartOfAccounts&#39; domain to decorate onto the Chart of Accounts.              These must take the format {domain}/{scope}/{code}, for example &#39;ChartOfAccounts/Manager/Id&#39;. If not provided will return all the entitled properties for that Chart of Accounts. | [optional] 

### Return type

[**ChartOfAccounts**](ChartOfAccounts.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Chart Of Accounts definition. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posting_module**
> PostingModuleResponse get_posting_module(scope, code, posting_module_code)

[EXPERIMENTAL] GetPostingModule: Get a Posting Module

Retrieve the definition of a Posting Module complete with its rules.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
posting_module_code = 'posting_module_code_example' # str | The code of the Posting Module.

    try:
        # [EXPERIMENTAL] GetPostingModule: Get a Posting Module
        api_response = api_instance.get_posting_module(scope, code, posting_module_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->get_posting_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **posting_module_code** | **str**| The code of the Posting Module. | 

### Return type

[**PostingModuleResponse**](PostingModuleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full definition of the Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> PagedResourceListOfAccount list_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListAccounts: List Accounts

List the accounts in a Chart of Accounts

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties decorated on Accounts. Defaults to the current LUSID              system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the Accounts. Defaults to              returning the latest version if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing charts of accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Account type, specify \"code eq '001'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'Account' domain to decorate onto the Account.              These must have the format {domain}/{scope}/{code}, for example 'Account/system/Name'. (optional)

    try:
        # [EXPERIMENTAL] ListAccounts: List Accounts
        api_response = api_instance.list_accounts(scope, code, effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->list_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts. | 
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties decorated on Accounts. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the Accounts. Defaults to              returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing charts of accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Account type, specify \&quot;code eq &#39;001&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;Account&#39; domain to decorate onto the Account.              These must have the format {domain}/{scope}/{code}, for example &#39;Account/system/Name&#39;. | [optional] 

### Return type

[**PagedResourceListOfAccount**](PagedResourceListOfAccount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Accounts in the given Chart of Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_charts_of_accounts**
> PagedResourceListOfChartOfAccounts list_charts_of_accounts(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)

[EXPERIMENTAL] ListChartsOfAccounts: List Charts of Accounts

List all the Charts of Accounts matching particular criteria.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to list the TimeVariant properties for the Chart Of Accounts. Defaults to the current LUSID              system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the charts of accounts. Defaults to returning the latest version              of each Chart of Accounts if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing charts of accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Chart of Accounts type, specify \"id.Code eq '001'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
property_keys = ['property_keys_example'] # list[str] | A list of property keys from the 'ChartOfAccounts' domain to decorate onto each Chart of Accounts.              These must take the format {domain}/{scope}/{code}, for example 'ChartOfAccounts/Manager/Id'. (optional)

    try:
        # [EXPERIMENTAL] ListChartsOfAccounts: List Charts of Accounts
        api_response = api_instance.list_charts_of_accounts(effective_at=effective_at, as_at=as_at, page=page, start=start, limit=limit, filter=filter, property_keys=property_keys)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->list_charts_of_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to list the TimeVariant properties for the Chart Of Accounts. Defaults to the current LUSID              system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to list the charts of accounts. Defaults to returning the latest version              of each Chart of Accounts if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing charts of accounts; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Chart of Accounts type, specify \&quot;id.Code eq &#39;001&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **property_keys** | [**list[str]**](str.md)| A list of property keys from the &#39;ChartOfAccounts&#39; domain to decorate onto each Chart of Accounts.              These must take the format {domain}/{scope}/{code}, for example &#39;ChartOfAccounts/Manager/Id&#39;. | [optional] 

### Return type

[**PagedResourceListOfChartOfAccounts**](PagedResourceListOfChartOfAccounts.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Charts of Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_posting_module_rules**
> PagedResourceListOfPostingModuleRule list_posting_module_rules(scope, code, posting_module_code, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListPostingModuleRules: List Posting Module Rules

List the Rules in a Posting Module

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
posting_module_code = 'posting_module_code_example' # str | The code of the posting module.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing posting module rules; this              value is returned from the previous call. If a pagination token is provided, the filter              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the rule id, specify \"ruleId eq 'rule 1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)

    try:
        # [EXPERIMENTAL] ListPostingModuleRules: List Posting Module Rules
        api_response = api_instance.list_posting_module_rules(scope, code, posting_module_code, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->list_posting_module_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **posting_module_code** | **str**| The code of the posting module. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing posting module rules; this              value is returned from the previous call. If a pagination token is provided, the filter              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the rule id, specify \&quot;ruleId eq &#39;rule 1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 

### Return type

[**PagedResourceListOfPostingModuleRule**](PagedResourceListOfPostingModuleRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The rules in the given Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_posting_modules**
> PagedResourceListOfPostingModuleResponse list_posting_modules(scope, code, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListPostingModules: List Posting Modules

List all the Posting Modules matching particular criteria.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Posting Module. Defaults to returning the latest version              of each Posting Module if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing Posting Modules; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Posting Module status, specify \"status eq 'Active'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)

    try:
        # [EXPERIMENTAL] ListPostingModules: List Posting Modules
        api_response = api_instance.list_posting_modules(scope, code, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->list_posting_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **as_at** | **datetime**| The asAt datetime at which to list the Posting Module. Defaults to returning the latest version              of each Posting Module if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Posting Modules; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Posting Module status, specify \&quot;status eq &#39;Active&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 

### Return type

[**PagedResourceListOfPostingModuleResponse**](PagedResourceListOfPostingModuleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Posting Modules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_posting_module_details**
> PostingModuleResponse set_posting_module_details(scope, code, posting_module_code, posting_module_details)

[EXPERIMENTAL] SetPostingModuleDetails: Set the details of a Posting Module

Update the given Posting Module details.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
posting_module_code = 'posting_module_code_example' # str | The code of the Posting Module to be updated.
posting_module_details = {"displayName":"PostingModuleNameUpdated","description":"PostingModuleDescriptionUpdated","status":"Active"} # PostingModuleDetails | The new details for the Posting Module.

    try:
        # [EXPERIMENTAL] SetPostingModuleDetails: Set the details of a Posting Module
        api_response = api_instance.set_posting_module_details(scope, code, posting_module_code, posting_module_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->set_posting_module_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **posting_module_code** | **str**| The code of the Posting Module to be updated. | 
 **posting_module_details** | [**PostingModuleDetails**](PostingModuleDetails.md)| The new details for the Posting Module. | 

### Return type

[**PostingModuleResponse**](PostingModuleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated Posting Module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_posting_module_rules**
> PostingModuleRulesUpdatedResponse set_posting_module_rules(scope, code, posting_module_code, posting_module_rule)

[EXPERIMENTAL] SetPostingModuleRules: Set the rules of a Posting Module

Set the given Posting Modules rules, this will replace the existing set of rules for the posting module.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts.
posting_module_code = 'posting_module_code_example' # str | The code of the Posting Module to be updated.
posting_module_rule = [{"ruleId":"rule 1","account":"100002354","ruleFilter":"1 eq 1"},{"ruleId":"rule 2","account":"123456789","ruleFilter":"true eq true"}] # list[PostingModuleRule] | The new rule set for the Posting Module.

    try:
        # [EXPERIMENTAL] SetPostingModuleRules: Set the rules of a Posting Module
        api_response = api_instance.set_posting_module_rules(scope, code, posting_module_code, posting_module_rule)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->set_posting_module_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **posting_module_code** | **str**| The code of the Posting Module to be updated. | 
 **posting_module_rule** | [**list[PostingModuleRule]**](PostingModuleRule.md)| The new rule set for the Posting Module. | 

### Return type

[**PostingModuleRulesUpdatedResponse**](PostingModuleRulesUpdatedResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Posting Module with updated rules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_account_properties**
> AccountProperties upsert_account_properties(scope, code, account_code, request_body=request_body)

[EXPERIMENTAL] UpsertAccountProperties: Upsert account properties

Update or insert one or more properties onto a single account. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'Account'.                Upserting a property that exists for an account, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts to update or insert the properties onto.
code = 'code_example' # str | The code of the Chart of Accounts to update or insert the properties onto. Together with the scope this uniquely identifies the Chart of Accounts.
account_code = 'account_code_example' # str | The unique ID of the account to create or update properties for.
request_body = {"Account/MyScope/FundManagerName":{"key":"Account/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"Account/MyScope/SomeProperty":{"key":"Account/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"Account/MyScope/AnotherProperty":{"key":"Account/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"Account/MyScope/ReBalanceInterval":{"key":"Account/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # dict(str, ModelProperty) | The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"Account/Manager/Id\". (optional)

    try:
        # [EXPERIMENTAL] UpsertAccountProperties: Upsert account properties
        api_response = api_instance.upsert_account_properties(scope, code, account_code, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->upsert_account_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts to update or insert the properties onto. | 
 **code** | **str**| The code of the Chart of Accounts to update or insert the properties onto. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **account_code** | **str**| The unique ID of the account to create or update properties for. | 
 **request_body** | [**dict(str, ModelProperty)**](ModelProperty.md)| The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;Account/Manager/Id\&quot;. | [optional] 

### Return type

[**AccountProperties**](AccountProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_accounts**
> AccountsUpsertResponse upsert_accounts(scope, code, account)

[EXPERIMENTAL] UpsertAccounts: Upsert Accounts

Create or update accounts in the Chart of Accounts. An account will be updated  if it already exists and created if it does not.  The maximum number of accounts that this method can upsert per request is 2,000.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts.
code = 'code_example' # str | The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts.
account = [{"code":"001456","description":"Cash","type":"Asset","status":"Active","control":"Manual","properties":{}},{"code":"123653","description":"Dividends","type":"Revenue","status":"Inactive","control":"System","properties":{}}] # list[Account] | A list of accounts to be created or updated.

    try:
        # [EXPERIMENTAL] UpsertAccounts: Upsert Accounts
        api_response = api_instance.upsert_accounts(scope, code, account)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->upsert_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts. | 
 **code** | **str**| The code of the Chart of Accounts. Together with the scope this uniquely identifies              the Chart of Accounts. | 
 **account** | [**list[Account]**](Account.md)| A list of accounts to be created or updated. | 

### Return type

[**AccountsUpsertResponse**](AccountsUpsertResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The newly upserted Accounts. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_chart_of_accounts_properties**
> ChartOfAccountsProperties upsert_chart_of_accounts_properties(scope, code, request_body=request_body)

[EXPERIMENTAL] UpsertChartOfAccountsProperties: Upsert Chart of Accounts properties

Update or insert one or more properties onto a single Chart of Accounts. A property will be updated if it  already exists and inserted if it does not. All properties must be of the domain 'ChartOfAccounts'.                Upserting a property that exists for a Chart of Accounts, with a null value, will delete the instance of the property for that group.                Properties have an <i>effectiveFrom</i> datetime for which the property is valid, and an <i>effectiveUntil</i>  datetime until which the property is valid. Not supplying an <i>effectiveUntil</i> datetime results in the property being  valid indefinitely, or until the next <i>effectiveFrom</i> datetime of the property.

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
    api_instance = lusid.ChartOfAccountsApi(api_client)
    scope = 'scope_example' # str | The scope of the Chart of Accounts to update or insert the properties onto.
code = 'code_example' # str | The code of the Chart of Accounts to update or insert the properties onto. Together with the scope this uniquely identifies the Chart of Accounts.
request_body = {"ChartOfAccounts/MyScope/FundManagerName":{"key":"ChartOfAccounts/MyScope/FundManagerName","value":{"labelValue":"Smith"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00"},"ChartOfAccounts/MyScope/SomeProperty":{"key":"ChartOfAccounts/MyScope/SomeProperty","value":{"labelValue":"SomeValue"},"effectiveFrom":"2016-01-01T00:00:00.0000000+00:00"},"ChartOfAccounts/MyScope/AnotherProperty":{"key":"ChartOfAccounts/MyScope/AnotherProperty","value":{"labelValue":"AnotherValue"},"effectiveFrom":"2018-03-05T00:00:00.0000000+00:00","effectiveUntil":"2020-01-01T00:00:00.0000000+00:00"},"ChartOfAccounts/MyScope/ReBalanceInterval":{"key":"ChartOfAccounts/MyScope/ReBalanceInterval","value":{"metricValue":{"value":30,"unit":"Days"}}}} # dict(str, ModelProperty) | The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \"ChartOfAccounts/Manager/Id\". (optional)

    try:
        # [EXPERIMENTAL] UpsertChartOfAccountsProperties: Upsert Chart of Accounts properties
        api_response = api_instance.upsert_chart_of_accounts_properties(scope, code, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChartOfAccountsApi->upsert_chart_of_accounts_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Chart of Accounts to update or insert the properties onto. | 
 **code** | **str**| The code of the Chart of Accounts to update or insert the properties onto. Together with the scope this uniquely identifies the Chart of Accounts. | 
 **request_body** | [**dict(str, ModelProperty)**](ModelProperty.md)| The properties to be updated or inserted onto the chart of account. Each property in               the request must be keyed by its unique property key. This has the format {domain}/{scope}/{code} e.g. \&quot;ChartOfAccounts/Manager/Id\&quot;. | [optional] 

### Return type

[**ChartOfAccountsProperties**](ChartOfAccountsProperties.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated or inserted properties. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

