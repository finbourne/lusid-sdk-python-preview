# lusid.FeesAndCommissionsApi

All URIs are relative to *http://local-unit-test-server.lusid.com:48796*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_applicable_fees**](FeesAndCommissionsApi.md#get_applicable_fees) | **GET** /api/feesandcommissions | [EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.
[**list_all_fees**](FeesAndCommissionsApi.md#list_all_fees) | **GET** /api/feesandcommissions/rules | [EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.


# **get_applicable_fees**
> ResourceListOfFeeCalculationDetails get_applicable_fees(instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, additional_search_keys=additional_search_keys, file_name=file_name)

[EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.

Additionally, matching can be based on the instrument's properties, its portfolio properties, and any additional property keys present in the data file.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:48796
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:48796"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:48796"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.FeesAndCommissionsApi(api_client)
    instrument_identifier_type = 'instrument_identifier_type_example' # str | Optional. The unique identifier type to use, eg 'Figi' or 'LusidInstrumentId'. (optional)
instrument_identifier = 'instrument_identifier_example' # str | Optional. The Instrument Identifier to get properties for. (optional)
portfolio_scope = 'portfolio_scope_example' # str | Optional. The scope of the portfolio to fetch additional properties from. (optional)
portfolio_code = 'portfolio_code_example' # str | Optional. The code of the portfolio to fetch additional properties from. (optional)
additional_search_keys = ['additional_search_keys_example'] # list[str] | Any other property keys or fields and their corresponding values that should be matched for fees. Eg. \"Instrument/default/Name=exampleValue\" or \"AdditionalKey2=Value2\".              The list of fields available is as follows : \"RuleName\", \"Country\", \"FeeType\", \"FeeRate\", \"MinFee\", \"MaxFee\", \"PropertyKey\",               \"TransactionType\", \"Counterparty\", \"SettlementCurrency\", \"TransactionCurrency\", \"ExecutionBroker\",               \"Custodian\", \"Exchange\" (optional)
file_name = 'file_name_example' # str | Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your {fees-and-commissions} Drive folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker. (optional)

    try:
        # [EXPERIMENTAL] GetApplicableFees: Get the Fees and Commissions that may be applicable to a transaction.
        api_response = api_instance.get_applicable_fees(instrument_identifier_type=instrument_identifier_type, instrument_identifier=instrument_identifier, portfolio_scope=portfolio_scope, portfolio_code=portfolio_code, additional_search_keys=additional_search_keys, file_name=file_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeesAndCommissionsApi->get_applicable_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instrument_identifier_type** | **str**| Optional. The unique identifier type to use, eg &#39;Figi&#39; or &#39;LusidInstrumentId&#39;. | [optional] 
 **instrument_identifier** | **str**| Optional. The Instrument Identifier to get properties for. | [optional] 
 **portfolio_scope** | **str**| Optional. The scope of the portfolio to fetch additional properties from. | [optional] 
 **portfolio_code** | **str**| Optional. The code of the portfolio to fetch additional properties from. | [optional] 
 **additional_search_keys** | [**list[str]**](str.md)| Any other property keys or fields and their corresponding values that should be matched for fees. Eg. \&quot;Instrument/default/Name&#x3D;exampleValue\&quot; or \&quot;AdditionalKey2&#x3D;Value2\&quot;.              The list of fields available is as follows : \&quot;RuleName\&quot;, \&quot;Country\&quot;, \&quot;FeeType\&quot;, \&quot;FeeRate\&quot;, \&quot;MinFee\&quot;, \&quot;MaxFee\&quot;, \&quot;PropertyKey\&quot;,               \&quot;TransactionType\&quot;, \&quot;Counterparty\&quot;, \&quot;SettlementCurrency\&quot;, \&quot;TransactionCurrency\&quot;, \&quot;ExecutionBroker\&quot;,               \&quot;Custodian\&quot;, \&quot;Exchange\&quot; | [optional] 
 **file_name** | **str**| Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your {fees-and-commissions} Drive folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker. | [optional] 

### Return type

[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The List of applicable fee calculations details |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_fees**
> ResourceListOfFeeCalculationDetails list_all_fees(additional_search_keys=additional_search_keys, file_name=file_name)

[EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.

By default, will list ALL rules available. Additional keys and be specified to list a smaller subset of rules.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://local-unit-test-server.lusid.com:48796
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:48796"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid.Configuration(
    host = "http://local-unit-test-server.lusid.com:48796"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid.FeesAndCommissionsApi(api_client)
    additional_search_keys = ['additional_search_keys_example'] # list[str] | Any other property keys or fields and their corresponding values that should be matched to reduce the list of rules returned. Eg. \"Instrument/default/Name=exampleValue\" or \"AdditionalKey2=Value2\".              The minimum list of fields available is as follows : \"RuleName\", \"Country\", \"FeeCalculationMethod\", \"FeeMultiplier\", \"MinFeeCalculationMethod\",              \"MinFeeMultiplier\", \"MaxFeeCalculationMethod\", \"MaxFeeMultiplier\", \"PropertyKey\",              \"TransactionType\", \"Counterparty\", \"SettlementCurrency\", \"TransactionCurrency\", \"ExecutionBroker\",              \"Custodian\", \"Exchange\" (optional)
file_name = 'file_name_example' # str | Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your Drive {fees-and-commissions} folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker. (optional)

    try:
        # [EXPERIMENTAL] ListAllFees: List the rules available for fees and commissions.
        api_response = api_instance.list_all_fees(additional_search_keys=additional_search_keys, file_name=file_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeesAndCommissionsApi->list_all_fees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_search_keys** | [**list[str]**](str.md)| Any other property keys or fields and their corresponding values that should be matched to reduce the list of rules returned. Eg. \&quot;Instrument/default/Name&#x3D;exampleValue\&quot; or \&quot;AdditionalKey2&#x3D;Value2\&quot;.              The minimum list of fields available is as follows : \&quot;RuleName\&quot;, \&quot;Country\&quot;, \&quot;FeeCalculationMethod\&quot;, \&quot;FeeMultiplier\&quot;, \&quot;MinFeeCalculationMethod\&quot;,              \&quot;MinFeeMultiplier\&quot;, \&quot;MaxFeeCalculationMethod\&quot;, \&quot;MaxFeeMultiplier\&quot;, \&quot;PropertyKey\&quot;,              \&quot;TransactionType\&quot;, \&quot;Counterparty\&quot;, \&quot;SettlementCurrency\&quot;, \&quot;TransactionCurrency\&quot;, \&quot;ExecutionBroker\&quot;,              \&quot;Custodian\&quot;, \&quot;Exchange\&quot; | [optional] 
 **file_name** | **str**| Optionally provide the filename of an alternative to the default fees file ({fees.csv})              in your Drive {fees-and-commissions} folder, to support different fee structures.              For example, you might use one to understand the effect of different fees when considering a change in broker. | [optional] 

### Return type

[**ResourceListOfFeeCalculationDetails**](ResourceListOfFeeCalculationDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The List of all fee and commission rules available |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

