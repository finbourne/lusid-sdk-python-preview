# lusid.CounterpartyApi

All URIs are relative to *http://local-unit-test-server.lusid.com:57352*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_counterparty**](CounterpartyApi.md#delete_counterparty) | **DELETE** /api/counterparties/counterparties/counterparty/{scope}/{code} | [EXPERIMENTAL] Delete the Counterparty of given scope and code, assuming that it is present.
[**delete_credit_support_annex**](CounterpartyApi.md#delete_credit_support_annex) | **DELETE** /api/counterparties/counterparties/csa/{scope}/{code} | [EXPERIMENTAL] Delete the CSA of given scope and code, assuming that it is present.
[**get_counterparty**](CounterpartyApi.md#get_counterparty) | **GET** /api/counterparties/counterparties/counterparty/{scope}/{code} | [EXPERIMENTAL] Get Counterparty
[**get_credit_support_annex**](CounterpartyApi.md#get_credit_support_annex) | **GET** /api/counterparties/counterparties/csa/{scope}/{code} | [EXPERIMENTAL] Get CSA
[**list_counterparties**](CounterpartyApi.md#list_counterparties) | **GET** /api/counterparties/counterparties/counterparty | [EXPERIMENTAL] List the set of Counterparties
[**list_credit_support_annexes**](CounterpartyApi.md#list_credit_support_annexes) | **GET** /api/counterparties/counterparties/csa | [EXPERIMENTAL] List the set of CSAs
[**upsert_counterparty**](CounterpartyApi.md#upsert_counterparty) | **POST** /api/counterparties/counterparties/counterparty | [EXPERIMENTAL] Upsert Counterparty. This creates or updates the data in Lusid.
[**upsert_credit_support_annex**](CounterpartyApi.md#upsert_credit_support_annex) | **POST** /api/counterparties/counterparties/csa | [EXPERIMENTAL] Upsert CSA. This creates or updates the data in Lusid.


# **delete_counterparty**
> AnnulSingleStructuredDataResponse delete_counterparty(scope, code)

[EXPERIMENTAL] Delete the Counterparty of given scope and code, assuming that it is present.

Delete the specified Counterparty from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:57352
configuration.host = "http://local-unit-test-server.lusid.com:57352"
# Create an instance of the API class
api_instance = lusid.CounterpartyApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the Counterparty to delete.
code = 'code_example' # str | The Counterparty to delete.

try:
    # [EXPERIMENTAL] Delete the Counterparty of given scope and code, assuming that it is present.
    api_response = api_instance.delete_counterparty(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->delete_counterparty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Counterparty to delete. | 
 **code** | **str**| The Counterparty to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credit_support_annex**
> AnnulSingleStructuredDataResponse delete_credit_support_annex(scope, code)

[EXPERIMENTAL] Delete the CSA of given scope and code, assuming that it is present.

Delete the specified CSA from a single scope.  The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:57352
configuration.host = "http://local-unit-test-server.lusid.com:57352"
# Create an instance of the API class
api_instance = lusid.CounterpartyApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the CSA to delete.
code = 'code_example' # str | The CSA to delete.

try:
    # [EXPERIMENTAL] Delete the CSA of given scope and code, assuming that it is present.
    api_response = api_instance.delete_credit_support_annex(scope, code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->delete_credit_support_annex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the CSA to delete. | 
 **code** | **str**| The CSA to delete. | 

### Return type

[**AnnulSingleStructuredDataResponse**](AnnulSingleStructuredDataResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The AsAt of deletion or failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_counterparty**
> GetCounterpartyResponse get_counterparty(scope, code, as_at=as_at)

[EXPERIMENTAL] Get Counterparty

Get a Counterparty from a single scope.  The response will return either the counterparty that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:57352
configuration.host = "http://local-unit-test-server.lusid.com:57352"
# Create an instance of the API class
api_instance = lusid.CounterpartyApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the Counterparty to retrieve.
code = 'code_example' # str | The name of the Counterparty to retrieve the data for.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the counterparty. Defaults to return the latest version if not specified. (optional)

try:
    # [EXPERIMENTAL] Get Counterparty
    api_response = api_instance.get_counterparty(scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->get_counterparty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Counterparty to retrieve. | 
 **code** | **str**| The name of the Counterparty to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the counterparty. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCounterpartyResponse**](GetCounterpartyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved counterparty or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_support_annex**
> GetCreditSupportAnnexResponse get_credit_support_annex(scope, code, as_at=as_at)

[EXPERIMENTAL] Get CSA

Get a CSA from a single scope.  The response will return either the CSA that has been stored, or a failure explaining why the request was unsuccessful.  It is important to always check for any unsuccessful requests (failures).

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:57352
configuration.host = "http://local-unit-test-server.lusid.com:57352"
# Create an instance of the API class
api_instance = lusid.CounterpartyApi(lusid.ApiClient(configuration))
scope = 'scope_example' # str | The scope of the CSA to retrieve.
code = 'code_example' # str | The name of the CSA to retrieve the data for.
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to retrieve the CSA. Defaults to return the latest version if not specified. (optional)

try:
    # [EXPERIMENTAL] Get CSA
    api_response = api_instance.get_credit_support_annex(scope, code, as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->get_credit_support_annex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the CSA to retrieve. | 
 **code** | **str**| The name of the CSA to retrieve the data for. | 
 **as_at** | **datetime**| The asAt datetime at which to retrieve the CSA. Defaults to return the latest version if not specified. | [optional] 

### Return type

[**GetCreditSupportAnnexResponse**](GetCreditSupportAnnexResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The successfully retrieved credit support annexes or any failure |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_counterparties**
> ResourceListOfGetCounterpartyResponse list_counterparties(as_at=as_at)

[EXPERIMENTAL] List the set of Counterparties

List the set of Counterparties at the specified AsAt date/time

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:57352
configuration.host = "http://local-unit-test-server.lusid.com:57352"
# Create an instance of the API class
api_instance = lusid.CounterpartyApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the counterparty. Defaults to latest if not specified. (optional)

try:
    # [EXPERIMENTAL] List the set of Counterparties
    api_response = api_instance.list_counterparties(as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->list_counterparties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the counterparty. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCounterpartyResponse**](ResourceListOfGetCounterpartyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested counterparties |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credit_support_annexes**
> ResourceListOfGetCreditSupportAnnexResponse list_credit_support_annexes(as_at=as_at)

[EXPERIMENTAL] List the set of CSAs

List the set of CSAs at the specified AsAt date/time

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:57352
configuration.host = "http://local-unit-test-server.lusid.com:57352"
# Create an instance of the API class
api_instance = lusid.CounterpartyApi(lusid.ApiClient(configuration))
as_at = '2013-10-20T19:20:30+01:00' # datetime | The asAt datetime at which to list the CSAs. Defaults to latest if not specified. (optional)

try:
    # [EXPERIMENTAL] List the set of CSAs
    api_response = api_instance.list_credit_support_annexes(as_at=as_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->list_credit_support_annexes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| The asAt datetime at which to list the CSAs. Defaults to latest if not specified. | [optional] 

### Return type

[**ResourceListOfGetCreditSupportAnnexResponse**](ResourceListOfGetCreditSupportAnnexResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested CSAs |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_counterparty**
> UpsertSingleStructuredDataResponse upsert_counterparty(upsert_counterparty_request)

[EXPERIMENTAL] Upsert Counterparty. This creates or updates the data in Lusid.

Update or insert Counterparty in a single scope. An item will be updated if it already exists and inserted if it does not.                The response will return the successfully updated or inserted Counterparty or failure message if unsuccessful                It is important to always check to verify success (or failure).

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:57352
configuration.host = "http://local-unit-test-server.lusid.com:57352"
# Create an instance of the API class
api_instance = lusid.CounterpartyApi(lusid.ApiClient(configuration))
upsert_counterparty_request = {"counterparty":{"counterpartyId":"12345","counterpartyName":"some-bank-of-somewhere","countryOfRisk":"United States","issuerRatings":[{"ratingSource":"S&P","rating":"BB"}],"industryScheme":{"schemeName":"TRCS","schemeId":"5010201010","economicSector":"Energy","businessSector":"Energy - Fossil Fuels","industry":"Oil & Gas","industryActivity":"Integrated Oil & Gas"},"scope":"some-scope","code":"some-code"}} # UpsertCounterpartyRequest | The Counterparty to update or insert

try:
    # [EXPERIMENTAL] Upsert Counterparty. This creates or updates the data in Lusid.
    api_response = api_instance.upsert_counterparty(upsert_counterparty_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->upsert_counterparty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_counterparty_request** | [**UpsertCounterpartyRequest**](UpsertCounterpartyRequest.md)| The Counterparty to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

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

# **upsert_credit_support_annex**
> UpsertSingleStructuredDataResponse upsert_credit_support_annex(upsert_credit_support_annex_request)

[EXPERIMENTAL] Upsert CSA. This creates or updates the data in Lusid.

Update or insert CSA in a single scope. An item will be updated if it already exists and inserted if it does not.                The response will return the successfully updated or inserted CSA or failure message if unsuccessful                It is important to always check to verify success (or failure).

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

# Defining host is optional and default to http://local-unit-test-server.lusid.com:57352
configuration.host = "http://local-unit-test-server.lusid.com:57352"
# Create an instance of the API class
api_instance = lusid.CounterpartyApi(lusid.ApiClient(configuration))
upsert_credit_support_annex_request = {"creditSupportAnnex":{"referenceCurrency":"GBP","collateralCurrencies":["GBP"],"isdaAgreementVersion":"ISDA2002","marginCallFrequency":"1W","valuationAgent":"Institution","thresholdAmount":0,"roundingDecimalPlaces":2,"initialMarginAmount":100000,"minimumTransferAmount":10000,"scope":"some-scope","code":"some-code"}} # UpsertCreditSupportAnnexRequest | The CSA to update or insert

try:
    # [EXPERIMENTAL] Upsert CSA. This creates or updates the data in Lusid.
    api_response = api_instance.upsert_credit_support_annex(upsert_credit_support_annex_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CounterpartyApi->upsert_credit_support_annex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_credit_support_annex_request** | [**UpsertCreditSupportAnnexRequest**](UpsertCreditSupportAnnexRequest.md)| The CSA to update or insert | 

### Return type

[**UpsertSingleStructuredDataResponse**](UpsertSingleStructuredDataResponse.md)

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

