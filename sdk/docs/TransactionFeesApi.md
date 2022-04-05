# lusid.TransactionFeesApi

All URIs are relative to *http://local-unit-test-server.lusid.com:41431*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_applicable_transaction_fees**](TransactionFeesApi.md#get_applicable_transaction_fees) | **POST** /api/transactions/fees/$GetApplicableFees | [EXPERIMENTAL] GetApplicableTransactionFees: Get the Fees and Commissions that may be applicable to a transaction.
[**get_transaction_fee_rule**](TransactionFeesApi.md#get_transaction_fee_rule) | **GET** /api/transactions/fees/rules/{code} | [EXPERIMENTAL] GetTransactionFeeRule: Retrieve the definition of single fee rule.
[**list_transaction_fee_rules**](TransactionFeesApi.md#list_transaction_fee_rules) | **GET** /api/transactions/fees/rules | [EXPERIMENTAL] ListTransactionFeeRules: List fee rules, with optional filtering.
[**upsert_transaction_fee_rules**](TransactionFeesApi.md#upsert_transaction_fee_rules) | **POST** /api/transactions/fees/rules | [EXPERIMENTAL] UpsertTransactionFeeRules: Upsert fee rules.


# **get_applicable_transaction_fees**
> ResourceListOfFeeRule get_applicable_transaction_fees(effective_at=effective_at, as_at=as_at, instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, request_body=request_body)

[EXPERIMENTAL] GetApplicableTransactionFees: Get the Fees and Commissions that may be applicable to a transaction.

Additionally, matching can be based on the instrument's properties, its portfolio properties, and any additional property keys present in the data file.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41431
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41431"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41431"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionFeesApi(api_client)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to match rule definitions. Defaults to the current LUSID  system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to match rule definitions. Defaults to returning the latest version if not  specified. (optional)
instrument_identifier_type = 'instrument_identifier_type_example' # str | Optional. The unique identifier type to use, eg 'Figi' or 'LusidInstrumentId'. (optional)
instrument_identifier = 'instrument_identifier_example' # str | Optional. The Instrument Identifier to get properties for. (optional)
portfolio_scope = 'portfolio_scope_example' # str | Optional. The scope of the portfolio to fetch properties from. (optional)
portfolio_code = 'portfolio_code_example' # str | Optional. The code of the portfolio to fetch properties from. (optional)
request_body = {"settlementCurrency":"GBP","country":"UK","office":"London"} # dict(str, str) | Any other property keys or fields, including the top-level fields of the              fee rule (e.g. \"ExecutionBroker\" and \"SettlementCurrency\" ) and those defined in AdditionalKeys, along with              their corresponding values that should be matched for fees. Eg. \"Instrument/default/Name=exampleValue\" or              \"AdditionalKey2=Value2\". (optional)

    try:
        # [EXPERIMENTAL] GetApplicableTransactionFees: Get the Fees and Commissions that may be applicable to a transaction.
        api_response = api_instance.get_applicable_transaction_fees(effective_at=effective_at, as_at=as_at, instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionFeesApi->get_applicable_transaction_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective_at** | **str**| The effective datetime or cut label at which to match rule definitions. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to match rule definitions. Defaults to returning the latest version if not  specified. | [optional] 
 **instrument_identifier_type** | **str**| Optional. The unique identifier type to use, eg &#39;Figi&#39; or &#39;LusidInstrumentId&#39;. | [optional] 
 **instrument_identifier** | **str**| Optional. The Instrument Identifier to get properties for. | [optional] 
 **portfolio_scope** | **str**| Optional. The scope of the portfolio to fetch properties from. | [optional] 
 **portfolio_code** | **str**| Optional. The code of the portfolio to fetch properties from. | [optional] 
 **request_body** | [**dict(str, str)**](str.md)| Any other property keys or fields, including the top-level fields of the              fee rule (e.g. \&quot;ExecutionBroker\&quot; and \&quot;SettlementCurrency\&quot; ) and those defined in AdditionalKeys, along with              their corresponding values that should be matched for fees. Eg. \&quot;Instrument/default/Name&#x3D;exampleValue\&quot; or              \&quot;AdditionalKey2&#x3D;Value2\&quot;. | [optional] 

### Return type

[**ResourceListOfFeeRule**](ResourceListOfFeeRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of applicable fee rules. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_fee_rule**
> FeeRule get_transaction_fee_rule(code, effective_at=effective_at, as_at=as_at)

[EXPERIMENTAL] GetTransactionFeeRule: Retrieve the definition of single fee rule.

Retrieves the fee rule definition at the given effective and as at times.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41431
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41431"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41431"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionFeesApi(api_client)
    code = 'code_example' # str | The fee rule code.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID  system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. (optional)

    try:
        # [EXPERIMENTAL] GetTransactionFeeRule: Retrieve the definition of single fee rule.
        api_response = api_instance.get_transaction_fee_rule(code, effective_at=effective_at, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionFeesApi->get_transaction_fee_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The fee rule code. | 
 **effective_at** | **str**| The effective datetime or cut label at which to retrieve the rule definition. Defaults to the current LUSID  system datetime if not specified. | [optional] 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the rule definition. Defaults to returning the latest version if not  specified. | [optional] 

### Return type

[**FeeRule**](FeeRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of one fee rule. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transaction_fee_rules**
> ResourceListOfFeeRule list_transaction_fee_rules(effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, page=page)

[EXPERIMENTAL] ListTransactionFeeRules: List fee rules, with optional filtering.

For more information about filtering results,  see https://support.lusid.com/knowledgebase/article/KA-01914.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41431
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41431"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41431"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionFeesApi(api_client)
    effective_at = 'effective_at_example' # str | The effective datetime or cut label at which to retrieve the rule definitions. Defaults to the current LUSID  system datetime if not specified. (optional)
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the rule definitions. Defaults to returning the latest version if not  specified. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results. (optional)
page = 'page_example' # str | The pagination token to use to continue listing entities; this value is returned from the previous call. If  a pagination token is provided, the filter, effectiveAt and asAt fields must not have changed since the  original request. (optional)

    try:
        # [EXPERIMENTAL] ListTransactionFeeRules: List fee rules, with optional filtering.
        api_response = api_instance.list_transaction_fee_rules(effective_at=effective_at, as_at=as_at, limit=limit, filter=filter, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionFeesApi->list_transaction_fee_rules: %s\n" % e)
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

[**ResourceListOfFeeRule**](ResourceListOfFeeRule.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A filtered list of fee rules available. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_transaction_fee_rules**
> FeeRuleUpsertResponse upsert_transaction_fee_rules(request_body, effective_at=effective_at)

[EXPERIMENTAL] UpsertTransactionFeeRules: Upsert fee rules.

To upsert a new rule, the code field must be left empty, a code will then be assigned and returned as part  of the response. To update an existing rule, include the fee code. It is possible to both create and update  fee rules in the same request.                The upsert is transactional - either all create/update operations will succeed or none of them will.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:41431
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41431"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:41431"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.TransactionFeesApi(api_client)
    request_body = {"update":{"code":"FeeRule_1","transactionPropertyKey":"Transaction/default/fee","transactionType":"*","country":"UK","counterparty":"*","transactionCurrency":"*","settlementCurrency":"*","executionBroker":"*","custodian":"*","exchange":"My Exchange","fee":{"calculationMethod":"BasisPoints","multiplier":"Value","calculationAmount":10},"additionalKeys":{"office":"London"},"description":"Basic fee rule to be updated."},"create":{"transactionPropertyKey":"Transaction/default/fee","transactionType":"*","country":"UK","counterparty":"*","transactionCurrency":"*","settlementCurrency":"*","executionBroker":"*","custodian":"*","exchange":"My Exchange","fee":{"calculationMethod":"BasisPoints","multiplier":"Value","calculationAmount":10},"minFee":{"calculationMethod":"Flat","multiplier":"Value","calculationAmount":5},"maxFee":{"calculationMethod":"Flat","multiplier":"Value","calculationAmount":25},"additionalKeys":{"office":"London"},"description":"Basic fee rule with minimum/maximum to be created"}} # dict(str, FeeRuleUpsertRequest) | A dictionary of upsert request identifiers to rule upsert requests. The request               identifiers are valid for the request only and can be used to link the upserted fee rule to the code of a               created fee rule.
effective_at = 'effective_at_example' # str | The effective datetime or cut label at which the rule will take effect. Defaults to the current LUSID  system datetime if not specified. In the case of an update, the changes will take place from this effective  time until the next effective time that the rule as been upserted at. For example, consider a rule that  already exists, and has previously had an update applied so that the definition will change on the first day  of the coming month. An upsert effective from the current day will only change the definition until the  first day of the coming month. An additional upsert at the same time (first day of the month) is required  if the newly-updated definition is to supersede the future definition. (optional)

    try:
        # [EXPERIMENTAL] UpsertTransactionFeeRules: Upsert fee rules.
        api_response = api_instance.upsert_transaction_fee_rules(request_body, effective_at=effective_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionFeesApi->upsert_transaction_fee_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**dict(str, FeeRuleUpsertRequest)**](FeeRuleUpsertRequest.md)| A dictionary of upsert request identifiers to rule upsert requests. The request               identifiers are valid for the request only and can be used to link the upserted fee rule to the code of a               created fee rule. | 
 **effective_at** | **str**| The effective datetime or cut label at which the rule will take effect. Defaults to the current LUSID  system datetime if not specified. In the case of an update, the changes will take place from this effective  time until the next effective time that the rule as been upserted at. For example, consider a rule that  already exists, and has previously had an update applied so that the definition will change on the first day  of the coming month. An upsert effective from the current day will only change the definition until the  first day of the coming month. An additional upsert at the same time (first day of the month) is required  if the newly-updated definition is to supersede the future definition. | [optional] 

### Return type

[**FeeRuleUpsertResponse**](FeeRuleUpsertResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upsert fee rules. New fee rules must have an empty code field. Where a code is given, this rule must already exist and will be updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

