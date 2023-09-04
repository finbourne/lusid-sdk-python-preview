# lusid.PostingModulesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_posting_module**](PostingModulesApi.md#create_posting_module) | **POST** /api/postingmodule/{scope} | [EXPERIMENTAL] CreatePostingModule: Create a Posting Module
[**delete_posting_module**](PostingModulesApi.md#delete_posting_module) | **DELETE** /api/postingmodule/{scope}/{code} | [EXPERIMENTAL] DeletePostingModule: Delete a PostingModule.
[**list_posting_module_rules**](PostingModulesApi.md#list_posting_module_rules) | **GET** /api/postingmodule/{scope}/{code}/postingrules | [EXPERIMENTAL] ListPostingModuleRules: List Posting Module Rules
[**list_posting_modules**](PostingModulesApi.md#list_posting_modules) | **GET** /api/postingmodule | [EXPERIMENTAL] ListPostingModules: List Posting Modules
[**set_posting_module_details**](PostingModulesApi.md#set_posting_module_details) | **PUT** /api/postingmodule/{scope}/{code} | [EXPERIMENTAL] SetPostingModuleDetails: Set the details of a Posting Module
[**set_posting_module_rules**](PostingModulesApi.md#set_posting_module_rules) | **PUT** /api/postingmodule/{scope}/{code}/postingrules | [EXPERIMENTAL] SetPostingModuleRules: Set the rules of a Posting Module


# **create_posting_module**
> PostingModuleCreateResponse create_posting_module(scope, posting_module_request)

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
    api_instance = lusid.PostingModulesApi(api_client)
    scope = 'scope_example' # str | The scope of the Posting Module.
posting_module_request = {"code":"PostingModuleCode","chartOfAccountsId":{"scope":"ChartOfAccountsScope","code":"ChartOfAccountsCode"},"displayName":"PostingModuleName","description":"PostingModuleDescription","rules":[{"ruleId":"rule1Id","account":"account1","ruleFilter":"Transaction.TransactionId eq 'Transaction_1'"}]} # PostingModuleRequest | The definition of the Posting Module.

    try:
        # [EXPERIMENTAL] CreatePostingModule: Create a Posting Module
        api_response = api_instance.create_posting_module(scope, posting_module_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostingModulesApi->create_posting_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Posting Module. | 
 **posting_module_request** | [**PostingModuleRequest**](PostingModuleRequest.md)| The definition of the Posting Module. | 

### Return type

[**PostingModuleCreateResponse**](PostingModuleCreateResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The newly created posting module. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_posting_module**
> DeletedEntityResponse delete_posting_module(scope, code)

[EXPERIMENTAL] DeletePostingModule: Delete a PostingModule.

Delete the given PostingModule.

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
    api_instance = lusid.PostingModulesApi(api_client)
    scope = 'scope_example' # str | The scope of the PostingModule to be deleted.
code = 'code_example' # str | The code of the PostingModule to be deleted. Together with the scope this uniquely identifies the PostingModule.

    try:
        # [EXPERIMENTAL] DeletePostingModule: Delete a PostingModule.
        api_response = api_instance.delete_posting_module(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostingModulesApi->delete_posting_module: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the PostingModule to be deleted. | 
 **code** | **str**| The code of the PostingModule to be deleted. Together with the scope this uniquely identifies the PostingModule. | 

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
**200** | The datetime that the PostingModule was deleted |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_posting_module_rules**
> PagedResourceListOfPostingModuleRule list_posting_module_rules(scope, code, as_at=as_at, page=page, start=start, limit=limit, filter=filter)

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
    api_instance = lusid.PostingModulesApi(api_client)
    scope = 'scope_example' # str | The scope of the posting module.
code = 'code_example' # str | The code of the posting module. Together with the scope this uniquely identifies              the Posting Module.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing posting module; this              value is returned from the previous call. If a pagination token is provided, the filter              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the rule type, specify \"id eq 'rule 1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)

    try:
        # [EXPERIMENTAL] ListPostingModuleRules: List Posting Module Rules
        api_response = api_instance.list_posting_module_rules(scope, code, as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostingModulesApi->list_posting_module_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the posting module. | 
 **code** | **str**| The code of the posting module. Together with the scope this uniquely identifies              the Posting Module. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the instrument. Defaults to              returning the latest version if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing posting module; this              value is returned from the previous call. If a pagination token is provided, the filter              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the rule type, specify \&quot;id eq &#39;rule 1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 

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
> PagedResourceListOfPostingModuleResponse list_posting_modules(as_at=as_at, page=page, start=start, limit=limit, filter=filter)

[EXPERIMENTAL] ListPostingModules: List Posting Modules

List all the posting rules matching particular criteria.

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
    api_instance = lusid.PostingModulesApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the Posting Module. Defaults to returning the latest version              of each Posting Module if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing Posting Modules; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
start = 56 # int | When paginating, skip this number of results. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the PostingModule type, specify \"id.Code eq '001'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)

    try:
        # [EXPERIMENTAL] ListPostingModules: List Posting Modules
        api_response = api_instance.list_posting_modules(as_at=as_at, page=page, start=start, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostingModulesApi->list_posting_modules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the Posting Module. Defaults to returning the latest version              of each Posting Module if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing Posting Modules; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **start** | **int**| When paginating, skip this number of results. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the PostingModule type, specify \&quot;id.Code eq &#39;001&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 

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
**200** | The requested Posting Modules |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_posting_module_details**
> PostingModuleResponse set_posting_module_details(scope, code, posting_module_details)

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
    api_instance = lusid.PostingModulesApi(api_client)
    scope = 'scope_example' # str | The scope of the Posting Module to be updated.
code = 'code_example' # str | The code of the Posting Module to be updated. Together with the scope this uniquely identifies the Posting Module.
posting_module_details = {"chartOfAccountsId":{"scope":"PostingModuleScope","code":"PostingModuleCode"},"displayName":"PostingModuleNameUpdated","description":"PostingModuleDescriptionUpdated","status":"Active"} # PostingModuleDetails | The new details for the Posting Module.

    try:
        # [EXPERIMENTAL] SetPostingModuleDetails: Set the details of a Posting Module
        api_response = api_instance.set_posting_module_details(scope, code, posting_module_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostingModulesApi->set_posting_module_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Posting Module to be updated. | 
 **code** | **str**| The code of the Posting Module to be updated. Together with the scope this uniquely identifies the Posting Module. | 
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
**200** | The updated posting module |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_posting_module_rules**
> PostingModuleRulesUpdatedResponse set_posting_module_rules(scope, code, posting_module_rule)

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
    api_instance = lusid.PostingModulesApi(api_client)
    scope = 'scope_example' # str | The scope of the Posting Module to be updated.
code = 'code_example' # str | The code of the Posting Module to be updated. Together with the scope this uniquely identifies the Posting Module.
posting_module_rule = [{"ruleId":"rule 1","account":"100002354","ruleFilter":"1 eq 1"},{"ruleId":"rule 2","account":"123456789","ruleFilter":"true eq true"}] # list[PostingModuleRule] | The new rule set for the Posting Module.

    try:
        # [EXPERIMENTAL] SetPostingModuleRules: Set the rules of a Posting Module
        api_response = api_instance.set_posting_module_rules(scope, code, posting_module_rule)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostingModulesApi->set_posting_module_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Posting Module to be updated. | 
 **code** | **str**| The code of the Posting Module to be updated. Together with the scope this uniquely identifies the Posting Module. | 
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
**200** | The posting module with updated rules |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

