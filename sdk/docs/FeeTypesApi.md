# lusid.FeeTypesApi

All URIs are relative to *https://www.lusid.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fee_type**](FeeTypesApi.md#create_fee_type) | **POST** /api/feetypes/{scope} | [EXPERIMENTAL] CreateFeeType: Create a FeeType.
[**delete_fee_type**](FeeTypesApi.md#delete_fee_type) | **DELETE** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] DeleteFeeType: Delete a FeeType.
[**get_fee_template_specifications**](FeeTypesApi.md#get_fee_template_specifications) | **GET** /api/feetypes/feetransactiontemplatespecification | [EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.
[**get_fee_type**](FeeTypesApi.md#get_fee_type) | **GET** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] GetFeeType: Get a FeeType
[**list_fee_types**](FeeTypesApi.md#list_fee_types) | **GET** /api/feetypes | [EXPERIMENTAL] ListFeeTypes: List FeeTypes
[**update_fee_type**](FeeTypesApi.md#update_fee_type) | **PUT** /api/feetypes/{scope}/{code} | [EXPERIMENTAL] UpdateFeeType: Update a FeeType.


# **create_fee_type**
> FeeType create_fee_type(scope, fee_type_request)

[EXPERIMENTAL] CreateFeeType: Create a FeeType.

Create a FeeType that contains templates used to create fee transactions.

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
    api_instance = lusid.FeeTypesApi(api_client)
    scope = 'scope_example' # str | The scope of the FeeType.
fee_type_request = {"code":"AdminFees","displayName":"AdminFees","description":"Generating transactions to accrue and settle admin fees for funds","componentTransactions":[{"displayName":"Transaction for admin fee accruals","transactionFieldMap":{"transactionId":"{{FundFee.defaultFeeTransactionId}}-Accrual","type":"FeeAccrual","source":"default","instrument":"{{FundFee.feeInstrument}}","transactionDate":"{{FundFee.valuationPointDate}}","settlementDate":"{{FundFee.valuationPointDate}}","units":"{{FundFee.amount}}","transactionPrice":{"price":"1.0","type":"Price"},"transactionCurrency":"{{FundFee.feeCurrency}}","exchangeRate":"1.0","totalConsideration":{"currency":"{{FundFee.feeCurrency}}","amount":"{{FundFee.amount}}"}},"transactionPropertyMap":[],"preserveTaxLotStructure":false},{"displayName":"Transaction for admin fee payables","transactionFieldMap":{"transactionId":"{{FundFee.defaultFeeTransactionId}}-Payable","type":"FeePayment","source":"default","instrument":"{{FundFee.feeInstrument}}","transactionDate":"{{FundFee.valuationPointDate}}","settlementDate":"{{FundFee.valuationPointDate}}","units":"{{FundFee.amount}}","transactionPrice":{"price":"1.0","type":"Price"},"transactionCurrency":"{{FundFee.feeCurrency}}","exchangeRate":"1.0","totalConsideration":{"currency":"{{FundFee.feeCurrency}}","amount":"{{FundFee.amount}}"}},"transactionPropertyMap":[],"preserveTaxLotStructure":false}]} # FeeTypeRequest | The contents of the FeeType.

    try:
        # [EXPERIMENTAL] CreateFeeType: Create a FeeType.
        api_response = api_instance.create_fee_type(scope, fee_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeeTypesApi->create_fee_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **fee_type_request** | [**FeeTypeRequest**](FeeTypeRequest.md)| The contents of the FeeType. | 

### Return type

[**FeeType**](FeeType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fee_type**
> DeletedEntityResponse delete_fee_type(scope, code)

[EXPERIMENTAL] DeleteFeeType: Delete a FeeType.

Delete a FeeType that contains templates used to create fee transactions.

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
    api_instance = lusid.FeeTypesApi(api_client)
    scope = 'scope_example' # str | The scope of the FeeType.
code = 'code_example' # str | The code of the fee type

    try:
        # [EXPERIMENTAL] DeleteFeeType: Delete a FeeType.
        api_response = api_instance.delete_fee_type(scope, code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeeTypesApi->delete_fee_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **code** | **str**| The code of the fee type | 

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
**200** | Delete a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_template_specifications**
> FeeTransactionTemplateSpecification get_fee_template_specifications()

[EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.

Get FeeTemplateSpecifications used in the FeeType.

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
    api_instance = lusid.FeeTypesApi(api_client)
    
    try:
        # [EXPERIMENTAL] GetFeeTemplateSpecifications: Get FeeTemplateSpecifications used in the FeeType.
        api_response = api_instance.get_fee_template_specifications()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeeTypesApi->get_fee_template_specifications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeeTransactionTemplateSpecification**](FeeTransactionTemplateSpecification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fee template specifications used with a FeeType. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee_type**
> FeeType get_fee_type(scope, code, as_at=as_at)

[EXPERIMENTAL] GetFeeType: Get a FeeType

Get a FeeType that contains templates used to create fee transactions.

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
    api_instance = lusid.FeeTypesApi(api_client)
    scope = 'scope_example' # str | The scope of the FeeType
code = 'code_example' # str | The code of the FeeType
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the FeeType. Defaults to returning the latest version of the FeeType, if not specified. (optional)

    try:
        # [EXPERIMENTAL] GetFeeType: Get a FeeType
        api_response = api_instance.get_fee_type(scope, code, as_at=as_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeeTypesApi->get_fee_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType | 
 **code** | **str**| The code of the FeeType | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the FeeType. Defaults to returning the latest version of the FeeType, if not specified. | [optional] 

### Return type

[**FeeType**](FeeType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fee_types**
> PagedResourceListOfFeeType list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)

[EXPERIMENTAL] ListFeeTypes: List FeeTypes

List FeeTypes that contain templates used to create fee transactions.

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
    api_instance = lusid.FeeTypesApi(api_client)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the FeeTypes. Defaults to returning the latest version of each FeeType if not specified. (optional)
page = 'page_example' # str | The pagination token to use to continue listing FeeTypes; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. (optional)
limit = 56 # int | When paginating, limit the results to this number. Defaults to 100 if not specified. (optional)
filter = 'filter_example' # str | Expression to filter the results.              For example, to filter on the Code of the FeeType type, specify \"id.Code eq 'FeeType1'\". For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. (optional)
sort_by = ['sort_by_example'] # list[str] | A list of field names or properties to sort by, each suffixed by \" ASC\" or \" DESC\" (optional)

    try:
        # [EXPERIMENTAL] ListFeeTypes: List FeeTypes
        api_response = api_instance.list_fee_types(as_at=as_at, page=page, limit=limit, filter=filter, sort_by=sort_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeeTypesApi->list_fee_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the FeeTypes. Defaults to returning the latest version of each FeeType if not specified. | [optional] 
 **page** | **str**| The pagination token to use to continue listing FeeTypes; this              value is returned from the previous call. If a pagination token is provided, the filter, effectiveAt              and asAt fields must not have changed since the original request. | [optional] 
 **limit** | **int**| When paginating, limit the results to this number. Defaults to 100 if not specified. | [optional] 
 **filter** | **str**| Expression to filter the results.              For example, to filter on the Code of the FeeType type, specify \&quot;id.Code eq &#39;FeeType1&#39;\&quot;. For more information about filtering              results, see https://support.lusid.com/knowledgebase/article/KA-01914. | [optional] 
 **sort_by** | [**list[str]**](str.md)| A list of field names or properties to sort by, each suffixed by \&quot; ASC\&quot; or \&quot; DESC\&quot; | [optional] 

### Return type

[**PagedResourceListOfFeeType**](PagedResourceListOfFeeType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested Fee Types |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fee_type**
> FeeType update_fee_type(scope, code, update_fee_type_request)

[EXPERIMENTAL] UpdateFeeType: Update a FeeType.

Update a FeeType that contains templates used to create fee transactions.

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
    api_instance = lusid.FeeTypesApi(api_client)
    scope = 'scope_example' # str | The scope of the FeeType.
code = 'code_example' # str | The code of the fee type
update_fee_type_request = {"displayName":"AdminFees","description":"Generating transactions to accrue and settle admin fees for funds","componentTransactions":[{"displayName":"Transaction for admin fee accruals","transactionFieldMap":{"transactionId":"{{FundFee.defaultFeeTransactionId}}-Accrual","type":"FeeAccrual","source":"default","instrument":"{{FundFee.feeInstrument}}","transactionDate":"{{FundFee.valuationPointDate}}","settlementDate":"{{FundFee.valuationPointDate}}","units":"{{FundFee.amount}}","transactionPrice":{"price":"1.0","type":"Price"},"transactionCurrency":"{{FundFee.feeCurrency}}","exchangeRate":"1.0","totalConsideration":{"currency":"{{FundFee.feeCurrency}}","amount":"{{FundFee.amount}}"}},"transactionPropertyMap":[],"preserveTaxLotStructure":false},{"displayName":"Transaction for admin fee payables","transactionFieldMap":{"transactionId":"{{FundFee.defaultFeeTransactionId}}-Payable","type":"FeePayment","source":"default","instrument":"{{FundFee.feeInstrument}}","transactionDate":"{{FundFee.valuationPointDate}}","settlementDate":"{{FundFee.valuationPointDate}}","units":"{{FundFee.amount}}","transactionPrice":{"price":"1.0","type":"Price"},"transactionCurrency":"{{FundFee.feeCurrency}}","exchangeRate":"1.0","totalConsideration":{"currency":"{{FundFee.feeCurrency}}","amount":"{{FundFee.amount}}"}},"transactionPropertyMap":[],"preserveTaxLotStructure":false}]} # UpdateFeeTypeRequest | The contents of the FeeType.

    try:
        # [EXPERIMENTAL] UpdateFeeType: Update a FeeType.
        api_response = api_instance.update_fee_type(scope, code, update_fee_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FeeTypesApi->update_fee_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the FeeType. | 
 **code** | **str**| The code of the fee type | 
 **update_fee_type_request** | [**UpdateFeeTypeRequest**](UpdateFeeTypeRequest.md)| The contents of the FeeType. | 

### Return type

[**FeeType**](FeeType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a FeeType. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

