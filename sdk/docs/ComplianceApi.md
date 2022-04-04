# lusid.ComplianceApi

All URIs are relative to *http://local-unit-test-server.lusid.com:41809*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_compliance_rule**](ComplianceApi.md#get_compliance_rule) | **GET** /api/compliance/rules/{scope}/{code} | [EXPERIMENTAL] GetComplianceRule: Retrieve the definition of single compliance rule.
[**get_compliance_run**](ComplianceApi.md#get_compliance_run) | **GET** /api/compliance/{runId} | [EXPERIMENTAL] GetComplianceRun: Get the details of a single compliance run.
[**list_compliance_rules**](ComplianceApi.md#list_compliance_rules) | **GET** /api/compliance/rules | [EXPERIMENTAL] ListComplianceRules: List compliance rules, with optional filtering.
[**list_compliance_runs**](ComplianceApi.md#list_compliance_runs) | **GET** /api/compliance | [EXPERIMENTAL] ListComplianceRuns: List historical compliance runs.
[**run_compliance_check**](ComplianceApi.md#run_compliance_check) | **POST** /api/compliance/run | [EXPERIMENTAL] RunComplianceCheck: Kick off the compliance check process
[**upsert_compliance_rules**](ComplianceApi.md#upsert_compliance_rules) | **POST** /api/compliance/rules | [EXPERIMENTAL] UpsertComplianceRules: Upsert compliance rules.


# **get_compliance_rule**
> ComplianceRule get_compliance_rule(scope, code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetComplianceRule: Retrieve the definition of single compliance rule.

Retrieves the compliance rule definition at the given effective and as at times.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41809
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    scope = 'scope_example' # str | The compliance rule scope.
code = 'code_example' # str | The compliance rule code.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID  system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. (optional)

    try:
        # [EXPERIMENTAL] GetComplianceRule: Retrieve the definition of single compliance rule.
        api_response = api_instance.get_compliance_rule(scope, code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->get_compliance_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The compliance rule scope. | 
 **code** | **str**| The compliance rule code. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. | [optional] 

### Return type

[**ComplianceRule**](ComplianceRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of one compliance rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compliance_run**
> PagedResourceListOfComplianceRuleResult get_compliance_run(run_id, page=page, limit=limit, filter=filter)

[EXPERIMENTAL] GetComplianceRun: Get the details of a single compliance run.

Use this endpoint to fetch the detail associated with a specific compliance run, including a breakdown  of the passing state of each rule, portfolio combination.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41809
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    run_id = 'run_id_example' # str | The unique identifier of the compliance run requested.
page = 'page_example' # str | The pagination token to use to continue listing compliance rule results from a previous call to list compliance rule result.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EXPERIMENTAL] GetComplianceRun: Get the details of a single compliance run.
        api_response = api_instance.get_compliance_run(run_id, page=page, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->get_compliance_run: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **str**| The unique identifier of the compliance run requested. | 
 **page** | **str**| The pagination token to use to continue listing compliance rule results from a previous call to list compliance rule result.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfComplianceRuleResult**](PagedResourceListOfComplianceRuleResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details of a specific compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_rules**
> ResourceListOfComplianceRule list_compliance_rules(effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, page=page)

[EXPERIMENTAL] ListComplianceRules: List compliance rules, with optional filtering.

For more information about filtering results,  see https://support.lusid.com/knowledgebase/article/KA-01914.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41809
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID  system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results. (optional)
page = 'page_example' # str | The pagination token to use to continue listing entities; this value is returned from the previous call. If  a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the  original request. (optional)

    try:
        # [EXPERIMENTAL] ListComplianceRules: List compliance rules, with optional filtering.
        api_response = api_instance.list_compliance_rules(effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results. | [optional] 
 **page** | **str**| The pagination token to use to continue listing entities; this value is returned from the previous call. If  a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the  original request. | [optional] 

### Return type

[**ResourceListOfComplianceRule**](ResourceListOfComplianceRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A filtered list of compliance rules available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compliance_runs**
> PagedResourceListOfComplianceRun list_compliance_runs(page=page, limit=limit, filter=filter)

[EXPERIMENTAL] ListComplianceRuns: List historical compliance runs.

Use this endpoint to fetch a list of all historical compliance runs.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41809
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    page = 'page_example' # str | The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. (optional)
limit = 56 # int | When paginating, limit the number of returned results to this many. (optional)
filter = 'filter_example' # str | Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. (optional)

    try:
        # [EXPERIMENTAL] ListComplianceRuns: List historical compliance runs.
        api_response = api_instance.list_compliance_runs(page=page, limit=limit, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->list_compliance_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| The pagination token to use to continue listing compliance runs from a previous call to list compliance runs.              This value is returned from the previous call. If a pagination token is provided the sortBy, filter, and asAt fields              must not have changed since the original request. Also, if set, a start value cannot be provided. | [optional] 
 **limit** | **int**| When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about filtering results from LUSID here https://support.lusid.com/filtering-results-from-lusid. | [optional] 

### Return type

[**PagedResourceListOfComplianceRun**](PagedResourceListOfComplianceRun.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The List of all compliance runs completed |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_compliance_check**
> ComplianceRun run_compliance_check(file_name)

[EXPERIMENTAL] RunComplianceCheck: Kick off the compliance check process

Use this endpoint to fetch the start a compliance run, based on a pre-set mapping file.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41809
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    file_name = 'file_name_example' # str | The name of compliance mappings file to use. Has to exist in drive ComplianceRules folder

    try:
        # [EXPERIMENTAL] RunComplianceCheck: Kick off the compliance check process
        api_response = api_instance.run_compliance_check(file_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->run_compliance_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The name of compliance mappings file to use. Has to exist in drive ComplianceRules folder | 

### Return type

[**ComplianceRun**](ComplianceRun.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifying information of a compliance run |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_compliance_rules**
> ComplianceRuleUpsertResponse upsert_compliance_rules(request_body, effective_at=effective_at)

[EXPERIMENTAL] UpsertComplianceRules: Upsert compliance rules.

To upsert a new rule, the code field must be left empty, a code will then be assigned and returned as part  of the response. To update an existing rule, include the rule code. It is possible to both create and update  compliance rules in the same request.                The upsert is transactional - either all create/update operations will succeed or none of them will.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41809
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41809"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.ComplianceApi(api_client)
    request_body = {"create":{"scope":"CompanyPolicies","displayName":"Max 200 Securities","type":"RangeNumberSecurities","lowerBound":0,"upperBound":200,"schedule":"PreAndPostTrade","hardRequirement":true,"targetPortfolioIds":[{"scope":"CorePortfolios","code":"UK"},{"scope":"CorePortfolios","code":"World"}],"description":"Portfolio must contain no more than 200 securities."},"update":{"scope":"FundObjectives","code":"ComplianceRule_1","displayName":"30 percent bonds","type":"RangePercentSecurityType","value":"Bond","lowerBound":25,"upperBound":35,"schedule":"PostTrade","hardRequirement":false,"targetPortfolioIds":[{"scope":"CorePortfolios","code":"Balanced"}],"description":"Portfolio must contain 30% bonds by value."}} # dict(str, ComplianceRuleUpsertRequest) | A dictionary of upsert request identifiers to rule upsert requests. The request               identifiers are valid for the request only and can be used to link the upserted compliance rule to the code               of a created compliance rule.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the rule will take effect. Defaults to the current LUSID  system datetime if not specified. In the case of an update, the changes will take place from this effective  time until the next effective time that the rule as been upserted at. For example, consider a rule that  already exists, and has previously had an update applied so that the definition will change on the first day  of the coming month. An upsert effective from the current day will only change the definition until the  first day of the coming month. An additional upsert at the same time (first day of the month) is required  if the newly-updated definition is to supersede the future definition. (optional)

    try:
        # [EXPERIMENTAL] UpsertComplianceRules: Upsert compliance rules.
        api_response = api_instance.upsert_compliance_rules(request_body, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplianceApi->upsert_compliance_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, ComplianceRuleUpsertRequest)**](ComplianceRuleUpsertRequest.md)| A dictionary of upsert request identifiers to rule upsert requests. The request               identifiers are valid for the request only and can be used to link the upserted compliance rule to the code               of a created compliance rule. | 
 **effective_at** | **str**| The effective datetime or cut label at which the rule will take effect. Defaults to the current LUSID  system datetime if not specified. In the case of an update, the changes will take place from this effective  time until the next effective time that the rule as been upserted at. For example, consider a rule that  already exists, and has previously had an update applied so that the definition will change on the first day  of the coming month. An upsert effective from the current day will only change the definition until the  first day of the coming month. An additional upsert at the same time (first day of the month) is required  if the newly-updated definition is to supersede the future definition. | [optional] 

### Return type

[**ComplianceRuleUpsertResponse**](ComplianceRuleUpsertResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upsert compliance rules. New compliance rules must have an empty code field. Where a codeis given, this rule must already exist and will be updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

